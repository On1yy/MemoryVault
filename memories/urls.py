from django.urls import path
from .views import create_memory, memory_list, render, edit_memory, delete_memory, toggle_favorite, \
    favorites_memories_list, toggle_archive,archives_memories_list,fullscreen_memory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create',create_memory,name='create_memory'),
    path('list',memory_list,name='memories_list'),
    path("edit/<int:id>/",edit_memory, name="edit_memory"),
    path('delete/<int:id>/',delete_memory,name='delete_memory'),
    path('favorite/<int:id>/',toggle_favorite,name='toggle_favorite'),
    path('favorites_list',favorites_memories_list,name='favorites_memories_list'),
    path('archive/<int:id>/',toggle_archive,name='toggle_archive'),
    path('archives_list',archives_memories_list,name='archives_memories_list'),
    path('fullscreen_memory/<int:id>/', fullscreen_memory, name='fullscreen_memory'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)