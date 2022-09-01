from django.urls import path
from profiles_api import views

urlpatterns = [
    path("",views.HElloAPIView.as_view(),name="hello_view")
]
