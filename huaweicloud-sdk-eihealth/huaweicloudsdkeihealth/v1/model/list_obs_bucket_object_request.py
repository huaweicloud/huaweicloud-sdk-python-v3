# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketObjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'path': 'str',
        'search_key': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'limit': 'limit',
        'offset': 'offset',
        'path': 'path',
        'search_key': 'search_key'
    }

    def __init__(self, bucket_name=None, limit=None, offset=None, path=None, search_key=None):
        """ListObsBucketObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称
        :type bucket_name: str
        :param limit: 限制量，单次查询总量[1, 1000]，默认100
        :type limit: int
        :param offset: 偏移量，查询起始偏移，默认为0
        :type offset: int
        :param path: 子路径
        :type path: str
        :param search_key: 查询关键词
        :type search_key: str
        """
        
        

        self._bucket_name = None
        self._limit = None
        self._offset = None
        self._path = None
        self._search_key = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if path is not None:
            self.path = path
        if search_key is not None:
            self.search_key = search_key

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListObsBucketObjectRequest.

        桶名称

        :return: The bucket_name of this ListObsBucketObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListObsBucketObjectRequest.

        桶名称

        :param bucket_name: The bucket_name of this ListObsBucketObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def limit(self):
        """Gets the limit of this ListObsBucketObjectRequest.

        限制量，单次查询总量[1, 1000]，默认100

        :return: The limit of this ListObsBucketObjectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListObsBucketObjectRequest.

        限制量，单次查询总量[1, 1000]，默认100

        :param limit: The limit of this ListObsBucketObjectRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListObsBucketObjectRequest.

        偏移量，查询起始偏移，默认为0

        :return: The offset of this ListObsBucketObjectRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListObsBucketObjectRequest.

        偏移量，查询起始偏移，默认为0

        :param offset: The offset of this ListObsBucketObjectRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def path(self):
        """Gets the path of this ListObsBucketObjectRequest.

        子路径

        :return: The path of this ListObsBucketObjectRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListObsBucketObjectRequest.

        子路径

        :param path: The path of this ListObsBucketObjectRequest.
        :type path: str
        """
        self._path = path

    @property
    def search_key(self):
        """Gets the search_key of this ListObsBucketObjectRequest.

        查询关键词

        :return: The search_key of this ListObsBucketObjectRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ListObsBucketObjectRequest.

        查询关键词

        :param search_key: The search_key of this ListObsBucketObjectRequest.
        :type search_key: str
        """
        self._search_key = search_key

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
        if not isinstance(other, ListObsBucketObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
