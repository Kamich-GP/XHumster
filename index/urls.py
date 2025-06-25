from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('product/<int:pk>', views.product_page),
    path('search', views.search),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('to-cart/<int:pk>', views.add_to_cart),
    path('del-from-cart/<int:pk>', views.del_from_cart),
    path('cart', views.show_cart)
]
