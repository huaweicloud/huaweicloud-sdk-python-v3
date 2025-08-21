# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowLimitStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy_type': 'str',
        'item_type': 'str',
        'limit_value': 'str',
        'alarm_percent_threshold': 'str',
        'ban_time': 'str'
    }

    attribute_map = {
        'strategy_type': 'strategy_type',
        'item_type': 'item_type',
        'limit_value': 'limit_value',
        'alarm_percent_threshold': 'alarm_percent_threshold',
        'ban_time': 'ban_time'
    }

    def __init__(self, strategy_type=None, item_type=None, limit_value=None, alarm_percent_threshold=None, ban_time=None):
        r"""FlowLimitStrategy

        The model defined in huaweicloud sdk

        :param strategy_type: **参数解释：**  用量统计类型 **约束限制：** 不涉及 **取值范围：** - instant: 瞬时用量 - hour: 累计用量（小时） - day: 累计用量（天） **默认取值：** 不涉及
        :type strategy_type: str
        :param item_type: **参数解释：**  用量封顶类型 **约束限制：** 不涉及 **取值范围：** - bandwidth: 带宽封顶，单位: bit/s - traffic: 流量封顶，单位: bit **默认取值：** 不涉及
        :type item_type: str
        :param limit_value: **参数解释：** 用量封顶阈值，域名用量达到该阈值后，将会停用域名 **约束限制：** 不涉及 **取值范围：** 必须为正整数 **默认取值：** 不涉及
        :type limit_value: str
        :param alarm_percent_threshold: **参数解释：** 用量告警阈值，域名用量达到该阈值后，将会发送告警 **约束限制：** 不涉及 **取值范围：** 1-90 **默认取值：** 不涉及
        :type alarm_percent_threshold: str
        :param ban_time: **参数解释：** 域名封禁周期 **约束限制：** ban_time设置为0时，表示不自动解封，需要客户手动解封域名 **取值范围：** - 0: 不自动解封 - 60: 60分钟，即1个小时 - 720: 720分钟，即12个小时 - 1440: 1440分钟，即24个小时 - 4320: 4320分钟，即3天 **默认取值：** 不涉及
        :type ban_time: str
        """
        
        

        self._strategy_type = None
        self._item_type = None
        self._limit_value = None
        self._alarm_percent_threshold = None
        self._ban_time = None
        self.discriminator = None

        if strategy_type is not None:
            self.strategy_type = strategy_type
        if item_type is not None:
            self.item_type = item_type
        if limit_value is not None:
            self.limit_value = limit_value
        if alarm_percent_threshold is not None:
            self.alarm_percent_threshold = alarm_percent_threshold
        if ban_time is not None:
            self.ban_time = ban_time

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this FlowLimitStrategy.

        **参数解释：**  用量统计类型 **约束限制：** 不涉及 **取值范围：** - instant: 瞬时用量 - hour: 累计用量（小时） - day: 累计用量（天） **默认取值：** 不涉及

        :return: The strategy_type of this FlowLimitStrategy.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this FlowLimitStrategy.

        **参数解释：**  用量统计类型 **约束限制：** 不涉及 **取值范围：** - instant: 瞬时用量 - hour: 累计用量（小时） - day: 累计用量（天） **默认取值：** 不涉及

        :param strategy_type: The strategy_type of this FlowLimitStrategy.
        :type strategy_type: str
        """
        self._strategy_type = strategy_type

    @property
    def item_type(self):
        r"""Gets the item_type of this FlowLimitStrategy.

        **参数解释：**  用量封顶类型 **约束限制：** 不涉及 **取值范围：** - bandwidth: 带宽封顶，单位: bit/s - traffic: 流量封顶，单位: bit **默认取值：** 不涉及

        :return: The item_type of this FlowLimitStrategy.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        r"""Sets the item_type of this FlowLimitStrategy.

        **参数解释：**  用量封顶类型 **约束限制：** 不涉及 **取值范围：** - bandwidth: 带宽封顶，单位: bit/s - traffic: 流量封顶，单位: bit **默认取值：** 不涉及

        :param item_type: The item_type of this FlowLimitStrategy.
        :type item_type: str
        """
        self._item_type = item_type

    @property
    def limit_value(self):
        r"""Gets the limit_value of this FlowLimitStrategy.

        **参数解释：** 用量封顶阈值，域名用量达到该阈值后，将会停用域名 **约束限制：** 不涉及 **取值范围：** 必须为正整数 **默认取值：** 不涉及

        :return: The limit_value of this FlowLimitStrategy.
        :rtype: str
        """
        return self._limit_value

    @limit_value.setter
    def limit_value(self, limit_value):
        r"""Sets the limit_value of this FlowLimitStrategy.

        **参数解释：** 用量封顶阈值，域名用量达到该阈值后，将会停用域名 **约束限制：** 不涉及 **取值范围：** 必须为正整数 **默认取值：** 不涉及

        :param limit_value: The limit_value of this FlowLimitStrategy.
        :type limit_value: str
        """
        self._limit_value = limit_value

    @property
    def alarm_percent_threshold(self):
        r"""Gets the alarm_percent_threshold of this FlowLimitStrategy.

        **参数解释：** 用量告警阈值，域名用量达到该阈值后，将会发送告警 **约束限制：** 不涉及 **取值范围：** 1-90 **默认取值：** 不涉及

        :return: The alarm_percent_threshold of this FlowLimitStrategy.
        :rtype: str
        """
        return self._alarm_percent_threshold

    @alarm_percent_threshold.setter
    def alarm_percent_threshold(self, alarm_percent_threshold):
        r"""Sets the alarm_percent_threshold of this FlowLimitStrategy.

        **参数解释：** 用量告警阈值，域名用量达到该阈值后，将会发送告警 **约束限制：** 不涉及 **取值范围：** 1-90 **默认取值：** 不涉及

        :param alarm_percent_threshold: The alarm_percent_threshold of this FlowLimitStrategy.
        :type alarm_percent_threshold: str
        """
        self._alarm_percent_threshold = alarm_percent_threshold

    @property
    def ban_time(self):
        r"""Gets the ban_time of this FlowLimitStrategy.

        **参数解释：** 域名封禁周期 **约束限制：** ban_time设置为0时，表示不自动解封，需要客户手动解封域名 **取值范围：** - 0: 不自动解封 - 60: 60分钟，即1个小时 - 720: 720分钟，即12个小时 - 1440: 1440分钟，即24个小时 - 4320: 4320分钟，即3天 **默认取值：** 不涉及

        :return: The ban_time of this FlowLimitStrategy.
        :rtype: str
        """
        return self._ban_time

    @ban_time.setter
    def ban_time(self, ban_time):
        r"""Sets the ban_time of this FlowLimitStrategy.

        **参数解释：** 域名封禁周期 **约束限制：** ban_time设置为0时，表示不自动解封，需要客户手动解封域名 **取值范围：** - 0: 不自动解封 - 60: 60分钟，即1个小时 - 720: 720分钟，即12个小时 - 1440: 1440分钟，即24个小时 - 4320: 4320分钟，即3天 **默认取值：** 不涉及

        :param ban_time: The ban_time of this FlowLimitStrategy.
        :type ban_time: str
        """
        self._ban_time = ban_time

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
        if not isinstance(other, FlowLimitStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
