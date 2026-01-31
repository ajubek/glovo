from .serializers import (UserProfileSerializer,CategoryListSerializer, CategoryDetailSerializer,ContactSerializer,
                          CourierProductSerializer,StoreListSerializer,
                          AddressSerializer,StoreDetailSerializer,
                          StoreMenuListSerializer,StoreMenuDetailSerializer,
                          ProductListSerializer,ProductDetailSerializer,OrderSerializer,
                          ReviewSerializer, CustomLoginSerializers, CustomRegisterSerializers)

from .models import (UserProfile,Category,Contact,
                    CourierProduct,Store,Address,
                    StoreMenu,Product,Order,Review)

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import *
from rest_framework.filters import SearchFilter, OrderingFilter


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = CustomRegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.vaidated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter,]
    pagination_class = CategoryPagination
    filterset_fields = ['category_name']
    search_fields = ['category_name']

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer




class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class CourierProductViewSet(viewsets.ModelViewSet):
    queryset = CourierProduct.objects.all()
    serializer_class = CourierProductSerializer





class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_name','description','owner','created_date']

class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer



class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



class StoreMenuListAPIView(generics.ListAPIView):
    queryset = StoreMenu.objects.all()
    serializer_class = StoreMenuListSerializer


class StoreMenuDetailAPIView(generics.RetrieveAPIView):
    queryset = StoreMenu.objects.all()
    serializer_class = StoreMenuDetailSerializer



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter, OrderingFilter]
    filterset_fields = ['price','product_name','product_descriptions']
    search_fields = ['product_name']
    ordering_fields = ['price']




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    pagination_class = ProductPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'courier','status','products','delivery_address']




class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



