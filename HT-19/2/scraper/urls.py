from django.urls import path

from . import views


app_name = 'scraper'
urlpatterns = [

    path('', views.CreateMyChoiceView.as_view(), name="index"),
    # path('ask/', views.ask, name="ask"),
    # path('new/', views.new, name="new"),
    # path('show/', views.show, name="show"),
    # path('job/', views.job, name="job"),

]