from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.status import Status


class StatusView(ViewSet):
    def retrieve(self, request, pk):
        try:
            request_status = Status.objects.get(pk=pk)
            serializer = StatusSerializer(request_status)
            return Response(serializer.data)
        except Status.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        request_statuses = Status.objects.all()
        serializer = StatusSerializer(request_statuses, many=True)
        return Response(serializer.data)

    def create(self, request):
        request_status = Status.objects.create(
            label=request.data['label']
        )
        serializer = StatusSerializer(request_status)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        request_status = Status.objects.get(pk=pk)
        request_status.label = request.data['label']
        request_status.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request_status = Status.objects.get(pk=pk)
        request_status.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'
        depth = 1
