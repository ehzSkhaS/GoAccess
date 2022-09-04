from django.contrib import admin

from .models import *

admin.site.register(License)


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


