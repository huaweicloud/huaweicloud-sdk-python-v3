# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserAllRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_index': 'int',
        'page_size': 'int',
        'search': 'str'
    }

    attribute_map = {
        'page_index': 'page_index',
        'page_size': 'page_size',
        'search': 'search'
    }

    def __init__(self, page_index=None, page_size=None, search=None):
        r"""ListUserAllRepositoriesRequest

        The model defined in huaweicloud sdk

        :param page_index: 分页索引，从1开始计数
        :type page_index: int
        :param page_size: 每页条目数
        :type page_size: int
        :param search: 搜索关键字
        :type search: str
        """
        
        

        self._page_index = None
        self._page_size = None
        self._search = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if search is not None:
            self.search = search

    @property
    def page_index(self):
        r"""Gets the page_index of this ListUserAllRepositoriesRequest.

        分页索引，从1开始计数

        :return: The page_index of this ListUserAllRepositoriesRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListUserAllRepositoriesRequest.

        分页索引，从1开始计数

        :param page_index: The page_index of this ListUserAllRepositoriesRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListUserAllRepositoriesRequest.

        每页条目数

        :return: The page_size of this ListUserAllRepositoriesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListUserAllRepositoriesRequest.

        每页条目数

        :param page_size: The page_size of this ListUserAllRepositoriesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def search(self):
        r"""Gets the search of this ListUserAllRepositoriesRequest.

        搜索关键字

        :return: The search of this ListUserAllRepositoriesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListUserAllRepositoriesRequest.

        搜索关键字

        :param search: The search of this ListUserAllRepositoriesRequest.
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
        if not isinstance(other, ListUserAllRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
