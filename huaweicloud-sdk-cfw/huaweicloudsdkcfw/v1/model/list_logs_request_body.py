# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filters': 'list[Filter]',
        'limit': 'int',
        'offset': 'int',
        'log_id': 'str',
        'next_date': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'log_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'filters': 'filters',
        'limit': 'limit',
        'offset': 'offset',
        'log_id': 'log_id',
        'next_date': 'next_date',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'log_type': 'log_type',
        'type': 'type'
    }

    def __init__(self, filters=None, limit=None, offset=None, log_id=None, next_date=None, start_time=None, end_time=None, log_type=None, type=None):
        r"""ListLogsRequestBody

        The model defined in huaweicloud sdk

        :param filters: **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及
        :type filters: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        :param limit: **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及
        :type limit: int
        :param offset: **参数解释**： 偏移量 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 相对于上一页的偏移量 **默认取值**： 不涉及
        :type offset: int
        :param log_id: **参数解释**： 文档ID **约束限制**： 第一页为空，其他页不为空 **取值范围**： 上一次查询最后一条数据的log_id **默认取值**： 不涉及
        :type log_id: str
        :param next_date: **参数解释**： 下个日期 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 查询流量日志时为上一次查询最后一条数据的end_time **默认取值**： 不涉及
        :type next_date: int
        :param start_time: **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type start_time: int
        :param end_time: **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type end_time: int
        :param log_type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及
        :type log_type: str
        :param type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及
        :type type: str
        """
        
        

        self._filters = None
        self._limit = None
        self._offset = None
        self._log_id = None
        self._next_date = None
        self._start_time = None
        self._end_time = None
        self._log_type = None
        self._type = None
        self.discriminator = None

        if filters is not None:
            self.filters = filters
        self.limit = limit
        if offset is not None:
            self.offset = offset
        if log_id is not None:
            self.log_id = log_id
        if next_date is not None:
            self.next_date = next_date
        self.start_time = start_time
        self.end_time = end_time
        self.log_type = log_type
        self.type = type

    @property
    def filters(self):
        r"""Gets the filters of this ListLogsRequestBody.

        **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :return: The filters of this ListLogsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ListLogsRequestBody.

        **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :param filters: The filters of this ListLogsRequestBody.
        :type filters: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        """
        self._filters = filters

    @property
    def limit(self):
        r"""Gets the limit of this ListLogsRequestBody.

        **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :return: The limit of this ListLogsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLogsRequestBody.

        **参数解释**： 每页显示个数 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :param limit: The limit of this ListLogsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListLogsRequestBody.

        **参数解释**： 偏移量 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 相对于上一页的偏移量 **默认取值**： 不涉及

        :return: The offset of this ListLogsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLogsRequestBody.

        **参数解释**： 偏移量 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 相对于上一页的偏移量 **默认取值**： 不涉及

        :param offset: The offset of this ListLogsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def log_id(self):
        r"""Gets the log_id of this ListLogsRequestBody.

        **参数解释**： 文档ID **约束限制**： 第一页为空，其他页不为空 **取值范围**： 上一次查询最后一条数据的log_id **默认取值**： 不涉及

        :return: The log_id of this ListLogsRequestBody.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this ListLogsRequestBody.

        **参数解释**： 文档ID **约束限制**： 第一页为空，其他页不为空 **取值范围**： 上一次查询最后一条数据的log_id **默认取值**： 不涉及

        :param log_id: The log_id of this ListLogsRequestBody.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def next_date(self):
        r"""Gets the next_date of this ListLogsRequestBody.

        **参数解释**： 下个日期 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 查询流量日志时为上一次查询最后一条数据的end_time **默认取值**： 不涉及

        :return: The next_date of this ListLogsRequestBody.
        :rtype: int
        """
        return self._next_date

    @next_date.setter
    def next_date(self, next_date):
        r"""Sets the next_date of this ListLogsRequestBody.

        **参数解释**： 下个日期 **约束限制**： 第一页为空，其他页不为空 **取值范围**： 查询流量日志时为上一次查询最后一条数据的end_time **默认取值**： 不涉及

        :param next_date: The next_date of this ListLogsRequestBody.
        :type next_date: int
        """
        self._next_date = next_date

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLogsRequestBody.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ListLogsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLogsRequestBody.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ListLogsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLogsRequestBody.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ListLogsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLogsRequestBody.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ListLogsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def log_type(self):
        r"""Gets the log_type of this ListLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :return: The log_type of this ListLogsRequestBody.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ListLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :param log_type: The log_type of this ListLogsRequestBody.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def type(self):
        r"""Gets the type of this ListLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及

        :return: The type of this ListLogsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及

        :param type: The type of this ListLogsRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
