from . import views
from django.urls import path,re_path,register_converter

urlpatterns = [
    path('', views.index),
    path('statistic/<int:stat_id>/', views.statistic_testing),
    path('statistic/<slug:stat_slug>/', views.statistic_by_slug),
    path('statistic_data/<int:test_data_id>/', views.show_test_data, name='data_tests'),
]