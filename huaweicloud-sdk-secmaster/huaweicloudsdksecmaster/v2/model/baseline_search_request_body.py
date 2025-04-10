# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineSearchRequestBody:

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
        'condition': 'object'
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
        r"""BaselineSearchRequestBody

        The model defined in huaweicloud sdk

        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        :param sort_by: 排序关键字
        :type sort_by: str
        :param order: 降序或升序, DESC|ESC
        :type order: str
        :param from_date: 起始时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type from_date: str
        :param to_date: 截止时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type to_date: str
        :param condition: 搜索条件表达式
        :type condition: object
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
        r"""Gets the limit of this BaselineSearchRequestBody.

        分页大小

        :return: The limit of this BaselineSearchRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BaselineSearchRequestBody.

        分页大小

        :param limit: The limit of this BaselineSearchRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this BaselineSearchRequestBody.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this BaselineSearchRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BaselineSearchRequestBody.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this BaselineSearchRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this BaselineSearchRequestBody.

        排序关键字

        :return: The sort_by of this BaselineSearchRequestBody.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this BaselineSearchRequestBody.

        排序关键字

        :param sort_by: The sort_by of this BaselineSearchRequestBody.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this BaselineSearchRequestBody.

        降序或升序, DESC|ESC

        :return: The order of this BaselineSearchRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this BaselineSearchRequestBody.

        降序或升序, DESC|ESC

        :param order: The order of this BaselineSearchRequestBody.
        :type order: str
        """
        self._order = order

    @property
    def from_date(self):
        r"""Gets the from_date of this BaselineSearchRequestBody.

        起始时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The from_date of this BaselineSearchRequestBody.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this BaselineSearchRequestBody.

        起始时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param from_date: The from_date of this BaselineSearchRequestBody.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this BaselineSearchRequestBody.

        截止时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The to_date of this BaselineSearchRequestBody.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this BaselineSearchRequestBody.

        截止时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param to_date: The to_date of this BaselineSearchRequestBody.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def condition(self):
        r"""Gets the condition of this BaselineSearchRequestBody.

        搜索条件表达式

        :return: The condition of this BaselineSearchRequestBody.
        :rtype: object
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this BaselineSearchRequestBody.

        搜索条件表达式

        :param condition: The condition of this BaselineSearchRequestBody.
        :type condition: object
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
        if not isinstance(other, BaselineSearchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
