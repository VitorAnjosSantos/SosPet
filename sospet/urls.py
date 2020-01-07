from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pet/all/', views.list_all_pets),
    path('pet/user/', views.list_user_pets),
    path('pet/detall/<id>/', views.pet_detall),
    path('pet/register/', views.pet_register),
    path('pet/register/submit', views.set_pet),
    path('pet/delete/<id>/', views.pet_delete),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
