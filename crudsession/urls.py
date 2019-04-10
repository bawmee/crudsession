from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import crudapp.views
import portapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.index, name="index"),
    path('blog/new', crudapp.views.new, name="new"),
    path('blog/<int:blog_id>', crudapp.views.detail, name="detail"),
    path('blog/edit/<int:blog_id>', crudapp.views.edit, name="edit"),
    path('blog/delete/<int:blog_id>', crudapp.views.delete, name="delete"),
    path('port', portapp.views.home, name="home"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
