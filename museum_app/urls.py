from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [

    path('', views.auth, name='auth'),
    url(r'^admin/', admin.site.urls),
    path('user/', views.index, name='home'),

    #страницы шаблонов
    path('user/author/', views.index_author, name='author'),
    path('user/exhibition/', views.index_exhibition, name='exhibition'),
    path('user/card/', views.index_card, name='card'),
    path('user/org/', views.index_org, name='org'),
    path('user/user/', views.index_user, name='user'),
    path('user/move/', views.index_control, name='control'),

    #пути для авторов
    path('user/author/add/', views.view_author.add_author, name='add_author'),
    path("user/author/del/", views.view_author.del_data, name="del_data"),
    path("user/author/up/", views.view_author.update_data, name="update_data"),
    #пути для выставок
    path('user/exhibition/adde/', views.view_exhibition.add_exhibition, name='add_author'),
    path("user/exhibition/dele/", views.view_exhibition.del_exhibition, name="del_data"),
    path("user/exhibition/upe/", views.view_exhibition.update_exhibition, name="update_data"),
    #пути для карт
    path('user/card/addc/', views.view_card.add_card, name='add_author'),
    path("user/card/delc/", views.view_card.del_card, name="del_data"),
    path("user/card/upc/", views.view_card.update_card, name="update_data"),
    #пути для организаций
    path('user/org/addo/', views.view_org.add_org, name='add_author'),
    path("user/org/delo/", views.view_org.del_org, name="del_data"),
    path("user/org/upo/", views.view_org.update_org, name="update_data"),
    #пути для пользователя
    path('user/add/', views.view_user.add_user, name='add_author'),
    path("user/del/", views.view_user.del_user, name="del_data"),
    path("user/up/", views.view_user.update_user, name="update_data"),
    #пути для контроля движения
    path('user/move/addm/', views.view_move.add_move, name='add_author'),
    path("user/move/delm/", views.view_move.del_move, name="del_data"),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]