from django.urls import path, include
from documents import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"doc", views.DocumentView)
router.register(r"types", views.DocumenttypesView)
router.register(r"classification", views.DocumentclassificationView)

urlpatterns = [
    path("", include(router.urls)),
]
