from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import Author_db, Exhibition_db, Card_db, Organization, User, Control
from .forms import AddData, AddExh, AddCard, AddOrg, AddUser, AddControl
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from firstapp import forms

z = "user"

#Домашние страницы шаблонов

def auth(request):
    return render(request, "auth.html")

def index(request):
    return render(request, "index.html")

def index_author(request):
    global z
    form_add = AddData()
    data = Author_db.objects.all()
    var = z
    return render(request, "firstapp/Template_Author.html", {"form":form_add, "data_show":data, "uname":var})

def index_exhibition(request):
    form_ex = AddExh()
    data = Exhibition_db.objects.all()
    return render(request, "firstapp/Template_Exhibition.html", {"form":form_ex, "data_show":data})

def index_org(request):
    form_ex = AddOrg()
    data = Organization.objects.all()
    return render(request, "firstapp/Template_Organization.html", {"form":form_ex, "data_show":data})

def index_card(request):
    form_ca = AddCard()
    data = Card_db.objects.all()
    return render(request, "firstapp/Template_Card.html", {"form":form_ca, "data_show":data})

def index_user(request):
    form_ca = AddUser()
    data = User.objects.all()
    return render(request, "firstapp/Template_User.html", {"form":form_ca, "data_show":data})

def index_control(request):
    form_ca = AddControl()
    data = Control.objects.all()
    return render(request, "firstapp/Template_Control.html", {"form":form_ca, "data_show":data})

#Определение view

class view_move(View):
    def add_move(request):
        if request.method == "POST":
            new_author = Control()
            new_author.card_id = Card_db.objects.get(id=request.POST.get("card_id"))
            new_author.author_id = Author_db.objects.get(id=request.POST.get("author_id"))
            new_author.add_stor = request.POST.get("add_stor")
            new_author.off_stor = request.POST.get("off_stor")
            new_author.exhibition_id = Exhibition_db.objects.get(id=request.POST.get("card_id"))
            new_author.organization_id = Organization.objects.get(id=request.POST.get("author_id"))
            new_author.trans_ex = request.POST.get("trans_ex")
            new_author.return_ex = request.POST.get("return_ex")
            new_author.save()
            return HttpResponseRedirect("/user/move")

    def del_move(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Organization.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/move")

class view_org(View):
    def add_org(request):
        if request.method == "POST":
            new_author = Organization()
            new_author.name = request.POST.get("name")
            new_author.address = request.POST.get("address")
            new_author.phone = request.POST.get("phone")
            new_author.person = request.POST.get("person")
            new_author.exhibition_id = Exhibition_db.objects.get(id=request.POST.get("exhibition_id"))
            new_author.save()
            return HttpResponseRedirect("/user/org")

    def del_org(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Organization.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/org")

    def update_org(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Organization.objects.get(id=q)
            que.name = request.POST.get("name")
            que.address = request.POST.get("address")
            que.phone = request.POST.get("phone")
            que.person = request.POST.get("person")
            que.save()
            return HttpResponseRedirect("/user/org")

class view_card(View):
    def add_card(request):
        if request.method == "POST":
            new_author = Card_db()
            new_author.number = request.POST.get("number")
            new_author.name = request.POST.get("name")
            new_author.create_date = request.POST.get("create_date")
            new_author.accuracy_date = request.POST.get("accuracy_date")
            new_author.author_id = Author_db.objects.get(id=request.POST.get("author_id"))
            new_author.exhibition_id = Exhibition_db.objects.get(id=request.POST.get("exhibition_id"))
            new_author.save()
            return HttpResponseRedirect("/user/card")

    def del_card(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Card_db.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/card")

    def update_card(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Card_db.objects.get(id=q)
            que.number = request.POST.get("number")
            que.name = request.POST.get("name")
            que.create_date = request.POST.get("create_date")
            que.accuracy_date = request.POST.get("accuracy_date")
            que.save()
            return HttpResponseRedirect("/user/card")

class view_exhibition(View):
    def add_exhibition(request):
        if request.method == "POST":
            new_author = Exhibition_db()
            new_author.name = request.POST.get("name")
            new_author.date_of_birth = request.POST.get("start_date")
            new_author.finish_date = request.POST.get("finish_date")
            new_author.save()
            return HttpResponseRedirect("/user/exhibition")

    def del_exhibition(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Exhibition_db.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/exhibition")

    def update_exhibition(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Exhibition_db.objects.get(id=q)
            que.name = request.POST.get("name")
            que.date_of_birth = request.POST.get("start_date")
            que.finish_date = request.POST.get("finish_date")
            que.save()
            return HttpResponseRedirect("/user/exhibition")

class view_author(View):
    def add_author(request):
        if request.method == "POST":
            new_author = Author_db()
            new_author.name = request.POST.get("name")
            new_author.date_of_birth = request.POST.get("date_of_birth")
            new_author.country = request.POST.get("country")
            new_author.save()
            return HttpResponseRedirect("/user/author")

    def del_data(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Author_db.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/author")

    def update_data(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Author_db.objects.get(id=q)
            que.name = request.POST.get("name")
            que.date_of_birth = request.POST.get("date_of_birth")
            que.country = request.POST.get("country")
            que.save()
            return HttpResponseRedirect("/user/author")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            user = User()
            user.number = request.POST.get("number")
            user.name = request.POST.get("name")
            user.phone = request.POST.get("phone")
            user.position = request.POST.get("position")
            user.fund_name = request.POST.get("fund_name")
            user.save()
            return HttpResponseRedirect("/user/user")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = User.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user/user")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = User.objects.get(id=q)
            que.number = request.POST.get("number")
            que.name = request.POST.get("name")
            que.phone = request.POST.get("phone")
            que.position = request.POST.get("position")
            que.fund_name = request.POST.get("fund_name")
            que.save()
            return HttpResponseRedirect("/user/user")
