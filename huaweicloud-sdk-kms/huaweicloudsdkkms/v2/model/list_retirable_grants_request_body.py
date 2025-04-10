# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRetirableGrantsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sequence': 'sequence'
    }

    def __init__(self, limit=None, marker=None, sequence=None):
        r"""ListRetirableGrantsRequestBody

        The model defined in huaweicloud sdk

        :param limit: 指定查询可退役授权返回记录条数，如果查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。 取值在授权最大个数范围以内。例如：100
        :type limit: str
        :param marker: 分页查询起始位置标识。 分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的“next_marker”的值。例如：10。
        :type marker: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._limit = None
        self._marker = None
        self._sequence = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sequence is not None:
            self.sequence = sequence

    @property
    def limit(self):
        r"""Gets the limit of this ListRetirableGrantsRequestBody.

        指定查询可退役授权返回记录条数，如果查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。 取值在授权最大个数范围以内。例如：100

        :return: The limit of this ListRetirableGrantsRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRetirableGrantsRequestBody.

        指定查询可退役授权返回记录条数，如果查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。 取值在授权最大个数范围以内。例如：100

        :param limit: The limit of this ListRetirableGrantsRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRetirableGrantsRequestBody.

        分页查询起始位置标识。 分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的“next_marker”的值。例如：10。

        :return: The marker of this ListRetirableGrantsRequestBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRetirableGrantsRequestBody.

        分页查询起始位置标识。 分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的“next_marker”的值。例如：10。

        :param marker: The marker of this ListRetirableGrantsRequestBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def sequence(self):
        r"""Gets the sequence of this ListRetirableGrantsRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this ListRetirableGrantsRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this ListRetirableGrantsRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this ListRetirableGrantsRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, ListRetirableGrantsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
