from django.urls import path,include
from .views import (UserProfileViewSet, ContactViewSet,
                    CategoryListAPIView, CategoryDetailAPIView,
                     CourierProductViewSet,
                    ProductListAPIView,ProductDetailAPIView,StoreListAPIView,StoreDetailAPIView,
                    StoreMenuListAPIView,StoreMenuDetailAPIView,AddressViewSet,
                    ReviewViewSet,OrderViewSet, CustomLoginView, RegisterAPIView)


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UserProfileViewSet)
router.register(r'contact',ContactViewSet)
router.register(r'courier_product',CourierProductViewSet)
router.register(r'address',AddressViewSet)
router.register(r'review',ReviewViewSet)
router.register(r'order',OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('store_menu/', StoreMenuListAPIView.as_view(), name='stor_menu'),
    path('store_menu/<int:pk>/', StoreMenuDetailAPIView.as_view(), name='store_detail'),
    path('product/', ProductListAPIView.as_view(),name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(),name='product_detail'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),

]