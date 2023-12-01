# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkJobTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'keyword': 'str',
        'page_size': 'int',
        'current_page': 'int'
    }

    attribute_map = {
        'type': 'type',
        'keyword': 'keyword',
        'page_size': 'page-size',
        'current_page': 'current-page'
    }

    def __init__(self, type=None, keyword=None, page_size=None, current_page=None):
        """ListSparkJobTemplatesRequest

        The model defined in huaweicloud sdk

        :param type: 类型。
        :type type: str
        :param keyword: 模板名过滤关键字，模糊匹配，获取模板名含有该关键字的所有模板。
        :type keyword: str
        :param page_size: 每页显示的最大结果行数，范围: [1, 100]。默认值为：50。
        :type page_size: int
        :param current_page: 当前页码，默认为第一页。
        :type current_page: int
        """
        
        

        self._type = None
        self._keyword = None
        self._page_size = None
        self._current_page = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if keyword is not None:
            self.keyword = keyword
        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page

    @property
    def type(self):
        """Gets the type of this ListSparkJobTemplatesRequest.

        类型。

        :return: The type of this ListSparkJobTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSparkJobTemplatesRequest.

        类型。

        :param type: The type of this ListSparkJobTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def keyword(self):
        """Gets the keyword of this ListSparkJobTemplatesRequest.

        模板名过滤关键字，模糊匹配，获取模板名含有该关键字的所有模板。

        :return: The keyword of this ListSparkJobTemplatesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListSparkJobTemplatesRequest.

        模板名过滤关键字，模糊匹配，获取模板名含有该关键字的所有模板。

        :param keyword: The keyword of this ListSparkJobTemplatesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def page_size(self):
        """Gets the page_size of this ListSparkJobTemplatesRequest.

        每页显示的最大结果行数，范围: [1, 100]。默认值为：50。

        :return: The page_size of this ListSparkJobTemplatesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListSparkJobTemplatesRequest.

        每页显示的最大结果行数，范围: [1, 100]。默认值为：50。

        :param page_size: The page_size of this ListSparkJobTemplatesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this ListSparkJobTemplatesRequest.

        当前页码，默认为第一页。

        :return: The current_page of this ListSparkJobTemplatesRequest.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListSparkJobTemplatesRequest.

        当前页码，默认为第一页。

        :param current_page: The current_page of this ListSparkJobTemplatesRequest.
        :type current_page: int
        """
        self._current_page = current_page

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
        if not isinstance(other, ListSparkJobTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
