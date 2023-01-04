
from django.urls import path
from Home import views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('api/', views.TodoView.as_view(), name='api'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login_api'),
    path('delete_api/<int:id>', views.deleteView.as_view(), name='delete_api'),]
