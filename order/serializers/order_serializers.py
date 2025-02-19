from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)  # Somente leitura
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True  # Gravável
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        # Calcula o total somando os preços dos produtos
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ['id', 'product', 'products_id', 'total', 'user']
        extra_kwargs = {'product': {'required':False}}

    #Aula 6: Serializers e ViewSets // ele adiciona o que já existia nas aulas anteriores:

    def create(self, validated_data):
        # Remove os dados dos produtos do validated_data
        products_data = validated_data.pop('products_id')

        # Cria o pedido com o usuário e outros campos
        order = Order.objects.create(**validated_data)

        # Associa os produtos ao pedido
        for product in products_data:
            order.product.add(product)

        return order