# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportLogsRequestBody:

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
        'start_time': 'int',
        'end_time': 'int',
        'log_type': 'str',
        'type': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'filters': 'filters',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'log_type': 'log_type',
        'type': 'type',
        'time_zone': 'time_zone'
    }

    def __init__(self, filters=None, start_time=None, end_time=None, log_type=None, type=None, time_zone=None):
        r"""ExportLogsRequestBody

        The model defined in huaweicloud sdk

        :param filters: **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及
        :type filters: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        :param start_time: **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type start_time: int
        :param end_time: **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type end_time: int
        :param log_type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及
        :type log_type: str
        :param type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及
        :type type: str
        :param time_zone: **参数解释**： 时区 **约束限制**： 不涉及 **取值范围**： \&quot;GMT+08:00\&quot; **默认取值**： 不涉及
        :type time_zone: str
        """
        
        

        self._filters = None
        self._start_time = None
        self._end_time = None
        self._log_type = None
        self._type = None
        self._time_zone = None
        self.discriminator = None

        if filters is not None:
            self.filters = filters
        self.start_time = start_time
        self.end_time = end_time
        self.log_type = log_type
        self.type = type
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def filters(self):
        r"""Gets the filters of this ExportLogsRequestBody.

        **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :return: The filters of this ExportLogsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ExportLogsRequestBody.

        **参数解释**： 过滤条件 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :param filters: The filters of this ExportLogsRequestBody.
        :type filters: list[:class:`huaweicloudsdkcfw.v1.Filter`]
        """
        self._filters = filters

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportLogsRequestBody.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ExportLogsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportLogsRequestBody.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ExportLogsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportLogsRequestBody.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ExportLogsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportLogsRequestBody.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ExportLogsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def log_type(self):
        r"""Gets the log_type of this ExportLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :return: The log_type of this ExportLogsRequestBody.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ExportLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :param log_type: The log_type of this ExportLogsRequestBody.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def type(self):
        r"""Gets the type of this ExportLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及

        :return: The type of this ExportLogsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExportLogsRequestBody.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： attack为攻击日志、acl 访问控制日志，flow 流量日志，url url日志 **默认取值**： 不涉及

        :param type: The type of this ExportLogsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ExportLogsRequestBody.

        **参数解释**： 时区 **约束限制**： 不涉及 **取值范围**： \"GMT+08:00\" **默认取值**： 不涉及

        :return: The time_zone of this ExportLogsRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ExportLogsRequestBody.

        **参数解释**： 时区 **约束限制**： 不涉及 **取值范围**： \"GMT+08:00\" **默认取值**： 不涉及

        :param time_zone: The time_zone of this ExportLogsRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, ExportLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
