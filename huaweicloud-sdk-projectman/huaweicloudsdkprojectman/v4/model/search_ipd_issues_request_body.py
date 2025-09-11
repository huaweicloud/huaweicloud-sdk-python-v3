# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchIpdIssuesRequestBody:

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
        'page': 'PageInfoVO',
        'return_fields': 'list[str]',
        'sort': 'list[SortInfo]'
    }

    attribute_map = {
        'filter': 'filter',
        'page': 'page',
        'return_fields': 'return_fields',
        'sort': 'sort'
    }

    def __init__(self, filter=None, page=None, return_fields=None, sort=None):
        r"""SearchIpdIssuesRequestBody

        The model defined in huaweicloud sdk

        :param filter: 过滤条件
        :type filter: list[dict(str, ConditionVO)]
        :param page: 
        :type page: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        :param return_fields: 返回字段
        :type return_fields: list[str]
        :param sort: 排序字段
        :type sort: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        """
        
        

        self._filter = None
        self._page = None
        self._return_fields = None
        self._sort = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if page is not None:
            self.page = page
        if return_fields is not None:
            self.return_fields = return_fields
        if sort is not None:
            self.sort = sort

    @property
    def filter(self):
        r"""Gets the filter of this SearchIpdIssuesRequestBody.

        过滤条件

        :return: The filter of this SearchIpdIssuesRequestBody.
        :rtype: list[dict(str, ConditionVO)]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this SearchIpdIssuesRequestBody.

        过滤条件

        :param filter: The filter of this SearchIpdIssuesRequestBody.
        :type filter: list[dict(str, ConditionVO)]
        """
        self._filter = filter

    @property
    def page(self):
        r"""Gets the page of this SearchIpdIssuesRequestBody.

        :return: The page of this SearchIpdIssuesRequestBody.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this SearchIpdIssuesRequestBody.

        :param page: The page of this SearchIpdIssuesRequestBody.
        :type page: :class:`huaweicloudsdkprojectman.v4.PageInfoVO`
        """
        self._page = page

    @property
    def return_fields(self):
        r"""Gets the return_fields of this SearchIpdIssuesRequestBody.

        返回字段

        :return: The return_fields of this SearchIpdIssuesRequestBody.
        :rtype: list[str]
        """
        return self._return_fields

    @return_fields.setter
    def return_fields(self, return_fields):
        r"""Sets the return_fields of this SearchIpdIssuesRequestBody.

        返回字段

        :param return_fields: The return_fields of this SearchIpdIssuesRequestBody.
        :type return_fields: list[str]
        """
        self._return_fields = return_fields

    @property
    def sort(self):
        r"""Gets the sort of this SearchIpdIssuesRequestBody.

        排序字段

        :return: The sort of this SearchIpdIssuesRequestBody.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this SearchIpdIssuesRequestBody.

        排序字段

        :param sort: The sort of this SearchIpdIssuesRequestBody.
        :type sort: list[:class:`huaweicloudsdkprojectman.v4.SortInfo`]
        """
        self._sort = sort

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
        if not isinstance(other, SearchIpdIssuesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
