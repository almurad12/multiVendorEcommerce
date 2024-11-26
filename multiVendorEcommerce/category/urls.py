from django.urls import path,include
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewset
router = DefaultRouter()
router.register(r'',CategoryViewset)
urlpatterns = [
    # Include category viewset
    path('', include(router.urls)),
]