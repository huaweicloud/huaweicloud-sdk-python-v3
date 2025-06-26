# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Credential:

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
        'access_key': 'str',
        'access_secret': 'str'
    }

    attribute_map = {
        'type': 'type',
        'access_key': 'access_key',
        'access_secret': 'access_secret'
    }

    def __init__(self, type=None, access_key=None, access_secret=None):
        r"""Credential

        The model defined in huaweicloud sdk

        :param type: 认证方式，目前只支持basic
        :type type: str
        :param access_key: 访问ID
        :type access_key: str
        :param access_secret: 访问密码
        :type access_secret: str
        """
        
        

        self._type = None
        self._access_key = None
        self._access_secret = None
        self.discriminator = None

        self.type = type
        self.access_key = access_key
        self.access_secret = access_secret

    @property
    def type(self):
        r"""Gets the type of this Credential.

        认证方式，目前只支持basic

        :return: The type of this Credential.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Credential.

        认证方式，目前只支持basic

        :param type: The type of this Credential.
        :type type: str
        """
        self._type = type

    @property
    def access_key(self):
        r"""Gets the access_key of this Credential.

        访问ID

        :return: The access_key of this Credential.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this Credential.

        访问ID

        :param access_key: The access_key of this Credential.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def access_secret(self):
        r"""Gets the access_secret of this Credential.

        访问密码

        :return: The access_secret of this Credential.
        :rtype: str
        """
        return self._access_secret

    @access_secret.setter
    def access_secret(self, access_secret):
        r"""Sets the access_secret of this Credential.

        访问密码

        :param access_secret: The access_secret of this Credential.
        :type access_secret: str
        """
        self._access_secret = access_secret

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
        if not isinstance(other, Credential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
