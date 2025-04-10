# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'device_property_condition': 'DeviceDataCondition',
        'simple_timer_condition': 'SimpleTimerType',
        'daily_timer_condition': 'DailyTimerType',
        'device_linkage_status_condition': 'DeviceLinkageStatusCondition'
    }

    attribute_map = {
        'type': 'type',
        'device_property_condition': 'device_property_condition',
        'simple_timer_condition': 'simple_timer_condition',
        'daily_timer_condition': 'daily_timer_condition',
        'device_linkage_status_condition': 'device_linkage_status_condition'
    }

    def __init__(self, type=None, device_property_condition=None, simple_timer_condition=None, daily_timer_condition=None, device_linkage_status_condition=None):
        r"""RuleCondition

        The model defined in huaweicloud sdk

        :param type: **参数说明**：规则条件的类型。 **取值范围**： - DEVICE_DATA：设备属性数据类型条件。 - SIMPLE_TIMER：简单定时类型条件。 - DAILY_TIMER：每日定时类型条件。 - DEVICE_LINKAGE_STATUS：设备状态类型条件。
        :type type: str
        :param device_property_condition: 
        :type device_property_condition: :class:`huaweicloudsdkiotda.v5.DeviceDataCondition`
        :param simple_timer_condition: 
        :type simple_timer_condition: :class:`huaweicloudsdkiotda.v5.SimpleTimerType`
        :param daily_timer_condition: 
        :type daily_timer_condition: :class:`huaweicloudsdkiotda.v5.DailyTimerType`
        :param device_linkage_status_condition: 
        :type device_linkage_status_condition: :class:`huaweicloudsdkiotda.v5.DeviceLinkageStatusCondition`
        """
        
        

        self._type = None
        self._device_property_condition = None
        self._simple_timer_condition = None
        self._daily_timer_condition = None
        self._device_linkage_status_condition = None
        self.discriminator = None

        self.type = type
        if device_property_condition is not None:
            self.device_property_condition = device_property_condition
        if simple_timer_condition is not None:
            self.simple_timer_condition = simple_timer_condition
        if daily_timer_condition is not None:
            self.daily_timer_condition = daily_timer_condition
        if device_linkage_status_condition is not None:
            self.device_linkage_status_condition = device_linkage_status_condition

    @property
    def type(self):
        r"""Gets the type of this RuleCondition.

        **参数说明**：规则条件的类型。 **取值范围**： - DEVICE_DATA：设备属性数据类型条件。 - SIMPLE_TIMER：简单定时类型条件。 - DAILY_TIMER：每日定时类型条件。 - DEVICE_LINKAGE_STATUS：设备状态类型条件。

        :return: The type of this RuleCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleCondition.

        **参数说明**：规则条件的类型。 **取值范围**： - DEVICE_DATA：设备属性数据类型条件。 - SIMPLE_TIMER：简单定时类型条件。 - DAILY_TIMER：每日定时类型条件。 - DEVICE_LINKAGE_STATUS：设备状态类型条件。

        :param type: The type of this RuleCondition.
        :type type: str
        """
        self._type = type

    @property
    def device_property_condition(self):
        r"""Gets the device_property_condition of this RuleCondition.

        :return: The device_property_condition of this RuleCondition.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceDataCondition`
        """
        return self._device_property_condition

    @device_property_condition.setter
    def device_property_condition(self, device_property_condition):
        r"""Sets the device_property_condition of this RuleCondition.

        :param device_property_condition: The device_property_condition of this RuleCondition.
        :type device_property_condition: :class:`huaweicloudsdkiotda.v5.DeviceDataCondition`
        """
        self._device_property_condition = device_property_condition

    @property
    def simple_timer_condition(self):
        r"""Gets the simple_timer_condition of this RuleCondition.

        :return: The simple_timer_condition of this RuleCondition.
        :rtype: :class:`huaweicloudsdkiotda.v5.SimpleTimerType`
        """
        return self._simple_timer_condition

    @simple_timer_condition.setter
    def simple_timer_condition(self, simple_timer_condition):
        r"""Sets the simple_timer_condition of this RuleCondition.

        :param simple_timer_condition: The simple_timer_condition of this RuleCondition.
        :type simple_timer_condition: :class:`huaweicloudsdkiotda.v5.SimpleTimerType`
        """
        self._simple_timer_condition = simple_timer_condition

    @property
    def daily_timer_condition(self):
        r"""Gets the daily_timer_condition of this RuleCondition.

        :return: The daily_timer_condition of this RuleCondition.
        :rtype: :class:`huaweicloudsdkiotda.v5.DailyTimerType`
        """
        return self._daily_timer_condition

    @daily_timer_condition.setter
    def daily_timer_condition(self, daily_timer_condition):
        r"""Sets the daily_timer_condition of this RuleCondition.

        :param daily_timer_condition: The daily_timer_condition of this RuleCondition.
        :type daily_timer_condition: :class:`huaweicloudsdkiotda.v5.DailyTimerType`
        """
        self._daily_timer_condition = daily_timer_condition

    @property
    def device_linkage_status_condition(self):
        r"""Gets the device_linkage_status_condition of this RuleCondition.

        :return: The device_linkage_status_condition of this RuleCondition.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceLinkageStatusCondition`
        """
        return self._device_linkage_status_condition

    @device_linkage_status_condition.setter
    def device_linkage_status_condition(self, device_linkage_status_condition):
        r"""Sets the device_linkage_status_condition of this RuleCondition.

        :param device_linkage_status_condition: The device_linkage_status_condition of this RuleCondition.
        :type device_linkage_status_condition: :class:`huaweicloudsdkiotda.v5.DeviceLinkageStatusCondition`
        """
        self._device_linkage_status_condition = device_linkage_status_condition

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
        if not isinstance(other, RuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
