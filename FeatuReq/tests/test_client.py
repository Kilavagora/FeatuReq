import json
import unittest

from tests._base import _IntegrationTestBase


class ClientIntegrationTestCase(_IntegrationTestBase):

    def test_create_client(self):
        """Test API can create a client (POST request)"""
        res = self.api_client().post('/clients/',
                                     data=json.dumps(self.client),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertDictContainsSubset(self.client, json.loads(res.data))

    def test_get_clients(self):
        """Test API can get a client (GET request)."""
        res = self.api_client().post('/clients/',
                                     data=json.dumps(self.client),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.api_client().get('/clients/')
        self.assertEqual(res.status_code, 200)
        self.assertDictContainsSubset(self.client, json.loads(res.data)[0])

    def test_get_client(self):
        """Test API can get a single client by using it's id."""
        res = self.api_client().post('/clients/',
                                     data=json.dumps(self.client),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        client = json.loads(res.data)
        client_id = client['id']
        res = self.api_client().get(f'/clients/{client_id}')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(client, json.loads(res.data))

    def test_update_client(self):
        """Test API can edit an existing client. (PUT request)"""
        res = self.api_client().post('/clients/',
                                     data=json.dumps(self.client),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        client_id = json.loads(res.data)['id']
        mod_client = {'name': 'Mod Client'}
        res = self.api_client().put(f'/clients/{client_id}',
                                    data=json.dumps(mod_client),
                                    content_type='application/json')
        self.assertEqual(res.status_code, 200)
        res = self.api_client().get(f'/clients/{client_id}')
        self.assertDictContainsSubset(mod_client, json.loads(res.data))

    def test_delete_client(self):
        """Test API can delete an existing client. (DELETE request)."""
        res = self.api_client().post('/clients/',
                                     data=json.dumps(self.client),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        client_id = json.loads(res.data)['id']
        res = self.api_client().delete(f'/clients/{client_id}')
        self.assertEqual(res.status_code, 200)
        result = self.api_client().get(f'/clients/{client_id}')
        self.assertEqual(result.status_code, 404)