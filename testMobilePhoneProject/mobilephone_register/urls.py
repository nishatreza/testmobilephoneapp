from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.mobile_form, name='mobile_insert'),
    path('<int:id>/', views.mobile_form, name='mobile_update'),
    path('list/', views.mobile_list, name='mobile_list'),
    path('delete/<int:id>/', views.mobile_delete, name='mobile_delete'),
    path('search-mobile', csrf_exempt(views.search_mobile), name='search_mobile'),

]

