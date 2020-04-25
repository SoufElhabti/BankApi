from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register()
router.register('api/transactions',TransactionViewSet,'transactions')
