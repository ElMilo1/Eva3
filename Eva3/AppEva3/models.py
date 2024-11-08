from django.db import models

# Create your models here.

class UserData(models.Model):
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=50)

class Weapon(models.Model):
    WeaponName = models.CharField(max_length=25)
    WeaponType = models.CharField(max_length=25)
    WeaponSlot = models.CharField(max_length=25)
    Critical_Utility = models.FloatField()
    CriticalDMG_Utility = models.FloatField()
    Status_Utility = models.FloatField()

class Warframe(models.Model):
    WarframeName = models.CharField(max_length=25)
    Critical_Utility = models.FloatField()
    CriticalDMG_Utility = models.FloatField()
    Status_Utility = models.FloatField()

class WeaponUtility(models.Model):
    WeaponName = models.ForeignKey(Weapon , on_delete=models.CASCADE , related_name='Utility_WeaponName')
    WeaponUtility = models.FloatField()
    WeaponSlot = models.ForeignKey(Weapon , on_delete=models.CASCADE , related_name='Utility_WeaponSlot')

class WarframeUtility(models.Model):
    WarframeName = models.ForeignKey(Warframe , on_delete=models.CASCADE , related_name='Utility_WarframeName')
    WarframeUtility = models.FloatField()

class BuildResume(models.Model):
    UserName = models.ForeignKey(UserData , on_delete=models.CASCADE , related_name='Build_UserName')
    WarframeName = models.ForeignKey(WarframeUtility , on_delete=models.CASCADE , related_name='Build_WarframeName')
    WarframeID = models.IntegerField()
    Primary = models.ForeignKey(WeaponUtility , on_delete=models.CASCADE , related_query_name='Build_PrimaryWeapon')
    Secondary = models.ForeignKey(WeaponUtility , on_delete=models.CASCADE , related_name='Build_SecondaryWeapon')
    Melee = models.ForeignKey(WeaponUtility , on_delete=models.CASCADE , related_name='Build_MeleeWeapon')
    TotalUtility = models.FloatField()

    def save(self , *args , **kwargs):
        self.Utilidad_total()
        super().save(*args , **kwargs)

    def Utilidad_total(self):
        PrimaryCrit = self.Primary.Critical_Utility / 100
        PrimaryDmg = self.Primary.CriticalDMG_Utility
        PrimaryStat = self.Primary.Status_Utility / 100
        PrimaryUtility = ((PrimaryCrit+PrimaryStat)*PrimaryDmg)/2

        SecondaryCrit = self.Secondary.Critical_Utility
        SecondaryDmg = self.Secondary.CriticalDMG_Utility
        SecondaryStat = self.Secondary.Status_Utility
        SecondaryUtility = ((SecondaryCrit+SecondaryStat)*SecondaryDmg)/2

        MeleeCrit = self.Melee.Critical_Utility
        MeleeDmg = self.Melee.CriticalDMG_Utility
        MeleeStat = self.Melee.Status_Utility
        MeleeUtility = ((MeleeCrit+MeleeStat)*MeleeDmg)/2

        Utility = (PrimaryUtility + SecondaryUtility + MeleeUtility) / 3

        self.TotalUtility = Utility


        