from django.conf.urls import url
from rest_framework.urls import path
from rest_framework import routers
from testgrej import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^split/$", views.hello_world),
    path("upload/", views.UploadView.as_view(), name="upload"),
    path(
        "download/<str:song>/<str:filename>/",
        views.DownloadView.as_view(),
        name="download",
    ),
]