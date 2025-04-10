# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthInfoRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'secret': 'str',
        'secondary_secret': 'str',
        'fingerprint': 'str',
        'secondary_fingerprint': 'str',
        'secure_access': 'bool',
        'timeout': 'int'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'secret': 'secret',
        'secondary_secret': 'secondary_secret',
        'fingerprint': 'fingerprint',
        'secondary_fingerprint': 'secondary_fingerprint',
        'secure_access': 'secure_access',
        'timeout': 'timeout'
    }

    def __init__(self, auth_type=None, secret=None, secondary_secret=None, fingerprint=None, secondary_fingerprint=None, secure_access=None, timeout=None):
        r"""AuthInfoRes

        The model defined in huaweicloud sdk

        :param auth_type: **参数说明**：鉴权类型。注意：不填写auth_type默认为密钥认证接入方式(SECRET)。 **取值范围**： - SECRET:使用密钥认证接入方式。 - CERTIFICATES:使用证书认证接入方式。
        :type auth_type: str
        :param secret: **参数说明**：设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type secret: str
        :param secondary_secret: **参数说明**：设备备用密钥，认证类型使用密钥认证接入(SECRET)该字段有效，当主密钥校验不通过时，会启用辅密钥校验，辅密钥与主密钥有相同的效力；辅密钥对coap协议接入的设备不生效。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type secondary_secret: str
        :param fingerprint: **参数说明**：证书指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，注册设备时不填写该字段则取第一次设备接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。
        :type fingerprint: str
        :param secondary_fingerprint: **参数说明**：证书备用指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，当主指纹校验不通过时，会启用辅指纹校验，辅指纹与主指纹有相同的效力。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。
        :type secondary_fingerprint: str
        :param secure_access: **参数说明**：指设备是否通过安全协议方式接入。 **取值范围**： - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。非安全接入的设备存在被仿冒等安全风险，请谨慎使用。
        :type secure_access: bool
        :param timeout: **参数说明**：设备接入的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示平台不会删除该设备的注册信息（建议填写为“0”）。 注意：该参数只对直连设备生效。
        :type timeout: int
        """
        
        

        self._auth_type = None
        self._secret = None
        self._secondary_secret = None
        self._fingerprint = None
        self._secondary_fingerprint = None
        self._secure_access = None
        self._timeout = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if secret is not None:
            self.secret = secret
        if secondary_secret is not None:
            self.secondary_secret = secondary_secret
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if secondary_fingerprint is not None:
            self.secondary_fingerprint = secondary_fingerprint
        if secure_access is not None:
            self.secure_access = secure_access
        if timeout is not None:
            self.timeout = timeout

    @property
    def auth_type(self):
        r"""Gets the auth_type of this AuthInfoRes.

        **参数说明**：鉴权类型。注意：不填写auth_type默认为密钥认证接入方式(SECRET)。 **取值范围**： - SECRET:使用密钥认证接入方式。 - CERTIFICATES:使用证书认证接入方式。

        :return: The auth_type of this AuthInfoRes.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this AuthInfoRes.

        **参数说明**：鉴权类型。注意：不填写auth_type默认为密钥认证接入方式(SECRET)。 **取值范围**： - SECRET:使用密钥认证接入方式。 - CERTIFICATES:使用证书认证接入方式。

        :param auth_type: The auth_type of this AuthInfoRes.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def secret(self):
        r"""Gets the secret of this AuthInfoRes.

        **参数说明**：设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The secret of this AuthInfoRes.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this AuthInfoRes.

        **参数说明**：设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param secret: The secret of this AuthInfoRes.
        :type secret: str
        """
        self._secret = secret

    @property
    def secondary_secret(self):
        r"""Gets the secondary_secret of this AuthInfoRes.

        **参数说明**：设备备用密钥，认证类型使用密钥认证接入(SECRET)该字段有效，当主密钥校验不通过时，会启用辅密钥校验，辅密钥与主密钥有相同的效力；辅密钥对coap协议接入的设备不生效。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The secondary_secret of this AuthInfoRes.
        :rtype: str
        """
        return self._secondary_secret

    @secondary_secret.setter
    def secondary_secret(self, secondary_secret):
        r"""Sets the secondary_secret of this AuthInfoRes.

        **参数说明**：设备备用密钥，认证类型使用密钥认证接入(SECRET)该字段有效，当主密钥校验不通过时，会启用辅密钥校验，辅密钥与主密钥有相同的效力；辅密钥对coap协议接入的设备不生效。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；查询设备列表接口不返回该参数。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param secondary_secret: The secondary_secret of this AuthInfoRes.
        :type secondary_secret: str
        """
        self._secondary_secret = secondary_secret

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this AuthInfoRes.

        **参数说明**：证书指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，注册设备时不填写该字段则取第一次设备接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :return: The fingerprint of this AuthInfoRes.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this AuthInfoRes.

        **参数说明**：证书指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，注册设备时不填写该字段则取第一次设备接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :param fingerprint: The fingerprint of this AuthInfoRes.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def secondary_fingerprint(self):
        r"""Gets the secondary_fingerprint of this AuthInfoRes.

        **参数说明**：证书备用指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，当主指纹校验不通过时，会启用辅指纹校验，辅指纹与主指纹有相同的效力。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :return: The secondary_fingerprint of this AuthInfoRes.
        :rtype: str
        """
        return self._secondary_fingerprint

    @secondary_fingerprint.setter
    def secondary_fingerprint(self, secondary_fingerprint):
        r"""Sets the secondary_fingerprint of this AuthInfoRes.

        **参数说明**：证书备用指纹，认证类型使用证书认证接入(CERTIFICATES)该字段有效，当主指纹校验不通过时，会启用辅指纹校验，辅指纹与主指纹有相同的效力。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :param secondary_fingerprint: The secondary_fingerprint of this AuthInfoRes.
        :type secondary_fingerprint: str
        """
        self._secondary_fingerprint = secondary_fingerprint

    @property
    def secure_access(self):
        r"""Gets the secure_access of this AuthInfoRes.

        **参数说明**：指设备是否通过安全协议方式接入。 **取值范围**： - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。非安全接入的设备存在被仿冒等安全风险，请谨慎使用。

        :return: The secure_access of this AuthInfoRes.
        :rtype: bool
        """
        return self._secure_access

    @secure_access.setter
    def secure_access(self, secure_access):
        r"""Sets the secure_access of this AuthInfoRes.

        **参数说明**：指设备是否通过安全协议方式接入。 **取值范围**： - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。非安全接入的设备存在被仿冒等安全风险，请谨慎使用。

        :param secure_access: The secure_access of this AuthInfoRes.
        :type secure_access: bool
        """
        self._secure_access = secure_access

    @property
    def timeout(self):
        r"""Gets the timeout of this AuthInfoRes.

        **参数说明**：设备接入的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示平台不会删除该设备的注册信息（建议填写为“0”）。 注意：该参数只对直连设备生效。

        :return: The timeout of this AuthInfoRes.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this AuthInfoRes.

        **参数说明**：设备接入的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示平台不会删除该设备的注册信息（建议填写为“0”）。 注意：该参数只对直连设备生效。

        :param timeout: The timeout of this AuthInfoRes.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, AuthInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
