from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')),

    # #rest-auth
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/signup/', include('rest_auth.registration.urls')),

    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),
    path('hand/', include('hand.urls')),
    # path('boards/', include('boards.urls')),
    # path('tests/', include('testapi.urls')),
]
