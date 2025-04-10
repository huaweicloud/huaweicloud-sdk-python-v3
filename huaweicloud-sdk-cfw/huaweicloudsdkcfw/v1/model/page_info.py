# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfo:

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
        'list': 'list[object]',
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
        'end_row': 'endRow',
        'has_next_page': 'hasNextPage',
        'has_previous_page': 'hasPreviousPage',
        'is_first_page': 'isFirstPage',
        'is_last_page': 'isLastPage',
        'list': 'list',
        'navigate_first_page': 'navigateFirstPage',
        'navigate_last_page': 'navigateLastPage',
        'navigate_pages': 'navigatePages',
        'navigatepage_nums': 'navigatepageNums',
        'next_page': 'nextPage',
        'page_num': 'pageNum',
        'page_size': 'pageSize',
        'pages': 'pages',
        'pre_page': 'prePage',
        'size': 'size',
        'start_row': 'startRow',
        'total': 'total'
    }

    def __init__(self, end_row=None, has_next_page=None, has_previous_page=None, is_first_page=None, is_last_page=None, list=None, navigate_first_page=None, navigate_last_page=None, navigate_pages=None, navigatepage_nums=None, next_page=None, page_num=None, page_size=None, pages=None, pre_page=None, size=None, start_row=None, total=None):
        r"""PageInfo

        The model defined in huaweicloud sdk

        :param end_row: 
        :type end_row: int
        :param has_next_page: 
        :type has_next_page: bool
        :param has_previous_page: 
        :type has_previous_page: bool
        :param is_first_page: 
        :type is_first_page: bool
        :param is_last_page: 
        :type is_last_page: bool
        :param list: 
        :type list: list[object]
        :param navigate_first_page: 
        :type navigate_first_page: int
        :param navigate_last_page: 
        :type navigate_last_page: int
        :param navigate_pages: 
        :type navigate_pages: int
        :param navigatepage_nums: 
        :type navigatepage_nums: list[int]
        :param next_page: 
        :type next_page: int
        :param page_num: 
        :type page_num: int
        :param page_size: 
        :type page_size: int
        :param pages: 
        :type pages: int
        :param pre_page: 
        :type pre_page: int
        :param size: 
        :type size: int
        :param start_row: 
        :type start_row: int
        :param total: 
        :type total: int
        """
        
        

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
        r"""Gets the end_row of this PageInfo.

        :return: The end_row of this PageInfo.
        :rtype: int
        """
        return self._end_row

    @end_row.setter
    def end_row(self, end_row):
        r"""Sets the end_row of this PageInfo.

        :param end_row: The end_row of this PageInfo.
        :type end_row: int
        """
        self._end_row = end_row

    @property
    def has_next_page(self):
        r"""Gets the has_next_page of this PageInfo.

        :return: The has_next_page of this PageInfo.
        :rtype: bool
        """
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, has_next_page):
        r"""Sets the has_next_page of this PageInfo.

        :param has_next_page: The has_next_page of this PageInfo.
        :type has_next_page: bool
        """
        self._has_next_page = has_next_page

    @property
    def has_previous_page(self):
        r"""Gets the has_previous_page of this PageInfo.

        :return: The has_previous_page of this PageInfo.
        :rtype: bool
        """
        return self._has_previous_page

    @has_previous_page.setter
    def has_previous_page(self, has_previous_page):
        r"""Sets the has_previous_page of this PageInfo.

        :param has_previous_page: The has_previous_page of this PageInfo.
        :type has_previous_page: bool
        """
        self._has_previous_page = has_previous_page

    @property
    def is_first_page(self):
        r"""Gets the is_first_page of this PageInfo.

        :return: The is_first_page of this PageInfo.
        :rtype: bool
        """
        return self._is_first_page

    @is_first_page.setter
    def is_first_page(self, is_first_page):
        r"""Sets the is_first_page of this PageInfo.

        :param is_first_page: The is_first_page of this PageInfo.
        :type is_first_page: bool
        """
        self._is_first_page = is_first_page

    @property
    def is_last_page(self):
        r"""Gets the is_last_page of this PageInfo.

        :return: The is_last_page of this PageInfo.
        :rtype: bool
        """
        return self._is_last_page

    @is_last_page.setter
    def is_last_page(self, is_last_page):
        r"""Sets the is_last_page of this PageInfo.

        :param is_last_page: The is_last_page of this PageInfo.
        :type is_last_page: bool
        """
        self._is_last_page = is_last_page

    @property
    def list(self):
        r"""Gets the list of this PageInfo.

        :return: The list of this PageInfo.
        :rtype: list[object]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this PageInfo.

        :param list: The list of this PageInfo.
        :type list: list[object]
        """
        self._list = list

    @property
    def navigate_first_page(self):
        r"""Gets the navigate_first_page of this PageInfo.

        :return: The navigate_first_page of this PageInfo.
        :rtype: int
        """
        return self._navigate_first_page

    @navigate_first_page.setter
    def navigate_first_page(self, navigate_first_page):
        r"""Sets the navigate_first_page of this PageInfo.

        :param navigate_first_page: The navigate_first_page of this PageInfo.
        :type navigate_first_page: int
        """
        self._navigate_first_page = navigate_first_page

    @property
    def navigate_last_page(self):
        r"""Gets the navigate_last_page of this PageInfo.

        :return: The navigate_last_page of this PageInfo.
        :rtype: int
        """
        return self._navigate_last_page

    @navigate_last_page.setter
    def navigate_last_page(self, navigate_last_page):
        r"""Sets the navigate_last_page of this PageInfo.

        :param navigate_last_page: The navigate_last_page of this PageInfo.
        :type navigate_last_page: int
        """
        self._navigate_last_page = navigate_last_page

    @property
    def navigate_pages(self):
        r"""Gets the navigate_pages of this PageInfo.

        :return: The navigate_pages of this PageInfo.
        :rtype: int
        """
        return self._navigate_pages

    @navigate_pages.setter
    def navigate_pages(self, navigate_pages):
        r"""Sets the navigate_pages of this PageInfo.

        :param navigate_pages: The navigate_pages of this PageInfo.
        :type navigate_pages: int
        """
        self._navigate_pages = navigate_pages

    @property
    def navigatepage_nums(self):
        r"""Gets the navigatepage_nums of this PageInfo.

        :return: The navigatepage_nums of this PageInfo.
        :rtype: list[int]
        """
        return self._navigatepage_nums

    @navigatepage_nums.setter
    def navigatepage_nums(self, navigatepage_nums):
        r"""Sets the navigatepage_nums of this PageInfo.

        :param navigatepage_nums: The navigatepage_nums of this PageInfo.
        :type navigatepage_nums: list[int]
        """
        self._navigatepage_nums = navigatepage_nums

    @property
    def next_page(self):
        r"""Gets the next_page of this PageInfo.

        :return: The next_page of this PageInfo.
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        r"""Sets the next_page of this PageInfo.

        :param next_page: The next_page of this PageInfo.
        :type next_page: int
        """
        self._next_page = next_page

    @property
    def page_num(self):
        r"""Gets the page_num of this PageInfo.

        :return: The page_num of this PageInfo.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this PageInfo.

        :param page_num: The page_num of this PageInfo.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this PageInfo.

        :return: The page_size of this PageInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this PageInfo.

        :param page_size: The page_size of this PageInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def pages(self):
        r"""Gets the pages of this PageInfo.

        :return: The pages of this PageInfo.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this PageInfo.

        :param pages: The pages of this PageInfo.
        :type pages: int
        """
        self._pages = pages

    @property
    def pre_page(self):
        r"""Gets the pre_page of this PageInfo.

        :return: The pre_page of this PageInfo.
        :rtype: int
        """
        return self._pre_page

    @pre_page.setter
    def pre_page(self, pre_page):
        r"""Sets the pre_page of this PageInfo.

        :param pre_page: The pre_page of this PageInfo.
        :type pre_page: int
        """
        self._pre_page = pre_page

    @property
    def size(self):
        r"""Gets the size of this PageInfo.

        :return: The size of this PageInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PageInfo.

        :param size: The size of this PageInfo.
        :type size: int
        """
        self._size = size

    @property
    def start_row(self):
        r"""Gets the start_row of this PageInfo.

        :return: The start_row of this PageInfo.
        :rtype: int
        """
        return self._start_row

    @start_row.setter
    def start_row(self, start_row):
        r"""Sets the start_row of this PageInfo.

        :param start_row: The start_row of this PageInfo.
        :type start_row: int
        """
        self._start_row = start_row

    @property
    def total(self):
        r"""Gets the total of this PageInfo.

        :return: The total of this PageInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this PageInfo.

        :param total: The total of this PageInfo.
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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
