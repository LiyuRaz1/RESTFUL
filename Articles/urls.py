from django.urls import path 
from . import views
# from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView


app_name = 'articles' 

urlpatterns = [
    path('articles/',views.articles_list, name='articles_list'),
    path('add_article/',views.add_article, name='add_article'),
    path('delete_article/<slug:slug>',views.delete_article, name='delete_article'),
    path('update_article/<slug:slug>',views.update_article, name='update_article'),
    path('articles/<slug:slug>/', views.article_details, name='details'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/',views.register, name='register'),
    path('change_password/',PasswordChangeView.as_view(), name='changepsw'),
    path('password_change_done/',PasswordChangeDoneView.as_view(), name="password_change_done"),
]
