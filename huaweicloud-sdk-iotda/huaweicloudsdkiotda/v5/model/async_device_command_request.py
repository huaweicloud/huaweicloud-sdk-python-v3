# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncDeviceCommandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'command_name': 'str',
        'paras': 'object',
        'expire_time': 'int',
        'send_strategy': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'command_name': 'command_name',
        'paras': 'paras',
        'expire_time': 'expire_time',
        'send_strategy': 'send_strategy'
    }

    def __init__(self, service_id=None, command_name=None, paras=None, expire_time=None, send_strategy=None):
        """AsyncDeviceCommandRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数说明**：设备命令所属的设备服务ID，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过64的字符串。
        :type service_id: str
        :param command_name: **参数说明**：设备命令名称，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过128的字符串。
        :type command_name: str
        :param paras: **参数说明**：设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\&quot;value\&quot;:\&quot;1\&quot;}，具体格式需要应用和设备约定， 最大32K。
        :type paras: object
        :param expire_time: **参数说明**：物联网平台缓存命令的时长， 单位秒, 平台最多缓存20条消息（即最多缓存20条PENDING状态的命令） 该参数在send_strategy字段为delay时有效，默认缓存24小时，最大缓存2天。
        :type expire_time: int
        :param send_strategy: **参数说明**：下发策略，默认缓存下发。 **取值范围**： - immediately:表示立即下发，此时expire_time无效。 - delay:表示缓存下发，等数据上报或者设备上线之后下发。expire_time为0或空时，命令会默认缓存24小时。
        :type send_strategy: str
        """
        
        

        self._service_id = None
        self._command_name = None
        self._paras = None
        self._expire_time = None
        self._send_strategy = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if command_name is not None:
            self.command_name = command_name
        self.paras = paras
        if expire_time is not None:
            self.expire_time = expire_time
        self.send_strategy = send_strategy

    @property
    def service_id(self):
        """Gets the service_id of this AsyncDeviceCommandRequest.

        **参数说明**：设备命令所属的设备服务ID，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过64的字符串。

        :return: The service_id of this AsyncDeviceCommandRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this AsyncDeviceCommandRequest.

        **参数说明**：设备命令所属的设备服务ID，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过64的字符串。

        :param service_id: The service_id of this AsyncDeviceCommandRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def command_name(self):
        """Gets the command_name of this AsyncDeviceCommandRequest.

        **参数说明**：设备命令名称，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过128的字符串。

        :return: The command_name of this AsyncDeviceCommandRequest.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this AsyncDeviceCommandRequest.

        **参数说明**：设备命令名称，在设备关联的产品模型中定义。如设备需要编解码插件来解析命令，此参数为必填项。 **取值范围**：长度不超过128的字符串。

        :param command_name: The command_name of this AsyncDeviceCommandRequest.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def paras(self):
        """Gets the paras of this AsyncDeviceCommandRequest.

        **参数说明**：设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\"value\":\"1\"}，具体格式需要应用和设备约定， 最大32K。

        :return: The paras of this AsyncDeviceCommandRequest.
        :rtype: object
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this AsyncDeviceCommandRequest.

        **参数说明**：设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\"value\":\"1\"}，具体格式需要应用和设备约定， 最大32K。

        :param paras: The paras of this AsyncDeviceCommandRequest.
        :type paras: object
        """
        self._paras = paras

    @property
    def expire_time(self):
        """Gets the expire_time of this AsyncDeviceCommandRequest.

        **参数说明**：物联网平台缓存命令的时长， 单位秒, 平台最多缓存20条消息（即最多缓存20条PENDING状态的命令） 该参数在send_strategy字段为delay时有效，默认缓存24小时，最大缓存2天。

        :return: The expire_time of this AsyncDeviceCommandRequest.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this AsyncDeviceCommandRequest.

        **参数说明**：物联网平台缓存命令的时长， 单位秒, 平台最多缓存20条消息（即最多缓存20条PENDING状态的命令） 该参数在send_strategy字段为delay时有效，默认缓存24小时，最大缓存2天。

        :param expire_time: The expire_time of this AsyncDeviceCommandRequest.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def send_strategy(self):
        """Gets the send_strategy of this AsyncDeviceCommandRequest.

        **参数说明**：下发策略，默认缓存下发。 **取值范围**： - immediately:表示立即下发，此时expire_time无效。 - delay:表示缓存下发，等数据上报或者设备上线之后下发。expire_time为0或空时，命令会默认缓存24小时。

        :return: The send_strategy of this AsyncDeviceCommandRequest.
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        """Sets the send_strategy of this AsyncDeviceCommandRequest.

        **参数说明**：下发策略，默认缓存下发。 **取值范围**： - immediately:表示立即下发，此时expire_time无效。 - delay:表示缓存下发，等数据上报或者设备上线之后下发。expire_time为0或空时，命令会默认缓存24小时。

        :param send_strategy: The send_strategy of this AsyncDeviceCommandRequest.
        :type send_strategy: str
        """
        self._send_strategy = send_strategy

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
        if not isinstance(other, AsyncDeviceCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
