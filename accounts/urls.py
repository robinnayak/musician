from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterPage, name="register"),
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.LogoutPage, name="logout"),
    path('user-page/', views.UserPage, name="user-page"),
    path('account-setting/', views.settingPage, name="account-setting"),

    path('',views.home, name='home'),
    path('album_list/',views.AlbumList, name='album_list'),
    path('show_musician/<str:pk>', views.ShowMusician, name='show_musician'),

    path('create_album/<str:pk>/', views.Createalbum, name="create_album"),
    path('update_musician/<str:pk>/', views.Updatemusician, name="update_musician"),
    path('delete_album/<str:pk>', views.Deletealbum, name="delete_album"),
]
