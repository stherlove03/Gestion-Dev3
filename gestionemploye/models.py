from django.db import models

# Create your models here.
class Adresseemp(models.Model):
    adresse_id = models.AutoField(primary_key=True)
    rue = models.CharField(max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    codepostal = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adresseemp'


class Departement(models.Model):
    codedept = models.CharField(primary_key=True, max_length=10)
    nomdept = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departement'


class Employe(models.Model):
    cin = models.CharField(primary_key=True, max_length=10)
    nomemp = models.CharField(max_length=50, blank=True, null=True)
    prenomemp = models.CharField(max_length=50, blank=True, null=True)
    date_naissanceemp = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    adresseemp = models.ForeignKey(Adresseemp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employe'


class Travailler(models.Model):
    cin = models.OneToOneField(Employe, models.DO_NOTHING, db_column='cin', primary_key=True)  # The composite primary key (cin, codedept) found, that is not supported. The first column is selected.
    codedept = models.ForeignKey(Departement, models.DO_NOTHING, db_column='codedept')
    datedebuttravail = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travailler'
        unique_together = (('cin', 'codedept'),)
