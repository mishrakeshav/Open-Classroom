"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path('comments', include('comments.urls')),
    path('admin/', admin.site.urls),
    path('classroom/',include('classroom.urls')),
    path('', views.landing, name='landing-page'),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('posts/', include('posts.urls')),
    path('whiteboard/', include('whiteboard.urls')),
    path('assignments/', include('assignments.urls')),
    path('ide/', include('ide.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('contactus/', include('contactus.urls')),
    path('password-reset/', 
    auth_views.PasswordResetView.as_view(
        template_name = 'users/password_reset.html'),
        name = 'password_reset'
    ),
    path('password-reset/done/', 
    auth_views.PasswordResetDoneView.as_view(
        template_name = 'users/password_reset_done.html'),
        name = 'password_reset_done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
    ),
        name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
    ),
      name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
