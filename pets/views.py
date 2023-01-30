from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404

from .models import Pet
from .serializers import PetSerializer

class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()
        serializer = PetSerializer(instance=pets, many=True)
        
        return Response({"animals": serializer.data}, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return(Response.serializer.data)
    
    def delete(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)