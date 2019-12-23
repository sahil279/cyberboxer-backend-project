from django.contrib import admin
from django.urls import path,include
from .views import Product_list_View
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.Product_list_View.as_view(),name='home'),
    path('product/<int:pk>/detail',views.ProductDetailView.as_view(),name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
