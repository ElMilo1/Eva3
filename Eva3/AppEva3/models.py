from django.db import models

# Create your models here.

class UserData(models.Model):
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=50)

class Weapon(models.Model):
    WeaponName = models.CharField(max_length=255)
    WeaponType = models.CharField(max_length=50)
    WeaponSlot = models.CharField(max_length=50)
    Critical_Utility = models.FloatField()
    CriticalDMG_Utility = models.FloatField()
    Status_Utility = models.FloatField()

    TotalUtility = models.FloatField()
    def save(self , *args , **kwargs):
        self.Utilidad()
        super().save(*args , **kwargs)

    def Utilidad(self):
        x1 = self.Critical_Utility*100
        x2 = self.CriticalDMG_Utility
        x3 = self.Status_Utility*100
        xt = ((x1 + x3)*x2)/2

        self.TotalUtility = xt

class Warframe(models.Model):
    WarframeName = models.CharField(max_length=25)
    Critical_Utility = models.FloatField()
    CriticalDMG_Utility = models.FloatField()
    Status_Utility = models.FloatField()

    TotalUtility = models.FloatField()
    def save(self , *args , **kwargs):
        self.Utilidad()
        super().save(*args , **kwargs)

    def Utilidad(self):
        x1 = self.Critical_Utility/100
        x2 = self.CriticalDMG_Utility
        x3 = self.Status_Utility/100
        xt = ((x1 + x3)*x2)/4
        
        self.TotalUtility = xt*100

class WeaponUtility(models.Model):
    WeaponName = models.CharField(max_length=255)
    WeaponUtility = models.FloatField()
    WeaponSlot = models.CharField(max_length=50)


class WarframeUtility(models.Model):
    WarframeName = models.CharField(max_length=25)
    WarframeUtility = models.FloatField()

class BuildResume(models.Model):
    UserName = models.CharField(max_length=255)
    WarframeName = models.CharField(max_length=255)
    WarframeID = models.ForeignKey(Warframe,on_delete=models.CASCADE,related_name='Int_WarframeID')
    Primary = models.CharField(max_length=255)
    Secondary = models.CharField(max_length=255)
    Melee = models.CharField(max_length=255)
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