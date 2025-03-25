from rest_framework.routers import DefaultRouter

from api.views import UserModelVievSet, UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)

urlpatterns = [
    
]

urlpatterns.extend(router.urls)

