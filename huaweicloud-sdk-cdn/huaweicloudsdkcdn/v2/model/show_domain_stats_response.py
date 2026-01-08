# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'stat_type': 'str',
        'action': 'str',
        'interval': 'int',
        'result': 'dict(str, object)'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type',
        'action': 'action',
        'interval': 'interval',
        'result': 'result'
    }

    def __init__(self, start_time=None, end_time=None, stat_type=None, action=None, interval=None, result=None):
        r"""ShowDomainStatsResponse

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间戳。
        :type start_time: int
        :param end_time: 查询结束时间戳
        :type end_time: int
        :param stat_type: 参数类型支持：flux(流量)，req_num(请求总数)。
        :type stat_type: str
        :param action: **参数解释：** 规则行为 **约束限制：** 不涉及
        :type action: str
        :param interval: 查询时间间隔，单位：秒
        :type interval: int
        :param result: 按指定的分组方式组织的数据
        :type result: dict(str, object)
        """
        
        super().__init__()

        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self._action = None
        self._interval = None
        self._result = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if stat_type is not None:
            self.stat_type = stat_type
        if action is not None:
            self.action = action
        if interval is not None:
            self.interval = interval
        if result is not None:
            self.result = result

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDomainStatsResponse.

        查询起始时间戳。

        :return: The start_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDomainStatsResponse.

        查询起始时间戳。

        :param start_time: The start_time of this ShowDomainStatsResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDomainStatsResponse.

        查询结束时间戳

        :return: The end_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDomainStatsResponse.

        查询结束时间戳

        :param end_time: The end_time of this ShowDomainStatsResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDomainStatsResponse.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :return: The stat_type of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDomainStatsResponse.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :param stat_type: The stat_type of this ShowDomainStatsResponse.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def action(self):
        r"""Gets the action of this ShowDomainStatsResponse.

        **参数解释：** 规则行为 **约束限制：** 不涉及

        :return: The action of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowDomainStatsResponse.

        **参数解释：** 规则行为 **约束限制：** 不涉及

        :param action: The action of this ShowDomainStatsResponse.
        :type action: str
        """
        self._action = action

    @property
    def interval(self):
        r"""Gets the interval of this ShowDomainStatsResponse.

        查询时间间隔，单位：秒

        :return: The interval of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDomainStatsResponse.

        查询时间间隔，单位：秒

        :param interval: The interval of this ShowDomainStatsResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def result(self):
        r"""Gets the result of this ShowDomainStatsResponse.

        按指定的分组方式组织的数据

        :return: The result of this ShowDomainStatsResponse.
        :rtype: dict(str, object)
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowDomainStatsResponse.

        按指定的分组方式组织的数据

        :param result: The result of this ShowDomainStatsResponse.
        :type result: dict(str, object)
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainStatsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDomainStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
