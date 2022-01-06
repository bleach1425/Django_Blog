"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


from Blog_data.views import PostListView, PostDetailView, about, handler404, handler500, \
                            login, test, BootStrip
from rest_framework.routers import DefaultRouter
from Blog_data import views

router = DefaultRouter()
router.register('Blog_article', views.PostViewSet)
# router.register('')

error_handler404 = handler404
error_handler500 = handler500

urlpatterns = [
    # nav
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('about/', about),
    # ---------------------------------------------------- #
    # auth
    path('login', login),
    path('logout/', LogoutView),
    # ---------------------------------------------------- #
    path('', PostListView.as_view()),
    path('<pk>', PostDetailView.as_view()),
    # ---------------------------------------------------- #
    path('test/', test),
    path('BootStrip/', BootStrip),
    # ---------------------------------------------------- #
    path('accounts/', include('allauth.urls')),
    # ---------------------------------------------------- #
]
