# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataobjectSearch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'condition': 'DataobjectSearchCondition'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'condition': 'condition'
    }

    def __init__(self, limit=None, offset=None, sort_by=None, order=None, from_date=None, to_date=None, condition=None):
        r"""DataobjectSearch

        The model defined in huaweicloud sdk

        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param sort_by: 排序字段：create_time | update_time
        :type sort_by: str
        :param order: 排序方式：DESC | ASC
        :type order: str
        :param from_date: 搜索开始时间，例如：2023-02-20T00:00:00.000Z
        :type from_date: str
        :param to_date: 搜索结束时间，例如：2023-02-27T23:59:59.999Z
        :type to_date: str
        :param condition: 
        :type condition: :class:`huaweicloudsdksecmaster.v2.DataobjectSearchCondition`
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._from_date = None
        self._to_date = None
        self._condition = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if condition is not None:
            self.condition = condition

    @property
    def limit(self):
        r"""Gets the limit of this DataobjectSearch.

        分页大小

        :return: The limit of this DataobjectSearch.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this DataobjectSearch.

        分页大小

        :param limit: The limit of this DataobjectSearch.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this DataobjectSearch.

        偏移量

        :return: The offset of this DataobjectSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this DataobjectSearch.

        偏移量

        :param offset: The offset of this DataobjectSearch.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this DataobjectSearch.

        排序字段：create_time | update_time

        :return: The sort_by of this DataobjectSearch.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this DataobjectSearch.

        排序字段：create_time | update_time

        :param sort_by: The sort_by of this DataobjectSearch.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this DataobjectSearch.

        排序方式：DESC | ASC

        :return: The order of this DataobjectSearch.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this DataobjectSearch.

        排序方式：DESC | ASC

        :param order: The order of this DataobjectSearch.
        :type order: str
        """
        self._order = order

    @property
    def from_date(self):
        r"""Gets the from_date of this DataobjectSearch.

        搜索开始时间，例如：2023-02-20T00:00:00.000Z

        :return: The from_date of this DataobjectSearch.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this DataobjectSearch.

        搜索开始时间，例如：2023-02-20T00:00:00.000Z

        :param from_date: The from_date of this DataobjectSearch.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this DataobjectSearch.

        搜索结束时间，例如：2023-02-27T23:59:59.999Z

        :return: The to_date of this DataobjectSearch.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this DataobjectSearch.

        搜索结束时间，例如：2023-02-27T23:59:59.999Z

        :param to_date: The to_date of this DataobjectSearch.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def condition(self):
        r"""Gets the condition of this DataobjectSearch.

        :return: The condition of this DataobjectSearch.
        :rtype: :class:`huaweicloudsdksecmaster.v2.DataobjectSearchCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this DataobjectSearch.

        :param condition: The condition of this DataobjectSearch.
        :type condition: :class:`huaweicloudsdksecmaster.v2.DataobjectSearchCondition`
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
        if not isinstance(other, DataobjectSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
