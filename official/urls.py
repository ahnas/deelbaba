from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'official'

urlpatterns = [
    path('login/', views.login_view,name="login"),
    path('', views.home,name="home"),
    path('logout/', views.logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)