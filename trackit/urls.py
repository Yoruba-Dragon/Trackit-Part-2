"""
URL configuration for trackit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import  views as user_views
from workout import views
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path( '', user_views.home ,name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('signup/', user_views.user_signup, name ='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/update/', user_views.update_profile, name='update_profile'),
    path('dashboard', user_views.dashboard, name='dashboard'),
    path('edit_workout_plan/<int:workout_id>/', views.edit_workout_plan, name='edit_workout_plan'),
    
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

