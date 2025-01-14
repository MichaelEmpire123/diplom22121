# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class Appeals(models.Model):
    id_appeals = models.IntegerField(primary_key=True)
    id_citizen = models.ForeignKey('Citizens', models.DO_NOTHING, db_column='id_citizen', blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    id_category = models.ForeignKey('Categories', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    description_problem = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    id_sotrudnik = models.ForeignKey('Employees', models.DO_NOTHING, db_column='id_sotrudnik', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeals'


class Categories(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name_official = models.CharField(max_length=255, blank=True, null=True)
    name_short = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Cities(models.Model):
    id_city = models.IntegerField(primary_key=True)
    name_city = models.CharField(max_length=100, blank=True, null=True)

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
    id_city = models.ForeignKey(
        'Cities',
        on_delete=models.DO_NOTHING,
        db_column='id_city',  # Явно указываем колонку в базе данных
        blank=True,
        null=True
    )
    id_street = models.ForeignKey(
        'Streets',
        on_delete=models.DO_NOTHING,
        db_column='id_street',  # Аналогично для улиц
        blank=True,
        null=True
    )
    house = models.CharField(max_length=255, blank=True, null=True)
    flat = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'citizens'



class Employees(models.Model):
    id_sotrudnik = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    id_service = models.ForeignKey('Services', models.DO_NOTHING, db_column='id_service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Messages(models.Model):
    id_message = models.IntegerField(primary_key=True)
    id_appeals = models.ForeignKey(Appeals, models.DO_NOTHING, db_column='id_appeals', blank=True, null=True)
    id_sotrudnik = models.ForeignKey(Employees, models.DO_NOTHING, db_column='id_sotrudnik', blank=True, null=True)
    id_citizen = models.ForeignKey(Citizens, models.DO_NOTHING, db_column='id_citizen', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Processing(models.Model):
    id_process = models.IntegerField(primary_key=True)
    id_appeal = models.ForeignKey(Appeals, models.DO_NOTHING, db_column='id_appeal', blank=True, null=True)
    id_status = models.ForeignKey('Statuses', models.DO_NOTHING, db_column='id_status', blank=True, null=True)
    date_time_setting_status = models.DateTimeField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processing'


class Services(models.Model):
    id_service = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    id_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='id_city', blank=True, null=True)
    id_street = models.ForeignKey('Streets', models.DO_NOTHING, db_column='id_street', blank=True, null=True)
    house = models.CharField(max_length=100, blank=True, null=True)
    flat = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Statuses(models.Model):
    id_status = models.IntegerField(primary_key=True)
    name_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuses'


class Streets(models.Model):
    id_street = models.IntegerField(primary_key=True)
    name_street = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streets'


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # связь с встроенной моделью пользователя
    id_citizen = models.ForeignKey(Citizens, on_delete=models.CASCADE, blank=True, null=True)  # Роль "житель"
    id_sotrudnik = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=True, null=True)  # Роль "сотрудник"

    class Meta:
        db_table = 'users'
