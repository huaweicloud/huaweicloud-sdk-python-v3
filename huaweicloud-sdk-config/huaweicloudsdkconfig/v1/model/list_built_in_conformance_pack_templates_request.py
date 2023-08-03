# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBuiltInConformancePackTemplatesRequest:

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
        'template_key': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'template_key': 'template_key',
        'x_language': 'X-Language'
    }

    def __init__(self, limit=None, marker=None, template_key=None, x_language=None):
        """ListBuiltInConformancePackTemplatesRequest

        The model defined in huaweicloud sdk

        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param template_key: 预定义合规包模板名称。
        :type template_key: str
        :param x_language: 选择接口返回的信息的语言，默认为\&quot;zh-cn\&quot;中文
        :type x_language: str
        """
        
        

        self._limit = None
        self._marker = None
        self._template_key = None
        self._x_language = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if template_key is not None:
            self.template_key = template_key
        if x_language is not None:
            self.x_language = x_language

    @property
    def limit(self):
        """Gets the limit of this ListBuiltInConformancePackTemplatesRequest.

        最大的返回数量

        :return: The limit of this ListBuiltInConformancePackTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBuiltInConformancePackTemplatesRequest.

        最大的返回数量

        :param limit: The limit of this ListBuiltInConformancePackTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListBuiltInConformancePackTemplatesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListBuiltInConformancePackTemplatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBuiltInConformancePackTemplatesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListBuiltInConformancePackTemplatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def template_key(self):
        """Gets the template_key of this ListBuiltInConformancePackTemplatesRequest.

        预定义合规包模板名称。

        :return: The template_key of this ListBuiltInConformancePackTemplatesRequest.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        """Sets the template_key of this ListBuiltInConformancePackTemplatesRequest.

        预定义合规包模板名称。

        :param template_key: The template_key of this ListBuiltInConformancePackTemplatesRequest.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def x_language(self):
        """Gets the x_language of this ListBuiltInConformancePackTemplatesRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :return: The x_language of this ListBuiltInConformancePackTemplatesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListBuiltInConformancePackTemplatesRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :param x_language: The x_language of this ListBuiltInConformancePackTemplatesRequest.
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
        if not isinstance(other, ListBuiltInConformancePackTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
