from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.index, name='home'),
    path('up/<int:post_id>/', views.up_view, name='up_vote'),
    path('down/<int:post_id>/', views.down_view, name='down_vote'),
    path('boasts', views.boasts, name='boasts'),
    path('roasts', views.roasts, name='roasts'),
    path('addpost', views.addpost, name='addpost'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('ranked', views.ranked_view, name='ranked'),
    path('manage_post/<str:post_hk>', views.manage_post, name='manage_post'),
    path('delete/<str:post_hk>', views.delete_post, name='delete')
]