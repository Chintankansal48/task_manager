from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.all() if self.request.method == 'GET' else Task.objects.filter(user=self.request.user)

        completed = self.request.query_params.get('completed')
        if completed is not None:
            queryset = queryset.filter(completed=(completed.lower() == 'true'))

        created_after = self.request.query_params.get('created_after')
        if created_after:
            queryset = queryset.filter(created_at__gte=parse_date(created_after))

        return queryset
