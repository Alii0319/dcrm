from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('new_record/',views.add_record,name='add_record'),
    path('customer_record/<int:pk>',views.customer_record,name='customer_record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
    
    ]
