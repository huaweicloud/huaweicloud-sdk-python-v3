# coding: utf-8

import pprint
import re

import six





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
        'addition': 'list[str]',
        'smn_forwarding': 'ActionSmnForwarding',
        'device_alarm': 'ActionDeviceAlarm',
        'device_command': 'ActionDeviceCommand',
        'dis_forwarding': 'ActionDisForwarding',
        'obs_forwarding': 'ActionObsForwarding',
        'roma_forwarding': 'ActionRomaForwarding',
        'iota_forwarding': 'ActionIoTAForwarding',
        'kafka_forwarding': 'ActionKafkaForwarding'
    }

    attribute_map = {
        'type': 'type',
        'addition': 'addition',
        'smn_forwarding': 'smn_forwarding',
        'device_alarm': 'device_alarm',
        'device_command': 'device_command',
        'dis_forwarding': 'dis_forwarding',
        'obs_forwarding': 'obs_forwarding',
        'roma_forwarding': 'roma_forwarding',
        'iota_forwarding': 'iota_forwarding',
        'kafka_forwarding': 'kafka_forwarding'
    }

    def __init__(self, type=None, addition=None, smn_forwarding=None, device_alarm=None, device_command=None, dis_forwarding=None, obs_forwarding=None, roma_forwarding=None, iota_forwarding=None, kafka_forwarding=None):
        """RuleAction - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._addition = None
        self._smn_forwarding = None
        self._device_alarm = None
        self._device_command = None
        self._dis_forwarding = None
        self._obs_forwarding = None
        self._roma_forwarding = None
        self._iota_forwarding = None
        self._kafka_forwarding = None
        self.discriminator = None

        self.type = type
        if addition is not None:
            self.addition = addition
        if smn_forwarding is not None:
            self.smn_forwarding = smn_forwarding
        if device_alarm is not None:
            self.device_alarm = device_alarm
        if device_command is not None:
            self.device_command = device_command
        if dis_forwarding is not None:
            self.dis_forwarding = dis_forwarding
        if obs_forwarding is not None:
            self.obs_forwarding = obs_forwarding
        if roma_forwarding is not None:
            self.roma_forwarding = roma_forwarding
        if iota_forwarding is not None:
            self.iota_forwarding = iota_forwarding
        if kafka_forwarding is not None:
            self.kafka_forwarding = kafka_forwarding

    @property
    def type(self):
        """Gets the type of this RuleAction.

        规则动作的类型，取值范围： - DEVICE_CMD：下发设备命令消息类型。 - SMN_FORWARDING：发送SMN消息类型。 - DEVICE_ALARM：上报设备告警消息类型。当选择该类型时，condition中必须有DEVICE_DATA条件类型。该类型动作只能唯一。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - ROMA_FORWARDING：转发ROMA服务消息类型。 - IoTA_FORWARDING：转发IoTA服务消息类型。 - KAFKA_FORWARDING：转发kafka消息类型。 

        :return: The type of this RuleAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleAction.

        规则动作的类型，取值范围： - DEVICE_CMD：下发设备命令消息类型。 - SMN_FORWARDING：发送SMN消息类型。 - DEVICE_ALARM：上报设备告警消息类型。当选择该类型时，condition中必须有DEVICE_DATA条件类型。该类型动作只能唯一。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - ROMA_FORWARDING：转发ROMA服务消息类型。 - IoTA_FORWARDING：转发IoTA服务消息类型。 - KAFKA_FORWARDING：转发kafka消息类型。 

        :param type: The type of this RuleAction.
        :type: str
        """
        self._type = type

    @property
    def addition(self):
        """Gets the addition of this RuleAction.

        附加信息，在默认规则执行结果中附加额外内容，仅设备属性和消息类型数据转发规则支持，取值范围：PRODUCT_ID

        :return: The addition of this RuleAction.
        :rtype: list[str]
        """
        return self._addition

    @addition.setter
    def addition(self, addition):
        """Sets the addition of this RuleAction.

        附加信息，在默认规则执行结果中附加额外内容，仅设备属性和消息类型数据转发规则支持，取值范围：PRODUCT_ID

        :param addition: The addition of this RuleAction.
        :type: list[str]
        """
        self._addition = addition

    @property
    def smn_forwarding(self):
        """Gets the smn_forwarding of this RuleAction.


        :return: The smn_forwarding of this RuleAction.
        :rtype: ActionSmnForwarding
        """
        return self._smn_forwarding

    @smn_forwarding.setter
    def smn_forwarding(self, smn_forwarding):
        """Sets the smn_forwarding of this RuleAction.


        :param smn_forwarding: The smn_forwarding of this RuleAction.
        :type: ActionSmnForwarding
        """
        self._smn_forwarding = smn_forwarding

    @property
    def device_alarm(self):
        """Gets the device_alarm of this RuleAction.


        :return: The device_alarm of this RuleAction.
        :rtype: ActionDeviceAlarm
        """
        return self._device_alarm

    @device_alarm.setter
    def device_alarm(self, device_alarm):
        """Sets the device_alarm of this RuleAction.


        :param device_alarm: The device_alarm of this RuleAction.
        :type: ActionDeviceAlarm
        """
        self._device_alarm = device_alarm

    @property
    def device_command(self):
        """Gets the device_command of this RuleAction.


        :return: The device_command of this RuleAction.
        :rtype: ActionDeviceCommand
        """
        return self._device_command

    @device_command.setter
    def device_command(self, device_command):
        """Sets the device_command of this RuleAction.


        :param device_command: The device_command of this RuleAction.
        :type: ActionDeviceCommand
        """
        self._device_command = device_command

    @property
    def dis_forwarding(self):
        """Gets the dis_forwarding of this RuleAction.


        :return: The dis_forwarding of this RuleAction.
        :rtype: ActionDisForwarding
        """
        return self._dis_forwarding

    @dis_forwarding.setter
    def dis_forwarding(self, dis_forwarding):
        """Sets the dis_forwarding of this RuleAction.


        :param dis_forwarding: The dis_forwarding of this RuleAction.
        :type: ActionDisForwarding
        """
        self._dis_forwarding = dis_forwarding

    @property
    def obs_forwarding(self):
        """Gets the obs_forwarding of this RuleAction.


        :return: The obs_forwarding of this RuleAction.
        :rtype: ActionObsForwarding
        """
        return self._obs_forwarding

    @obs_forwarding.setter
    def obs_forwarding(self, obs_forwarding):
        """Sets the obs_forwarding of this RuleAction.


        :param obs_forwarding: The obs_forwarding of this RuleAction.
        :type: ActionObsForwarding
        """
        self._obs_forwarding = obs_forwarding

    @property
    def roma_forwarding(self):
        """Gets the roma_forwarding of this RuleAction.


        :return: The roma_forwarding of this RuleAction.
        :rtype: ActionRomaForwarding
        """
        return self._roma_forwarding

    @roma_forwarding.setter
    def roma_forwarding(self, roma_forwarding):
        """Sets the roma_forwarding of this RuleAction.


        :param roma_forwarding: The roma_forwarding of this RuleAction.
        :type: ActionRomaForwarding
        """
        self._roma_forwarding = roma_forwarding

    @property
    def iota_forwarding(self):
        """Gets the iota_forwarding of this RuleAction.


        :return: The iota_forwarding of this RuleAction.
        :rtype: ActionIoTAForwarding
        """
        return self._iota_forwarding

    @iota_forwarding.setter
    def iota_forwarding(self, iota_forwarding):
        """Sets the iota_forwarding of this RuleAction.


        :param iota_forwarding: The iota_forwarding of this RuleAction.
        :type: ActionIoTAForwarding
        """
        self._iota_forwarding = iota_forwarding

    @property
    def kafka_forwarding(self):
        """Gets the kafka_forwarding of this RuleAction.


        :return: The kafka_forwarding of this RuleAction.
        :rtype: ActionKafkaForwarding
        """
        return self._kafka_forwarding

    @kafka_forwarding.setter
    def kafka_forwarding(self, kafka_forwarding):
        """Sets the kafka_forwarding of this RuleAction.


        :param kafka_forwarding: The kafka_forwarding of this RuleAction.
        :type: ActionKafkaForwarding
        """
        self._kafka_forwarding = kafka_forwarding

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
