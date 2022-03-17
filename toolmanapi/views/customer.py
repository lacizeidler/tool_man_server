from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, status
from toolmanapi.models.customer import Customer
from toolmanapi.models.status import Status
from rest_framework.decorators import action


class CustomerView(ViewSet):
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Status.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def currentcustomer(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1
