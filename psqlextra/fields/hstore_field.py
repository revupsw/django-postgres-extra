from typing import List, Tuple, Union

from django.contrib.postgres.fields import HStoreField as DjangoHStoreField


class HStoreField(DjangoHStoreField):
    """Improved version of Django's :see:HStoreField that
    adds support for database-level constraints.

    Notes:
        - For the implementation of uniqueness, see the
          custom database back-end.
    """

    def __init__(self, *args, **kwargs):
        if 'required' in kwargs: required = kwargs['required']; del kwargs['required']
        else: required = None
        if 'uniqueness' in kwargs: uniqueness = kwargs['uniqueness']; del kwargs['uniqueness']
        else: uniqueness = None
        """Initializes a new instance of :see:HStoreField."""

        super(HStoreField, self).__init__(*args, **kwargs)

        self.uniqueness = uniqueness
        self.required = required

    def deconstruct(self):
        """Gets the values to pass to :see:__init__ when
        re-creating this object."""

        name, path, args, kwargs = super(
            HStoreField, self).deconstruct()

        kwargs['uniqueness'] = self.uniqueness or []
        kwargs['required'] = self.required or []

        return name, path, args, kwargs
