# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departement(models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    nom = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departement'
    


class Employe(models.Model):
    cin = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=200,blank=True, null=True)
    titre= models.CharField(max_length=100, blank=True, null=True)
    departement = models.ForeignKey(Departement, models.DO_NOTHING, db_column='departement', blank=True, null=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_debut_travail = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employe'


class Travailler(models.Model):
    cin = models.OneToOneField(Employe, models.DO_NOTHING, db_column='cin', primary_key=True)  # The composite primary key (cin, code) found, that is not supported. The first column is selected.
    code = models.ForeignKey(Departement, models.DO_NOTHING, db_column='code')
    date_debut_travail = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travailler'
        unique_together = (('cin', 'code'),)