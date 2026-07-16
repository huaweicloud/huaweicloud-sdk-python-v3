# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlgorithmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'group_by': 'str',
        'items': 'list[AlgorithmResponse]'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'group_by': 'group_by',
        'items': 'items'
    }

    def __init__(self, total=None, count=None, limit=None, offset=None, sort_by=None, order=None, group_by=None, items=None):
        r"""ListAlgorithmsResponse

        The model defined in huaweicloud sdk

        :param total: 查询到当前用户名下的所有算法总数。
        :type total: int
        :param count: 查询到当前用户名下的所有符合查询条件的算法总数。
        :type count: int
        :param limit: 查询到当前用户名下的所有算法限制个数。
        :type limit: int
        :param offset: 查询到当前用户名下的所有算法查询偏移量。
        :type offset: int
        :param sort_by: 查询到当前用户名下的所有算法排序依赖字段。
        :type sort_by: str
        :param order: 查询到当前用户名下的所有算法排序方式，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。
        :type order: str
        :param group_by: 查询到当前用户名下的所有算法分组方式。
        :type group_by: str
        :param items: 查询到当前用户名下的所有符合查询条件的算法详情。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponse`]
        """
        
        super().__init__()

        self._total = None
        self._count = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._group_by = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if group_by is not None:
            self.group_by = group_by
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法总数。

        :return: The total of this ListAlgorithmsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法总数。

        :param total: The total of this ListAlgorithmsResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        r"""Gets the count of this ListAlgorithmsResponse.

        查询到当前用户名下的所有符合查询条件的算法总数。

        :return: The count of this ListAlgorithmsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlgorithmsResponse.

        查询到当前用户名下的所有符合查询条件的算法总数。

        :param count: The count of this ListAlgorithmsResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法限制个数。

        :return: The limit of this ListAlgorithmsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法限制个数。

        :param limit: The limit of this ListAlgorithmsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法查询偏移量。

        :return: The offset of this ListAlgorithmsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法查询偏移量。

        :param offset: The offset of this ListAlgorithmsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法排序依赖字段。

        :return: The sort_by of this ListAlgorithmsResponse.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法排序依赖字段。

        :param sort_by: The sort_by of this ListAlgorithmsResponse.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法排序方式，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :return: The order of this ListAlgorithmsResponse.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法排序方式，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :param order: The order of this ListAlgorithmsResponse.
        :type order: str
        """
        self._order = order

    @property
    def group_by(self):
        r"""Gets the group_by of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法分组方式。

        :return: The group_by of this ListAlgorithmsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ListAlgorithmsResponse.

        查询到当前用户名下的所有算法分组方式。

        :param group_by: The group_by of this ListAlgorithmsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def items(self):
        r"""Gets the items of this ListAlgorithmsResponse.

        查询到当前用户名下的所有符合查询条件的算法详情。

        :return: The items of this ListAlgorithmsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListAlgorithmsResponse.

        查询到当前用户名下的所有符合查询条件的算法详情。

        :param items: The items of this ListAlgorithmsResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponse`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListAlgorithmsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAlgorithmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
