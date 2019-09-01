from my_api.api.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', StudentViewSet, basename='my_api')
urlpatterns = router.urls
