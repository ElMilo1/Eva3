from django.contrib import admin
from AppEva3.models import Warframe, Weapon, BuildResume

# Register your models here.
class WarframeAdmin(admin.ModelAdmin):
    list_display = ['WarframeName', 'Critical_Utility', 'CriticalDMG_Utility', 'Status_Utility']

class WeaponAdmin(admin.ModelAdmin):
    list_display = ['WeaponName','WeaponType','WeaponSlot','Critical_Utility','CriticalDMG_Utility','Status_Utility']

class BuildResumeAdmin(admin.ModelAdmin):
    list_display = ['UserName','WarframeName','WarframeID','Primary','Secondary','Melee','TotalUtility']

admin.site.register(Warframe, WarframeAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(BuildResume,BuildResumeAdmin)