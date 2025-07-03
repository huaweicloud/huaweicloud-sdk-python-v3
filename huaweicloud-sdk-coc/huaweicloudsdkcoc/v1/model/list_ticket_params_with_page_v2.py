# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTicketParamsWithPageV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[str]',
        'count_filters': 'list[ListTicketParamsV2CountFilters]',
        'string_filters': 'list[ObjectFilterV2]',
        'group_by_filter': 'ObjectFilterV2',
        'int_filters': 'list[ObjectFilterV2]',
        'sort_filter': 'ObjectFilterV2',
        'condition': 'str',
        'page': 'int',
        'per_page': 'int',
        'contain_all': 'bool',
        'contain_total': 'bool',
        'contain_sub_ticket': 'bool',
        'ticket_types': 'list[str]'
    }

    attribute_map = {
        'fields': 'fields',
        'count_filters': 'count_filters',
        'string_filters': 'string_filters',
        'group_by_filter': 'group_by_filter',
        'int_filters': 'int_filters',
        'sort_filter': 'sort_filter',
        'condition': 'condition',
        'page': 'page',
        'per_page': 'per_page',
        'contain_all': 'contain_all',
        'contain_total': 'contain_total',
        'contain_sub_ticket': 'contain_sub_ticket',
        'ticket_types': 'ticket_types'
    }

    def __init__(self, fields=None, count_filters=None, string_filters=None, group_by_filter=None, int_filters=None, sort_filter=None, condition=None, page=None, per_page=None, contain_all=None, contain_total=None, contain_sub_ticket=None, ticket_types=None):
        r"""ListTicketParamsWithPageV2

        The model defined in huaweicloud sdk

        :param fields: 返回字段
        :type fields: list[str]
        :param count_filters: 批量计数
        :type count_filters: list[:class:`huaweicloudsdkcoc.v1.ListTicketParamsV2CountFilters`]
        :param string_filters: 字符串搜索条件
        :type string_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        :param group_by_filter: 
        :type group_by_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        :param int_filters: 整形过滤器
        :type int_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        :param sort_filter: 
        :type sort_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        :param condition: 表达式，对复杂表达式进行组装，可以用英文括号()、与&amp;、或|。示例：( filterName1 &amp; filterName2) | filterName3。filterName*：取自string_filters ObjectFilter.name。如果为空，string_filters中的条件默认是与的关系
        :type condition: str
        :param page: 当前页
        :type page: int
        :param per_page: 每页数量
        :type per_page: int
        :param contain_all: 是否返回所有数据
        :type contain_all: bool
        :param contain_total: 是否返回总数
        :type contain_total: bool
        :param contain_sub_ticket: 是否包含子单
        :type contain_sub_ticket: bool
        :param ticket_types: 搜索的工单类型
        :type ticket_types: list[str]
        """
        
        

        self._fields = None
        self._count_filters = None
        self._string_filters = None
        self._group_by_filter = None
        self._int_filters = None
        self._sort_filter = None
        self._condition = None
        self._page = None
        self._per_page = None
        self._contain_all = None
        self._contain_total = None
        self._contain_sub_ticket = None
        self._ticket_types = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if count_filters is not None:
            self.count_filters = count_filters
        if string_filters is not None:
            self.string_filters = string_filters
        if group_by_filter is not None:
            self.group_by_filter = group_by_filter
        if int_filters is not None:
            self.int_filters = int_filters
        if sort_filter is not None:
            self.sort_filter = sort_filter
        if condition is not None:
            self.condition = condition
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if contain_all is not None:
            self.contain_all = contain_all
        if contain_total is not None:
            self.contain_total = contain_total
        if contain_sub_ticket is not None:
            self.contain_sub_ticket = contain_sub_ticket
        if ticket_types is not None:
            self.ticket_types = ticket_types

    @property
    def fields(self):
        r"""Gets the fields of this ListTicketParamsWithPageV2.

        返回字段

        :return: The fields of this ListTicketParamsWithPageV2.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListTicketParamsWithPageV2.

        返回字段

        :param fields: The fields of this ListTicketParamsWithPageV2.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def count_filters(self):
        r"""Gets the count_filters of this ListTicketParamsWithPageV2.

        批量计数

        :return: The count_filters of this ListTicketParamsWithPageV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ListTicketParamsV2CountFilters`]
        """
        return self._count_filters

    @count_filters.setter
    def count_filters(self, count_filters):
        r"""Sets the count_filters of this ListTicketParamsWithPageV2.

        批量计数

        :param count_filters: The count_filters of this ListTicketParamsWithPageV2.
        :type count_filters: list[:class:`huaweicloudsdkcoc.v1.ListTicketParamsV2CountFilters`]
        """
        self._count_filters = count_filters

    @property
    def string_filters(self):
        r"""Gets the string_filters of this ListTicketParamsWithPageV2.

        字符串搜索条件

        :return: The string_filters of this ListTicketParamsWithPageV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        return self._string_filters

    @string_filters.setter
    def string_filters(self, string_filters):
        r"""Sets the string_filters of this ListTicketParamsWithPageV2.

        字符串搜索条件

        :param string_filters: The string_filters of this ListTicketParamsWithPageV2.
        :type string_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        self._string_filters = string_filters

    @property
    def group_by_filter(self):
        r"""Gets the group_by_filter of this ListTicketParamsWithPageV2.

        :return: The group_by_filter of this ListTicketParamsWithPageV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        return self._group_by_filter

    @group_by_filter.setter
    def group_by_filter(self, group_by_filter):
        r"""Sets the group_by_filter of this ListTicketParamsWithPageV2.

        :param group_by_filter: The group_by_filter of this ListTicketParamsWithPageV2.
        :type group_by_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        self._group_by_filter = group_by_filter

    @property
    def int_filters(self):
        r"""Gets the int_filters of this ListTicketParamsWithPageV2.

        整形过滤器

        :return: The int_filters of this ListTicketParamsWithPageV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        return self._int_filters

    @int_filters.setter
    def int_filters(self, int_filters):
        r"""Sets the int_filters of this ListTicketParamsWithPageV2.

        整形过滤器

        :param int_filters: The int_filters of this ListTicketParamsWithPageV2.
        :type int_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        self._int_filters = int_filters

    @property
    def sort_filter(self):
        r"""Gets the sort_filter of this ListTicketParamsWithPageV2.

        :return: The sort_filter of this ListTicketParamsWithPageV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        return self._sort_filter

    @sort_filter.setter
    def sort_filter(self, sort_filter):
        r"""Sets the sort_filter of this ListTicketParamsWithPageV2.

        :param sort_filter: The sort_filter of this ListTicketParamsWithPageV2.
        :type sort_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        self._sort_filter = sort_filter

    @property
    def condition(self):
        r"""Gets the condition of this ListTicketParamsWithPageV2.

        表达式，对复杂表达式进行组装，可以用英文括号()、与&、或|。示例：( filterName1 & filterName2) | filterName3。filterName*：取自string_filters ObjectFilter.name。如果为空，string_filters中的条件默认是与的关系

        :return: The condition of this ListTicketParamsWithPageV2.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ListTicketParamsWithPageV2.

        表达式，对复杂表达式进行组装，可以用英文括号()、与&、或|。示例：( filterName1 & filterName2) | filterName3。filterName*：取自string_filters ObjectFilter.name。如果为空，string_filters中的条件默认是与的关系

        :param condition: The condition of this ListTicketParamsWithPageV2.
        :type condition: str
        """
        self._condition = condition

    @property
    def page(self):
        r"""Gets the page of this ListTicketParamsWithPageV2.

        当前页

        :return: The page of this ListTicketParamsWithPageV2.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListTicketParamsWithPageV2.

        当前页

        :param page: The page of this ListTicketParamsWithPageV2.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListTicketParamsWithPageV2.

        每页数量

        :return: The per_page of this ListTicketParamsWithPageV2.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListTicketParamsWithPageV2.

        每页数量

        :param per_page: The per_page of this ListTicketParamsWithPageV2.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def contain_all(self):
        r"""Gets the contain_all of this ListTicketParamsWithPageV2.

        是否返回所有数据

        :return: The contain_all of this ListTicketParamsWithPageV2.
        :rtype: bool
        """
        return self._contain_all

    @contain_all.setter
    def contain_all(self, contain_all):
        r"""Sets the contain_all of this ListTicketParamsWithPageV2.

        是否返回所有数据

        :param contain_all: The contain_all of this ListTicketParamsWithPageV2.
        :type contain_all: bool
        """
        self._contain_all = contain_all

    @property
    def contain_total(self):
        r"""Gets the contain_total of this ListTicketParamsWithPageV2.

        是否返回总数

        :return: The contain_total of this ListTicketParamsWithPageV2.
        :rtype: bool
        """
        return self._contain_total

    @contain_total.setter
    def contain_total(self, contain_total):
        r"""Sets the contain_total of this ListTicketParamsWithPageV2.

        是否返回总数

        :param contain_total: The contain_total of this ListTicketParamsWithPageV2.
        :type contain_total: bool
        """
        self._contain_total = contain_total

    @property
    def contain_sub_ticket(self):
        r"""Gets the contain_sub_ticket of this ListTicketParamsWithPageV2.

        是否包含子单

        :return: The contain_sub_ticket of this ListTicketParamsWithPageV2.
        :rtype: bool
        """
        return self._contain_sub_ticket

    @contain_sub_ticket.setter
    def contain_sub_ticket(self, contain_sub_ticket):
        r"""Sets the contain_sub_ticket of this ListTicketParamsWithPageV2.

        是否包含子单

        :param contain_sub_ticket: The contain_sub_ticket of this ListTicketParamsWithPageV2.
        :type contain_sub_ticket: bool
        """
        self._contain_sub_ticket = contain_sub_ticket

    @property
    def ticket_types(self):
        r"""Gets the ticket_types of this ListTicketParamsWithPageV2.

        搜索的工单类型

        :return: The ticket_types of this ListTicketParamsWithPageV2.
        :rtype: list[str]
        """
        return self._ticket_types

    @ticket_types.setter
    def ticket_types(self, ticket_types):
        r"""Sets the ticket_types of this ListTicketParamsWithPageV2.

        搜索的工单类型

        :param ticket_types: The ticket_types of this ListTicketParamsWithPageV2.
        :type ticket_types: list[str]
        """
        self._ticket_types = ticket_types

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
        if not isinstance(other, ListTicketParamsWithPageV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
