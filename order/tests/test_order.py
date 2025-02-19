import pytest
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order

@pytest.mark.django_db
def test_create_order():
   
    user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )

   
    product = Product.objects.create(
        title="Produto",
        description="Descrição do Produto",
        price=100,
        active=True
    )

   
    order = Order.objects.create(user=user)

   
    order.product.add(product)

   
    assert order.user == user 
    assert product in order.product.all()  