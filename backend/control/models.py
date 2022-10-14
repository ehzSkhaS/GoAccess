from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class License(models.Model):
    LIC_STATES = (
        (1, 'Enabled'),
        (2, 'Disabled'),
    )    
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    end = models.DateField(null=False)
    quantity = models.IntegerField(default=5)
    state = models.PositiveSmallIntegerField(choices=LIC_STATES, null=True, default=1)
    
    class Meta:
        db_table = 'license'
        verbose_name = 'License'
        verbose_name_plural = 'Licenses'
        
    def __str__(self):
        return str(self.pk)
    
    
class Type(models.Model):
    DELIVERY = 0
    NORMAL_VISIT = 1
    WORKER = 2
    TAXI_VISIT = 3
    WALKER_VISIT = 4
    TAXI_SERVICE = 5
    NOT_INVITE_DELIVERY = 6
    NOT_INVITE_NORMAL = 7
    NOT_INVITE_TAXI = 8
    NOT_INVITE_WALKER = 9
    PROVIDER_VISIT = 10
    PROVIDER_VISIT_WALKER = 11
    
    CHOICES = (
        (DELIVERY, 'Delivery'),
        (NORMAL_VISIT, 'Normal Visit'),
        (WORKER, 'Worker'),
        (TAXI_VISIT, 'Taxi Visit'),
        (WALKER_VISIT, 'Walker Visit'),
        (TAXI_SERVICE, 'Taxi Service'),
        (NOT_INVITE_DELIVERY, 'Not Invite Dedlivery'),
        (NOT_INVITE_NORMAL, 'Not Invite Normal'),
        (NOT_INVITE_TAXI, 'Not Invite Taxi'),
        (NOT_INVITE_WALKER, 'Not Invite Walker'),
        (PROVIDER_VISIT, 'Provider Visit'),
        (PROVIDER_VISIT_WALKER, 'Provider Visit Walker'),
    )
    
    type = models.PositiveSmallIntegerField(choices=CHOICES, null=False)
    is_qr = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = 'type'
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        
    def __str__(self):
        return str(self.type)


class State(models.Model):
    PENDING = 0
    ACCEPTED = 1
    DENIED = 2
    CANCELED = 3
    EXPIRED = 4
    FINISHED = 5
    
    CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DENIED, 'Denied'),
        (CANCELED, 'Canceled'),
        (EXPIRED, 'Expired'),
        (FINISHED, 'Finished'),
    )
    
    state = models.PositiveSmallIntegerField(choices=CHOICES, null=True, default=0)
    
    class Meta:
        db_table = 'state'
        verbose_name = 'State'
        verbose_name_plural = 'States'
        
    def __str__(self):
        return str(self.state)


class RouteSuperArea(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    condo = models.ForeignKey(to='structure.Condo', related_name='routesuperarea', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Supervisor', related_name='routesuperarea', blank=True, null=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'route_super_area'
        verbose_name = 'Route Super Area'
        verbose_name_plural = 'Route Super Areas'
        
    def __str__(self):
        return str(self.name)
    
    def clean(self):
        from structure.models import Condo
        try:
            from authentication.models import Supervisor
            condo_obj = Condo.objects.get(id = self.condo.id)        
            supervisor_qobj = Supervisor.objects.filter(user = self.user)
            
            if supervisor_qobj.exists():
                if condo_obj.agency != supervisor_qobj.get().agency:
                    raise ValidationError({'user': 'Supervisor must belong to the same agency as condo'})    
        except Condo.DoesNotExist:
            pass


class RouteArea(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    condo = models.ForeignKey(to='structure.Condo', related_name='routearea', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Supervisor', related_name='routearea', blank=True, null=True, on_delete=models.DO_NOTHING)
    route_super_area = models.ForeignKey(RouteSuperArea, related_name='routearea', blank=True, null=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'route_area'
        verbose_name = 'Route Area'
        verbose_name_plural = 'Route Areas'
        
    def __str__(self):
        return str(self.name)
    
    def clean(self):
        try:
            from structure.models import Condo
            from authentication.models import Supervisor
            condo_obj = Condo.objects.get(id = self.condo.id)
            supervisor_qobj = Supervisor.objects.filter(user = self.user)
            
            try:
                route_super_area_obj = RouteSuperArea.objects.get(id = self.route_super_area.id)
                if condo_obj != route_super_area_obj.condo:
                    raise ValidationError({'route_super_area': "Route Super Area don't belongs to the same Condo as Route Area"})
                if supervisor_qobj.exists():
                    raise ValidationError({'user': "This Route Area is already assigned to a Route Super Area and don't need a Supervisor"})
            except AttributeError:
                if supervisor_qobj.exists():
                    if supervisor_qobj.get().agency != condo_obj.agency:
                        raise ValidationError({'user': "Supervisor must belong to the same Agency as the Condo"})
        except Condo.DoesNotExist:
            pass


class Route(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    route_area = models.ForeignKey(RouteArea, related_name='route', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'route'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        
    def __str__(self):
        return str(self.name)


class Checkpoint(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    qr = models.CharField(max_length=255, blank=False)
    route = models.ForeignKey(Route, related_name='checkpoint', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'checkpoint'
        verbose_name = 'Checkpoint'
        verbose_name_plural = 'Checkpoints'
        
    def __str__(self):
        return str(self.name)


class SentryBox(models.Model):
    checkpoint = models.OneToOneField(Checkpoint, primary_key=True , on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sentry_box'
        verbose_name = 'Sentry Box'
        verbose_name_plural = 'Sentry Boxes'
        
    def __str__(self):
        return str(self.checkpoint.name)


class Round(models.Model):
    name = models.CharField(max_length=255, blank=False)
    time_ini = models.TimeField(null=False)
    time_end = models.TimeField(null=False)
    is_active = models.BooleanField(default=True, null=False)
    agency = models.ForeignKey(to='structure.Agency', related_name='round', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'round'
        verbose_name = 'Round'
        verbose_name_plural = 'Rounds'
        
    def __str__(self):
        return str(self.name)

    def clean(self):
        try:
            if self.time_ini > self.time_end:
                raise ValidationError({'time_ini': "The initial time of the round must be minor than the ending time"})
        except TypeError:
            pass
    
    
class DutyShift(models.Model):
    date = models.DateField(default=timezone.now, null=False)
    sentry = models.ForeignKey(SentryBox, related_name='dutyshift', null=False, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, related_name='dutyshift', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Security', related_name='dutyshift', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'duty_shift'
        verbose_name = 'Duty Shift'
        verbose_name_plural = 'Duty Shifts'
        
    def __str__(self):
        return str(self.date)
    
    def clean(self):
        try:
            from authentication.models import Security
            sentry_agency = self.sentry.checkpoint.route.route_area.condo.agency
            round_obj = Round.objects.get(id = self.round.id)
            security_obj = Security.objects.get(user = self.user)
            
            if sentry_agency != security_obj.agency:
                raise ValidationError({'user': "This security and the sentry don't belong to the same agency"})
            if sentry_agency != round_obj.agency:
                raise ValidationError({'round': "This security and the sentry don't belong to the same agency"})
            if security_obj.agency != round_obj.agency:
                raise ValidationError({'user': "This security and the round don't belong to the same agency"})
        except SentryBox.DoesNotExist:
            pass


class CheckpointLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    checkpoint = models.ForeignKey(Checkpoint, related_name='checkpointlog', null=False, on_delete=models.CASCADE)
    duty_shift = models.ForeignKey(DutyShift, related_name='checkpointlog', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'checkpoint_log'
        verbose_name = 'Checkpoint Log'
        verbose_name_plural = 'Checkpoint Logs'
        
    def __str__(self):
        return str(self.timestamp)
    
    
class SentryBoxLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    sentry = models.ForeignKey(SentryBox, related_name='sentryboxlog', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Supervisor', related_name='sentryboxlog', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sentry_box_log'
        verbose_name = 'Sentry Box Log'
        verbose_name_plural = 'Sentry Box Logs'
        
    def __str__(self):
        return str(self.timestamp)
    
    
class Report(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    duty_shift = models.ForeignKey(DutyShift, related_name='report', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'report'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        
    def __str__(self):
        return str(self.description)
    
    
class Supervision(models.Model):
    description = models.CharField(max_length=255,null=False, blank=False)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    duty_shift = models.ForeignKey(DutyShift, related_name='supervision', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Supervisor', related_name='supervision', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'supervision'
        verbose_name = 'Supervision'
        verbose_name_plural = 'Supervisions'
        
    def __str__(self):
        return str(self.description)
    
    def clean(self):
        from authentication.models import Supervisor
        try:
            if self.user.agency != self.duty_shift.round.agency:
                raise ValidationError({'user': "This supervisor don't belong to the same agency as the security"})
            route_area = self.duty_shift.sentry.checkpoint.route.route_area
            if route_area.user != self.user and route_area.route_super_area.user != self.user:
                raise ValidationError({'user': "This supervisor can't supervise this area"})           
        except Supervisor.DoesNotExist:
            pass


class Reservation(models.Model):
    date = models.DateField(default=timezone.now, null=False)
    invited_first_name = models.CharField(max_length=255)
    invited_last_name = models.CharField(max_length=255)
    invited_identification = models.CharField(max_length=15, blank=True)
    car_registration = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_brand = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_ini = models.TimeField(default=timezone.now, null=False)
    date_end = models.TimeField(null=False)
    qr = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(to='authentication.Resident', null=False, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, null=False, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=False,  on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        
    def __str__(self):
        return str(self.date)


class ReservationRegistry(models.Model):
    date = models.DateTimeField(default=timezone.now, null=False)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(to='authentication.Security', null=False, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservation_registry'
        verbose_name = 'Reservation Registry'
        verbose_name_plural = 'Reservation Registries'
        
    def __str__(self):
        return str(self.description)


class Event(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now, null=False)
    time_ini = models.TimeField(default=timezone.now, null=False)
    time_end = models.TimeField(null=False)
    amount_people = models.IntegerField(default=10, null=False)
    token = models.CharField(max_length=30)
    user = models.ForeignKey(to='authentication.Resident', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return str(self.name)


class EventReservation(models.Model):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'event_reservation'
        verbose_name = 'Event Reservation'
        verbose_name_plural = 'Event Reservations'

    def __str__(self):
        return str(self.pk)


class EventArea(models.Model):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    area = models.ForeignKey(to='structure.Area', null=False, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'event_area'
        verbose_name = 'Event Area'
        verbose_name_plural = 'Event Areas'
        
    def __str__(self):
        return str(self.pk)


class InvitationRequest(models.Model):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    identification = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'invitation_request'
        verbose_name = 'Invitation Request'
        verbose_name_plural = 'Invitation Requests'

    def __str__(self):
        return str(self.date)

