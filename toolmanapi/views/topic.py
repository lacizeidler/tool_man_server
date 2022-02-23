from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.topic import Topic


class TopicView(ViewSet):
    def retrieve(self, request, pk):
        try:
            topic = Topic.objects.get(pk=pk)
            serializer = TopicSerializer(topic)
            return Response(serializer.data)
        except Topic.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def create(self, request):
        topic = Topic.objects.create(
            label=request.data['label']
        )
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        topic = Topic.objects.get(pk=pk)
        topic.label = request.data['label']
        topic.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        topic = Topic.objects.get(pk=pk)
        topic.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1
