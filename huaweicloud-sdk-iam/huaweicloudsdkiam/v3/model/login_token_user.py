# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginTokenUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'LoginTokenDomain',
        'name': 'str',
        'password_expires_at': 'str',
        'id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'name': 'name',
        'password_expires_at': 'password_expires_at',
        'id': 'id'
    }

    def __init__(self, domain=None, name=None, password_expires_at=None, id=None):
        r"""LoginTokenUser

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.LoginTokenDomain`
        :param name: 被委托方用户名。
        :type name: str
        :param password_expires_at: 被委托方用户的密码过期时间。
        :type password_expires_at: str
        :param id: 被委托方用户ID。
        :type id: str
        """
        
        

        self._domain = None
        self._name = None
        self._password_expires_at = None
        self._id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if name is not None:
            self.name = name
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at
        if id is not None:
            self.id = id

    @property
    def domain(self):
        r"""Gets the domain of this LoginTokenUser.

        :return: The domain of this LoginTokenUser.
        :rtype: :class:`huaweicloudsdkiam.v3.LoginTokenDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this LoginTokenUser.

        :param domain: The domain of this LoginTokenUser.
        :type domain: :class:`huaweicloudsdkiam.v3.LoginTokenDomain`
        """
        self._domain = domain

    @property
    def name(self):
        r"""Gets the name of this LoginTokenUser.

        被委托方用户名。

        :return: The name of this LoginTokenUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoginTokenUser.

        被委托方用户名。

        :param name: The name of this LoginTokenUser.
        :type name: str
        """
        self._name = name

    @property
    def password_expires_at(self):
        r"""Gets the password_expires_at of this LoginTokenUser.

        被委托方用户的密码过期时间。

        :return: The password_expires_at of this LoginTokenUser.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        r"""Sets the password_expires_at of this LoginTokenUser.

        被委托方用户的密码过期时间。

        :param password_expires_at: The password_expires_at of this LoginTokenUser.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

    @property
    def id(self):
        r"""Gets the id of this LoginTokenUser.

        被委托方用户ID。

        :return: The id of this LoginTokenUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoginTokenUser.

        被委托方用户ID。

        :param id: The id of this LoginTokenUser.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, LoginTokenUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
