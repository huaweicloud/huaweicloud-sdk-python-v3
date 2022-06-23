# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoredQueriesRequest:

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
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name'
    }

    def __init__(self, limit=None, marker=None, name=None):
        """ListStoredQueriesRequest

        The model defined in huaweicloud sdk

        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param name: ResourceQL 名字
        :type name: str
        """
        
        

        self._limit = None
        self._marker = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name

    @property
    def limit(self):
        """Gets the limit of this ListStoredQueriesRequest.

        最大的返回数量

        :return: The limit of this ListStoredQueriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStoredQueriesRequest.

        最大的返回数量

        :param limit: The limit of this ListStoredQueriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListStoredQueriesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListStoredQueriesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListStoredQueriesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListStoredQueriesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListStoredQueriesRequest.

        ResourceQL 名字

        :return: The name of this ListStoredQueriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListStoredQueriesRequest.

        ResourceQL 名字

        :param name: The name of this ListStoredQueriesRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListStoredQueriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
