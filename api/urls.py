from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet
import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/', views.GetMessageView.as_view())
]