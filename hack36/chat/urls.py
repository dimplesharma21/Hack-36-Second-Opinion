from django.conf.urls import url
from . import views

urlpatterns = [
    
    
    url(r'^regdetails/add$', views.regdetailsadd, name='regdetailsadd'),
    url(r'^regdetails/create$', views.regdetailscreate, name='regdetailscreate'),
    url(r'^regdetails/edit/(?P<id>\d+)$', views.regdetailsedit, name='regdetailsedit'),
    url(r'^regdetails/edit/update/(?P<id>\d+)$', views.regdetailsupdate, name='regdetailsupdate'),
    url(r'^regdetails/delete/(?P<id>\d+)$', views.regdetailsdelete, name='regdetailsdelete'),

    url(r'^cardio/see$', views.cardiosee, name='cardiosee'),
    url(r'^cardio/add$', views.cardioadd, name='cardioadd'),
    url(r'^cardio/create$', views.cardiocreate, name='cardioceate'),
    url(r'^cardio/edit/(?P<id>\d+)$', views.cardioedit, name='cardioedit'),
    url(r'^cardio/edit/update/(?P<id>\d+)$', views.cardioupdate, name='cardioupdate'),
    url(r'^cardio/delete/(?P<id>\d+)$', views.cardiodelete, name='cardiodelete'),


    url(r'^neurologyform/see$', views.neurologyformsee, name='neurologyformsee'),
    url(r'^neurologyform/add$', views.neurologyformadd, name='neurologyformadd'),
    url(r'^neurologyform/create$', views.neurologyformcreate, name='neurologyformcreate'),
    url(r'^neurologyform/edit/(?P<id>\d+)$', views.neurologyformedit, name='neurologyformedit'),
    url(r'^neurologyform/edit/update/(?P<id>\d+)$', views.neurologyformupdate, name='neurologyformupdate'),
    url(r'^neurologyform/delete/(?P<id>\d+)$', views.neurologyformdelete, name='neurologyformdelete'),

    url(r'^nephrology/see$', views.nephrologysee, name='nephrologysee'),
    url(r'^nephrology/add$', views.nephrologyadd, name='nephrologyadd'),
    url(r'^nephrology/create$', views.nephrologycreate, name='nephrologycreate'),
    url(r'^nephrology/edit/(?P<id>\d+)$', views.nephrologyedit, name='nephrologyedit'),
    url(r'^nephrology/edit/update/(?P<id>\d+)$', views.nephrologyupdate, name='nephrologyupdate'),
    url(r'^nephrology/delete/(?P<id>\d+)$', views.nephrologydelete, name='nephrologydelete'),






]