

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import IntroductionViewSet

router = DefaultRouter()
router.register(r'introductions', IntroductionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Other URL patterns if any
]
