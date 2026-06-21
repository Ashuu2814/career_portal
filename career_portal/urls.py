from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import create_admin

from accounts.views import (
    home,
    signup,
    user_login,
    user_logout,
    dashboard,
    profile,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('signup/', signup, name='signup'),

    path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),

    path('profile/', profile, name='profile'),

    path(
    'create-admin/',
    create_admin,
),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)