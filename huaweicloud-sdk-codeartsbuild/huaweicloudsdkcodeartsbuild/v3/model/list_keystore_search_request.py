# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeystoreSearchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page': 'int',
        'search': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page': 'page',
        'search': 'search'
    }

    def __init__(self, page_size=None, page=None, search=None):
        r"""ListKeystoreSearchRequest

        The model defined in huaweicloud sdk

        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        :param page: 分页页码，表示从此页开始查询， page大于等于1
        :type page: int
        :param search: 搜索的文件名
        :type search: str
        """
        
        

        self._page_size = None
        self._page = None
        self._search = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page
        if search is not None:
            self.search = search

    @property
    def page_size(self):
        r"""Gets the page_size of this ListKeystoreSearchRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListKeystoreSearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListKeystoreSearchRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListKeystoreSearchRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page(self):
        r"""Gets the page of this ListKeystoreSearchRequest.

        分页页码，表示从此页开始查询， page大于等于1

        :return: The page of this ListKeystoreSearchRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListKeystoreSearchRequest.

        分页页码，表示从此页开始查询， page大于等于1

        :param page: The page of this ListKeystoreSearchRequest.
        :type page: int
        """
        self._page = page

    @property
    def search(self):
        r"""Gets the search of this ListKeystoreSearchRequest.

        搜索的文件名

        :return: The search of this ListKeystoreSearchRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListKeystoreSearchRequest.

        搜索的文件名

        :param search: The search of this ListKeystoreSearchRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListKeystoreSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
