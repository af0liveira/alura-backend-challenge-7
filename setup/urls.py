"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import (ReviewsViewSet, SelectedReviewsViewSet,
                       DestinationsViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Jornada Milhas API",
      default_version='v1',
      description="",
      terms_of_service="#",
      contact=openapi.Contact(url="https://www.linkedin.com/in/af0liveira"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('depoimentos', ReviewsViewSet, basename='Reviews')
router.register('depoimentos-home', SelectedReviewsViewSet, basename='SelectedReviews')
router.register('destinos', DestinationsViewSet, basename='Destinations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-reference/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)