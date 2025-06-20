from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('product/<int:pk>', views.product_page)
]
