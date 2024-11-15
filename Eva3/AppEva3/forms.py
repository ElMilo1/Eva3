from  django import forms
from django.core.exceptions import ValidationError 
from django.core import validators
from AppEva3.models import Warframe, UserData, Weapon

class WarframeForm(forms.ModelForm):
    class Meta:
        model = Warframe
        fields = ['WarframeName','Critical_Utility','CriticalDMG_Utility','Status_Utility']
        
    def clean_CriticalUtility(self):
        critical_utility = self.cleaned_data.get('Critical_Utility')
        if critical_utility < 0:
            raise forms.ValidationError("Critical Utility no puede ser menor a 0")
        elif critical_utility > 50:
            raise forms.ValidationError("Critical Utility no puede ser mayor a 50")
        
        CalculoCritical_Utility = critical_utility / 100
        
        return CalculoCritical_Utility

    def clean_CriticalDMG(self):
        critical_dmg = self.cleaned_data.get('CriticalDMG_Utility')
        if critical_dmg < 1:
            raise forms.ValidationError("CriticalDMG no puede ser menor a 1")
        elif critical_dmg > 5:
            raise forms.ValidationError("CriticalDMG no puede ser mayor a 5")
        return critical_dmg

    def clean_StatusUtility(self):
        status_utility = self.cleaned_data.get('Status_Utility')
        if status_utility < 0:
            raise forms.ValidationError("Critical Utility no puede ser menor a 0")
        elif status_utility > 50:
            raise forms.ValidationError("Status Utility no puede ser mayor a 50")
        
        CalculoStatus_Utility = status_utility / 100
        
        return CalculoStatus_Utility
    
    def clean(self):
        cleaned_data = super().clean()
        warframe_nombre = self.cleaned_data.get('WarframeName')
        critical_utility = self.cleaned_data.get('Critical_Utility')
        critical_dmg = self.cleaned_data.get('CriticalDMG_Utility')
        status_utility = self.cleaned_data.get('Status_Utility')
        
        if warframe_nombre is None or critical_utility is None or critical_dmg is None or status_utility is None:
            raise forms.ValidationError("Todos los campos son obligatorios")
        
        return cleaned_data
    
class WeaponForm(forms.ModelForm):
    
    Weapon_Slot_OptionVar = [
    ('',''),
    ('PRIMARY','PRIMARY'),
    ('SECONDARY','SECONDARY'),
    ('MELEE','MELEE')
    ]

    Weapon_TypeVar = [
    ('',''),
    ('CLOSE RANGE','CLOSE RANGE'),
    ('MID RANGE','MID RANGE'),
    ('LONG RANGE','LONG RANGE')
    ]

    def Percentaje_Val(x):
        if x>50 or x<0:
            raise forms.ValidationError("Ingresa un valor entre 0 y 50")
    
    WeaponName = forms.CharField(validators=[
        validators.MaxLengthValidator(255),
        validators.MinLengthValidator(5)
    ])
    WeaponType = forms.ChoiceField(choices=Weapon_TypeVar)
    WeaponSlot = forms.ChoiceField(choices=Weapon_Slot_OptionVar)
    Critical_Utility = forms.FloatField(validators=[Percentaje_Val])
    CriticalDMG_Utility = forms.FloatField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(5)
    ])
    Status_Utility = forms.FloatField(validators=[Percentaje_Val])

    class Meta:
        model = Weapon
        fields = ['WeaponName','WeaponType','WeaponSlot','Critical_Utility','CriticalDMG_Utility','Status_Utility']


class User(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        User_Name = self.cleaned_data.get('UserName')
        Password = self.cleaned_data.get('Password')
        
        if User_Name is None or Password is None:
            raise forms.ValidationError("Todos los campos son obligatorios")
        
        return cleaned_data