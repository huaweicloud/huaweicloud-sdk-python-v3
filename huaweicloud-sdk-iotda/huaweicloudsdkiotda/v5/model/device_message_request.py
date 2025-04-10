# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'message': 'object',
        'properties': 'PropertiesDTO',
        'encoding': 'str',
        'payload_format': 'str',
        'topic': 'str',
        'topic_full_name': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'message_id': 'message_id',
        'name': 'name',
        'message': 'message',
        'properties': 'properties',
        'encoding': 'encoding',
        'payload_format': 'payload_format',
        'topic': 'topic',
        'topic_full_name': 'topic_full_name',
        'ttl': 'ttl'
    }

    def __init__(self, message_id=None, name=None, message=None, properties=None, encoding=None, payload_format=None, topic=None, topic_full_name=None, ttl=None):
        r"""DeviceMessageRequest

        The model defined in huaweicloud sdk

        :param message_id: **参数说明**：消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户填写的id在设备下不唯一， 则接口返回错误。 **取值范围**：长度不超过100，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type message_id: str
        :param name: **参数说明**：消息名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type name: str
        :param message: **参数说明**：消息内容，支持string和json格式。
        :type message: object
        :param properties: 
        :type properties: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        :param encoding: **参数说明**：消息内容编码格式。默认值none。 **取值范围**： - none  - base64
        :type encoding: str
        :param payload_format: **参数说明**：有效负载格式，在消息内容编码格式为none时有效。默认值standard（平台封装的标准格式）。 **取值范围**： - standard  - raw：直接将消息内容作为有效负载下发。
        :type payload_format: str
        :param topic: **参数说明**：消息下行到设备的自定义topic后缀, 可选， 仅适用于MQTT协议接入的设备。 用户只能填写在租户产品界面配置的topic, 否则会校验不通过。 平台给消息topic添加的前缀为$oc/devices/{device_id}/user/， 用户可以在前缀的基础上增加自定义部分， 如增加messageDown，则平台拼接前缀后完整的topic为 $oc/devices/{device_id}/user/messageDown，其中device_id以实际设备的网关id替代。 如果用户指定该topic，消息会通过该topic下行到设备，如果用户不指定， 则消息通过系统默认的topic下行到设备,系统默认的topic格式为： $oc/devices/{device_id}/sys/messages/down。此字段与topic_full_name字段只可填写一个。
        :type topic: str
        :param topic_full_name: **参数说明**：消息下行到设备的完整topic名称, 可选。用户需要下发用户自定义的topic给设备时，可以使用该参数指定完整的topic名称，物联网平台不校验该topic是否在平台定义，直接透传给设备。设备需要提前订阅该topic。此字段与topic字段只可填写一个。
        :type topic_full_name: str
        :param ttl: **参数说明**：下发消息在平台缓存的老化时间，时间单位是分钟，默认值1440；ttl参数数值必须是5的倍数，即以5分钟为粒度；指定为0时表示不缓存消息，最大缓存时间1440分钟，即缓存一天
        :type ttl: int
        """
        
        

        self._message_id = None
        self._name = None
        self._message = None
        self._properties = None
        self._encoding = None
        self._payload_format = None
        self._topic = None
        self._topic_full_name = None
        self._ttl = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if name is not None:
            self.name = name
        self.message = message
        if properties is not None:
            self.properties = properties
        if encoding is not None:
            self.encoding = encoding
        if payload_format is not None:
            self.payload_format = payload_format
        if topic is not None:
            self.topic = topic
        if topic_full_name is not None:
            self.topic_full_name = topic_full_name
        if ttl is not None:
            self.ttl = ttl

    @property
    def message_id(self):
        r"""Gets the message_id of this DeviceMessageRequest.

        **参数说明**：消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户填写的id在设备下不唯一， 则接口返回错误。 **取值范围**：长度不超过100，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The message_id of this DeviceMessageRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        r"""Sets the message_id of this DeviceMessageRequest.

        **参数说明**：消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户填写的id在设备下不唯一， 则接口返回错误。 **取值范围**：长度不超过100，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param message_id: The message_id of this DeviceMessageRequest.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def name(self):
        r"""Gets the name of this DeviceMessageRequest.

        **参数说明**：消息名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The name of this DeviceMessageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeviceMessageRequest.

        **参数说明**：消息名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param name: The name of this DeviceMessageRequest.
        :type name: str
        """
        self._name = name

    @property
    def message(self):
        r"""Gets the message of this DeviceMessageRequest.

        **参数说明**：消息内容，支持string和json格式。

        :return: The message of this DeviceMessageRequest.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DeviceMessageRequest.

        **参数说明**：消息内容，支持string和json格式。

        :param message: The message of this DeviceMessageRequest.
        :type message: object
        """
        self._message = message

    @property
    def properties(self):
        r"""Gets the properties of this DeviceMessageRequest.

        :return: The properties of this DeviceMessageRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this DeviceMessageRequest.

        :param properties: The properties of this DeviceMessageRequest.
        :type properties: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        """
        self._properties = properties

    @property
    def encoding(self):
        r"""Gets the encoding of this DeviceMessageRequest.

        **参数说明**：消息内容编码格式。默认值none。 **取值范围**： - none  - base64

        :return: The encoding of this DeviceMessageRequest.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this DeviceMessageRequest.

        **参数说明**：消息内容编码格式。默认值none。 **取值范围**： - none  - base64

        :param encoding: The encoding of this DeviceMessageRequest.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def payload_format(self):
        r"""Gets the payload_format of this DeviceMessageRequest.

        **参数说明**：有效负载格式，在消息内容编码格式为none时有效。默认值standard（平台封装的标准格式）。 **取值范围**： - standard  - raw：直接将消息内容作为有效负载下发。

        :return: The payload_format of this DeviceMessageRequest.
        :rtype: str
        """
        return self._payload_format

    @payload_format.setter
    def payload_format(self, payload_format):
        r"""Sets the payload_format of this DeviceMessageRequest.

        **参数说明**：有效负载格式，在消息内容编码格式为none时有效。默认值standard（平台封装的标准格式）。 **取值范围**： - standard  - raw：直接将消息内容作为有效负载下发。

        :param payload_format: The payload_format of this DeviceMessageRequest.
        :type payload_format: str
        """
        self._payload_format = payload_format

    @property
    def topic(self):
        r"""Gets the topic of this DeviceMessageRequest.

        **参数说明**：消息下行到设备的自定义topic后缀, 可选， 仅适用于MQTT协议接入的设备。 用户只能填写在租户产品界面配置的topic, 否则会校验不通过。 平台给消息topic添加的前缀为$oc/devices/{device_id}/user/， 用户可以在前缀的基础上增加自定义部分， 如增加messageDown，则平台拼接前缀后完整的topic为 $oc/devices/{device_id}/user/messageDown，其中device_id以实际设备的网关id替代。 如果用户指定该topic，消息会通过该topic下行到设备，如果用户不指定， 则消息通过系统默认的topic下行到设备,系统默认的topic格式为： $oc/devices/{device_id}/sys/messages/down。此字段与topic_full_name字段只可填写一个。

        :return: The topic of this DeviceMessageRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this DeviceMessageRequest.

        **参数说明**：消息下行到设备的自定义topic后缀, 可选， 仅适用于MQTT协议接入的设备。 用户只能填写在租户产品界面配置的topic, 否则会校验不通过。 平台给消息topic添加的前缀为$oc/devices/{device_id}/user/， 用户可以在前缀的基础上增加自定义部分， 如增加messageDown，则平台拼接前缀后完整的topic为 $oc/devices/{device_id}/user/messageDown，其中device_id以实际设备的网关id替代。 如果用户指定该topic，消息会通过该topic下行到设备，如果用户不指定， 则消息通过系统默认的topic下行到设备,系统默认的topic格式为： $oc/devices/{device_id}/sys/messages/down。此字段与topic_full_name字段只可填写一个。

        :param topic: The topic of this DeviceMessageRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_full_name(self):
        r"""Gets the topic_full_name of this DeviceMessageRequest.

        **参数说明**：消息下行到设备的完整topic名称, 可选。用户需要下发用户自定义的topic给设备时，可以使用该参数指定完整的topic名称，物联网平台不校验该topic是否在平台定义，直接透传给设备。设备需要提前订阅该topic。此字段与topic字段只可填写一个。

        :return: The topic_full_name of this DeviceMessageRequest.
        :rtype: str
        """
        return self._topic_full_name

    @topic_full_name.setter
    def topic_full_name(self, topic_full_name):
        r"""Sets the topic_full_name of this DeviceMessageRequest.

        **参数说明**：消息下行到设备的完整topic名称, 可选。用户需要下发用户自定义的topic给设备时，可以使用该参数指定完整的topic名称，物联网平台不校验该topic是否在平台定义，直接透传给设备。设备需要提前订阅该topic。此字段与topic字段只可填写一个。

        :param topic_full_name: The topic_full_name of this DeviceMessageRequest.
        :type topic_full_name: str
        """
        self._topic_full_name = topic_full_name

    @property
    def ttl(self):
        r"""Gets the ttl of this DeviceMessageRequest.

        **参数说明**：下发消息在平台缓存的老化时间，时间单位是分钟，默认值1440；ttl参数数值必须是5的倍数，即以5分钟为粒度；指定为0时表示不缓存消息，最大缓存时间1440分钟，即缓存一天

        :return: The ttl of this DeviceMessageRequest.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this DeviceMessageRequest.

        **参数说明**：下发消息在平台缓存的老化时间，时间单位是分钟，默认值1440；ttl参数数值必须是5的倍数，即以5分钟为粒度；指定为0时表示不缓存消息，最大缓存时间1440分钟，即缓存一天

        :param ttl: The ttl of this DeviceMessageRequest.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, DeviceMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
