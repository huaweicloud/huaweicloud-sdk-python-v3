# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'maxitems': 'str',
        'runtime': 'str',
        'category': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'maxitems': 'maxitems',
        'runtime': 'runtime',
        'category': 'category',
        'x_language': 'X-Language'
    }

    def __init__(self, marker=None, maxitems=None, runtime=None, category=None, x_language=None):
        """ListAppTemplatesRequest

        The model defined in huaweicloud sdk

        :param marker: 本次查询起始位置，默认值0
        :type marker: str
        :param maxitems: 本次查询最大返回的数据条数，最大值500，默认值100
        :type maxitems: str
        :param runtime: 模板执行运行时
        :type runtime: str
        :param category: 模板类别
        :type category: str
        :param x_language: 模板语言
        :type x_language: str
        """
        
        

        self._marker = None
        self._maxitems = None
        self._runtime = None
        self._category = None
        self._x_language = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if x_language is not None:
            self.x_language = x_language

    @property
    def marker(self):
        """Gets the marker of this ListAppTemplatesRequest.

        本次查询起始位置，默认值0

        :return: The marker of this ListAppTemplatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAppTemplatesRequest.

        本次查询起始位置，默认值0

        :param marker: The marker of this ListAppTemplatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        """Gets the maxitems of this ListAppTemplatesRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :return: The maxitems of this ListAppTemplatesRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        """Sets the maxitems of this ListAppTemplatesRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :param maxitems: The maxitems of this ListAppTemplatesRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

    @property
    def runtime(self):
        """Gets the runtime of this ListAppTemplatesRequest.

        模板执行运行时

        :return: The runtime of this ListAppTemplatesRequest.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ListAppTemplatesRequest.

        模板执行运行时

        :param runtime: The runtime of this ListAppTemplatesRequest.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def category(self):
        """Gets the category of this ListAppTemplatesRequest.

        模板类别

        :return: The category of this ListAppTemplatesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListAppTemplatesRequest.

        模板类别

        :param category: The category of this ListAppTemplatesRequest.
        :type category: str
        """
        self._category = category

    @property
    def x_language(self):
        """Gets the x_language of this ListAppTemplatesRequest.

        模板语言

        :return: The x_language of this ListAppTemplatesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListAppTemplatesRequest.

        模板语言

        :param x_language: The x_language of this ListAppTemplatesRequest.
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
        if not isinstance(other, ListAppTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
