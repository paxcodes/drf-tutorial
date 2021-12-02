from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

# Because we are using viewsets instead of views, we can automatically generate the
# URL conf for our API, by simply registering the viewsets with a router class.
# If we need more control over the API URLs we can drop down to using regular
# class-based views, and writing the URL conf explicitly.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # Include default login and logout views for use with the browsable API.
    # This is optional if your API requires authentication and you want to use the
    # browsable API.
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
