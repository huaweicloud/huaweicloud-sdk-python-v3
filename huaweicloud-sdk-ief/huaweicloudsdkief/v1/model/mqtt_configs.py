# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MqttConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enable_mqtt': 'bool',
        'mqtts': 'list[Mqtt]'
    }

    attribute_map = {
        'enable_mqtt': 'enable_mqtt',
        'mqtts': 'mqtts'
    }

    def __init__(self, enable_mqtt=None, mqtts=None):
        """MqttConfigs

        The model defined in huaweicloud sdk

        :param enable_mqtt: 是否启用MQTT
        :type enable_mqtt: bool
        :param mqtts: MQTT配置 当enable_mqtt取值为false时，mqtts需要为空数组
        :type mqtts: list[:class:`huaweicloudsdkief.v1.Mqtt`]
        """
        
        

        self._enable_mqtt = None
        self._mqtts = None
        self.discriminator = None

        self.enable_mqtt = enable_mqtt
        self.mqtts = mqtts

    @property
    def enable_mqtt(self):
        """Gets the enable_mqtt of this MqttConfigs.

        是否启用MQTT

        :return: The enable_mqtt of this MqttConfigs.
        :rtype: bool
        """
        return self._enable_mqtt

    @enable_mqtt.setter
    def enable_mqtt(self, enable_mqtt):
        """Sets the enable_mqtt of this MqttConfigs.

        是否启用MQTT

        :param enable_mqtt: The enable_mqtt of this MqttConfigs.
        :type enable_mqtt: bool
        """
        self._enable_mqtt = enable_mqtt

    @property
    def mqtts(self):
        """Gets the mqtts of this MqttConfigs.

        MQTT配置 当enable_mqtt取值为false时，mqtts需要为空数组

        :return: The mqtts of this MqttConfigs.
        :rtype: list[:class:`huaweicloudsdkief.v1.Mqtt`]
        """
        return self._mqtts

    @mqtts.setter
    def mqtts(self, mqtts):
        """Sets the mqtts of this MqttConfigs.

        MQTT配置 当enable_mqtt取值为false时，mqtts需要为空数组

        :param mqtts: The mqtts of this MqttConfigs.
        :type mqtts: list[:class:`huaweicloudsdkief.v1.Mqtt`]
        """
        self._mqtts = mqtts

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
        if not isinstance(other, MqttConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
