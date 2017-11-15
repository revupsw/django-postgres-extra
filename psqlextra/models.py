from django.db import models

from .manager import PostgresManager


class PostgresModel(models.Model):
    """Base class for for taking advantage of PostgreSQL specific features."""

    class Meta(object):
        abstract = True
        base_manager_name = 'objects'

    objects = PostgresManager()
