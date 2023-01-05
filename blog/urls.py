from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('mountain_list/', views.MountainView.as_view(), name='mountain_list'),
    path('flower_list/', views.FlowerView.as_view(), name='flower_list'),
    path('cat-list/', views.CatView.as_view(), name='cat_list'),
    path('dailylife-list/', views.DailylifeView.as_view(), name='dailylife_list'),
    path('good/<int:pk>', views.goodfunc, name='good'),
]
