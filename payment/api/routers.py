from rest_framework import routers
from payment.api.api import ServiceViewSet,PaymentUserViewSet, ExpiredPaymentViewSet


router = routers.DefaultRouter()
router.register("services",ServiceViewSet,basename="services")
router.register("payment_user",PaymentUserViewSet,basename="payment_user")
router.register("expired_payment",ExpiredPaymentViewSet,basename="expired_payment")

urlpatterns = router.urls