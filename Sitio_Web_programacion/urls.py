from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    postListView,
    postDetailView,
    postCreateView,
    postUpdateView,
    postDeleteView,
    like
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', postListView.as_view(), name='list'),
    path('create/', postCreateView.as_view(), name='created'),
    path('<slug>/', postDetailView.as_view(), name='detail'),
    path('<slug>/update/', postUpdateView.as_view(), name='Update'),
    path('<slug>/delete/', postDeleteView.as_view(), name='delete'),
    path('like/<slug>/', like, name='like')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)