import pytest

from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    data = {
        "title": "Título",
        "slug": "esse-e-um-slug",
        "description": "essa é uma descrição",
        "active": True,
    }

    serializer = CategorySerializer(data=data)
    assert serializer.is_valid(), serializer.errors 
    category = serializer.save()

    serialized_category = CategorySerializer(category).data
    assert serialized_category['title'] == 'Título'
    assert serialized_category['slug'] == 'esse-e-um-slug'
    assert serialized_category['description'] == 'essa é uma descrição'
    assert serialized_category['active'] == True