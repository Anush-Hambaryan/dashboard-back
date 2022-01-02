from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from .models import StandardJob, Job5
from .serializers import StandardJobSerializer, Job5Serializer


# Create your views here.
class StandardJobViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = StandardJobSerializer
    permission_classes = [IsAuthenticated]

    filter_fields = {
        'owner': ['exact'],
        'job_type': ['exact'],
    }

    def get_queryset(self):
        user = self.request.user
        return StandardJob.objects.filter(owner__level__contains=user.level)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Job5ViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Job5.objects.all()
    serializer_class = Job5Serializer
    permission_classes = [IsAuthenticated]

    filter_fields = {
        'owner': ['exact'],
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)