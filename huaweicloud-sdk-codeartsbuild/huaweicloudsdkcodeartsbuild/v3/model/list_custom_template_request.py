# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomTemplateRequest:

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
        'filter': 'str',
        'page': 'int',
        'page_size': 'int',
        'tags': 'str'
    }

    attribute_map = {
        'name': 'name',
        'filter': 'filter',
        'page': 'page',
        'page_size': 'page_size',
        'tags': 'tags'
    }

    def __init__(self, name=None, filter=None, page=None, page_size=None, tags=None):
        r"""ListCustomTemplateRequest

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param filter: 过滤条件
        :type filter: str
        :param page: 分页页码，表示从此页开始查询，page大于等于1
        :type page: int
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        :param tags: 构建状态过滤条件
        :type tags: str
        """
        
        

        self._name = None
        self._filter = None
        self._page = None
        self._page_size = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if filter is not None:
            self.filter = filter
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this ListCustomTemplateRequest.

        名称

        :return: The name of this ListCustomTemplateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCustomTemplateRequest.

        名称

        :param name: The name of this ListCustomTemplateRequest.
        :type name: str
        """
        self._name = name

    @property
    def filter(self):
        r"""Gets the filter of this ListCustomTemplateRequest.

        过滤条件

        :return: The filter of this ListCustomTemplateRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListCustomTemplateRequest.

        过滤条件

        :param filter: The filter of this ListCustomTemplateRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def page(self):
        r"""Gets the page of this ListCustomTemplateRequest.

        分页页码，表示从此页开始查询，page大于等于1

        :return: The page of this ListCustomTemplateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListCustomTemplateRequest.

        分页页码，表示从此页开始查询，page大于等于1

        :param page: The page of this ListCustomTemplateRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this ListCustomTemplateRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListCustomTemplateRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListCustomTemplateRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListCustomTemplateRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def tags(self):
        r"""Gets the tags of this ListCustomTemplateRequest.

        构建状态过滤条件

        :return: The tags of this ListCustomTemplateRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListCustomTemplateRequest.

        构建状态过滤条件

        :param tags: The tags of this ListCustomTemplateRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListCustomTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
