# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTicketParamsV2:

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
        'condition': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'count_filters': 'count_filters',
        'string_filters': 'string_filters',
        'group_by_filter': 'group_by_filter',
        'int_filters': 'int_filters',
        'sort_filter': 'sort_filter',
        'condition': 'condition'
    }

    def __init__(self, fields=None, count_filters=None, string_filters=None, group_by_filter=None, int_filters=None, sort_filter=None, condition=None):
        r"""ListTicketParamsV2

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
        """
        
        

        self._fields = None
        self._count_filters = None
        self._string_filters = None
        self._group_by_filter = None
        self._int_filters = None
        self._sort_filter = None
        self._condition = None
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

    @property
    def fields(self):
        r"""Gets the fields of this ListTicketParamsV2.

        返回字段

        :return: The fields of this ListTicketParamsV2.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListTicketParamsV2.

        返回字段

        :param fields: The fields of this ListTicketParamsV2.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def count_filters(self):
        r"""Gets the count_filters of this ListTicketParamsV2.

        批量计数

        :return: The count_filters of this ListTicketParamsV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ListTicketParamsV2CountFilters`]
        """
        return self._count_filters

    @count_filters.setter
    def count_filters(self, count_filters):
        r"""Sets the count_filters of this ListTicketParamsV2.

        批量计数

        :param count_filters: The count_filters of this ListTicketParamsV2.
        :type count_filters: list[:class:`huaweicloudsdkcoc.v1.ListTicketParamsV2CountFilters`]
        """
        self._count_filters = count_filters

    @property
    def string_filters(self):
        r"""Gets the string_filters of this ListTicketParamsV2.

        字符串搜索条件

        :return: The string_filters of this ListTicketParamsV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        return self._string_filters

    @string_filters.setter
    def string_filters(self, string_filters):
        r"""Sets the string_filters of this ListTicketParamsV2.

        字符串搜索条件

        :param string_filters: The string_filters of this ListTicketParamsV2.
        :type string_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        self._string_filters = string_filters

    @property
    def group_by_filter(self):
        r"""Gets the group_by_filter of this ListTicketParamsV2.

        :return: The group_by_filter of this ListTicketParamsV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        return self._group_by_filter

    @group_by_filter.setter
    def group_by_filter(self, group_by_filter):
        r"""Sets the group_by_filter of this ListTicketParamsV2.

        :param group_by_filter: The group_by_filter of this ListTicketParamsV2.
        :type group_by_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        self._group_by_filter = group_by_filter

    @property
    def int_filters(self):
        r"""Gets the int_filters of this ListTicketParamsV2.

        整形过滤器

        :return: The int_filters of this ListTicketParamsV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        return self._int_filters

    @int_filters.setter
    def int_filters(self, int_filters):
        r"""Sets the int_filters of this ListTicketParamsV2.

        整形过滤器

        :param int_filters: The int_filters of this ListTicketParamsV2.
        :type int_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        self._int_filters = int_filters

    @property
    def sort_filter(self):
        r"""Gets the sort_filter of this ListTicketParamsV2.

        :return: The sort_filter of this ListTicketParamsV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        return self._sort_filter

    @sort_filter.setter
    def sort_filter(self, sort_filter):
        r"""Sets the sort_filter of this ListTicketParamsV2.

        :param sort_filter: The sort_filter of this ListTicketParamsV2.
        :type sort_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilterV2`
        """
        self._sort_filter = sort_filter

    @property
    def condition(self):
        r"""Gets the condition of this ListTicketParamsV2.

        表达式，对复杂表达式进行组装，可以用英文括号()、与&、或|。示例：( filterName1 & filterName2) | filterName3。filterName*：取自string_filters ObjectFilter.name。如果为空，string_filters中的条件默认是与的关系

        :return: The condition of this ListTicketParamsV2.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ListTicketParamsV2.

        表达式，对复杂表达式进行组装，可以用英文括号()、与&、或|。示例：( filterName1 & filterName2) | filterName3。filterName*：取自string_filters ObjectFilter.name。如果为空，string_filters中的条件默认是与的关系

        :param condition: The condition of this ListTicketParamsV2.
        :type condition: str
        """
        self._condition = condition

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
        if not isinstance(other, ListTicketParamsV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
