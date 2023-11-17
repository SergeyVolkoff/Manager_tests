from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('statistic/<int:stat_id>/', views.statistic_testing),
    path('statistic/<slug:stat_slug>/', views.statistic_by_slug),
]