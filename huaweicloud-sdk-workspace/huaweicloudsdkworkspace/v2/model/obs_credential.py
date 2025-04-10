# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsCredential:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access': 'str',
        'secret': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'access': 'access',
        'secret': 'secret',
        'security_token': 'security_token'
    }

    def __init__(self, access=None, secret=None, security_token=None):
        r"""ObsCredential

        The model defined in huaweicloud sdk

        :param access: access key。
        :type access: str
        :param secret: secret key。
        :type secret: str
        :param security_token: 安全校验token。
        :type security_token: str
        """
        
        

        self._access = None
        self._secret = None
        self._security_token = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if secret is not None:
            self.secret = secret
        if security_token is not None:
            self.security_token = security_token

    @property
    def access(self):
        r"""Gets the access of this ObsCredential.

        access key。

        :return: The access of this ObsCredential.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        r"""Sets the access of this ObsCredential.

        access key。

        :param access: The access of this ObsCredential.
        :type access: str
        """
        self._access = access

    @property
    def secret(self):
        r"""Gets the secret of this ObsCredential.

        secret key。

        :return: The secret of this ObsCredential.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this ObsCredential.

        secret key。

        :param secret: The secret of this ObsCredential.
        :type secret: str
        """
        self._secret = secret

    @property
    def security_token(self):
        r"""Gets the security_token of this ObsCredential.

        安全校验token。

        :return: The security_token of this ObsCredential.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this ObsCredential.

        安全校验token。

        :param security_token: The security_token of this ObsCredential.
        :type security_token: str
        """
        self._security_token = security_token

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
        if not isinstance(other, ObsCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
