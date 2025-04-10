# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdpToken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issued_at': 'str',
        'expires_at': 'str',
        'methods': 'list[str]',
        'user': 'UnscopedTokenUser'
    }

    attribute_map = {
        'issued_at': 'issued_at',
        'expires_at': 'expires_at',
        'methods': 'methods',
        'user': 'user'
    }

    def __init__(self, issued_at=None, expires_at=None, methods=None, user=None):
        r"""IdpToken

        The model defined in huaweicloud sdk

        :param issued_at: token产生时间。
        :type issued_at: str
        :param expires_at: token到期时间。
        :type expires_at: str
        :param methods: 获取token的方式。
        :type methods: list[str]
        :param user: 
        :type user: :class:`huaweicloudsdkiam.v3.UnscopedTokenUser`
        """
        
        

        self._issued_at = None
        self._expires_at = None
        self._methods = None
        self._user = None
        self.discriminator = None

        self.issued_at = issued_at
        self.expires_at = expires_at
        self.methods = methods
        self.user = user

    @property
    def issued_at(self):
        r"""Gets the issued_at of this IdpToken.

        token产生时间。

        :return: The issued_at of this IdpToken.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        r"""Sets the issued_at of this IdpToken.

        token产生时间。

        :param issued_at: The issued_at of this IdpToken.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def expires_at(self):
        r"""Gets the expires_at of this IdpToken.

        token到期时间。

        :return: The expires_at of this IdpToken.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this IdpToken.

        token到期时间。

        :param expires_at: The expires_at of this IdpToken.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def methods(self):
        r"""Gets the methods of this IdpToken.

        获取token的方式。

        :return: The methods of this IdpToken.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        r"""Sets the methods of this IdpToken.

        获取token的方式。

        :param methods: The methods of this IdpToken.
        :type methods: list[str]
        """
        self._methods = methods

    @property
    def user(self):
        r"""Gets the user of this IdpToken.

        :return: The user of this IdpToken.
        :rtype: :class:`huaweicloudsdkiam.v3.UnscopedTokenUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this IdpToken.

        :param user: The user of this IdpToken.
        :type user: :class:`huaweicloudsdkiam.v3.UnscopedTokenUser`
        """
        self._user = user

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
        if not isinstance(other, IdpToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
