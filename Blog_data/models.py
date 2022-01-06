# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField('標題', max_length=30)
    content = models.CharField('內容', max_length=5000)

    def __str__(self):
        return self.title

class Table(models.Model):
    singer = models.TextField(db_column='Singer')
    song = models.TextField(db_column='Song')
    year = models.TextField(db_column='Year')
    country = models.TextField(db_column='Country')
    click = models.IntegerField(db_column='Click')

    class Meta:
        managed = False
        db_table = 'leaderboard'

class User(models.Model):
    account = models.TextField(db_column="account")
    password = models.TextField(db_column="password")

    class Meta:
        managed = False
        db_table = 'User'

