# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisResetDbUserPasswordRequestBody:

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
        'password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password'
    }

    def __init__(self, name=None, password=None):
        r"""RedisResetDbUserPasswordRequestBody

        The model defined in huaweicloud sdk

        :param name: 账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。
        :type name: str
        :param password: 需重置的密码。  - 密码长度为8~32位。  - 密码需包含大写字母、小写字母、数字和特殊字符中的至少三种，支持的特殊字符为!@#$%^&amp;*()_+-&#x3D; 。
        :type password: str
        """
        
        

        self._name = None
        self._password = None
        self.discriminator = None

        self.name = name
        self.password = password

    @property
    def name(self):
        r"""Gets the name of this RedisResetDbUserPasswordRequestBody.

        账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。

        :return: The name of this RedisResetDbUserPasswordRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RedisResetDbUserPasswordRequestBody.

        账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。

        :param name: The name of this RedisResetDbUserPasswordRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        r"""Gets the password of this RedisResetDbUserPasswordRequestBody.

        需重置的密码。  - 密码长度为8~32位。  - 密码需包含大写字母、小写字母、数字和特殊字符中的至少三种，支持的特殊字符为!@#$%^&*()_+-= 。

        :return: The password of this RedisResetDbUserPasswordRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RedisResetDbUserPasswordRequestBody.

        需重置的密码。  - 密码长度为8~32位。  - 密码需包含大写字母、小写字母、数字和特殊字符中的至少三种，支持的特殊字符为!@#$%^&*()_+-= 。

        :param password: The password of this RedisResetDbUserPasswordRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, RedisResetDbUserPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
