# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStreamsRequest:

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
        'start_stream_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'start_stream_name': 'start_stream_name'
    }

    def __init__(self, limit=None, start_stream_name=None):
        r"""ListStreamsRequest

        The model defined in huaweicloud sdk

        :param limit: 单次请求返回通道列表的最大数量。
        :type limit: int
        :param start_stream_name: 从该通道开始返回通道列表，返回的通道列表不包括此通道名称。  如果需要分页查询，第一页查询时不传该字段。返回结果has_more_streams为true时，进行下一页查询，start_stream_name传入第一页查询结果的最后一条通道名称。
        :type start_stream_name: str
        """
        
        

        self._limit = None
        self._start_stream_name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if start_stream_name is not None:
            self.start_stream_name = start_stream_name

    @property
    def limit(self):
        r"""Gets the limit of this ListStreamsRequest.

        单次请求返回通道列表的最大数量。

        :return: The limit of this ListStreamsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListStreamsRequest.

        单次请求返回通道列表的最大数量。

        :param limit: The limit of this ListStreamsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_stream_name(self):
        r"""Gets the start_stream_name of this ListStreamsRequest.

        从该通道开始返回通道列表，返回的通道列表不包括此通道名称。  如果需要分页查询，第一页查询时不传该字段。返回结果has_more_streams为true时，进行下一页查询，start_stream_name传入第一页查询结果的最后一条通道名称。

        :return: The start_stream_name of this ListStreamsRequest.
        :rtype: str
        """
        return self._start_stream_name

    @start_stream_name.setter
    def start_stream_name(self, start_stream_name):
        r"""Sets the start_stream_name of this ListStreamsRequest.

        从该通道开始返回通道列表，返回的通道列表不包括此通道名称。  如果需要分页查询，第一页查询时不传该字段。返回结果has_more_streams为true时，进行下一页查询，start_stream_name传入第一页查询结果的最后一条通道名称。

        :param start_stream_name: The start_stream_name of this ListStreamsRequest.
        :type start_stream_name: str
        """
        self._start_stream_name = start_stream_name

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
        if not isinstance(other, ListStreamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
