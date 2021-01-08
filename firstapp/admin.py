from django.contrib import admin
from .models import Author_db, Exhibition_db, Card_db, Organization, User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number','name','phone','position','fund_name')

@admin.register(Author_db)
class ReptileAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth','country')

@admin.register(Exhibition_db)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','finish_date')

@admin.register(Card_db)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('number','name','create_date','accuracy_date')

@admin.register(Organization)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','person')

