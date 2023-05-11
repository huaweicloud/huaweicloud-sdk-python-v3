# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenUserResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'password_expires_at': 'str',
        'domain': 'TokenUserDomainResult'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'password_expires_at': 'password_expires_at',
        'domain': 'domain'
    }

    def __init__(self, name=None, id=None, password_expires_at=None, domain=None):
        """TokenUserResult

        The model defined in huaweicloud sdk

        :param name: IAM用户名。
        :type name: str
        :param id: IAM用户ID。
        :type id: str
        :param password_expires_at: 密码过期时间（UTC时间），“”表示密码不过期。
        :type password_expires_at: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.TokenUserDomainResult`
        """
        
        

        self._name = None
        self._id = None
        self._password_expires_at = None
        self._domain = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.password_expires_at = password_expires_at
        self.domain = domain

    @property
    def name(self):
        """Gets the name of this TokenUserResult.

        IAM用户名。

        :return: The name of this TokenUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenUserResult.

        IAM用户名。

        :param name: The name of this TokenUserResult.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this TokenUserResult.

        IAM用户ID。

        :return: The id of this TokenUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenUserResult.

        IAM用户ID。

        :param id: The id of this TokenUserResult.
        :type id: str
        """
        self._id = id

    @property
    def password_expires_at(self):
        """Gets the password_expires_at of this TokenUserResult.

        密码过期时间（UTC时间），“”表示密码不过期。

        :return: The password_expires_at of this TokenUserResult.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        """Sets the password_expires_at of this TokenUserResult.

        密码过期时间（UTC时间），“”表示密码不过期。

        :param password_expires_at: The password_expires_at of this TokenUserResult.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

    @property
    def domain(self):
        """Gets the domain of this TokenUserResult.

        :return: The domain of this TokenUserResult.
        :rtype: :class:`huaweicloudsdkiam.v3.TokenUserDomainResult`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TokenUserResult.

        :param domain: The domain of this TokenUserResult.
        :type domain: :class:`huaweicloudsdkiam.v3.TokenUserDomainResult`
        """
        self._domain = domain

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
        if not isinstance(other, TokenUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
