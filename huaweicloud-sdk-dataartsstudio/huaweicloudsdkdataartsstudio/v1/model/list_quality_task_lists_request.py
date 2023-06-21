# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQualityTaskListsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'int',
        'page_size': 'int',
        'offset': 'int',
        'limit': 'int',
        'category_id': 'int',
        'rule_name': 'str',
        'schedule_status': 'int',
        'schedule_period': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'result_status': 'int',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'start': 'start',
        'page_size': 'page_size',
        'offset': 'offset',
        'limit': 'limit',
        'category_id': 'category_id',
        'rule_name': 'rule_name',
        'schedule_status': 'schedule_status',
        'schedule_period': 'schedule_period',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result_status': 'result_status',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, start=None, page_size=None, offset=None, limit=None, category_id=None, rule_name=None, schedule_status=None, schedule_period=None, start_time=None, end_time=None, result_status=None, sort=None, order=None):
        """ListQualityTaskListsRequest

        The model defined in huaweicloud sdk

        :param start: start number
        :type start: int
        :param page_size: page size
        :type page_size: int
        :param offset: 分页查询偏移量
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param category_id: category id
        :type category_id: int
        :param rule_name: rule name
        :type rule_name: str
        :param schedule_status: schedule status
        :type schedule_status: int
        :param schedule_period: schedule period
        :type schedule_period: int
        :param start_time: 开始时间(搜索)
        :type start_time: str
        :param end_time: 结束时间(搜索)
        :type end_time: str
        :param result_status: 最近运行结果 0：运行中 1：异常 2：告警 3：正常
        :type result_status: int
        :param sort: 排序字段
        :type sort: str
        :param order: 排序方式
        :type order: str
        """
        
        

        self._start = None
        self._page_size = None
        self._offset = None
        self._limit = None
        self._category_id = None
        self._rule_name = None
        self._schedule_status = None
        self._schedule_period = None
        self._start_time = None
        self._end_time = None
        self._result_status = None
        self._sort = None
        self._order = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if page_size is not None:
            self.page_size = page_size
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if category_id is not None:
            self.category_id = category_id
        if rule_name is not None:
            self.rule_name = rule_name
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if schedule_period is not None:
            self.schedule_period = schedule_period
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result_status is not None:
            self.result_status = result_status
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def start(self):
        """Gets the start of this ListQualityTaskListsRequest.

        start number

        :return: The start of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListQualityTaskListsRequest.

        start number

        :param start: The start of this ListQualityTaskListsRequest.
        :type start: int
        """
        self._start = start

    @property
    def page_size(self):
        """Gets the page_size of this ListQualityTaskListsRequest.

        page size

        :return: The page_size of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListQualityTaskListsRequest.

        page size

        :param page_size: The page_size of this ListQualityTaskListsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def offset(self):
        """Gets the offset of this ListQualityTaskListsRequest.

        分页查询偏移量

        :return: The offset of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListQualityTaskListsRequest.

        分页查询偏移量

        :param offset: The offset of this ListQualityTaskListsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListQualityTaskListsRequest.

        每页显示的条目数量

        :return: The limit of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListQualityTaskListsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListQualityTaskListsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def category_id(self):
        """Gets the category_id of this ListQualityTaskListsRequest.

        category id

        :return: The category_id of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ListQualityTaskListsRequest.

        category id

        :param category_id: The category_id of this ListQualityTaskListsRequest.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ListQualityTaskListsRequest.

        rule name

        :return: The rule_name of this ListQualityTaskListsRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListQualityTaskListsRequest.

        rule name

        :param rule_name: The rule_name of this ListQualityTaskListsRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ListQualityTaskListsRequest.

        schedule status

        :return: The schedule_status of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ListQualityTaskListsRequest.

        schedule status

        :param schedule_status: The schedule_status of this ListQualityTaskListsRequest.
        :type schedule_status: int
        """
        self._schedule_status = schedule_status

    @property
    def schedule_period(self):
        """Gets the schedule_period of this ListQualityTaskListsRequest.

        schedule period

        :return: The schedule_period of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        """Sets the schedule_period of this ListQualityTaskListsRequest.

        schedule period

        :param schedule_period: The schedule_period of this ListQualityTaskListsRequest.
        :type schedule_period: int
        """
        self._schedule_period = schedule_period

    @property
    def start_time(self):
        """Gets the start_time of this ListQualityTaskListsRequest.

        开始时间(搜索)

        :return: The start_time of this ListQualityTaskListsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListQualityTaskListsRequest.

        开始时间(搜索)

        :param start_time: The start_time of this ListQualityTaskListsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListQualityTaskListsRequest.

        结束时间(搜索)

        :return: The end_time of this ListQualityTaskListsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListQualityTaskListsRequest.

        结束时间(搜索)

        :param end_time: The end_time of this ListQualityTaskListsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result_status(self):
        """Gets the result_status of this ListQualityTaskListsRequest.

        最近运行结果 0：运行中 1：异常 2：告警 3：正常

        :return: The result_status of this ListQualityTaskListsRequest.
        :rtype: int
        """
        return self._result_status

    @result_status.setter
    def result_status(self, result_status):
        """Sets the result_status of this ListQualityTaskListsRequest.

        最近运行结果 0：运行中 1：异常 2：告警 3：正常

        :param result_status: The result_status of this ListQualityTaskListsRequest.
        :type result_status: int
        """
        self._result_status = result_status

    @property
    def sort(self):
        """Gets the sort of this ListQualityTaskListsRequest.

        排序字段

        :return: The sort of this ListQualityTaskListsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListQualityTaskListsRequest.

        排序字段

        :param sort: The sort of this ListQualityTaskListsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        """Gets the order of this ListQualityTaskListsRequest.

        排序方式

        :return: The order of this ListQualityTaskListsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListQualityTaskListsRequest.

        排序方式

        :param order: The order of this ListQualityTaskListsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListQualityTaskListsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
