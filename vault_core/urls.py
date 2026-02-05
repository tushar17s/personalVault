from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
        path('resources/', views.first_api ),
        path('register/', views.register_api ),
        # path('login/', views.login_api ),
        # jwt provides its own login endpoint like api/token to authenticate , validate user and generates the token
        path('tag/', views.tag_api ),
        path('resources/<int:id>/', views.resource_operation_api ),
]


urlpatterns += [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += [

    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
