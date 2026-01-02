#!/usr/bin/env python
# ggdb/apis.py

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from config.selectors import get_system_status


class SystemViewSet(ViewSet):
    """
    API-only ViewSet.
    No templates. No UI.
    """
    
    @swagger_auto_schema(
        responses={200: "Success", 400: "Bad request", 500: "Server Error"},
        tags=["System"],
    )
    def list(self, request):
        return Response({
            "service": "ggdb",
            "status": "ok",
        })
    
    @swagger_auto_schema(
        responses={200: "Success", 400: "Bad request", 500: "Server Error"},
        tags=["System"],
    )
    @action(detail=False, methods=["get"])
    def health(self, request):
        return Response(get_system_status())
