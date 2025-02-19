import pytest

from product.models import Category

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title = "Título",
        slug = "Slug teste",
        description = "Descrição",
        active = True
    )
    
    assert category.title == "Título"
    assert category.slug == "Slug teste"
    assert category.description == "Descrição"
    assert category.active == True
