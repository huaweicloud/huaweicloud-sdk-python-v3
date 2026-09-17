# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'list[dict(str, ConditionVO)]',
        'filter_mode': 'str',
        'page': 'PageInfoVO',
        'sort': 'list[SortInfo]',
        'return_fields': 'list[str]'
    }

    attribute_map = {
        'filter': 'filter',
        'filter_mode': 'filter_mode',
        'page': 'page',
        'sort': 'sort',
        'return_fields': 'return_fields'
    }

    def __init__(self, filter=None, filter_mode=None, page=None, sort=None, return_fields=None):
        r"""QueryVO

        The model defined in huaweicloud sdk

        :param filter: 查询过滤器
        :type filter: list[dict(str, ConditionVO)]
        :param filter_mode: 过滤模式
        :type filter_mode: str
        :param page: 
        :type page: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        :param sort: 排序条件
        :type sort: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        :param return_fields: 返回字段
        :type return_fields: list[str]
        """
        
        

        self._filter = None
        self._filter_mode = None
        self._page = None
        self._sort = None
        self._return_fields = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if filter_mode is not None:
            self.filter_mode = filter_mode
        if page is not None:
            self.page = page
        if sort is not None:
            self.sort = sort
        if return_fields is not None:
            self.return_fields = return_fields

    @property
    def filter(self):
        r"""Gets the filter of this QueryVO.

        查询过滤器

        :return: The filter of this QueryVO.
        :rtype: list[dict(str, ConditionVO)]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this QueryVO.

        查询过滤器

        :param filter: The filter of this QueryVO.
        :type filter: list[dict(str, ConditionVO)]
        """
        self._filter = filter

    @property
    def filter_mode(self):
        r"""Gets the filter_mode of this QueryVO.

        过滤模式

        :return: The filter_mode of this QueryVO.
        :rtype: str
        """
        return self._filter_mode

    @filter_mode.setter
    def filter_mode(self, filter_mode):
        r"""Sets the filter_mode of this QueryVO.

        过滤模式

        :param filter_mode: The filter_mode of this QueryVO.
        :type filter_mode: str
        """
        self._filter_mode = filter_mode

    @property
    def page(self):
        r"""Gets the page of this QueryVO.

        :return: The page of this QueryVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this QueryVO.

        :param page: The page of this QueryVO.
        :type page: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        """
        self._page = page

    @property
    def sort(self):
        r"""Gets the sort of this QueryVO.

        排序条件

        :return: The sort of this QueryVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this QueryVO.

        排序条件

        :param sort: The sort of this QueryVO.
        :type sort: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        """
        self._sort = sort

    @property
    def return_fields(self):
        r"""Gets the return_fields of this QueryVO.

        返回字段

        :return: The return_fields of this QueryVO.
        :rtype: list[str]
        """
        return self._return_fields

    @return_fields.setter
    def return_fields(self, return_fields):
        r"""Sets the return_fields of this QueryVO.

        返回字段

        :param return_fields: The return_fields of this QueryVO.
        :type return_fields: list[str]
        """
        self._return_fields = return_fields

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
