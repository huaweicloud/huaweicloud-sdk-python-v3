# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAnalyzersRequest:

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
        'marker': 'str',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'type': 'type'
    }

    def __init__(self, limit=None, marker=None, type=None):
        """ListAnalyzersRequest

        The model defined in huaweicloud sdk

        :param limit: 单页最大结果数。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        :param type: 分析器的类型。
        :type type: str
        """
        
        

        self._limit = None
        self._marker = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if type is not None:
            self.type = type

    @property
    def limit(self):
        """Gets the limit of this ListAnalyzersRequest.

        单页最大结果数。

        :return: The limit of this ListAnalyzersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAnalyzersRequest.

        单页最大结果数。

        :param limit: The limit of this ListAnalyzersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAnalyzersRequest.

        页面标记。

        :return: The marker of this ListAnalyzersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAnalyzersRequest.

        页面标记。

        :param marker: The marker of this ListAnalyzersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def type(self):
        """Gets the type of this ListAnalyzersRequest.

        分析器的类型。

        :return: The type of this ListAnalyzersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAnalyzersRequest.

        分析器的类型。

        :param type: The type of this ListAnalyzersRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAnalyzersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
