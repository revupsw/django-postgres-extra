from django.db import models

from .manager import PostgresManager


class PostgresModel(models.Model):
    """Base class for for taking advantage of PostgreSQL specific features."""

    class Meta(object):
        abstract = True
        _base_manager = 'objects'

    objects = PostgresManager()
