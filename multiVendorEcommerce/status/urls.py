from django.urls import path,include
from status.views import StatusViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]