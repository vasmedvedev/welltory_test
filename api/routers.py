from rest_framework import routers
from api import views


router = routers.DefaultRouter()

router.register(r'sleep', views.SleepViewSet)
router.register(r'steps', views.StepsViewSet)
router.register(r'geo', views.GeoViewSet)

urlpatterns = router.urls
