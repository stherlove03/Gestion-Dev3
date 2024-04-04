from django.db import models

# Create your models here.
class Departement(models.Model):
    codedept = models.CharField(primary_key=True, max_length=5)
    nomdept = models.CharField(max_length=100, blank=True, null=True)
    descriptiondept = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departement'


class Employe(models.Model):
    cin = models.IntegerField(primary_key=True)
    nomemp = models.CharField(max_length=100, blank=True, null=True)
    prenomemp = models.CharField(max_length=100, blank=True, null=True)
    date_naissanceemp = models.DateField(blank=True, null=True)
    sexeemp = models.CharField(max_length=1, blank=True, null=True)
    emailemp = models.CharField(max_length=100, blank=True, null=True)
    telephoneemp = models.CharField(max_length=20, blank=True, null=True)
    adresseemp = models.TextField(blank=True, null=True)
    titreemp = models.CharField(max_length=100, blank=True, null=True)
    departement = models.ForeignKey(Departement, models.DO_NOTHING, db_column='departement', blank=True, null=True)
    salaireemp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    datedebuttravail = models.DateField(blank=True, null=True)

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
