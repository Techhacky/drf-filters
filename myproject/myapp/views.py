from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Introduction
from .serializers import IntroductionSerializer
from rest_framework import status
from rest_framework.response import Response
# Introduction viewset
class IntroductionViewSet(ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['=name', 'intro']
    ordering_fields = ['name', 'id']
    ordering = ['id']

  
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if 'search' in request.query_params and not queryset.exists():
         
            return Response({"message": "Searched item not foun."}, status=status.HTTP_404_NOT_FOUND)

        if 'ordering' in request.query_params and not queryset.exists():
         
            return Response({"message": "Ordered item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        for field_filter in self.filterset_fields:
            if field_filter in request.query_params and not queryset.exists():
               
                return Response({"message": f"{field_filter} NAME  or ID does not exist "}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
  class ModelDeleteView(DeleteView):
        model = Model
        template_name = ".html"
    





