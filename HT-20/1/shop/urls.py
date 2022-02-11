from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('login/', views.CreateUserForm.as_view(), name="login"),
    path('', views.main_page, name="main"),
    path('category/<str:category>/', views.category, name='category_name'),
    path('update/<slug:pk>/', views.UpdateItem.as_view(), name='update')
]
