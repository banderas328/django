
from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/' , main.views.homepage, name='homepage')
]
