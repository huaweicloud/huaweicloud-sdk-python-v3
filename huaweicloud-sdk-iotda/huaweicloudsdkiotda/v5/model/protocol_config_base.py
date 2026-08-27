# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtocolConfigBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol_id': 'str',
        'port': 'int',
        'keepalive_timeout': 'int',
        'protocol_type': 'str',
        'description': 'str',
        'ssl_enable': 'bool',
        'frame_decode_configs': 'list[FrameDecodeConfig]',
        'codec_mode': 'str',
        'func_urn': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'protocol_id': 'protocol_id',
        'port': 'port',
        'keepalive_timeout': 'keepalive_timeout',
        'protocol_type': 'protocol_type',
        'description': 'description',
        'ssl_enable': 'ssl_enable',
        'frame_decode_configs': 'frame_decode_configs',
        'codec_mode': 'codec_mode',
        'func_urn': 'func_urn',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, protocol_id=None, port=None, keepalive_timeout=None, protocol_type=None, description=None, ssl_enable=None, frame_decode_configs=None, codec_mode=None, func_urn=None, create_time=None, update_time=None):
        r"""ProtocolConfigBase

        The model defined in huaweicloud sdk

        :param protocol_id: **参数说明**：泛协议配置ID。
        :type protocol_id: str
        :param port: **参数说明**：泛协议配置的端口号。
        :type port: int
        :param keepalive_timeout: **参数说明**：连接空闲断链时间，单位（s）。
        :type keepalive_timeout: int
        :param protocol_type: **参数说明**：协议类型。 **取值范围**： - TCP：通用TCP协议接入
        :type protocol_type: str
        :param description: **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param ssl_enable: **参数说明**：是否开启tls加密传输。
        :type ssl_enable: bool
        :param frame_decode_configs: **参数说明**：码流拆包组包配置列表。
        :type frame_decode_configs: list[:class:`huaweicloudsdkiotda.v5.FrameDecodeConfig`]
        :param codec_mode: **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。
        :type codec_mode: str
        :param func_urn: **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。
        :type func_urn: str
        :param create_time: **参数说明**：在物联网平台查询自定义鉴权的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type create_time: str
        :param update_time: **参数说明**：在物联网平台更新查询自定义鉴权的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type update_time: str
        """
        
        

        self._protocol_id = None
        self._port = None
        self._keepalive_timeout = None
        self._protocol_type = None
        self._description = None
        self._ssl_enable = None
        self._frame_decode_configs = None
        self._codec_mode = None
        self._func_urn = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if protocol_id is not None:
            self.protocol_id = protocol_id
        if port is not None:
            self.port = port
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if description is not None:
            self.description = description
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if frame_decode_configs is not None:
            self.frame_decode_configs = frame_decode_configs
        if codec_mode is not None:
            self.codec_mode = codec_mode
        if func_urn is not None:
            self.func_urn = func_urn
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def protocol_id(self):
        r"""Gets the protocol_id of this ProtocolConfigBase.

        **参数说明**：泛协议配置ID。

        :return: The protocol_id of this ProtocolConfigBase.
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        r"""Sets the protocol_id of this ProtocolConfigBase.

        **参数说明**：泛协议配置ID。

        :param protocol_id: The protocol_id of this ProtocolConfigBase.
        :type protocol_id: str
        """
        self._protocol_id = protocol_id

    @property
    def port(self):
        r"""Gets the port of this ProtocolConfigBase.

        **参数说明**：泛协议配置的端口号。

        :return: The port of this ProtocolConfigBase.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ProtocolConfigBase.

        **参数说明**：泛协议配置的端口号。

        :param port: The port of this ProtocolConfigBase.
        :type port: int
        """
        self._port = port

    @property
    def keepalive_timeout(self):
        r"""Gets the keepalive_timeout of this ProtocolConfigBase.

        **参数说明**：连接空闲断链时间，单位（s）。

        :return: The keepalive_timeout of this ProtocolConfigBase.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        r"""Sets the keepalive_timeout of this ProtocolConfigBase.

        **参数说明**：连接空闲断链时间，单位（s）。

        :param keepalive_timeout: The keepalive_timeout of this ProtocolConfigBase.
        :type keepalive_timeout: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this ProtocolConfigBase.

        **参数说明**：协议类型。 **取值范围**： - TCP：通用TCP协议接入

        :return: The protocol_type of this ProtocolConfigBase.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this ProtocolConfigBase.

        **参数说明**：协议类型。 **取值范围**： - TCP：通用TCP协议接入

        :param protocol_type: The protocol_type of this ProtocolConfigBase.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def description(self):
        r"""Gets the description of this ProtocolConfigBase.

        **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this ProtocolConfigBase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProtocolConfigBase.

        **参数说明**：泛协议的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this ProtocolConfigBase.
        :type description: str
        """
        self._description = description

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this ProtocolConfigBase.

        **参数说明**：是否开启tls加密传输。

        :return: The ssl_enable of this ProtocolConfigBase.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this ProtocolConfigBase.

        **参数说明**：是否开启tls加密传输。

        :param ssl_enable: The ssl_enable of this ProtocolConfigBase.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def frame_decode_configs(self):
        r"""Gets the frame_decode_configs of this ProtocolConfigBase.

        **参数说明**：码流拆包组包配置列表。

        :return: The frame_decode_configs of this ProtocolConfigBase.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.FrameDecodeConfig`]
        """
        return self._frame_decode_configs

    @frame_decode_configs.setter
    def frame_decode_configs(self, frame_decode_configs):
        r"""Sets the frame_decode_configs of this ProtocolConfigBase.

        **参数说明**：码流拆包组包配置列表。

        :param frame_decode_configs: The frame_decode_configs of this ProtocolConfigBase.
        :type frame_decode_configs: list[:class:`huaweicloudsdkiotda.v5.FrameDecodeConfig`]
        """
        self._frame_decode_configs = frame_decode_configs

    @property
    def codec_mode(self):
        r"""Gets the codec_mode of this ProtocolConfigBase.

        **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。

        :return: The codec_mode of this ProtocolConfigBase.
        :rtype: str
        """
        return self._codec_mode

    @codec_mode.setter
    def codec_mode(self, codec_mode):
        r"""Sets the codec_mode of this ProtocolConfigBase.

        **参数说明**：编解码类型。 **取值范围**： - FGS：将编解码插件以函数形式部署到FunctionGraph。 - PLUGIN：将编解码插件以OSGI插件形式部署到设备接入平台，使用该方式需提工单联系技术支持。

        :param codec_mode: The codec_mode of this ProtocolConfigBase.
        :type codec_mode: str
        """
        self._codec_mode = codec_mode

    @property
    def func_urn(self):
        r"""Gets the func_urn of this ProtocolConfigBase.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :return: The func_urn of this ProtocolConfigBase.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this ProtocolConfigBase.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，采用FGS进行编解码的对应函数地址。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、分隔符（:）的组合。

        :param func_urn: The func_urn of this ProtocolConfigBase.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def create_time(self):
        r"""Gets the create_time of this ProtocolConfigBase.

        **参数说明**：在物联网平台查询自定义鉴权的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The create_time of this ProtocolConfigBase.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProtocolConfigBase.

        **参数说明**：在物联网平台查询自定义鉴权的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param create_time: The create_time of this ProtocolConfigBase.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ProtocolConfigBase.

        **参数说明**：在物联网平台更新查询自定义鉴权的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The update_time of this ProtocolConfigBase.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ProtocolConfigBase.

        **参数说明**：在物联网平台更新查询自定义鉴权的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param update_time: The update_time of this ProtocolConfigBase.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ProtocolConfigBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
