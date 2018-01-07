import json
import unittest

from tests._base import _IntegrationTestBase


class CategoryIntegrationTestCase(_IntegrationTestBase):

    def test_create_category(self):
        """Test API can create a category (POST request)"""
        res = self.api_client().post('/categories/',
                                     data=json.dumps(self.category),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertDictContainsSubset(self.category, json.loads(res.data))

    def test_get_categories(self):
        """Test API can get a category (GET request)."""
        res = self.api_client().post('/categories/',
                                     data=json.dumps(self.category),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.api_client().get('/categories/')
        self.assertEqual(res.status_code, 200)
        self.assertDictContainsSubset(self.category, json.loads(res.data)[0])

    def test_get_category(self):
        """Test API can get a single category by using it's id."""
        res = self.api_client().post('/categories/',
                                     data=json.dumps(self.category),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        category = json.loads(res.data)
        category_id = category['id']
        res = self.api_client().get(f'/categories/{category_id}')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(category, json.loads(res.data))

    def test_update_category(self):
        """Test API can edit an existing category. (PUT request)"""
        res = self.api_client().post('/categories/',
                                     data=json.dumps(self.category),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        category_id = json.loads(res.data)['id']
        mod_category = {'name': 'Mod Category'}
        res = self.api_client().put(f'/categories/{category_id}',
                                    data=json.dumps(mod_category),
                                    content_type='application/json')
        self.assertEqual(res.status_code, 200)
        res = self.api_client().get(f'/categories/{category_id}')
        self.assertDictContainsSubset(mod_category, json.loads(res.data))

    def test_delete_category(self):
        """Test API can delete an existing category. (DELETE request)."""
        res = self.api_client().post('/categories/',
                                     data=json.dumps(self.category),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        category_id = json.loads(res.data)['id']
        res = self.api_client().delete(f'/categories/{category_id}')
        self.assertEqual(res.status_code, 200)
        result = self.api_client().get(f'/categories/{category_id}')
        self.assertEqual(result.status_code, 404)
