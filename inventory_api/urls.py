from django.urls import path
from . import views

urlpatterns = [
    path('get_product/', views.ProductView.as_view()),
    path('add_product/', views.AddProduct.as_view()),
    path('update_product/<int:pk>/', views.UpdateProduct.as_view()),
    path('delete_product/<int:pk>/', views.DeleteProduct.as_view()),
]
