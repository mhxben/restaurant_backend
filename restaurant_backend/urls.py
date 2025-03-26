from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from orders.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'table',TableViewSet)
router.register(r'custom-category', CustomizationCategoryViewSet)
router.register(r'order',OrderViewSet)
router.register(r'product',ProductViewSet)
router.register(r'custom',CustomizationViewSet)
router.register(r'orderItem',OrderItemViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant Backend API",
      default_version='v1',
      description='ResPal API',
   ),
   public=True,
   permission_classes=(AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/" , include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]