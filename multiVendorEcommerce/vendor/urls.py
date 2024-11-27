from django.urls import path,include
from vendor.views import vendorViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',vendorViewset)

urlpatterns = [
    path('', include(router.urls)),
]