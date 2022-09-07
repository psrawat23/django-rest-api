from unicodedata import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
#addes the path to the router  for api acccess
router.register('hello-viewset',views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet) #when using modelview set basename is option deafult name= model name
router.register('feed',views.ProfileItemfeedViewSet)
urlpatterns = [
    path("hello-api",views.HElloAPIView.as_view(),name="hello_view"),
    path("login/",views.UserLoginApiView.as_view(),name="login"),
    path("",include(router.urls),name="api"),
]
