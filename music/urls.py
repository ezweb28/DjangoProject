from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # /music/register/
    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    # path('<int:album_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/detele/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/<album_id>/favorite/
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
