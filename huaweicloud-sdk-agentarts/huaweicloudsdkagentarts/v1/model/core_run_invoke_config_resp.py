# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunInvokeConfigResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'protocol': 'str',
        'file_transfer_config': 'CoreRunFileTransferConfig',
        'url_match_type': 'str'
    }

    attribute_map = {
        'port': 'port',
        'protocol': 'protocol',
        'file_transfer_config': 'file_transfer_config',
        'url_match_type': 'url_match_type'
    }

    def __init__(self, port=None, protocol=None, file_transfer_config=None, url_match_type=None):
        r"""CoreRunInvokeConfigResp

        The model defined in huaweicloud sdk

        :param port: **参数解释**: 智能体运行时监听的端口号，用于接收外部请求，默认值8080。 **约束限制**: 不涉及。 **取值范围**: 1 - 65535 **默认值**: 8080 
        :type port: int
        :param protocol: **参数解释**: 智能体运行时支持的协议类型，默认值HTTP。 - HTTP: HTTP协议 - MCP: MCP协议 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 4 个字符。允许的值为： - HTTP - MCP **默认值**: HTTP 
        :type protocol: str
        :param file_transfer_config: 
        :type file_transfer_config: :class:`huaweicloudsdkagentarts.v1.CoreRunFileTransferConfig`
        :param url_match_type: **参数解释**: 智能体运行时调用URL的匹配模式。 **取值范围**: - ACCURATE_MATCH - PREFIX_MATCH 
        :type url_match_type: str
        """
        
        

        self._port = None
        self._protocol = None
        self._file_transfer_config = None
        self._url_match_type = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if file_transfer_config is not None:
            self.file_transfer_config = file_transfer_config
        if url_match_type is not None:
            self.url_match_type = url_match_type

    @property
    def port(self):
        r"""Gets the port of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时监听的端口号，用于接收外部请求，默认值8080。 **约束限制**: 不涉及。 **取值范围**: 1 - 65535 **默认值**: 8080 

        :return: The port of this CoreRunInvokeConfigResp.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时监听的端口号，用于接收外部请求，默认值8080。 **约束限制**: 不涉及。 **取值范围**: 1 - 65535 **默认值**: 8080 

        :param port: The port of this CoreRunInvokeConfigResp.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时支持的协议类型，默认值HTTP。 - HTTP: HTTP协议 - MCP: MCP协议 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 4 个字符。允许的值为： - HTTP - MCP **默认值**: HTTP 

        :return: The protocol of this CoreRunInvokeConfigResp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时支持的协议类型，默认值HTTP。 - HTTP: HTTP协议 - MCP: MCP协议 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 4 个字符。允许的值为： - HTTP - MCP **默认值**: HTTP 

        :param protocol: The protocol of this CoreRunInvokeConfigResp.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def file_transfer_config(self):
        r"""Gets the file_transfer_config of this CoreRunInvokeConfigResp.

        :return: The file_transfer_config of this CoreRunInvokeConfigResp.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunFileTransferConfig`
        """
        return self._file_transfer_config

    @file_transfer_config.setter
    def file_transfer_config(self, file_transfer_config):
        r"""Sets the file_transfer_config of this CoreRunInvokeConfigResp.

        :param file_transfer_config: The file_transfer_config of this CoreRunInvokeConfigResp.
        :type file_transfer_config: :class:`huaweicloudsdkagentarts.v1.CoreRunFileTransferConfig`
        """
        self._file_transfer_config = file_transfer_config

    @property
    def url_match_type(self):
        r"""Gets the url_match_type of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时调用URL的匹配模式。 **取值范围**: - ACCURATE_MATCH - PREFIX_MATCH 

        :return: The url_match_type of this CoreRunInvokeConfigResp.
        :rtype: str
        """
        return self._url_match_type

    @url_match_type.setter
    def url_match_type(self, url_match_type):
        r"""Sets the url_match_type of this CoreRunInvokeConfigResp.

        **参数解释**: 智能体运行时调用URL的匹配模式。 **取值范围**: - ACCURATE_MATCH - PREFIX_MATCH 

        :param url_match_type: The url_match_type of this CoreRunInvokeConfigResp.
        :type url_match_type: str
        """
        self._url_match_type = url_match_type

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
        if not isinstance(other, CoreRunInvokeConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
