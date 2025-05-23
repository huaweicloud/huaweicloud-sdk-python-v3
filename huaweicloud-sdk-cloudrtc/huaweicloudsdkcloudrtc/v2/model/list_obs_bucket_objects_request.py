# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'prefix': 'str',
        'type': 'str',
        'location': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'prefix': 'prefix',
        'type': 'type',
        'location': 'location'
    }

    def __init__(self, bucket=None, prefix=None, type=None, location=None):
        r"""ListObsBucketObjectsRequest

        The model defined in huaweicloud sdk

        :param bucket: 要查询的桶名
        :type bucket: str
        :param prefix: 对象名前缀，可以理解为文件夹路径
        :type prefix: str
        :param type: 查询类似，取值“folders”“objects”前者为查询目录，后者为查询对象
        :type type: str
        :param location: 查询bucket所在的region
        :type location: str
        """
        
        

        self._bucket = None
        self._prefix = None
        self._type = None
        self._location = None
        self.discriminator = None

        self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        self.type = type
        self.location = location

    @property
    def bucket(self):
        r"""Gets the bucket of this ListObsBucketObjectsRequest.

        要查询的桶名

        :return: The bucket of this ListObsBucketObjectsRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ListObsBucketObjectsRequest.

        要查询的桶名

        :param bucket: The bucket of this ListObsBucketObjectsRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        r"""Gets the prefix of this ListObsBucketObjectsRequest.

        对象名前缀，可以理解为文件夹路径

        :return: The prefix of this ListObsBucketObjectsRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListObsBucketObjectsRequest.

        对象名前缀，可以理解为文件夹路径

        :param prefix: The prefix of this ListObsBucketObjectsRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def type(self):
        r"""Gets the type of this ListObsBucketObjectsRequest.

        查询类似，取值“folders”“objects”前者为查询目录，后者为查询对象

        :return: The type of this ListObsBucketObjectsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListObsBucketObjectsRequest.

        查询类似，取值“folders”“objects”前者为查询目录，后者为查询对象

        :param type: The type of this ListObsBucketObjectsRequest.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        r"""Gets the location of this ListObsBucketObjectsRequest.

        查询bucket所在的region

        :return: The location of this ListObsBucketObjectsRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ListObsBucketObjectsRequest.

        查询bucket所在的region

        :param location: The location of this ListObsBucketObjectsRequest.
        :type location: str
        """
        self._location = location

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
        if not isinstance(other, ListObsBucketObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
