from django.urls import path
from . import views
#from .views import delete

app_name='blog'


urlpatterns =[
    #funcation
   # path('<int:post_id>/delete',delete,name='delete'),
    path('cbv/',views.All_List.as_view(),name='all_list'),
    path('cbv/<int:pk>/detail',views.detail.as_view(),name='detail'),
    path('cbv/new',views.NewPost.as_view(),name='newpost'),
    path('cbv/<int:pk>/delete',views.Delete.as_view(),name='delete'),
    path('cbv/<int:pk>/Edit',views.Edit.as_view(),name='edit'),


]

