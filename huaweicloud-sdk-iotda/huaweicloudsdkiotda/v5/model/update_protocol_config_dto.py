# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtocolConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keepalive_timeout': 'int',
        'description': 'str',
        'codec_mode': 'str',
        'func_urn': 'str'
    }

    attribute_map = {
        'keepalive_timeout': 'keepalive_timeout',
        'description': 'description',
        'codec_mode': 'codec_mode',
        'func_urn': 'func_urn'
    }

    def __init__(self, keepalive_timeout=None, description=None, codec_mode=None, func_urn=None):
        r"""UpdateProtocolConfigDTO

        The model defined in huaweicloud sdk

        :param keepalive_timeout: **参数说明**：连接空闲断链时间，单位（s）。
        :type keepalive_timeout: int
        :param description: **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param codec_mode: **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。
        :type codec_mode: str
        :param func_urn: **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。
        :type func_urn: str
        """
        
        

        self._keepalive_timeout = None
        self._description = None
        self._codec_mode = None
        self._func_urn = None
        self.discriminator = None

        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if description is not None:
            self.description = description
        if codec_mode is not None:
            self.codec_mode = codec_mode
        if func_urn is not None:
            self.func_urn = func_urn

    @property
    def keepalive_timeout(self):
        r"""Gets the keepalive_timeout of this UpdateProtocolConfigDTO.

        **参数说明**：连接空闲断链时间，单位（s）。

        :return: The keepalive_timeout of this UpdateProtocolConfigDTO.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        r"""Sets the keepalive_timeout of this UpdateProtocolConfigDTO.

        **参数说明**：连接空闲断链时间，单位（s）。

        :param keepalive_timeout: The keepalive_timeout of this UpdateProtocolConfigDTO.
        :type keepalive_timeout: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def description(self):
        r"""Gets the description of this UpdateProtocolConfigDTO.

        **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this UpdateProtocolConfigDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateProtocolConfigDTO.

        **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this UpdateProtocolConfigDTO.
        :type description: str
        """
        self._description = description

    @property
    def codec_mode(self):
        r"""Gets the codec_mode of this UpdateProtocolConfigDTO.

        **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。

        :return: The codec_mode of this UpdateProtocolConfigDTO.
        :rtype: str
        """
        return self._codec_mode

    @codec_mode.setter
    def codec_mode(self, codec_mode):
        r"""Sets the codec_mode of this UpdateProtocolConfigDTO.

        **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。

        :param codec_mode: The codec_mode of this UpdateProtocolConfigDTO.
        :type codec_mode: str
        """
        self._codec_mode = codec_mode

    @property
    def func_urn(self):
        r"""Gets the func_urn of this UpdateProtocolConfigDTO.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :return: The func_urn of this UpdateProtocolConfigDTO.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this UpdateProtocolConfigDTO.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :param func_urn: The func_urn of this UpdateProtocolConfigDTO.
        :type func_urn: str
        """
        self._func_urn = func_urn

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
        if not isinstance(other, UpdateProtocolConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
