from django.urls import path 

from . import views


urlpatterns = [
    path('<int:number>',views.index, name = 'index'),
    path('db/',views.db_update,name='db_update')
]
