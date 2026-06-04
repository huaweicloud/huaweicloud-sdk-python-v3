# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuthConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_config_id': 'str',
        'sms_login_enabled': 'bool'
    }

    attribute_map = {
        'auth_config_id': 'auth_config_id',
        'sms_login_enabled': 'sms_login_enabled'
    }

    def __init__(self, auth_config_id=None, sms_login_enabled=None):
        r"""UpdateAuthConfigResponse

        The model defined in huaweicloud sdk

        :param auth_config_id: 认证配置ID。
        :type auth_config_id: str
        :param sms_login_enabled: 是否开启短信登录。
        :type sms_login_enabled: bool
        """
        
        super().__init__()

        self._auth_config_id = None
        self._sms_login_enabled = None
        self.discriminator = None

        if auth_config_id is not None:
            self.auth_config_id = auth_config_id
        if sms_login_enabled is not None:
            self.sms_login_enabled = sms_login_enabled

    @property
    def auth_config_id(self):
        r"""Gets the auth_config_id of this UpdateAuthConfigResponse.

        认证配置ID。

        :return: The auth_config_id of this UpdateAuthConfigResponse.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        r"""Sets the auth_config_id of this UpdateAuthConfigResponse.

        认证配置ID。

        :param auth_config_id: The auth_config_id of this UpdateAuthConfigResponse.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def sms_login_enabled(self):
        r"""Gets the sms_login_enabled of this UpdateAuthConfigResponse.

        是否开启短信登录。

        :return: The sms_login_enabled of this UpdateAuthConfigResponse.
        :rtype: bool
        """
        return self._sms_login_enabled

    @sms_login_enabled.setter
    def sms_login_enabled(self, sms_login_enabled):
        r"""Sets the sms_login_enabled of this UpdateAuthConfigResponse.

        是否开启短信登录。

        :param sms_login_enabled: The sms_login_enabled of this UpdateAuthConfigResponse.
        :type sms_login_enabled: bool
        """
        self._sms_login_enabled = sms_login_enabled

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAuthConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateAuthConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
