"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from LibreVenta.views import index, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, SignUp, Login, Logout, ProfileUpdate, ProfileCreate, ProfileDetail, MensajeCreate, MensajeDelete, MensajeList, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('about/', about, name="acerca_de_mi"),
    path('product/list', ProductList.as_view(), name="product-list"),
    path('product/<pk>/detail', ProductDetail.as_view(), name="product-detail"),
    path('product/create', ProductCreate.as_view(), name="product-create"),
    path('product/<pk>/update', ProductUpdate.as_view(), name="product-update"),
    path('product/<pk>/delete', ProductDelete.as_view(), name="product-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="actualizar_perfil"),
    path('profile/create/', ProfileCreate.as_view(), name="crear_perfil"),
    path('profile/<pk>/detail', ProfileDetail.as_view(), name="detalles_perfil"),
    path('mensaje/create', MensajeCreate.as_view(), name="crear_mensaje"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('mensaje/list', MensajeList.as_view(), name="lista_mensajes"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
