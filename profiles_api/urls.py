from unicodedata import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
#addes the path to the router  for api acccess
router.register('hello-viewset',views.HelloViewSet, basename='hello-viewset')
urlpatterns = [
    path("hello-api",views.HElloAPIView.as_view(),name="hello_view"),
    path("",include(router.urls),name="api"),
]
