from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('add-data/',TourismCreateView.as_view(),name='add-endpoint'),
    path('list-data/', TourismListView.as_view(), name='list-endpoint'),
    path('detail-data/<int:id>', TourismDetailView.as_view(), name='detail-endpoint'),
    path('update-data/<int:id>/', TourismUpdateView.as_view(), name='update-endpoint'),
    path('delete-data/<int:id>/', TourismDeleteView.as_view(), name='delete-endpoint'),



    path('create/', views.Tourism_create, name='create'),
    path('update/<int:id>/', views.Tourism_Update, name='update'),
    path('list/', views.Tourism_list, name='list'),
    path('detail/<int:id>/', views.Tourism_Detail, name='detail'),
    path('delete/<int:id>/', views.Tourism_delete, name='delete'),


    path('base/', views.base_view, name='base'),


    path('', views.userRegistration, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.loginpage, name='login'),
    path('index/', views.index, name='index'),
    path('user_view/', views.user_view, name='user_view'),
    path('admin_view/', views.admin_view, name='admin_view'),



    path('admin-create/', views.AdminTourismCreate, name='admin-create'),
    path('admin-update/<int:id>', views.AdminTourismUpdate, name='admin-update'),
    path('admin-list/', views.AdminTourismList, name='admin-list'),
    path('admin-detail/<int:id>', views.AdminTourismDetail, name='admin-detail'),
    path('admin-delete/<int:id>', views.AdminTourismDelete, name='admin-delete'),

]