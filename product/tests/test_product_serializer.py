import pytest
from product.models.category import Category
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    
    category1 = Category.objects.create(
        title="Utilidades",
        slug="utilidades",
        description="Categoria para itens de utilidade geral",
        active=True
    )
    category2 = Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Categoria para itens eletrônicos",
        active=True
    )

    
    data = {
        "title": "Título",
        "description": "essa é uma descrição",
        "price": 100,
        "active": True,
        "categories_id": [category1.id, category2.id], 
    }


    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors  


    product_saved = serializer.save()


    serialized_product = ProductSerializer(product_saved).data


    assert serialized_product['title'] == 'Título'
    assert serialized_product['description'] == 'essa é uma descrição'
    assert serialized_product['price'] == 100
    assert serialized_product['active'] is True
    assert serialized_product['category'] == [
        {
            "id": category1.id,
            "title": "Utilidades",
            "slug": "utilidades",
            "description": "Categoria para itens de utilidade geral",
            "active": True
        },
        {
            "id": category2.id,
            "title": "Eletrônicos",
            "slug": "eletronicos",
            "description": "Categoria para itens eletrônicos",
            "active": True
        }
    ] 