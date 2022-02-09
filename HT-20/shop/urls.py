from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.CreateUserForm.as_view(), name="login"),
    path('main/', views.main_page, name="main"),
    path('main/<str:category>/', views.category, name='category_name'),
    path('<str:category>/', views.category, name='category_name'),
    path('main/edit', views.edit, name='edit')
]
