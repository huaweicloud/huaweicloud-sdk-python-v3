# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelatedProjectInfoRequest:

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
        'page_no': 'int',
        'search': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_no': 'page_no',
        'search': 'search'
    }

    def __init__(self, page_size=None, page_no=None, search=None):
        r"""ListRelatedProjectInfoRequest

        The model defined in huaweicloud sdk

        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        :param page_no: 分页页码，表示从此页开始查询， page大于等于1
        :type page_no: int
        :param search: 搜索内容
        :type search: str
        """
        
        

        self._page_size = None
        self._page_no = None
        self._search = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_no is not None:
            self.page_no = page_no
        if search is not None:
            self.search = search

    @property
    def page_size(self):
        r"""Gets the page_size of this ListRelatedProjectInfoRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListRelatedProjectInfoRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListRelatedProjectInfoRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListRelatedProjectInfoRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        r"""Gets the page_no of this ListRelatedProjectInfoRequest.

        分页页码，表示从此页开始查询， page大于等于1

        :return: The page_no of this ListRelatedProjectInfoRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListRelatedProjectInfoRequest.

        分页页码，表示从此页开始查询， page大于等于1

        :param page_no: The page_no of this ListRelatedProjectInfoRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def search(self):
        r"""Gets the search of this ListRelatedProjectInfoRequest.

        搜索内容

        :return: The search of this ListRelatedProjectInfoRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRelatedProjectInfoRequest.

        搜索内容

        :param search: The search of this ListRelatedProjectInfoRequest.
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
        if not isinstance(other, ListRelatedProjectInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
