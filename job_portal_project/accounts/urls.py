from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/additional_data_form/', views.additional_profile_data, name='additional_profile_data'),
    path('profile/edit_profile/', views.edit_profile_view, name='edit_profile_view'),
    path('profile/delete_account/', views.delete_account, name='delete_account'),
]
