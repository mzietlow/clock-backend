from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


from api.tasks import async_5_user_creation
from pytz import datetime
from api.models import Contract, Shift, Report

from api.serializers import ContractSerializer, ShiftSerializer, ReportSerializer

# Proof of Concept that celery works


def index(request):
    async_5_user_creation.delay()
    return HttpResponse("A Dummy site.")


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    name = "contracts"

    def get_queryset(self):
        queryset = super(ContractViewSet, self).get_queryset()
        return queryset.filter(user__id=self.request.user.id)

    @action(detail=True, url_name="shifts", url_path="shifts", methods=["get"])
    def get_shifts_list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ShiftSerializer(instance.shifts, many=True)
        return Response(serializer.data)


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    name = "shifts"

    def get_queryset(self):
        queryset = super(ShiftViewSet, self).get_queryset()
        return queryset.filter(user__id=self.request.user.id)

    def list_month_year(self, request, month=None, year=None, *args, **kwargs):
        queryset = self.get_queryset().filter(started__month=month, started__year=year)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    name = "reports"

    def get_queryset(self):
        queryset = super(ReportViewSet, self).get_queryset()
        return queryset.filter(user__id=self.request.user.id)

    @action(detail=False, url_name="get_current", url_path="get_current")
    def get_current(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        queryset = self.get_queryset()
        instance = get_object_or_404(
            queryset, month_year__month=now.month, month_year__year=now.year
        )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
