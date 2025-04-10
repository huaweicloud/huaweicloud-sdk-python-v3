# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'mfa_authenticated': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'mfa_authenticated': 'mfa_authenticated'
    }

    def __init__(self, created_at=None, mfa_authenticated=None):
        r"""Attributes

        The model defined in huaweicloud sdk

        :param created_at: 颁发临时安全凭证时的时间（timestamp，为标准UTC时间，毫秒级，13位数字）。
        :type created_at: str
        :param mfa_authenticated: 是否已经通过MFA身份认证。
        :type mfa_authenticated: str
        """
        
        

        self._created_at = None
        self._mfa_authenticated = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if mfa_authenticated is not None:
            self.mfa_authenticated = mfa_authenticated

    @property
    def created_at(self):
        r"""Gets the created_at of this Attributes.

        颁发临时安全凭证时的时间（timestamp，为标准UTC时间，毫秒级，13位数字）。

        :return: The created_at of this Attributes.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Attributes.

        颁发临时安全凭证时的时间（timestamp，为标准UTC时间，毫秒级，13位数字）。

        :param created_at: The created_at of this Attributes.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def mfa_authenticated(self):
        r"""Gets the mfa_authenticated of this Attributes.

        是否已经通过MFA身份认证。

        :return: The mfa_authenticated of this Attributes.
        :rtype: str
        """
        return self._mfa_authenticated

    @mfa_authenticated.setter
    def mfa_authenticated(self, mfa_authenticated):
        r"""Sets the mfa_authenticated of this Attributes.

        是否已经通过MFA身份认证。

        :param mfa_authenticated: The mfa_authenticated of this Attributes.
        :type mfa_authenticated: str
        """
        self._mfa_authenticated = mfa_authenticated

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
        if not isinstance(other, Attributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
