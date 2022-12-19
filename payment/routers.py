from rest_framework import routers
from payment.api import ServiceViewSet,PaymentUserViewSet, ExpiredPaymentViewSet


router = routers.DefaultRouter()
router.register("services",ServiceViewSet,basename="services")
router.register("payment_user",PaymentUserViewSet,basename="services")
router.register("expired_payment",ExpiredPaymentViewSet,basename="services")

urlpatterns = router.urls