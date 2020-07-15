# coding: utf-8

import pprint
import re

import six





class DeviceMessageRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'name': 'str',
        'message': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'name': 'name',
        'message': 'message',
        'topic': 'topic'
    }

    def __init__(self, message_id=None, name=None, message=None, topic=None):
        """DeviceMessageRequest - a model defined in huaweicloud sdk"""
        
        

        self._message_id = None
        self._name = None
        self._message = None
        self._topic = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if name is not None:
            self.name = name
        self.message = message
        if topic is not None:
            self.topic = topic

    @property
    def message_id(self):
        """Gets the message_id of this DeviceMessageRequest.

        消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户填写的id在设备下不唯一， 则接口返回错误。

        :return: The message_id of this DeviceMessageRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this DeviceMessageRequest.

        消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户填写的id在设备下不唯一， 则接口返回错误。

        :param message_id: The message_id of this DeviceMessageRequest.
        :type: str
        """
        self._message_id = message_id

    @property
    def name(self):
        """Gets the name of this DeviceMessageRequest.

        消息名称

        :return: The name of this DeviceMessageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceMessageRequest.

        消息名称

        :param name: The name of this DeviceMessageRequest.
        :type: str
        """
        self._name = name

    @property
    def message(self):
        """Gets the message of this DeviceMessageRequest.

        设备执行的消息，字符串，具体格式需要应用和设备约定。 

        :return: The message of this DeviceMessageRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeviceMessageRequest.

        设备执行的消息，字符串，具体格式需要应用和设备约定。 

        :param message: The message of this DeviceMessageRequest.
        :type: str
        """
        self._message = message

    @property
    def topic(self):
        """Gets the topic of this DeviceMessageRequest.

        消息下行到设备的topic, 可选， 仅适用于MQTT协议接入的设备。 用户只能填写在租户产品界面配置的topic, 否则会校验不通过。 平台给消息topic添加的前缀为$oc/devices/{device_id}/user/， 用户可以在前缀的基础上增加自定义部分， 如增加messageDown，则平台拼接前缀后完整的topic为 $oc/devices/{device_id}/user/messageDown，其中device_id以实际设备的网关id替代。 如果用户指定该topic，消息会通过该topic下行到设备，如果用户不指定， 则消息通过系统默认的topic下行到设备,系统默认的topic格式为： $oc/devices/{device_id}/sys/messages/down。 

        :return: The topic of this DeviceMessageRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this DeviceMessageRequest.

        消息下行到设备的topic, 可选， 仅适用于MQTT协议接入的设备。 用户只能填写在租户产品界面配置的topic, 否则会校验不通过。 平台给消息topic添加的前缀为$oc/devices/{device_id}/user/， 用户可以在前缀的基础上增加自定义部分， 如增加messageDown，则平台拼接前缀后完整的topic为 $oc/devices/{device_id}/user/messageDown，其中device_id以实际设备的网关id替代。 如果用户指定该topic，消息会通过该topic下行到设备，如果用户不指定， 则消息通过系统默认的topic下行到设备,系统默认的topic格式为： $oc/devices/{device_id}/sys/messages/down。 

        :param topic: The topic of this DeviceMessageRequest.
        :type: str
        """
        self._topic = topic

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
        if not isinstance(other, DeviceMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
