from django.contrib import admin

from backend.logs import models


admin.site.register(models.Alert)
