from django.urls import path
from . import views

app_name='blog'


urlpatterns =[
    path('cbv/',views.All_List.as_view(),name='all_list'),
    path('cbv/<int:pk>/detail/',views.detail.as_view(),name='detail')

]