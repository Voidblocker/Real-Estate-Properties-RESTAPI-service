from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
# Create your views here.
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserCreateSerializer, AgentNameSerializer,AgentDetailsSerializer , CommentSerializer , AgentRatingSerializer
=======
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserCreateSerializer, PropertyTitleSerializer, AgentNameSerializer,AgentDetailsSerializer
>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374
from .models import Agent, Property
from .serializers import PropertySerializer,PropertyTitleSerializer

class UserViewSet(DjoserUserViewSet):
    queryset = Agent.objects.all()
    serializer_class = UserCreateSerializer

class AgentPropertiesView(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        agent_id = self.kwargs['agent_id']
        return Property.objects.filter(id=agent_id)

class CreatePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if property.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if property.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

<<<<<<< HEAD


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]


=======
class AgentNameViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentNameSerializer
    permission_classes = [AllowAny]


class AgentDetailsViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentDetailsSerializer
    permission_classes = [AllowAny]

>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374
class PropertyListViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertyTitleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        titles = [property['title'] for property in serializer.data]
        return Response(titles)
    
<<<<<<< HEAD
class AgentNameViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentNameSerializer
    permission_classes = [AllowAny]

class AgentDetailsViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentDetailsSerializer
    permission_classes = [AllowAny]
=======
class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374

class PropertySearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Retrieve the query parameters from the request
        location = self.request.query_params.get('location')
        property_type = self.request.query_params.get('property_type')
        min_price = self.request.query_params.get('price')
        max_price = self.request.query_params.get('price')

        # Apply filters based on query parameters
        if location:
            queryset = queryset.filter(location__icontains=location)
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
<<<<<<< HEAD
    

class AgentCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer

class AgentRatingCreateView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentRatingSerializer

    def create(self, request, *args, **kwargs):
        agent_id = self.kwargs['agent_id']
        try:
            agent = self.queryset.get(pk=agent_id)
        except Agent.DoesNotExist:
            raise ValidationError("Agent not found.")
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.validated_data['rating']

        agent.rating = rating
        agent.save()

        return Response({'success': 'Rating saved successfully.'}, status=201)
=======
>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374

