# product/tests/test_product_viewset.py
import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.product = ProductFactory(
            title='pro controller',
            price=200.00,
            active=True
        )

    def test_get_all_product(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        product_data = json.loads(response.content)
        
        # Verifica se a resposta é paginada
        if 'results' in product_data:
            results = product_data['results']
        else:
            results = product_data
        
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['title'], self.product.title)
        self.assertEqual(results[0]['price'], str(self.product.price))  # DRF pode serializar Decimal como string
        self.assertEqual(results[0]['active'], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories': [category.id]  # Campo correto para relacionamento
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(title='notebook')
        self.assertEqual(created_product.title, 'notebook')
        self.assertEqual(float(created_product.price), 800.00)  # Comparação segura com float
