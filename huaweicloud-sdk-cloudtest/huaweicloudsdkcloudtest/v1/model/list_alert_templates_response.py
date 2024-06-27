# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_row': 'int',
        'has_next_page': 'bool',
        'has_previous_page': 'bool',
        'is_first_page': 'bool',
        'is_last_page': 'bool',
        'list': 'list[AlertTemplateVo]',
        'navigate_first_page': 'int',
        'navigate_last_page': 'int',
        'navigate_pages': 'int',
        'navigatepage_nums': 'list[int]',
        'next_page': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'pages': 'int',
        'pre_page': 'int',
        'size': 'int',
        'start_row': 'int',
        'total': 'int'
    }

    attribute_map = {
        'end_row': 'end_row',
        'has_next_page': 'has_next_page',
        'has_previous_page': 'has_previous_page',
        'is_first_page': 'is_first_page',
        'is_last_page': 'is_last_page',
        'list': 'list',
        'navigate_first_page': 'navigate_first_page',
        'navigate_last_page': 'navigate_last_page',
        'navigate_pages': 'navigate_pages',
        'navigatepage_nums': 'navigatepage_nums',
        'next_page': 'next_page',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'pages': 'pages',
        'pre_page': 'pre_page',
        'size': 'size',
        'start_row': 'start_row',
        'total': 'total'
    }

    def __init__(self, end_row=None, has_next_page=None, has_previous_page=None, is_first_page=None, is_last_page=None, list=None, navigate_first_page=None, navigate_last_page=None, navigate_pages=None, navigatepage_nums=None, next_page=None, page_num=None, page_size=None, pages=None, pre_page=None, size=None, start_row=None, total=None):
        """ListAlertTemplatesResponse

        The model defined in huaweicloud sdk

        :param end_row: 当前页面最后一个元素在数据库中的行号
        :type end_row: int
        :param has_next_page: 是否有下一页
        :type has_next_page: bool
        :param has_previous_page: 是否有前一页
        :type has_previous_page: bool
        :param is_first_page: 是否为第一页
        :type is_first_page: bool
        :param is_last_page: 是否为最后一页
        :type is_last_page: bool
        :param list: 返回结果
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.AlertTemplateVo`]
        :param navigate_first_page: 导航条上的第一页
        :type navigate_first_page: int
        :param navigate_last_page: 导航条上的最后一页
        :type navigate_last_page: int
        :param navigate_pages: 导航页码数
        :type navigate_pages: int
        :param navigatepage_nums: 所有导航页号
        :type navigatepage_nums: list[int]
        :param next_page: 下一页
        :type next_page: int
        :param page_num: 当前页
        :type page_num: int
        :param page_size: 每页的数量
        :type page_size: int
        :param pages: 总页数
        :type pages: int
        :param pre_page: 前一页
        :type pre_page: int
        :param size: 当前页的数量
        :type size: int
        :param start_row: 当前页面第一个元素在数据库中的行号
        :type start_row: int
        :param total: 总条数
        :type total: int
        """
        
        super(ListAlertTemplatesResponse, self).__init__()

        self._end_row = None
        self._has_next_page = None
        self._has_previous_page = None
        self._is_first_page = None
        self._is_last_page = None
        self._list = None
        self._navigate_first_page = None
        self._navigate_last_page = None
        self._navigate_pages = None
        self._navigatepage_nums = None
        self._next_page = None
        self._page_num = None
        self._page_size = None
        self._pages = None
        self._pre_page = None
        self._size = None
        self._start_row = None
        self._total = None
        self.discriminator = None

        if end_row is not None:
            self.end_row = end_row
        if has_next_page is not None:
            self.has_next_page = has_next_page
        if has_previous_page is not None:
            self.has_previous_page = has_previous_page
        if is_first_page is not None:
            self.is_first_page = is_first_page
        if is_last_page is not None:
            self.is_last_page = is_last_page
        if list is not None:
            self.list = list
        if navigate_first_page is not None:
            self.navigate_first_page = navigate_first_page
        if navigate_last_page is not None:
            self.navigate_last_page = navigate_last_page
        if navigate_pages is not None:
            self.navigate_pages = navigate_pages
        if navigatepage_nums is not None:
            self.navigatepage_nums = navigatepage_nums
        if next_page is not None:
            self.next_page = next_page
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if pages is not None:
            self.pages = pages
        if pre_page is not None:
            self.pre_page = pre_page
        if size is not None:
            self.size = size
        if start_row is not None:
            self.start_row = start_row
        if total is not None:
            self.total = total

    @property
    def end_row(self):
        """Gets the end_row of this ListAlertTemplatesResponse.

        当前页面最后一个元素在数据库中的行号

        :return: The end_row of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._end_row

    @end_row.setter
    def end_row(self, end_row):
        """Sets the end_row of this ListAlertTemplatesResponse.

        当前页面最后一个元素在数据库中的行号

        :param end_row: The end_row of this ListAlertTemplatesResponse.
        :type end_row: int
        """
        self._end_row = end_row

    @property
    def has_next_page(self):
        """Gets the has_next_page of this ListAlertTemplatesResponse.

        是否有下一页

        :return: The has_next_page of this ListAlertTemplatesResponse.
        :rtype: bool
        """
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, has_next_page):
        """Sets the has_next_page of this ListAlertTemplatesResponse.

        是否有下一页

        :param has_next_page: The has_next_page of this ListAlertTemplatesResponse.
        :type has_next_page: bool
        """
        self._has_next_page = has_next_page

    @property
    def has_previous_page(self):
        """Gets the has_previous_page of this ListAlertTemplatesResponse.

        是否有前一页

        :return: The has_previous_page of this ListAlertTemplatesResponse.
        :rtype: bool
        """
        return self._has_previous_page

    @has_previous_page.setter
    def has_previous_page(self, has_previous_page):
        """Sets the has_previous_page of this ListAlertTemplatesResponse.

        是否有前一页

        :param has_previous_page: The has_previous_page of this ListAlertTemplatesResponse.
        :type has_previous_page: bool
        """
        self._has_previous_page = has_previous_page

    @property
    def is_first_page(self):
        """Gets the is_first_page of this ListAlertTemplatesResponse.

        是否为第一页

        :return: The is_first_page of this ListAlertTemplatesResponse.
        :rtype: bool
        """
        return self._is_first_page

    @is_first_page.setter
    def is_first_page(self, is_first_page):
        """Sets the is_first_page of this ListAlertTemplatesResponse.

        是否为第一页

        :param is_first_page: The is_first_page of this ListAlertTemplatesResponse.
        :type is_first_page: bool
        """
        self._is_first_page = is_first_page

    @property
    def is_last_page(self):
        """Gets the is_last_page of this ListAlertTemplatesResponse.

        是否为最后一页

        :return: The is_last_page of this ListAlertTemplatesResponse.
        :rtype: bool
        """
        return self._is_last_page

    @is_last_page.setter
    def is_last_page(self, is_last_page):
        """Sets the is_last_page of this ListAlertTemplatesResponse.

        是否为最后一页

        :param is_last_page: The is_last_page of this ListAlertTemplatesResponse.
        :type is_last_page: bool
        """
        self._is_last_page = is_last_page

    @property
    def list(self):
        """Gets the list of this ListAlertTemplatesResponse.

        返回结果

        :return: The list of this ListAlertTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlertTemplateVo`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ListAlertTemplatesResponse.

        返回结果

        :param list: The list of this ListAlertTemplatesResponse.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.AlertTemplateVo`]
        """
        self._list = list

    @property
    def navigate_first_page(self):
        """Gets the navigate_first_page of this ListAlertTemplatesResponse.

        导航条上的第一页

        :return: The navigate_first_page of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._navigate_first_page

    @navigate_first_page.setter
    def navigate_first_page(self, navigate_first_page):
        """Sets the navigate_first_page of this ListAlertTemplatesResponse.

        导航条上的第一页

        :param navigate_first_page: The navigate_first_page of this ListAlertTemplatesResponse.
        :type navigate_first_page: int
        """
        self._navigate_first_page = navigate_first_page

    @property
    def navigate_last_page(self):
        """Gets the navigate_last_page of this ListAlertTemplatesResponse.

        导航条上的最后一页

        :return: The navigate_last_page of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._navigate_last_page

    @navigate_last_page.setter
    def navigate_last_page(self, navigate_last_page):
        """Sets the navigate_last_page of this ListAlertTemplatesResponse.

        导航条上的最后一页

        :param navigate_last_page: The navigate_last_page of this ListAlertTemplatesResponse.
        :type navigate_last_page: int
        """
        self._navigate_last_page = navigate_last_page

    @property
    def navigate_pages(self):
        """Gets the navigate_pages of this ListAlertTemplatesResponse.

        导航页码数

        :return: The navigate_pages of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._navigate_pages

    @navigate_pages.setter
    def navigate_pages(self, navigate_pages):
        """Sets the navigate_pages of this ListAlertTemplatesResponse.

        导航页码数

        :param navigate_pages: The navigate_pages of this ListAlertTemplatesResponse.
        :type navigate_pages: int
        """
        self._navigate_pages = navigate_pages

    @property
    def navigatepage_nums(self):
        """Gets the navigatepage_nums of this ListAlertTemplatesResponse.

        所有导航页号

        :return: The navigatepage_nums of this ListAlertTemplatesResponse.
        :rtype: list[int]
        """
        return self._navigatepage_nums

    @navigatepage_nums.setter
    def navigatepage_nums(self, navigatepage_nums):
        """Sets the navigatepage_nums of this ListAlertTemplatesResponse.

        所有导航页号

        :param navigatepage_nums: The navigatepage_nums of this ListAlertTemplatesResponse.
        :type navigatepage_nums: list[int]
        """
        self._navigatepage_nums = navigatepage_nums

    @property
    def next_page(self):
        """Gets the next_page of this ListAlertTemplatesResponse.

        下一页

        :return: The next_page of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ListAlertTemplatesResponse.

        下一页

        :param next_page: The next_page of this ListAlertTemplatesResponse.
        :type next_page: int
        """
        self._next_page = next_page

    @property
    def page_num(self):
        """Gets the page_num of this ListAlertTemplatesResponse.

        当前页

        :return: The page_num of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListAlertTemplatesResponse.

        当前页

        :param page_num: The page_num of this ListAlertTemplatesResponse.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListAlertTemplatesResponse.

        每页的数量

        :return: The page_size of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAlertTemplatesResponse.

        每页的数量

        :param page_size: The page_size of this ListAlertTemplatesResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def pages(self):
        """Gets the pages of this ListAlertTemplatesResponse.

        总页数

        :return: The pages of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ListAlertTemplatesResponse.

        总页数

        :param pages: The pages of this ListAlertTemplatesResponse.
        :type pages: int
        """
        self._pages = pages

    @property
    def pre_page(self):
        """Gets the pre_page of this ListAlertTemplatesResponse.

        前一页

        :return: The pre_page of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._pre_page

    @pre_page.setter
    def pre_page(self, pre_page):
        """Sets the pre_page of this ListAlertTemplatesResponse.

        前一页

        :param pre_page: The pre_page of this ListAlertTemplatesResponse.
        :type pre_page: int
        """
        self._pre_page = pre_page

    @property
    def size(self):
        """Gets the size of this ListAlertTemplatesResponse.

        当前页的数量

        :return: The size of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListAlertTemplatesResponse.

        当前页的数量

        :param size: The size of this ListAlertTemplatesResponse.
        :type size: int
        """
        self._size = size

    @property
    def start_row(self):
        """Gets the start_row of this ListAlertTemplatesResponse.

        当前页面第一个元素在数据库中的行号

        :return: The start_row of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._start_row

    @start_row.setter
    def start_row(self, start_row):
        """Sets the start_row of this ListAlertTemplatesResponse.

        当前页面第一个元素在数据库中的行号

        :param start_row: The start_row of this ListAlertTemplatesResponse.
        :type start_row: int
        """
        self._start_row = start_row

    @property
    def total(self):
        """Gets the total of this ListAlertTemplatesResponse.

        总条数

        :return: The total of this ListAlertTemplatesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAlertTemplatesResponse.

        总条数

        :param total: The total of this ListAlertTemplatesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAlertTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
