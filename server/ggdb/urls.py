#!/usr/bin/env python
# ggdb/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ggdb.apis import SystemViewSet

router = DefaultRouter()
router.register(r"system", SystemViewSet, basename="system")

urlpatterns = [
    path("", include(router.urls)),
]