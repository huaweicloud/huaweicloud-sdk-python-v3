# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIProcessNetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listen_ip': 'str',
        'listen_protocol': 'str',
        'listen_port': 'int',
        'listen_status': 'str'
    }

    attribute_map = {
        'listen_ip': 'listen_ip',
        'listen_protocol': 'listen_protocol',
        'listen_port': 'listen_port',
        'listen_status': 'listen_status'
    }

    def __init__(self, listen_ip=None, listen_protocol=None, listen_port=None, listen_status=None):
        r"""AIProcessNetInfo

        The model defined in huaweicloud sdk

        :param listen_ip: **参数解释**： 应用进程监听IP **取值范围**： 取值0-2147483647 
        :type listen_ip: str
        :param listen_protocol: **参数解释**： 应用进程监听对应的网络协议 **取值范围**： - tcp：tcp协议 - udp：udp协议 
        :type listen_protocol: str
        :param listen_port: **参数解释**： 应用进程监听端口 **取值范围**： 取值0-2147483647 
        :type listen_port: int
        :param listen_status: **参数解释**： 应用进程监听状态 **取值范围**： - established：已建立连接 - closed：连接已关闭 - listening：监听中 - other：连接中间态 
        :type listen_status: str
        """
        
        

        self._listen_ip = None
        self._listen_protocol = None
        self._listen_port = None
        self._listen_status = None
        self.discriminator = None

        if listen_ip is not None:
            self.listen_ip = listen_ip
        if listen_protocol is not None:
            self.listen_protocol = listen_protocol
        if listen_port is not None:
            self.listen_port = listen_port
        if listen_status is not None:
            self.listen_status = listen_status

    @property
    def listen_ip(self):
        r"""Gets the listen_ip of this AIProcessNetInfo.

        **参数解释**： 应用进程监听IP **取值范围**： 取值0-2147483647 

        :return: The listen_ip of this AIProcessNetInfo.
        :rtype: str
        """
        return self._listen_ip

    @listen_ip.setter
    def listen_ip(self, listen_ip):
        r"""Sets the listen_ip of this AIProcessNetInfo.

        **参数解释**： 应用进程监听IP **取值范围**： 取值0-2147483647 

        :param listen_ip: The listen_ip of this AIProcessNetInfo.
        :type listen_ip: str
        """
        self._listen_ip = listen_ip

    @property
    def listen_protocol(self):
        r"""Gets the listen_protocol of this AIProcessNetInfo.

        **参数解释**： 应用进程监听对应的网络协议 **取值范围**： - tcp：tcp协议 - udp：udp协议 

        :return: The listen_protocol of this AIProcessNetInfo.
        :rtype: str
        """
        return self._listen_protocol

    @listen_protocol.setter
    def listen_protocol(self, listen_protocol):
        r"""Sets the listen_protocol of this AIProcessNetInfo.

        **参数解释**： 应用进程监听对应的网络协议 **取值范围**： - tcp：tcp协议 - udp：udp协议 

        :param listen_protocol: The listen_protocol of this AIProcessNetInfo.
        :type listen_protocol: str
        """
        self._listen_protocol = listen_protocol

    @property
    def listen_port(self):
        r"""Gets the listen_port of this AIProcessNetInfo.

        **参数解释**： 应用进程监听端口 **取值范围**： 取值0-2147483647 

        :return: The listen_port of this AIProcessNetInfo.
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        r"""Sets the listen_port of this AIProcessNetInfo.

        **参数解释**： 应用进程监听端口 **取值范围**： 取值0-2147483647 

        :param listen_port: The listen_port of this AIProcessNetInfo.
        :type listen_port: int
        """
        self._listen_port = listen_port

    @property
    def listen_status(self):
        r"""Gets the listen_status of this AIProcessNetInfo.

        **参数解释**： 应用进程监听状态 **取值范围**： - established：已建立连接 - closed：连接已关闭 - listening：监听中 - other：连接中间态 

        :return: The listen_status of this AIProcessNetInfo.
        :rtype: str
        """
        return self._listen_status

    @listen_status.setter
    def listen_status(self, listen_status):
        r"""Sets the listen_status of this AIProcessNetInfo.

        **参数解释**： 应用进程监听状态 **取值范围**： - established：已建立连接 - closed：连接已关闭 - listening：监听中 - other：连接中间态 

        :param listen_status: The listen_status of this AIProcessNetInfo.
        :type listen_status: str
        """
        self._listen_status = listen_status

    def to_dict(self):
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
        if not isinstance(other, AIProcessNetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
