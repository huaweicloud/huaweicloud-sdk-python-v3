# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiFirewallConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'str',
        'source_secret': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'source_id': 'source_id',
        'source_secret': 'source_secret',
        'app_id': 'app_id'
    }

    def __init__(self, source_id=None, source_secret=None, app_id=None):
        r"""ShowAiFirewallConfigResponse

        The model defined in huaweicloud sdk

        :param source_id: **参数解释**: 防火墙AK（Access Key），用于身份标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type source_id: str
        :param source_secret: **参数解释**: 防火墙SK（Secret Key），用于签名认证，解密返回 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type source_secret: str
        :param app_id: **参数解释**: 应用ID，标识接入防火墙的应用 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type app_id: str
        """
        
        super().__init__()

        self._source_id = None
        self._source_secret = None
        self._app_id = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if source_secret is not None:
            self.source_secret = source_secret
        if app_id is not None:
            self.app_id = app_id

    @property
    def source_id(self):
        r"""Gets the source_id of this ShowAiFirewallConfigResponse.

        **参数解释**: 防火墙AK（Access Key），用于身份标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The source_id of this ShowAiFirewallConfigResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ShowAiFirewallConfigResponse.

        **参数解释**: 防火墙AK（Access Key），用于身份标识 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param source_id: The source_id of this ShowAiFirewallConfigResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_secret(self):
        r"""Gets the source_secret of this ShowAiFirewallConfigResponse.

        **参数解释**: 防火墙SK（Secret Key），用于签名认证，解密返回 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The source_secret of this ShowAiFirewallConfigResponse.
        :rtype: str
        """
        return self._source_secret

    @source_secret.setter
    def source_secret(self, source_secret):
        r"""Sets the source_secret of this ShowAiFirewallConfigResponse.

        **参数解释**: 防火墙SK（Secret Key），用于签名认证，解密返回 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param source_secret: The source_secret of this ShowAiFirewallConfigResponse.
        :type source_secret: str
        """
        self._source_secret = source_secret

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowAiFirewallConfigResponse.

        **参数解释**: 应用ID，标识接入防火墙的应用 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The app_id of this ShowAiFirewallConfigResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowAiFirewallConfigResponse.

        **参数解释**: 应用ID，标识接入防火墙的应用 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param app_id: The app_id of this ShowAiFirewallConfigResponse.
        :type app_id: str
        """
        self._app_id = app_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowAiFirewallConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowAiFirewallConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
