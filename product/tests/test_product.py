import pytest

from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Titulo",
        description="Descrição",
        price=1000.00
    )

    assert product.title == "Titulo"
    assert product.description == "Descrição"
    assert product.price == 1000.00
    assert product.id is not None