
from django.urls import path
from . import views

urlpatterns = [
    #/food/
    path('',views.index, name='index'),
    #/foos/1
    path('<int:item_id>',views.detail,name='detail'),
    path('item/',views.item, name='item'),


]
