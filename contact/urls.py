from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('search/', views.search, name='search'), 
    
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), 
    path('contact/create/', views.create, name='create'),

    path('user/create/', views.register, name='register'), 

    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
]
