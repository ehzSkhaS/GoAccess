from django.contrib import admin

from .models import *


@admin.register(RouteSuperArea)
class RouteSuperAreaType(admin.ModelAdmin):
    list_display = ("name", "description", "condo")


@admin.register(RouteArea)
class RouteAreaType(admin.ModelAdmin):
    list_display = ("name", "description", "condo", "route_super_area")


@admin.register(Route)
class RouteType(admin.ModelAdmin):
    list_display = ("name", "description", "route_area")


@admin.register(Checkpoint)
class CheckpointType(admin.ModelAdmin):
    list_display = ("name", "description", "qr", "route")


@admin.register(Round)
class RoundType(admin.ModelAdmin):
    list_display = ("name", "time_ini", "time_end", "is_active")


@admin.register(RouteRound)
class RouteRoundType(admin.ModelAdmin):
    list_display = ("route", "round", "assigned_user")

    @admin.display(ordering='route__name', description='user')
    def assigned_user(self, element):
        if element.user.user.first_name == '':
            return element.user.user.email

        return f"{element.user.user.first_name} {element.user.user.last_name}"


@admin.register(License)
class LicenseType(admin.ModelAdmin):
    list_display = ("created", "updated", "end", "quantity", "current_state")

    @admin.display(ordering='state', description='state')
    def current_state(self, element):
        return dict(element.LIC_STATES)[element.state]


@admin.register(SentryBox)
class SentryBoxType(admin.ModelAdmin):
    list_display = ("checkpoint",)


@admin.register(DutyShift)
class DutyShiftType(admin.ModelAdmin):
    list_display = ("date", "round", "assigned_user", "sentry")

    @admin.display(ordering='user__id', description='user')
    def assigned_user(self, element):
        if element.user.first_name == '':
            return element.user.email

        return f"{element.user.first_name} {element.user.last_name}"


@admin.register(Report)
class ReportType(admin.ModelAdmin):
    list_display = ("description", "timestamp", "dutyshift")


@admin.register(Supervision)
class SupervisionType(admin.ModelAdmin):
    list_display = ("description", "timestamp", "dutyshift", "assigned_user")

    @admin.display(ordering='timestamp', description='user')
    def assigned_user(self, element):
        if element.user.user.first_name == '':
            return element.user.user.email

        return f"{element.user.user.first_name} {element.user.user.last_name}"


