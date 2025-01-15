# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AppealProcesses(models.Model):
    id_process = models.AutoField(primary_key=True)
    id_appeal = models.ForeignKey('Appeals', models.DO_NOTHING, db_column='id_appeal', blank=True, null=True)
    id_status = models.ForeignKey('Statuses', models.DO_NOTHING, db_column='id_status', blank=True, null=True)
    date_time_setting_status = models.DateTimeField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeal_processes'


class Appeals(models.Model):
    id_appeals = models.AutoField(primary_key=True)
    id_sitizen = models.ForeignKey('Citizens', models.DO_NOTHING, db_column='id_sitizen', blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    id_category = models.ForeignKey('Categories', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    description_problem = models.TextField()
    photo = models.TextField(blank=True, null=True)
    id_sotrudnik = models.ForeignKey('Employees', models.DO_NOTHING, db_column='id_sotrudnik', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeals'


class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_official = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Cities(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cities'


class Citizens(models.Model):
    id_citizen = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='id_city', blank=True, null=True)
    id_street = models.ForeignKey('Streets', models.DO_NOTHING, db_column='id_street', blank=True, null=True)
    house = models.CharField(max_length=255, blank=True, null=True)
    flat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizens'


class CityServices(models.Model):
    id_service = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='id_city', blank=True, null=True)
    id_street = models.ForeignKey('Streets', models.DO_NOTHING, db_column='id_street', blank=True, null=True)
    house = models.CharField(max_length=100, blank=True, null=True)
    flat = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_services'


class Employees(models.Model):
    id_sotrudnik = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    id_service = models.ForeignKey(CityServices, models.DO_NOTHING, db_column='id_service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Messages(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_appeals = models.ForeignKey(Appeals, models.DO_NOTHING, db_column='id_appeals', blank=True, null=True)
    id_sotrudnik = models.ForeignKey(Employees, models.DO_NOTHING, db_column='id_sotrudnik', blank=True, null=True)
    id_sitizen = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='id_sitizen', blank=True, null=True)
    message = models.TextField()
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Statuses(models.Model):
    id_status = models.AutoField(primary_key=True)
    name_status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'statuses'


class Streets(models.Model):
    id_street = models.AutoField(primary_key=True)
    name_street = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'streets'


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='user_id')  # Связь с auth_user
    id_citizen = models.ForeignKey(Citizens, on_delete=models.SET_NULL, null=True, db_column='id_citizen', blank=True)
    id_sotrudnik = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, db_column='id_sotrudnik', blank=True)

    class Meta:
        managed = False
        db_table = 'users'
