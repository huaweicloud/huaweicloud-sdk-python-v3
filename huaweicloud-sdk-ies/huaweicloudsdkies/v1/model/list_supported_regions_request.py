# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportedRegionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, x_language=None, limit=None, marker=None, sort_key=None, sort_dir=None):
        """ListSupportedRegionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 选择接口返回信息的语言类型，默认为中文\&quot;zh-cn\&quot;
        :type x_language: str
        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        :param sort_key: 排序字段
        :type sort_key: list[str]
        :param sort_dir: 排序方向，取值范围： - desc：降序 - acs：升序
        :type sort_dir: list[str]
        """
        
        

        self._x_language = None
        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def x_language(self):
        """Gets the x_language of this ListSupportedRegionsRequest.

        选择接口返回信息的语言类型，默认为中文\"zh-cn\"

        :return: The x_language of this ListSupportedRegionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListSupportedRegionsRequest.

        选择接口返回信息的语言类型，默认为中文\"zh-cn\"

        :param x_language: The x_language of this ListSupportedRegionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        """Gets the limit of this ListSupportedRegionsRequest.

        每页的数量

        :return: The limit of this ListSupportedRegionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSupportedRegionsRequest.

        每页的数量

        :param limit: The limit of this ListSupportedRegionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSupportedRegionsRequest.

        分页标识

        :return: The marker of this ListSupportedRegionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSupportedRegionsRequest.

        分页标识

        :param marker: The marker of this ListSupportedRegionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        """Gets the sort_key of this ListSupportedRegionsRequest.

        排序字段

        :return: The sort_key of this ListSupportedRegionsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListSupportedRegionsRequest.

        排序字段

        :param sort_key: The sort_key of this ListSupportedRegionsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListSupportedRegionsRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :return: The sort_dir of this ListSupportedRegionsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListSupportedRegionsRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :param sort_dir: The sort_dir of this ListSupportedRegionsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListSupportedRegionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
