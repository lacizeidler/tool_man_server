from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.customer import Customer
from toolmanapi.models.request import Request
from toolmanapi.models.status import Status
from toolmanapi.models.topic import Topic


class RequestView(ViewSet):
    def retrieve(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
            serializer = RequestSerializer(request)
            return Response(serializer.data)
        except Request.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def create(self, request):
        topic = Topic.objects.get(pk=request.data['topic_id'])
        request_status = Status.objects.get(pk=request.data['status_id'])
        customer = Customer.objects.get(user=request.auth.user)
        request = Request.objects.create(
            description=request.data['description'],
            read=request.data['read'],
            timestamp=request.data['timestamp'],
            budget=request.data['budget'],
            customer=customer,
            status=request_status,
            topic=topic
        )
        serializer = RequestSerializer(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        topic = Topic.objects.get(pk=request.data['topic'])
        request_status = Status.objects.get(pk=request.data['status'])

        request = Request.objects.get(pk=pk)
        request.description = request.data['description']
        request.read = request.data['read']
        request.timestamp = request.data['timestamp']
        request.budget = request.data['budget']
        request.topic = topic
        request.status = request_status

        request.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request = Request.objects.get(pk=pk)
        request.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('id', 'description', 'read', 'timestamp', 'budget', 'customer', 'status', 'topic', 'message_request')
        depth = 2
