# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBuiltInPolicyDefinitionsRequest:

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
        'marker': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_language=None, limit=None, marker=None):
        r"""ListBuiltInPolicyDefinitionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 选择接口返回的信息的语言，默认为\&quot;zh-cn\&quot;中文
        :type x_language: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._x_language = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_language(self):
        r"""Gets the x_language of this ListBuiltInPolicyDefinitionsRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :return: The x_language of this ListBuiltInPolicyDefinitionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListBuiltInPolicyDefinitionsRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :param x_language: The x_language of this ListBuiltInPolicyDefinitionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        r"""Gets the limit of this ListBuiltInPolicyDefinitionsRequest.

        最大的返回数量

        :return: The limit of this ListBuiltInPolicyDefinitionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBuiltInPolicyDefinitionsRequest.

        最大的返回数量

        :param limit: The limit of this ListBuiltInPolicyDefinitionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListBuiltInPolicyDefinitionsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListBuiltInPolicyDefinitionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListBuiltInPolicyDefinitionsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListBuiltInPolicyDefinitionsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListBuiltInPolicyDefinitionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
