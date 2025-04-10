# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key'
    }

    def __init__(self, access_key=None, secret_key=None):
        r"""AuthInfo

        The model defined in huaweicloud sdk

        :param access_key: 访问密钥
        :type access_key: str
        :param secret_key: 私钥
        :type secret_key: str
        """
        
        

        self._access_key = None
        self._secret_key = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def access_key(self):
        r"""Gets the access_key of this AuthInfo.

        访问密钥

        :return: The access_key of this AuthInfo.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this AuthInfo.

        访问密钥

        :param access_key: The access_key of this AuthInfo.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this AuthInfo.

        私钥

        :return: The secret_key of this AuthInfo.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this AuthInfo.

        私钥

        :param secret_key: The secret_key of this AuthInfo.
        :type secret_key: str
        """
        self._secret_key = secret_key

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
        if not isinstance(other, AuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
