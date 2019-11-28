from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('level/<id>',views.show, name = 'show'),
    path('' , views.index , name = 'index'),
    path('formulaire_utilisateur' , views.form_user , name = 'form_user'),
]
