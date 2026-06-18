# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectTenantSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_encryption_enabled': 'bool',
        'encryption_type': 'str',
        'permit_public': 'str'
    }

    attribute_map = {
        'default_encryption_enabled': 'default_encryption_enabled',
        'encryption_type': 'encryption_type',
        'permit_public': 'permit_public'
    }

    def __init__(self, default_encryption_enabled=None, encryption_type=None, permit_public=None):
        r"""ShowProjectTenantSettingsResponse

        The model defined in huaweicloud sdk

        :param default_encryption_enabled: **参数解释：** 仓库默认加密设置是否开启。
        :type default_encryption_enabled: bool
        :param encryption_type: **参数解释：** 租户设置的加密类型。 **取值范围：** KMS,normal,null,当为KMS时表示开启了KMS加密。
        :type encryption_type: str
        :param permit_public: **参数解释：** 允许公共访问。 **取值范围：** allow 允许 deny 拒绝。
        :type permit_public: str
        """
        
        super().__init__()

        self._default_encryption_enabled = None
        self._encryption_type = None
        self._permit_public = None
        self.discriminator = None

        if default_encryption_enabled is not None:
            self.default_encryption_enabled = default_encryption_enabled
        if encryption_type is not None:
            self.encryption_type = encryption_type
        if permit_public is not None:
            self.permit_public = permit_public

    @property
    def default_encryption_enabled(self):
        r"""Gets the default_encryption_enabled of this ShowProjectTenantSettingsResponse.

        **参数解释：** 仓库默认加密设置是否开启。

        :return: The default_encryption_enabled of this ShowProjectTenantSettingsResponse.
        :rtype: bool
        """
        return self._default_encryption_enabled

    @default_encryption_enabled.setter
    def default_encryption_enabled(self, default_encryption_enabled):
        r"""Sets the default_encryption_enabled of this ShowProjectTenantSettingsResponse.

        **参数解释：** 仓库默认加密设置是否开启。

        :param default_encryption_enabled: The default_encryption_enabled of this ShowProjectTenantSettingsResponse.
        :type default_encryption_enabled: bool
        """
        self._default_encryption_enabled = default_encryption_enabled

    @property
    def encryption_type(self):
        r"""Gets the encryption_type of this ShowProjectTenantSettingsResponse.

        **参数解释：** 租户设置的加密类型。 **取值范围：** KMS,normal,null,当为KMS时表示开启了KMS加密。

        :return: The encryption_type of this ShowProjectTenantSettingsResponse.
        :rtype: str
        """
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        r"""Sets the encryption_type of this ShowProjectTenantSettingsResponse.

        **参数解释：** 租户设置的加密类型。 **取值范围：** KMS,normal,null,当为KMS时表示开启了KMS加密。

        :param encryption_type: The encryption_type of this ShowProjectTenantSettingsResponse.
        :type encryption_type: str
        """
        self._encryption_type = encryption_type

    @property
    def permit_public(self):
        r"""Gets the permit_public of this ShowProjectTenantSettingsResponse.

        **参数解释：** 允许公共访问。 **取值范围：** allow 允许 deny 拒绝。

        :return: The permit_public of this ShowProjectTenantSettingsResponse.
        :rtype: str
        """
        return self._permit_public

    @permit_public.setter
    def permit_public(self, permit_public):
        r"""Sets the permit_public of this ShowProjectTenantSettingsResponse.

        **参数解释：** 允许公共访问。 **取值范围：** allow 允许 deny 拒绝。

        :param permit_public: The permit_public of this ShowProjectTenantSettingsResponse.
        :type permit_public: str
        """
        self._permit_public = permit_public

    def to_dict(self):
        import warnings
        warnings.warn("ShowProjectTenantSettingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowProjectTenantSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
