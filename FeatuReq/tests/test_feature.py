import json
import unittest
from datetime import datetime
from functools import wraps

from tests._base import _IntegrationTestBase


class FeatureIntegrationTestCase(_IntegrationTestBase):
    """This class represents the feature test case"""

    def _satisfy_contraints(func):
        @wraps(func)
        def wrapped(inst, *args, **kwargs):
            inst.api_client().post('/clients/',
                                   data=json.dumps(inst.client),
                                   content_type='application/json')
            inst.api_client().post('/categories/',
                                   data=json.dumps(inst.category),
                                   content_type='application/json')
            return func(inst, *args, **kwargs)
        return wrapped

    @_satisfy_contraints
    def test_create_feature(self):
        """Test API can create a feature (POST request)"""
        res = self.api_client().post('/features/',
                                     data=json.dumps(self.feature),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertDictContainsSubset(self.feature, json.loads(res.data))

    @_satisfy_contraints
    def test_get_features(self):
        """Test API can get a feature (GET request)."""
        res = self.api_client().post('/features/',
                                     data=json.dumps(self.feature),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.api_client().get('/features/')
        self.assertEqual(res.status_code, 200)
        self.assertDictContainsSubset(self.feature, json.loads(res.data)[0])

    @_satisfy_contraints
    def test_get_feature(self):
        """Test API can get a single feature by using it's id."""
        res = self.api_client().post('/features/',
                                     data=json.dumps(self.feature),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        feature = json.loads(res.data)
        feat_id = feature['id']
        res = self.api_client().get(f'/features/{feat_id}')
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(feature, json.loads(res.data))

    @_satisfy_contraints
    def test_update_feature(self):
        """Test API can edit an existing feature. (PUT request)"""
        res = self.api_client().post('/features/',
                                     data=json.dumps(self.feature),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        feat_id = json.loads(res.data)['id']
        mod_feat = {
            'title': 'Test feature update',
            'description': 'test feature description update',
            'priority': 2,
            'category': 1,
            'client': 1,
            'target_date': datetime(2021, 1, 1).isoformat(),
            'complete': True,
        }
        res = self.api_client().put(f'/features/{feat_id}',
                                    data=json.dumps(mod_feat),
                                    content_type='application/json')
        self.assertEqual(res.status_code, 200)
        res = self.api_client().get(f'/features/{feat_id}')
        self.assertDictContainsSubset(mod_feat, json.loads(res.data))

    @_satisfy_contraints
    def test_delete_feature(self):
        """Test API can delete an existing feature. (DELETE request)."""
        res = self.api_client().post('/features/',
                                     data=json.dumps(self.feature),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        feat_id = json.loads(res.data)['id']
        res = self.api_client().delete(f'/features/{feat_id}')
        self.assertEqual(res.status_code, 200)
        result = self.api_client().get(f'/features/{feat_id}')
        self.assertEqual(result.status_code, 404)
