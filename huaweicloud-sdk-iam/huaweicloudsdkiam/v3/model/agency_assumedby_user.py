# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyAssumedbyUser:

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
        'domain': 'AgencyAssumedbyUserDomain',
        'password_expires_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'domain': 'domain',
        'password_expires_at': 'password_expires_at'
    }

    def __init__(self, name=None, id=None, domain=None, password_expires_at=None):
        """AgencyAssumedbyUser

        The model defined in huaweicloud sdk

        :param name: 被委托方B中IAM用户的用户名。
        :type name: str
        :param id: 被委托方B中IAM用户的用户ID。
        :type id: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.AgencyAssumedbyUserDomain`
        :param password_expires_at: 被委托方B中IAM用户的密码过期时间（UTC时间），“”表示密码不过期。
        :type password_expires_at: str
        """
        
        

        self._name = None
        self._id = None
        self._domain = None
        self._password_expires_at = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.domain = domain
        self.password_expires_at = password_expires_at

    @property
    def name(self):
        """Gets the name of this AgencyAssumedbyUser.

        被委托方B中IAM用户的用户名。

        :return: The name of this AgencyAssumedbyUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgencyAssumedbyUser.

        被委托方B中IAM用户的用户名。

        :param name: The name of this AgencyAssumedbyUser.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this AgencyAssumedbyUser.

        被委托方B中IAM用户的用户ID。

        :return: The id of this AgencyAssumedbyUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgencyAssumedbyUser.

        被委托方B中IAM用户的用户ID。

        :param id: The id of this AgencyAssumedbyUser.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        """Gets the domain of this AgencyAssumedbyUser.


        :return: The domain of this AgencyAssumedbyUser.
        :rtype: :class:`huaweicloudsdkiam.v3.AgencyAssumedbyUserDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AgencyAssumedbyUser.


        :param domain: The domain of this AgencyAssumedbyUser.
        :type domain: :class:`huaweicloudsdkiam.v3.AgencyAssumedbyUserDomain`
        """
        self._domain = domain

    @property
    def password_expires_at(self):
        """Gets the password_expires_at of this AgencyAssumedbyUser.

        被委托方B中IAM用户的密码过期时间（UTC时间），“”表示密码不过期。

        :return: The password_expires_at of this AgencyAssumedbyUser.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        """Sets the password_expires_at of this AgencyAssumedbyUser.

        被委托方B中IAM用户的密码过期时间（UTC时间），“”表示密码不过期。

        :param password_expires_at: The password_expires_at of this AgencyAssumedbyUser.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

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
        if not isinstance(other, AgencyAssumedbyUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
