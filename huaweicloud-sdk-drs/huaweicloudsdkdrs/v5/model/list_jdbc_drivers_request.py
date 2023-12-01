# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJdbcDriversRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'x_language': 'X-Language'
    }

    def __init__(self, limit=None, offset=None, x_language=None):
        """ListJdbcDriversRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。默认为10
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._limit = None
        self._offset = None
        self._x_language = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if x_language is not None:
            self.x_language = x_language

    @property
    def limit(self):
        """Gets the limit of this ListJdbcDriversRequest.

        每页显示的条目数量。默认为10

        :return: The limit of this ListJdbcDriversRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJdbcDriversRequest.

        每页显示的条目数量。默认为10

        :param limit: The limit of this ListJdbcDriversRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListJdbcDriversRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this ListJdbcDriversRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJdbcDriversRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this ListJdbcDriversRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListJdbcDriversRequest.

        请求语言类型。

        :return: The x_language of this ListJdbcDriversRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListJdbcDriversRequest.

        请求语言类型。

        :param x_language: The x_language of this ListJdbcDriversRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListJdbcDriversRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
