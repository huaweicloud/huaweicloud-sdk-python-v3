# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'page': 'str',
        'page_size': 'str'
    }

    attribute_map = {
        'name': 'name',
        'page': 'page',
        'page_size': 'page_size'
    }

    def __init__(self, name=None, page=None, page_size=None):
        """ListTemplatesRequest

        The model defined in huaweicloud sdk

        :param name: 检索的模板的名字模糊查询
        :type name: str
        :param page: 分页页码， 表示从此页开始查询
        :type page: str
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: str
        """
        
        

        self._name = None
        self._page = None
        self._page_size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size

    @property
    def name(self):
        """Gets the name of this ListTemplatesRequest.

        检索的模板的名字模糊查询

        :return: The name of this ListTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTemplatesRequest.

        检索的模板的名字模糊查询

        :param name: The name of this ListTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def page(self):
        """Gets the page of this ListTemplatesRequest.

        分页页码， 表示从此页开始查询

        :return: The page of this ListTemplatesRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTemplatesRequest.

        分页页码， 表示从此页开始查询

        :param page: The page of this ListTemplatesRequest.
        :type page: str
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListTemplatesRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListTemplatesRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListTemplatesRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListTemplatesRequest.
        :type page_size: str
        """
        self._page_size = page_size

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
