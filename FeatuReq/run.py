import os
from datetime import datetime
from flask_migrate import Migrate
from app import create_app
from app.models import db
from app.models.feature import Feature
from app.models.client import Client
from app.models.category import Category


app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)


@app.cli.command()
def test():
    import unittest
    from tests import test_feature, test_category, test_client
    feature_suite = unittest.TestLoader().loadTestsFromModule(test_feature)
    category_suite = unittest.TestLoader().loadTestsFromModule(test_category)
    client_suite = unittest.TestLoader().loadTestsFromModule(test_client)
    suite = unittest.TestSuite([feature_suite, category_suite, client_suite])
    unittest.TextTestRunner(verbosity=2).run(suite)


@app.cli.command()
def dbcreate():
    db.create_all()

    client = Client("Placeholder Client")
    category = Category("Placeholder Category")

    client.save()
    category.save()

    client_id = client.id
    category_id = category.id

    feature = Feature("Demo Feature", "Demo Feature Description",
                      1, client_id, category_id, datetime(2018, 1, 1))
    feature.save()

if __name__ == '__main__':
    app.run()
