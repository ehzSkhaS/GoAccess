from django.db import models
from django.utils import timezone


class License(models.Model):
    LIC_STATES = (
        (1, 'Enabled'),
        (2, 'Disabled'),
    )    
    
    created = models.DateField(auto_now_add=True, null=False)
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
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    condo = models.ForeignKey(to='structure.Condo', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'route_super_area'
        verbose_name = 'Route Super Area'
        verbose_name_plural = 'Route Super Areas'
        
    def __str__(self):
        return str(self.name)


class RouteArea(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    condo = models.ForeignKey(to='structure.Condo', null=False, on_delete=models.CASCADE)
    route_super_area = models.ForeignKey(RouteSuperArea, null=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'route_area'
        verbose_name = 'Route Area'
        verbose_name_plural = 'Route Areas'
        
    def __str__(self):
        return str(self.name)


class Route(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    route_area = models.ForeignKey(RouteArea, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'route'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        
    def __str__(self):
        return str(self.name)


class Checkpoint(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    qr = models.CharField(max_length=255, null=False)
    route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'checkpoint'
        verbose_name = 'Checkpoint'
        verbose_name_plural = 'Checkpoints'
        
    def __str__(self):
        return str(self.name)


class Round(models.Model):
    name = models.CharField(max_length=255, null=False)
    time_ini = models.TimeField(null=False)
    time_end = models.TimeField(null=False)
    is_active = models.BooleanField(default=False, null=False)
    condo = models.ForeignKey(to='structure.Condo', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'round'
        verbose_name = 'Round'
        verbose_name_plural = 'Rounds'
        
    def __str__(self):
        return str(self.name)
    
    
class RouteRound(models.Model):
    route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='authentication.Security', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'route_round'
        verbose_name = "Route Round"
        verbose_name_plural = "Route Rounds"
        
    def __str__(self):
        return str(self.pk)


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