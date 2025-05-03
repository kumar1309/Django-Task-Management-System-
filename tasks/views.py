from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_at']
    search_fields = ['title']
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = Task.objects.all()
        
        # Handle date search
        search_date = self.request.query_params.get('search_date', None)
        if search_date:
            try:
                search_date = datetime.strptime(search_date, '%Y-%m-%d').date()
                queryset = queryset.filter(created_at__date=search_date)
            except ValueError:
                pass

        # Handle sorting by date
        sort_by_date = self.request.query_params.get('sort_by_date', None)
        if sort_by_date and sort_by_date.lower() == 'true':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset