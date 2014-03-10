import os

from flask import current_app

from elasticutils import S


class ElasticUtils(object):
    """
    A thin wrapper around elasticutils
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ELASTICSEARCH_URL',
                os.environ.get('ELASTICSEARCH_URL', 'http://localhost:9200/'))

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['elasticutils'] = S().es(urls=[app.config['ELASTICSEARCH_URL']])

    def __getattr__(self, item):
        if not 'elasticutils' in current_app.extensions.keys():
            raise Exception('not initialised, did you forget to call init_app?')
        return getattr(current_app.extensions['elasticutils'], item)
