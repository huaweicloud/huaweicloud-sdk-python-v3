# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBearerTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'identity_store_id': 'str',
        'tenant_id': 'str',
        'x_security_token': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'tenant_id': 'tenant_id',
        'x_security_token': 'X-Security-Token'
    }

    def __init__(self, identity_store_id=None, tenant_id=None, x_security_token=None):
        r"""CreateBearerTokenRequest

        The model defined in huaweicloud sdk

        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param tenant_id: 自动预置配置的全局唯一标识符（ID）
        :type tenant_id: str
        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        """
        
        

        self._identity_store_id = None
        self._tenant_id = None
        self._x_security_token = None
        self.discriminator = None

        self.identity_store_id = identity_store_id
        self.tenant_id = tenant_id
        if x_security_token is not None:
            self.x_security_token = x_security_token

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this CreateBearerTokenRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this CreateBearerTokenRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this CreateBearerTokenRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this CreateBearerTokenRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateBearerTokenRequest.

        自动预置配置的全局唯一标识符（ID）

        :return: The tenant_id of this CreateBearerTokenRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateBearerTokenRequest.

        自动预置配置的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this CreateBearerTokenRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this CreateBearerTokenRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this CreateBearerTokenRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this CreateBearerTokenRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this CreateBearerTokenRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

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
        if not isinstance(other, CreateBearerTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
