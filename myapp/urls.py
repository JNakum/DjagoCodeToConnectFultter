from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # views ko import karna hoga
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),  # ItemViewSet ko include karenge
    path('api/items/', views.create_item, name='create_item'),  # create_item ko map karenge
    path('api/items/<int:pk>/delete/', views.delete_item, name='delete_item'), 
    path('api/items/<int:pk>/', views.update_item, name='update_item'),
]
