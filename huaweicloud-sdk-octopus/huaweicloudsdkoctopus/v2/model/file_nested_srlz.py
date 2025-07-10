# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileNestedSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'sha256': 'str',
        'created_at': 'float',
        'updated_at': 'float',
        'path': 'str',
        'bucket': 'str',
        'filename': 'str',
        'ready': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'sha256': 'sha256',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'path': 'path',
        'bucket': 'bucket',
        'filename': 'filename',
        'ready': 'ready'
    }

    def __init__(self, url=None, sha256=None, created_at=None, updated_at=None, path=None, bucket=None, filename=None, ready=None):
        r"""FileNestedSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param sha256: 
        :type sha256: str
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param path: 
        :type path: str
        :param bucket: 
        :type bucket: str
        :param filename: 
        :type filename: str
        :param ready: 
        :type ready: bool
        """
        
        

        self._url = None
        self._sha256 = None
        self._created_at = None
        self._updated_at = None
        self._path = None
        self._bucket = None
        self._filename = None
        self._ready = None
        self.discriminator = None

        self.url = url
        self.sha256 = sha256
        self.created_at = created_at
        self.updated_at = updated_at
        self.path = path
        self.bucket = bucket
        self.filename = filename
        if ready is not None:
            self.ready = ready

    @property
    def url(self):
        r"""Gets the url of this FileNestedSrlz.

        :return: The url of this FileNestedSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this FileNestedSrlz.

        :param url: The url of this FileNestedSrlz.
        :type url: str
        """
        self._url = url

    @property
    def sha256(self):
        r"""Gets the sha256 of this FileNestedSrlz.

        :return: The sha256 of this FileNestedSrlz.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this FileNestedSrlz.

        :param sha256: The sha256 of this FileNestedSrlz.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def created_at(self):
        r"""Gets the created_at of this FileNestedSrlz.

        :return: The created_at of this FileNestedSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this FileNestedSrlz.

        :param created_at: The created_at of this FileNestedSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this FileNestedSrlz.

        :return: The updated_at of this FileNestedSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this FileNestedSrlz.

        :param updated_at: The updated_at of this FileNestedSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def path(self):
        r"""Gets the path of this FileNestedSrlz.

        :return: The path of this FileNestedSrlz.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this FileNestedSrlz.

        :param path: The path of this FileNestedSrlz.
        :type path: str
        """
        self._path = path

    @property
    def bucket(self):
        r"""Gets the bucket of this FileNestedSrlz.

        :return: The bucket of this FileNestedSrlz.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this FileNestedSrlz.

        :param bucket: The bucket of this FileNestedSrlz.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def filename(self):
        r"""Gets the filename of this FileNestedSrlz.

        :return: The filename of this FileNestedSrlz.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this FileNestedSrlz.

        :param filename: The filename of this FileNestedSrlz.
        :type filename: str
        """
        self._filename = filename

    @property
    def ready(self):
        r"""Gets the ready of this FileNestedSrlz.

        :return: The ready of this FileNestedSrlz.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        r"""Sets the ready of this FileNestedSrlz.

        :param ready: The ready of this FileNestedSrlz.
        :type ready: bool
        """
        self._ready = ready

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
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileNestedSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
