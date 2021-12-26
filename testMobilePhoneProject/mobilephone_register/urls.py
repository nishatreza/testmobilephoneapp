from django.urls import path
from . import views


urlpatterns = [
    path('', views.mobile_form, name='mobile_insert'),
    path('<int:id>/', views.mobile_form, name='mobile_update'),
    path('list/', views.mobile_list, name='mobile_list'),
    path('delete/<int:id>/', views.mobile_delete, name='mobile_delete'),

]

