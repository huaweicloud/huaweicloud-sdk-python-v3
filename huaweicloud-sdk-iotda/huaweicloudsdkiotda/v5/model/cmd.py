# coding: utf-8

import pprint
import re

import six





class Cmd:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'command_name': 'str',
        'command_body': 'object',
        'service_id': 'str',
        'buffer_timeout': 'int',
        'response_timeout': 'int',
        'mode': 'str'
    }

    attribute_map = {
        'command_name': 'command_name',
        'command_body': 'command_body',
        'service_id': 'service_id',
        'buffer_timeout': 'buffer_timeout',
        'response_timeout': 'response_timeout',
        'mode': 'mode'
    }

    def __init__(self, command_name=None, command_body=None, service_id=None, buffer_timeout=172800, response_timeout=1800, mode=None):
        """Cmd - a model defined in huaweicloud sdk"""
        
        

        self._command_name = None
        self._command_body = None
        self._service_id = None
        self._buffer_timeout = None
        self._response_timeout = None
        self._mode = None
        self.discriminator = None

        self.command_name = command_name
        self.command_body = command_body
        self.service_id = service_id
        if buffer_timeout is not None:
            self.buffer_timeout = buffer_timeout
        if response_timeout is not None:
            self.response_timeout = response_timeout
        if mode is not None:
            self.mode = mode

    @property
    def command_name(self):
        """Gets the command_name of this Cmd.

        设备命令名称，在设备关联的产品模型中定义。

        :return: The command_name of this Cmd.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this Cmd.

        设备命令名称，在设备关联的产品模型中定义。

        :param command_name: The command_name of this Cmd.
        :type: str
        """
        self._command_name = command_name

    @property
    def command_body(self):
        """Gets the command_body of this Cmd.

        设备命令参数，Json格式。 使用LWM2M协议设备命令示例：{\"value\":\"1\"}，里面是一个个健值对，每个健都是产品模型中命令的参数名（paraName）。 使用MQTT协议设备命令示例：{\"header\": {\"mode\": \"ACK\",\"from\": \"/users/testUser\",\"method\": \"SET_TEMPERATURE_READ_PERIOD\",\"to\":\"/devices/{device_id}/services/{service_id}\"},\"body\": {\"value\" : \"1\"}}。 - mode：必选，设备收到命令后是否需要回复确认消息，默认为ACK模式。ACK表示需要回复确认消息，NOACK表示不需要回复确认消息，其它值无效。 - from：可选，命令发送方的地址。App发起请求时格式为/users/{userId} ，应用服务器发起请求时格式为/{serviceName}，物联网平台发起请求时格式为/cloud/{serviceName}。 - to：可选，命令接收方的地址，格式为/devices/{device_id}/services/{service_id}。 - method：可选，产品模型中定义的命令名称。 - body：可选，命令的消息体，里面是一个个键值对，每个键都是产品模型中命令的参数名（paraName）。具体格式需要应用和设备约定。 

        :return: The command_body of this Cmd.
        :rtype: object
        """
        return self._command_body

    @command_body.setter
    def command_body(self, command_body):
        """Sets the command_body of this Cmd.

        设备命令参数，Json格式。 使用LWM2M协议设备命令示例：{\"value\":\"1\"}，里面是一个个健值对，每个健都是产品模型中命令的参数名（paraName）。 使用MQTT协议设备命令示例：{\"header\": {\"mode\": \"ACK\",\"from\": \"/users/testUser\",\"method\": \"SET_TEMPERATURE_READ_PERIOD\",\"to\":\"/devices/{device_id}/services/{service_id}\"},\"body\": {\"value\" : \"1\"}}。 - mode：必选，设备收到命令后是否需要回复确认消息，默认为ACK模式。ACK表示需要回复确认消息，NOACK表示不需要回复确认消息，其它值无效。 - from：可选，命令发送方的地址。App发起请求时格式为/users/{userId} ，应用服务器发起请求时格式为/{serviceName}，物联网平台发起请求时格式为/cloud/{serviceName}。 - to：可选，命令接收方的地址，格式为/devices/{device_id}/services/{service_id}。 - method：可选，产品模型中定义的命令名称。 - body：可选，命令的消息体，里面是一个个键值对，每个键都是产品模型中命令的参数名（paraName）。具体格式需要应用和设备约定。 

        :param command_body: The command_body of this Cmd.
        :type: object
        """
        self._command_body = command_body

    @property
    def service_id(self):
        """Gets the service_id of this Cmd.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this Cmd.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Cmd.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this Cmd.
        :type: str
        """
        self._service_id = service_id

    @property
    def buffer_timeout(self):
        """Gets the buffer_timeout of this Cmd.

        设备命令的缓存时间，单位为秒，表示物联网平台在把命令下发给设备前缓存命令的有效时间，超过这个时间后命令将不再下发，默认值为172800s（48小时）。 如果buffer_timeout设置为0，则无论物联网平台上设置的命令下发模式是什么，该命令都会立即下发给设备。 

        :return: The buffer_timeout of this Cmd.
        :rtype: int
        """
        return self._buffer_timeout

    @buffer_timeout.setter
    def buffer_timeout(self, buffer_timeout):
        """Sets the buffer_timeout of this Cmd.

        设备命令的缓存时间，单位为秒，表示物联网平台在把命令下发给设备前缓存命令的有效时间，超过这个时间后命令将不再下发，默认值为172800s（48小时）。 如果buffer_timeout设置为0，则无论物联网平台上设置的命令下发模式是什么，该命令都会立即下发给设备。 

        :param buffer_timeout: The buffer_timeout of this Cmd.
        :type: int
        """
        self._buffer_timeout = buffer_timeout

    @property
    def response_timeout(self):
        """Gets the response_timeout of this Cmd.

        命令响应的有效时间，单位为秒，表示设备接收到命令后，在response_timeout时间内响应有效，超过这个时间未收到命令的响应，则认为命令响应超时，默认值为1800s。

        :return: The response_timeout of this Cmd.
        :rtype: int
        """
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, response_timeout):
        """Sets the response_timeout of this Cmd.

        命令响应的有效时间，单位为秒，表示设备接收到命令后，在response_timeout时间内响应有效，超过这个时间未收到命令的响应，则认为命令响应超时，默认值为1800s。

        :param response_timeout: The response_timeout of this Cmd.
        :type: int
        """
        self._response_timeout = response_timeout

    @property
    def mode(self):
        """Gets the mode of this Cmd.

        设备命令的下发模式，仅当buffer_timeout的值大于0时有效。 - ACTIVE：主动模式，物联网平台主动将命令下发给设备。 - PASSIVE：被动模式，物联网平台创建设备命令后，会直接缓存命令。等到设备再次上线或者上报上一条命令的执行结果后才下发命令。 

        :return: The mode of this Cmd.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Cmd.

        设备命令的下发模式，仅当buffer_timeout的值大于0时有效。 - ACTIVE：主动模式，物联网平台主动将命令下发给设备。 - PASSIVE：被动模式，物联网平台创建设备命令后，会直接缓存命令。等到设备再次上线或者上报上一条命令的执行结果后才下发命令。 

        :param mode: The mode of this Cmd.
        :type: str
        """
        self._mode = mode

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
        if not isinstance(other, Cmd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
