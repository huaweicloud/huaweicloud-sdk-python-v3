# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_type': 'str',
        'search_value': 'str'
    }

    attribute_map = {
        'search_type': 'search_type',
        'search_value': 'search_value'
    }

    def __init__(self, search_type=None, search_value=None):
        r"""SearchRequest

        The model defined in huaweicloud sdk

        :param search_type: 过滤类型
        :type search_type: str
        :param search_value: 过滤条件
        :type search_value: str
        """
        
        

        self._search_type = None
        self._search_value = None
        self.discriminator = None

        if search_type is not None:
            self.search_type = search_type
        if search_value is not None:
            self.search_value = search_value

    @property
    def search_type(self):
        r"""Gets the search_type of this SearchRequest.

        过滤类型

        :return: The search_type of this SearchRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this SearchRequest.

        过滤类型

        :param search_type: The search_type of this SearchRequest.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def search_value(self):
        r"""Gets the search_value of this SearchRequest.

        过滤条件

        :return: The search_value of this SearchRequest.
        :rtype: str
        """
        return self._search_value

    @search_value.setter
    def search_value(self, search_value):
        r"""Sets the search_value of this SearchRequest.

        过滤条件

        :param search_value: The search_value of this SearchRequest.
        :type search_value: str
        """
        self._search_value = search_value

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
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
