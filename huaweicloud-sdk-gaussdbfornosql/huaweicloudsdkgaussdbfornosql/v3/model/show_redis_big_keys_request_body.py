# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRedisBigKeysRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'key_types': 'list[str]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'key_types': 'key_types'
    }

    def __init__(self, offset=None, limit=None, key_types=None):
        """ShowRedisBigKeysRequestBody

        The model defined in huaweicloud sdk

        :param offset: 索引位置偏移量，表示从查询到的大key列表偏移offset条数据后查询对应的大key信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从第一条大key开始查询。
        :type offset: int
        :param limit: 查询个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条大key。
        :type limit: int
        :param key_types: 大key的类型,一个字符串列表,支持\&quot;string\&quot;,\&quot;hash\&quot;,\&quot;zset\&quot;,\&quot;set\&quot;,\&quot;list\&quot;,\&quot;stream\&quot;六种类型。
        :type key_types: list[str]
        """
        
        

        self._offset = None
        self._limit = None
        self._key_types = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if key_types is not None:
            self.key_types = key_types

    @property
    def offset(self):
        """Gets the offset of this ShowRedisBigKeysRequestBody.

        索引位置偏移量，表示从查询到的大key列表偏移offset条数据后查询对应的大key信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从第一条大key开始查询。

        :return: The offset of this ShowRedisBigKeysRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowRedisBigKeysRequestBody.

        索引位置偏移量，表示从查询到的大key列表偏移offset条数据后查询对应的大key信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从第一条大key开始查询。

        :param offset: The offset of this ShowRedisBigKeysRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowRedisBigKeysRequestBody.

        查询个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条大key。

        :return: The limit of this ShowRedisBigKeysRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowRedisBigKeysRequestBody.

        查询个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条大key。

        :param limit: The limit of this ShowRedisBigKeysRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def key_types(self):
        """Gets the key_types of this ShowRedisBigKeysRequestBody.

        大key的类型,一个字符串列表,支持\"string\",\"hash\",\"zset\",\"set\",\"list\",\"stream\"六种类型。

        :return: The key_types of this ShowRedisBigKeysRequestBody.
        :rtype: list[str]
        """
        return self._key_types

    @key_types.setter
    def key_types(self, key_types):
        """Sets the key_types of this ShowRedisBigKeysRequestBody.

        大key的类型,一个字符串列表,支持\"string\",\"hash\",\"zset\",\"set\",\"list\",\"stream\"六种类型。

        :param key_types: The key_types of this ShowRedisBigKeysRequestBody.
        :type key_types: list[str]
        """
        self._key_types = key_types

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
        if not isinstance(other, ShowRedisBigKeysRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
