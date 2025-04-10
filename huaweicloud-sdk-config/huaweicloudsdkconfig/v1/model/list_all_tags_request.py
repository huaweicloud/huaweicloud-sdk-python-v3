# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'key': 'key',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, key=None, marker=None, limit=None):
        r"""ListAllTagsRequest

        The model defined in huaweicloud sdk

        :param key: 标签键名
        :type key: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param limit: 最大的返回数量。
        :type limit: int
        """
        
        

        self._key = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def key(self):
        r"""Gets the key of this ListAllTagsRequest.

        标签键名

        :return: The key of this ListAllTagsRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListAllTagsRequest.

        标签键名

        :param key: The key of this ListAllTagsRequest.
        :type key: str
        """
        self._key = key

    @property
    def marker(self):
        r"""Gets the marker of this ListAllTagsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListAllTagsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAllTagsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListAllTagsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAllTagsRequest.

        最大的返回数量。

        :return: The limit of this ListAllTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAllTagsRequest.

        最大的返回数量。

        :param limit: The limit of this ListAllTagsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAllTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
