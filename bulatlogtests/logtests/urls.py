from . import views
from django.urls import path,re_path,register_converter

urlpatterns = [
    path('', views.index,name='home'),
    # path('statistic/<int:stat_id>/', views.statistic_testing),
    path(
        'statistic_data/<int:test_data_id>/',
          views.show_test_detail, 
          name='data_tests'),
    path('report/', views.report, name='report'),
    path('log/', views.log, name='log'),
    path(
        'test_execution_log/',
        views.test_execution_log,
        name='test_log'),

    path(
        'detail/<int:test_data_id>/',
          views.show_test_detail, 
          name='data_tests'),
]