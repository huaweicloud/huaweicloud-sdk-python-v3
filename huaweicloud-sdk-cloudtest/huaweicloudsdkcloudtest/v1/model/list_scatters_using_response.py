# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScattersUsingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list': 'list[TaskCaseResponseTimeDetailVo]',
        'page_num': 'int',
        'page_size': 'int',
        'total_page': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'list': 'list',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'total_page': 'total_page',
        'total_size': 'total_size'
    }

    def __init__(self, list=None, page_num=None, page_size=None, total_page=None, total_size=None):
        """ListScattersUsingResponse

        The model defined in huaweicloud sdk

        :param list: 返回结果
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TaskCaseResponseTimeDetailVo`]
        :param page_num: 页码
        :type page_num: int
        :param page_size: 分页大小
        :type page_size: int
        :param total_page: 总页数
        :type total_page: int
        :param total_size: 总条数
        :type total_size: int
        """
        
        super(ListScattersUsingResponse, self).__init__()

        self._list = None
        self._page_num = None
        self._page_size = None
        self._total_page = None
        self._total_size = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if total_page is not None:
            self.total_page = total_page
        if total_size is not None:
            self.total_size = total_size

    @property
    def list(self):
        """Gets the list of this ListScattersUsingResponse.

        返回结果

        :return: The list of this ListScattersUsingResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TaskCaseResponseTimeDetailVo`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ListScattersUsingResponse.

        返回结果

        :param list: The list of this ListScattersUsingResponse.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TaskCaseResponseTimeDetailVo`]
        """
        self._list = list

    @property
    def page_num(self):
        """Gets the page_num of this ListScattersUsingResponse.

        页码

        :return: The page_num of this ListScattersUsingResponse.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListScattersUsingResponse.

        页码

        :param page_num: The page_num of this ListScattersUsingResponse.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListScattersUsingResponse.

        分页大小

        :return: The page_size of this ListScattersUsingResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListScattersUsingResponse.

        分页大小

        :param page_size: The page_size of this ListScattersUsingResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_page(self):
        """Gets the total_page of this ListScattersUsingResponse.

        总页数

        :return: The total_page of this ListScattersUsingResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this ListScattersUsingResponse.

        总页数

        :param total_page: The total_page of this ListScattersUsingResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_size(self):
        """Gets the total_size of this ListScattersUsingResponse.

        总条数

        :return: The total_size of this ListScattersUsingResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ListScattersUsingResponse.

        总条数

        :param total_size: The total_size of this ListScattersUsingResponse.
        :type total_size: int
        """
        self._total_size = total_size

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
        if not isinstance(other, ListScattersUsingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
