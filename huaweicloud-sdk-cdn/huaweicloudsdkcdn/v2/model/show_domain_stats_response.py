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
        'group_by': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'stat_type': 'str',
        'action': 'str',
        'interval': 'int',
        'result': 'dict(str, object)'
    }

    attribute_map = {
        'group_by': 'group_by',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type',
        'action': 'action',
        'interval': 'interval',
        'result': 'result'
    }

    def __init__(self, group_by=None, start_time=None, end_time=None, stat_type=None, action=None, interval=None, result=None):
        r"""ShowDomainStatsResponse

        The model defined in huaweicloud sdk

        :param group_by: **参数解释：** 数据分组方式 **取值范围：** domain：按域名分组 **默认取值：** 不分组
        :type group_by: str
        :param start_time: **参数解释：** 查询起始时间戳 **取值范围：** 不涉及
        :type start_time: int
        :param end_time: **参数解释：** 查询结束时间戳 **取值范围：** 不涉及
        :type end_time: int
        :param stat_type: **参数解释：** 统计指标类型 **取值范围：** - flux：流量 - req_num：请求总数
        :type stat_type: str
        :param action: **参数解释：** 查询数据类型 **取值范围：** - summary：汇总数据 - detail：明细数据
        :type action: str
        :param interval: **参数解释：** 查询时间粒度 **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应时间跨度的最小间隔 &gt; 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600
        :type interval: int
        :param result: **参数解释：** 按指定的分组方式组织的数据 **取值范围：** 不涉及
        :type result: dict(str, object)
        """
        
        super().__init__()

        self._group_by = None
        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self._action = None
        self._interval = None
        self._result = None
        self.discriminator = None

        if group_by is not None:
            self.group_by = group_by
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
    def group_by(self):
        r"""Gets the group_by of this ShowDomainStatsResponse.

        **参数解释：** 数据分组方式 **取值范围：** domain：按域名分组 **默认取值：** 不分组

        :return: The group_by of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowDomainStatsResponse.

        **参数解释：** 数据分组方式 **取值范围：** domain：按域名分组 **默认取值：** 不分组

        :param group_by: The group_by of this ShowDomainStatsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDomainStatsResponse.

        **参数解释：** 查询起始时间戳 **取值范围：** 不涉及

        :return: The start_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDomainStatsResponse.

        **参数解释：** 查询起始时间戳 **取值范围：** 不涉及

        :param start_time: The start_time of this ShowDomainStatsResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDomainStatsResponse.

        **参数解释：** 查询结束时间戳 **取值范围：** 不涉及

        :return: The end_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDomainStatsResponse.

        **参数解释：** 查询结束时间戳 **取值范围：** 不涉及

        :param end_time: The end_time of this ShowDomainStatsResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDomainStatsResponse.

        **参数解释：** 统计指标类型 **取值范围：** - flux：流量 - req_num：请求总数

        :return: The stat_type of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDomainStatsResponse.

        **参数解释：** 统计指标类型 **取值范围：** - flux：流量 - req_num：请求总数

        :param stat_type: The stat_type of this ShowDomainStatsResponse.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def action(self):
        r"""Gets the action of this ShowDomainStatsResponse.

        **参数解释：** 查询数据类型 **取值范围：** - summary：汇总数据 - detail：明细数据

        :return: The action of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowDomainStatsResponse.

        **参数解释：** 查询数据类型 **取值范围：** - summary：汇总数据 - detail：明细数据

        :param action: The action of this ShowDomainStatsResponse.
        :type action: str
        """
        self._action = action

    @property
    def interval(self):
        r"""Gets the interval of this ShowDomainStatsResponse.

        **参数解释：** 查询时间粒度 **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应时间跨度的最小间隔 > 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600

        :return: The interval of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDomainStatsResponse.

        **参数解释：** 查询时间粒度 **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应时间跨度的最小间隔 > 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600

        :param interval: The interval of this ShowDomainStatsResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def result(self):
        r"""Gets the result of this ShowDomainStatsResponse.

        **参数解释：** 按指定的分组方式组织的数据 **取值范围：** 不涉及

        :return: The result of this ShowDomainStatsResponse.
        :rtype: dict(str, object)
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowDomainStatsResponse.

        **参数解释：** 按指定的分组方式组织的数据 **取值范围：** 不涉及

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
