from django.db import models
import datetime

class Author_db(models.Model):
    name = models.CharField(max_length=45)
    date_of_birth = models.DateField(default=datetime.date.today)
    country = models.CharField(max_length=45)
    objects = models.Manager()

class Exhibition_db(models.Model):
    name = models.CharField(max_length=45)
    start_date = models.DateField(default=datetime.date.today)
    finish_date = models.DateField(default=datetime.date.today)
    objects = models.Manager()

class Card_db(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=45)
    create_date = models.DateField(default=datetime.date.today)
    accuracy_date = models.CharField(max_length=45)
    author_id = models.ForeignKey('Author_db', on_delete=models.CASCADE)
    exhibition_id = models.ForeignKey('Exhibition_db', on_delete=models.CASCADE)
    objects = models.Manager()

class Organization(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    person = models.CharField(max_length=45)
    exhibition_id = models.ForeignKey('Exhibition_db', on_delete=models.CASCADE)
    objects = models.Manager()

class User(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=40)
    position = models.CharField(max_length=45)
    fund_name = models.CharField(max_length=45)
    objects = models.Manager()

class Control(models.Model):
    card_id = models.ForeignKey('Card_db', on_delete=models.CASCADE)
    author_id = models.ForeignKey('Author_db', on_delete=models.CASCADE)
    add_stor = models.DateField(default=datetime.date.today)
    off_stor = models.DateField(default=datetime.date.today)
    exhibition_id = models.ForeignKey('Exhibition_db', on_delete=models.CASCADE)
    organization_id = models.ForeignKey('Organization', on_delete=models.CASCADE)
    trans_ex = models.DateField(default=datetime.date.today)
    return_ex = models.DateField(default=datetime.date.today)
    objects = models.Manager()