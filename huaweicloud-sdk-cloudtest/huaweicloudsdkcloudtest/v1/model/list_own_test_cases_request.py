# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOwnTestCasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'page_size': 'int',
        'sort_field': 'str',
        'sort_type': 'str',
        'keyword': 'str'
    }

    attribute_map = {
        'page_no': 'page_no',
        'page_size': 'page_size',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'keyword': 'keyword'
    }

    def __init__(self, page_no=None, page_size=None, sort_field=None, sort_type=None, keyword=None):
        """ListOwnTestCasesRequest

        The model defined in huaweicloud sdk

        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        :param keyword: 关键字查询，用例名或编号
        :type keyword: str
        """
        
        

        self._page_no = None
        self._page_size = None
        self._sort_field = None
        self._sort_type = None
        self._keyword = None
        self.discriminator = None

        self.page_no = page_no
        self.page_size = page_size
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if keyword is not None:
            self.keyword = keyword

    @property
    def page_no(self):
        """Gets the page_no of this ListOwnTestCasesRequest.

        当前页数

        :return: The page_no of this ListOwnTestCasesRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListOwnTestCasesRequest.

        当前页数

        :param page_no: The page_no of this ListOwnTestCasesRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ListOwnTestCasesRequest.

        每页条数

        :return: The page_size of this ListOwnTestCasesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListOwnTestCasesRequest.

        每页条数

        :param page_size: The page_size of this ListOwnTestCasesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_field(self):
        """Gets the sort_field of this ListOwnTestCasesRequest.

        排序字段

        :return: The sort_field of this ListOwnTestCasesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListOwnTestCasesRequest.

        排序字段

        :param sort_field: The sort_field of this ListOwnTestCasesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListOwnTestCasesRequest.

        排序方式

        :return: The sort_type of this ListOwnTestCasesRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListOwnTestCasesRequest.

        排序方式

        :param sort_type: The sort_type of this ListOwnTestCasesRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def keyword(self):
        """Gets the keyword of this ListOwnTestCasesRequest.

        关键字查询，用例名或编号

        :return: The keyword of this ListOwnTestCasesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListOwnTestCasesRequest.

        关键字查询，用例名或编号

        :param keyword: The keyword of this ListOwnTestCasesRequest.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, ListOwnTestCasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
