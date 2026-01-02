#!/usr/bin/env python
# ggdb/apis.py

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .selectors import get_system_status


class SystemViewSet(ViewSet):
    """
    API-only ViewSet.
    No templates. No UI.
    """

    def list(self, request):
        return Response({
            "service": "ggdb",
            "status": "ok",
        })

    @action(detail=False, methods=["get"])
    def health(self, request):
        return Response(get_system_status())
