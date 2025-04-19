from django.urls import path

from shop.views import index, CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path("", index, name="index"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("product/", ProductListView.as_view(), name="product-list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]


app_name = "shop"
