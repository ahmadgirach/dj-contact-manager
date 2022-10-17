from rest_framework.routers import DefaultRouter

from base.views import ContactViewSet

router = DefaultRouter()
router.register("contacts", ContactViewSet, basename="contacts")

urlpatterns = router.urls
