from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.request import Request
from toolmanapi.models.request_photo import RequestPhoto
from toolmanapi.models.status import Status


class RequestPhotoView(ViewSet):
    def retrieve(self, request, pk):
        try:
            request_photo = RequestPhoto.objects.get(pk=pk)
            serializer = RequestPhotoSerializer(request_photo)
            return Response(serializer.data)
        except Status.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        request_photos = RequestPhoto.objects.all()
        serializer = RequestPhotoSerializer(request_photos, many=True)
        return Response(serializer.data)

    def create(self, request):
        customer_request = Request.objects.get(pk=request.data['request_id'])
        request_photo = RequestPhoto.objects.create(
            image_url=request.data['image_url'],
            request=customer_request
        )
        serializer = RequestPhotoSerializer(request_photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        request_photo = RequestPhoto.objects.get(pk=pk)
        request_photo.image_url = request.data['image_url']
        request_photo.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request_photo = RequestPhoto.objects.get(pk=pk)
        request_photo.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RequestPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestPhoto
        fields = '__all__'
        depth = 1
