from django.urls import path
from .views import Sellerregister,buyerregister

#jwt authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
path('sellerregistration/',Sellerregister),
path('buyerregistration/',buyerregister),
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]