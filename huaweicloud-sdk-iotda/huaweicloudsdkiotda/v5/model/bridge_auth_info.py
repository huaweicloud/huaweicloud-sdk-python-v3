# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BridgeAuthInfo:

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
        'secret': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'secret': 'secret'
    }

    def __init__(self, auth_type=None, secret=None):
        r"""BridgeAuthInfo

        The model defined in huaweicloud sdk

        :param auth_type: 鉴权类型。当前支持密钥认证接入(SECRET)。使用密钥认证接入方式(SECRET)填写secret字段，不填写auth_type默认为密钥认证接入方式(SECRET)。
        :type auth_type: str
        :param secret: 网桥密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。
        :type secret: str
        """
        
        

        self._auth_type = None
        self._secret = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if secret is not None:
            self.secret = secret

    @property
    def auth_type(self):
        r"""Gets the auth_type of this BridgeAuthInfo.

        鉴权类型。当前支持密钥认证接入(SECRET)。使用密钥认证接入方式(SECRET)填写secret字段，不填写auth_type默认为密钥认证接入方式(SECRET)。

        :return: The auth_type of this BridgeAuthInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this BridgeAuthInfo.

        鉴权类型。当前支持密钥认证接入(SECRET)。使用密钥认证接入方式(SECRET)填写secret字段，不填写auth_type默认为密钥认证接入方式(SECRET)。

        :param auth_type: The auth_type of this BridgeAuthInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def secret(self):
        r"""Gets the secret of this BridgeAuthInfo.

        网桥密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。

        :return: The secret of this BridgeAuthInfo.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this BridgeAuthInfo.

        网桥密钥，认证类型使用密钥认证接入(SECRET)可填写该字段。

        :param secret: The secret of this BridgeAuthInfo.
        :type secret: str
        """
        self._secret = secret

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
        if not isinstance(other, BridgeAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
