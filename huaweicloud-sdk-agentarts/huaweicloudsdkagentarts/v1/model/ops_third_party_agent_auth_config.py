# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentAuthConfig:

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
        'api_key': 'str',
        'api_key_position': 'str',
        'api_key_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'api_key': 'api_key',
        'api_key_position': 'api_key_position',
        'api_key_name': 'api_key_name'
    }

    def __init__(self, type=None, api_key=None, api_key_position=None, api_key_name=None):
        r"""OpsThirdPartyAgentAuthConfig

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 鉴权类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** - API_KEY：API Key鉴权 - NONE：无需鉴权 **默认取值：** NONE。
        :type type: str
        :param api_key: **参数解释：** API Key值，当type为API_KEY时必填。 **约束限制：** 字符串类型，最大长度500。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type api_key: str
        :param api_key_position: **参数解释：** API Key传递位置，当type为API_KEY时必填。 **约束限制：** 必须为枚举值之一。 **取值范围：** - HEADER：放在HTTP请求Header中 - QUERY：放在HTTP请求Query参数中 **默认取值：** HEADER。
        :type api_key_position: str
        :param api_key_name: **参数解释：** API Key参数名，当type为API_KEY时必填。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字、点(.)、连字符(-)及下划线(_)组成的字符串，长度为1~100个字符。 **默认取值：** 不涉及。
        :type api_key_name: str
        """
        
        

        self._type = None
        self._api_key = None
        self._api_key_position = None
        self._api_key_name = None
        self.discriminator = None

        self.type = type
        if api_key is not None:
            self.api_key = api_key
        if api_key_position is not None:
            self.api_key_position = api_key_position
        if api_key_name is not None:
            self.api_key_name = api_key_name

    @property
    def type(self):
        r"""Gets the type of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** 鉴权类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** - API_KEY：API Key鉴权 - NONE：无需鉴权 **默认取值：** NONE。

        :return: The type of this OpsThirdPartyAgentAuthConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** 鉴权类型。 **约束限制：** 必须为枚举值之一。 **取值范围：** - API_KEY：API Key鉴权 - NONE：无需鉴权 **默认取值：** NONE。

        :param type: The type of this OpsThirdPartyAgentAuthConfig.
        :type type: str
        """
        self._type = type

    @property
    def api_key(self):
        r"""Gets the api_key of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key值，当type为API_KEY时必填。 **约束限制：** 字符串类型，最大长度500。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The api_key of this OpsThirdPartyAgentAuthConfig.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key值，当type为API_KEY时必填。 **约束限制：** 字符串类型，最大长度500。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param api_key: The api_key of this OpsThirdPartyAgentAuthConfig.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def api_key_position(self):
        r"""Gets the api_key_position of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key传递位置，当type为API_KEY时必填。 **约束限制：** 必须为枚举值之一。 **取值范围：** - HEADER：放在HTTP请求Header中 - QUERY：放在HTTP请求Query参数中 **默认取值：** HEADER。

        :return: The api_key_position of this OpsThirdPartyAgentAuthConfig.
        :rtype: str
        """
        return self._api_key_position

    @api_key_position.setter
    def api_key_position(self, api_key_position):
        r"""Sets the api_key_position of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key传递位置，当type为API_KEY时必填。 **约束限制：** 必须为枚举值之一。 **取值范围：** - HEADER：放在HTTP请求Header中 - QUERY：放在HTTP请求Query参数中 **默认取值：** HEADER。

        :param api_key_position: The api_key_position of this OpsThirdPartyAgentAuthConfig.
        :type api_key_position: str
        """
        self._api_key_position = api_key_position

    @property
    def api_key_name(self):
        r"""Gets the api_key_name of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key参数名，当type为API_KEY时必填。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字、点(.)、连字符(-)及下划线(_)组成的字符串，长度为1~100个字符。 **默认取值：** 不涉及。

        :return: The api_key_name of this OpsThirdPartyAgentAuthConfig.
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        r"""Sets the api_key_name of this OpsThirdPartyAgentAuthConfig.

        **参数解释：** API Key参数名，当type为API_KEY时必填。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字、点(.)、连字符(-)及下划线(_)组成的字符串，长度为1~100个字符。 **默认取值：** 不涉及。

        :param api_key_name: The api_key_name of this OpsThirdPartyAgentAuthConfig.
        :type api_key_name: str
        """
        self._api_key_name = api_key_name

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
        if not isinstance(other, OpsThirdPartyAgentAuthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
