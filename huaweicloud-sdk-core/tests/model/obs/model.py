# coding: utf-8
import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class _Model(object):
    openapi_types = {}

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))

        return result

    def to_str(self):
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


class ListBucketsResponse(_Model):
    sensitive_list = []

    openapi_types = {
        'owner': 'Owner',
        'buckets': 'Buckets'
    }

    attribute_map = {
        'owner': 'Owner',
        'buckets': 'Buckets'
    }

    def __init__(self, owner=None, buckets=None):
        super(ListBucketsResponse, self).__init__()

        self._owner = None
        self._buckets = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if buckets is not None:
            self.buckets = buckets

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def buckets(self):
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        self._buckets = buckets


class Owner(_Model):
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'display_name': 'DisplayName'
    }

    def __init__(self, id=None, display_name=None):
        self._id = None
        self._display_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name


class Buckets(_Model):
    sensitive_list = []

    openapi_types = {
        'bucket': 'list[Bucket]'
    }

    attribute_map = {
        'bucket': 'Bucket'
    }

    def __init__(self, bucket=None):
        self._bucket = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket

    @property
    def bucket(self):
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        self._bucket = bucket


class Bucket(_Model):
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'creation_date': 'str',
        'location': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'creation_date': 'CreationDate',
        'location': 'Location'
    }

    def __init__(self, name=None, creation_date=None, location=None):
        self._name = None
        self._creation_date = None
        self._location = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creation_date is not None:
            self.creation_date = creation_date
        if location is not None:
            self.location = location

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location
