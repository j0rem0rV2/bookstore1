import pytest
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order
from order.serializers.order_serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

    
    product1 = Product.objects.create(
        title="Produto 1",
        description="Descrição do Produto 1",
        price=100,
        active=True
    )
    product2 = Product.objects.create(
        title="Produto 2",
        description="Descrição do Produto 2",
        price=200,
        active=True
    )

    
    data = {
        "products_id": [product1.id, product2.id], 
        "user": user.id, 
    }

    
    serializer = OrderSerializer(data=data)
    assert serializer.is_valid(), serializer.errors  

    
    order = serializer.save()

    
    serialized_order = OrderSerializer(order).data

    assert serialized_order['total'] == 300 
    assert serialized_order['user'] == user.id  