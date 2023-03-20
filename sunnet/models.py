# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class GELEN_TAKILAR(models.Model):
    AD = models.TextField(db_column='Ad')  # Field name made lowercase.
    SOYAD = models.TextField(db_column='Soyad', blank=True, null=True)  # Field name made lowercase.
    ACIKLAMA = models.TextField(blank=True, null=True)
    MIKTAR = models.IntegerField(blank=True, null=True)
    TAKI_TUR = models.ForeignKey('TAKI_TURU', models.DO_NOTHING)
    KISI = models.ForeignKey('KISILER', models.DO_NOTHING)

class KISILER(models.Model):
    AD = models.TextField(blank=True, null=True)

class TAKI_TURU(models.Model):
    AD = models.TextField(blank=True, null=True)
