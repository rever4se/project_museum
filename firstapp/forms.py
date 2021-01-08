from django import forms
from .models import Exhibition_db, Author_db, Card_db, Organization


class AddData(forms.Form):
    name = forms.CharField(label="Имя")
    date_of_birth = forms.DateField(label="Дата рождения")
    country = forms.CharField(label="Страна")

class AddExh(forms.Form):
    name = forms.CharField(label="Название выставки")
    start_date = forms.DateField(label="Дата началы выставки")
    finish_date = forms.DateField(label="Дата окончания выставки")

class AddCard(forms.Form):
    number = forms.IntegerField(label="Номер карты")
    name = forms.CharField(label="Название экспоната")
    create_date = forms.DateField(label="Дата создания карты")
    accuracy_date = forms.CharField(label="Точно ли определена дата")
    exhibition_id = forms.ModelChoiceField(label="Выставка", queryset=Exhibition_db.objects.all().order_by('id'))
    author_id = forms.ModelChoiceField(label="Автор", queryset=Author_db.objects.all().order_by('id'))

class AddOrg(forms.Form):
    name = forms.CharField(label="Название орг.")
    address = forms.CharField(label="Адресс орг.")
    phone = forms.CharField(label="Телефон орг.")
    person = forms.CharField(label="Контакт. персона")
    exhibition_id = forms.ModelChoiceField(label="Выставка", queryset=Exhibition_db.objects.all().order_by('id'))

class AddUser(forms.Form):
    number = forms.IntegerField(label="Номер пользователя")
    name = forms.CharField(label="ФИО пользователя")
    phone = forms.CharField(label="Номер телефона")
    position = forms.CharField(label="Должность")
    fund_name = forms.CharField(label="Название фонда")

class AddControl(forms.Form):
    card_id = forms.ModelChoiceField(label="Карта", queryset=Card_db.objects.all().order_by('id'))
    author_id = forms.ModelChoiceField(label="Автор", queryset=Author_db.objects.all().order_by('id'))
    add_stor = forms.CharField(label="Прием на хранение")
    off_stor = forms.CharField(label="Списание")
    exhibition_id = forms.ModelChoiceField(label="Выставка", queryset=Exhibition_db.objects.all().order_by('id'))
    organization_id = forms.ModelChoiceField(label="Организация", queryset=Organization.objects.all().order_by('id'))
    trans_ex = forms.CharField(label="Передача на выставку")
    return_ex = forms.CharField(label="Прием с выставки")
