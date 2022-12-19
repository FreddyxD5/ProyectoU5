from rest_framework import routers
from payment.api import ServiceViewSet


router = routers.DefaultRouter()
router.register("services",ServiceViewSet,basename="services")

urlpatterns = router.urls