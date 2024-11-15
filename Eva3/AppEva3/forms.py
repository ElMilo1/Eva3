from  django import forms
from django.core.exceptions import ValidationError 
from django.core import validators
from AppEva3.models import Warframe, UserData, Weapon, BuildResume

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
        validators.MinLengthValidator(3)
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
    

class BuildResumeForm(forms.ModelForm):
    def WarframeRec(self):
        WarframeOpt = Warframe.objects.all()
        if WarframeOpt.exists():
            lista = []
            for i in WarframeOpt:
                lista.append(i)
            return lista
        else:
            return []
        
    def WarframeOptVar(self):
        WarframeVar = self.WarframeRec()
        lista = []
        for i in WarframeVar:
            lista.append((i.WarframeName, i.WarframeName))
        lista.insert(0, ('', ''))
        return lista

    def PrimaryRec(self):    
        WPrimary = Weapon.objects.filter(WeaponSlot='PRIMARY')
        if WPrimary.exists():
            lista = []
            for i in WPrimary:
                lista.append(i)
            return lista
        else:
            return []

    def SecondaryRec(self):
        WSecondary = Weapon.objects.filter(WeaponSlot='SECONDARY')
        if WSecondary.exists():
            lista = []
            for i in WSecondary:
                lista.append(i)
            return lista
        else:
            return []

    def MeleeRec(self):
        WMelee = Weapon.objects.filter(WeaponSlot='MELEE')
        if WMelee.exists():
            lista = []
            for i in WMelee:
                lista.append(i)
            return lista
        else:
            return []
        
    def PrimaryOptionVar(self):
        PrimaryWeapons = self.PrimaryRec()
        lista = []
        for i in PrimaryWeapons:
            lista.append((i.WeaponName, i.WeaponName))
        lista.insert(0, ('', ''))
        return lista

    def SecondaryOptionVar(self):
        SecondaryWeapons = self.SecondaryRec()
        lista = []
        for i in SecondaryWeapons:
            lista.append((i.WeaponName, i.WeaponName))
        lista.insert(0, ('', ''))
        return lista

    def MeleeOptionVar(self):
        MeleeWeapons = self.MeleeRec()
        lista = []
        for i in MeleeWeapons:
            lista.append((i.WeaponName, i.WeaponName))
        lista.insert(0, ('', ''))
        return lista
    
    def AsignBuild(self):
        self.Warframe = self.get_warframe(self.cleaned_data.get('WarframeName'))
        self.Primary = self.get_primary_weapon(self.cleaned_data.get('Primary'))
        self.Secondary = self.get_secondary_weapon(self.cleaned_data.get('Secondary'))
        self.Melee = self.get_melee_weapon(self.cleaned_data.get('Melee'))

    def get_warframe(self, warframe_name):
        try:
            return Warframe.objects.get(WarframeName=warframe_name)
        except Warframe.DoesNotExist:
            return None

    def get_primary_weapon(self, primary_name):
        try:
            return Weapon.objects.get(WeaponName=primary_name, WeaponSlot='PRIMARY')
        except Weapon.DoesNotExist:
            return None

    def get_secondary_weapon(self, secondary_name):
        try:
            return Weapon.objects.get(WeaponName=secondary_name, WeaponSlot='SECONDARY')
        except Weapon.DoesNotExist:
            return None

    def get_melee_weapon(self, melee_name):
        try:
            return Weapon.objects.get(WeaponName=melee_name, WeaponSlot='MELEE')
        except Weapon.DoesNotExist:
            return None

    def clean_WarframeName(self):
        warframe_name = self.cleaned_data.get('WarframeName')
        if warframe_name:
            try:
                Warframe.objects.get(WarframeName=warframe_name)
            except Warframe.DoesNotExist:
                raise forms.ValidationError("El Warframe seleccionado no existe")
        return warframe_name

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Asignar builds y obtener objetos relacionados
        self.AsignBuild()
        
        # Establecer WarframeID
        if self.Warframe:
            instance.WarframeID = self.Warframe.id
        else:
            raise forms.ValidationError("No se pudo obtener el ID del Warframe")
        
        # Calcular TotalUtility
        weapons_total = 0
        if self.Primary:
            weapons_total += min(100, self.Primary.TotalUtility)
        if self.Secondary:
            weapons_total += min(100, self.Secondary.TotalUtility)
        if self.Melee:
            weapons_total += min(100, self.Melee.TotalUtility)
        
        # Promedio de armas (no superará 100)
        weapons_utility = weapons_total / 3
        
        # TotalUtility del Warframe (no superará 100)
        warframe_utility = min(100, self.Warframe.TotalUtility) if self.Warframe else 0
        
        # Promedio final (no superará 100)
        instance.TotalUtility = (weapons_utility + warframe_utility) / 2
        
        if commit:
            instance.save()
        return instance

    UserName = forms.CharField(max_length=255)
    
    def __init__(self, *args, **kwargs):
        super(BuildResumeForm, self).__init__(*args, **kwargs)
        self.fields['WarframeName'] = forms.ChoiceField(
            choices=self.WarframeOptVar(),
            required=True
        )
        self.fields['Primary'] = forms.ChoiceField(
            choices=self.PrimaryOptionVar(),
            required=True
        )
        self.fields['Secondary'] = forms.ChoiceField(
            choices=self.SecondaryOptionVar(),
            required=True
        )
        self.fields['Melee'] = forms.ChoiceField(
            choices=self.MeleeOptionVar(),
            required=True
        )
    
    class Meta:
        model = BuildResume
        fields = ['UserName', 'WarframeName', 'Primary', 'Secondary', 'Melee']