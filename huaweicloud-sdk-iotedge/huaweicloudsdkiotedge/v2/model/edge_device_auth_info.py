# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeDeviceAuthInfo:

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
        'fingerprint': 'str',
        'secure_access': 'bool',
        'timeout': 'int'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'secret': 'secret',
        'fingerprint': 'fingerprint',
        'secure_access': 'secure_access',
        'timeout': 'timeout'
    }

    def __init__(self, auth_type=None, secret=None, fingerprint=None, secure_access=None, timeout=None):
        """EdgeDeviceAuthInfo

        The model defined in huaweicloud sdk

        :param auth_type: 鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写secret字段，使用证书认证接入方式(CERTIFICATES)填写fingerprint字段，不填写auth_type默认为密钥认证接入方式(SECRET)
        :type auth_type: str
        :param secret: 设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。
        :type secret: str
        :param fingerprint: 证书指纹，认证类型使用证书认证接入(CERTIFICATES)可填写该字段，注册设备时不填写该字段则取第一次设备接入时的证书指纹。注意：指纹只能为40位十六进制字符串或者64位十六进制字符串；修改设备、查询设备及查询设备列表接口不返回该参数。
        :type fingerprint: str
        :param secure_access: 指设备是否通过安全协议方式接入，默认值为true。 - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。 
        :type secure_access: bool
        :param timeout: 设备验证码的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示设备验证码不会失效（建议填写为“0”）。注意：只有注册设备接口或者修改设备接口修改timeout时返回该参数。 
        :type timeout: int
        """
        
        

        self._auth_type = None
        self._secret = None
        self._fingerprint = None
        self._secure_access = None
        self._timeout = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if secret is not None:
            self.secret = secret
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if secure_access is not None:
            self.secure_access = secure_access
        if timeout is not None:
            self.timeout = timeout

    @property
    def auth_type(self):
        """Gets the auth_type of this EdgeDeviceAuthInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写secret字段，使用证书认证接入方式(CERTIFICATES)填写fingerprint字段，不填写auth_type默认为密钥认证接入方式(SECRET)

        :return: The auth_type of this EdgeDeviceAuthInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this EdgeDeviceAuthInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写secret字段，使用证书认证接入方式(CERTIFICATES)填写fingerprint字段，不填写auth_type默认为密钥认证接入方式(SECRET)

        :param auth_type: The auth_type of this EdgeDeviceAuthInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def secret(self):
        """Gets the secret of this EdgeDeviceAuthInfo.

        设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。

        :return: The secret of this EdgeDeviceAuthInfo.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this EdgeDeviceAuthInfo.

        设备密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。注意：NB设备密钥由于协议特殊性，只支持十六进制密钥接入；修改设备、查询设备及查询设备列表接口不返回该参数。

        :param secret: The secret of this EdgeDeviceAuthInfo.
        :type secret: str
        """
        self._secret = secret

    @property
    def fingerprint(self):
        """Gets the fingerprint of this EdgeDeviceAuthInfo.

        证书指纹，认证类型使用证书认证接入(CERTIFICATES)可填写该字段，注册设备时不填写该字段则取第一次设备接入时的证书指纹。注意：指纹只能为40位十六进制字符串或者64位十六进制字符串；修改设备、查询设备及查询设备列表接口不返回该参数。

        :return: The fingerprint of this EdgeDeviceAuthInfo.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this EdgeDeviceAuthInfo.

        证书指纹，认证类型使用证书认证接入(CERTIFICATES)可填写该字段，注册设备时不填写该字段则取第一次设备接入时的证书指纹。注意：指纹只能为40位十六进制字符串或者64位十六进制字符串；修改设备、查询设备及查询设备列表接口不返回该参数。

        :param fingerprint: The fingerprint of this EdgeDeviceAuthInfo.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def secure_access(self):
        """Gets the secure_access of this EdgeDeviceAuthInfo.

        指设备是否通过安全协议方式接入，默认值为true。 - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。 

        :return: The secure_access of this EdgeDeviceAuthInfo.
        :rtype: bool
        """
        return self._secure_access

    @secure_access.setter
    def secure_access(self, secure_access):
        """Sets the secure_access of this EdgeDeviceAuthInfo.

        指设备是否通过安全协议方式接入，默认值为true。 - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。 

        :param secure_access: The secure_access of this EdgeDeviceAuthInfo.
        :type secure_access: bool
        """
        self._secure_access = secure_access

    @property
    def timeout(self):
        """Gets the timeout of this EdgeDeviceAuthInfo.

        设备验证码的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示设备验证码不会失效（建议填写为“0”）。注意：只有注册设备接口或者修改设备接口修改timeout时返回该参数。 

        :return: The timeout of this EdgeDeviceAuthInfo.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EdgeDeviceAuthInfo.

        设备验证码的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示设备验证码不会失效（建议填写为“0”）。注意：只有注册设备接口或者修改设备接口修改timeout时返回该参数。 

        :param timeout: The timeout of this EdgeDeviceAuthInfo.
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
        if not isinstance(other, EdgeDeviceAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
