from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.customer import Customer
from toolmanapi.models.request import Request
from toolmanapi.models.message import Message


class MessageView(ViewSet):
    def retrieve(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        request = Request.objects.get(pk=request.data['request_id'])
        sender = Customer.objects.get(user=request.auth.user)
        message = Message.objects.create(
            message=request.data['message'],
            read=request.data['read'],
            timestamp=request.data['timestamp'],
            budget=request.data['budget'],
            sender=sender,
            request=request
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        request = Request.objects.get(pk=request.data['request'])

        message = Message.objects.get(pk=pk)
        message.message = request.data['message']
        message.read = request.data['read']
        message.timestamp = request.data['timestamp']
        message.request = request

        message.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        depth = 2
