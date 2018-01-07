import unittest
from datetime import datetime
from app import create_app
from app.models import db


class _IntegrationTestBase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.api_client = self.app.test_client
        self.feature = {
            'title': 'Test feature',
            'description': 'test feature description',
            'priority': 2,
            'category': 1,
            'client': 1,
            'target_date': datetime(2020, 1, 1).isoformat(),
            'complete': False,
        }

        self.client = {'name': 'Test Client'}

        self.category = {'name': 'Test Category'}

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
