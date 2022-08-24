from django.contrib import admin
from django.utils.translation import gettext_lazy

admin.site.site_title = gettext_lazy('GoAccess')
admin.site.site_header = gettext_lazy('GoAccess Administration')
admin.site.index_title = gettext_lazy("Options")
admin.AdminSite.enable_nav_sidebar = False

# def get_app_list(self, request):
#     app_dict = self._build_app_dict(request)
#     from django.contrib.admin.sites import site
#     from django.apps import apps
#     for app_name in app_dict.keys():
#         app = app_dict[app_name]
#         model_priority = {
#             model['object_name']: getattr(
#                 site._registry[apps.get_model(app_name, model['object_name'])],
#                 'admin_priority',
#                 20
#             )
#             for model in app['models']
#         }
#         app['models'].sort(key=lambda x: model_priority[x['object_name']])
#         yield app

# admin.AdminSite.get_app_list = get_app_list