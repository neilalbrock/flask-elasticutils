==================
Flask-ElasticUtils
==================

Integrates ``elasticutils`` with Flask (a very thin wrapper).

Installation
------------

Flask-ElasticUtils is pip installable::

	$ pip install Flask-ElasticUtils

Configure
---------

The only configuration is ``ELASTICSEARCH_URL``, defaults to ``localhost:9200``

Usage
-----

Import the extension into your Flask project and initialise::

	from flask.ext.elasticutils import ElasticUtils

	es = ElasticUtils(app)

Development
-----------

Source code is hosted on `GitHub <https://github.com/neilalbrock/flask-elasticutils>`_ (contributions are welcome).
