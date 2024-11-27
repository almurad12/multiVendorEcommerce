from django.urls import path,include
from product.views import ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]