# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAction:

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
        'device_command': 'ActionDeviceCommand',
        'smn_forwarding': 'ActionSmnForwarding',
        'device_alarm': 'ActionDeviceAlarm'
    }

    attribute_map = {
        'type': 'type',
        'device_command': 'device_command',
        'smn_forwarding': 'smn_forwarding',
        'device_alarm': 'device_alarm'
    }

    def __init__(self, type=None, device_command=None, smn_forwarding=None, device_alarm=None):
        """RuleAction

        The model defined in huaweicloud sdk

        :param type: **参数说明**：规则动作的类型，端侧执行只支持下发设备命令消息类型。 **取值范围**： - DEVICE_CMD：下发设备命令消息类型。 - SMN_FORWARDING：发送SMN消息类型。 - DEVICE_ALARM：上报设备告警消息类型。当选择该类型时，condition中必须有DEVICE_DATA条件类型。该类型动作只能唯一。
        :type type: str
        :param device_command: 
        :type device_command: :class:`huaweicloudsdkiotda.v5.ActionDeviceCommand`
        :param smn_forwarding: 
        :type smn_forwarding: :class:`huaweicloudsdkiotda.v5.ActionSmnForwarding`
        :param device_alarm: 
        :type device_alarm: :class:`huaweicloudsdkiotda.v5.ActionDeviceAlarm`
        """
        
        

        self._type = None
        self._device_command = None
        self._smn_forwarding = None
        self._device_alarm = None
        self.discriminator = None

        self.type = type
        if device_command is not None:
            self.device_command = device_command
        if smn_forwarding is not None:
            self.smn_forwarding = smn_forwarding
        if device_alarm is not None:
            self.device_alarm = device_alarm

    @property
    def type(self):
        """Gets the type of this RuleAction.

        **参数说明**：规则动作的类型，端侧执行只支持下发设备命令消息类型。 **取值范围**： - DEVICE_CMD：下发设备命令消息类型。 - SMN_FORWARDING：发送SMN消息类型。 - DEVICE_ALARM：上报设备告警消息类型。当选择该类型时，condition中必须有DEVICE_DATA条件类型。该类型动作只能唯一。

        :return: The type of this RuleAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleAction.

        **参数说明**：规则动作的类型，端侧执行只支持下发设备命令消息类型。 **取值范围**： - DEVICE_CMD：下发设备命令消息类型。 - SMN_FORWARDING：发送SMN消息类型。 - DEVICE_ALARM：上报设备告警消息类型。当选择该类型时，condition中必须有DEVICE_DATA条件类型。该类型动作只能唯一。

        :param type: The type of this RuleAction.
        :type type: str
        """
        self._type = type

    @property
    def device_command(self):
        """Gets the device_command of this RuleAction.

        :return: The device_command of this RuleAction.
        :rtype: :class:`huaweicloudsdkiotda.v5.ActionDeviceCommand`
        """
        return self._device_command

    @device_command.setter
    def device_command(self, device_command):
        """Sets the device_command of this RuleAction.

        :param device_command: The device_command of this RuleAction.
        :type device_command: :class:`huaweicloudsdkiotda.v5.ActionDeviceCommand`
        """
        self._device_command = device_command

    @property
    def smn_forwarding(self):
        """Gets the smn_forwarding of this RuleAction.

        :return: The smn_forwarding of this RuleAction.
        :rtype: :class:`huaweicloudsdkiotda.v5.ActionSmnForwarding`
        """
        return self._smn_forwarding

    @smn_forwarding.setter
    def smn_forwarding(self, smn_forwarding):
        """Sets the smn_forwarding of this RuleAction.

        :param smn_forwarding: The smn_forwarding of this RuleAction.
        :type smn_forwarding: :class:`huaweicloudsdkiotda.v5.ActionSmnForwarding`
        """
        self._smn_forwarding = smn_forwarding

    @property
    def device_alarm(self):
        """Gets the device_alarm of this RuleAction.

        :return: The device_alarm of this RuleAction.
        :rtype: :class:`huaweicloudsdkiotda.v5.ActionDeviceAlarm`
        """
        return self._device_alarm

    @device_alarm.setter
    def device_alarm(self, device_alarm):
        """Sets the device_alarm of this RuleAction.

        :param device_alarm: The device_alarm of this RuleAction.
        :type device_alarm: :class:`huaweicloudsdkiotda.v5.ActionDeviceAlarm`
        """
        self._device_alarm = device_alarm

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
        if not isinstance(other, RuleAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
