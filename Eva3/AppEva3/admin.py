from django.contrib import admin
from AppEva3.models import Warframe

# Register your models here.
class WarframeAdmin(admin.ModelAdmin):
    list_display = ['WarframeName', 'Critical_Utility', 'CriticalDMG_Utility', 'Status_Utility']

admin.site.register(Warframe, WarframeAdmin)