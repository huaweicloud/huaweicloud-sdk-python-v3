# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetDatabasePassword:

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
        'host': 'str',
        'password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'password': 'password'
    }

    def __init__(self, name=None, host=None, password=None):
        """ResetDatabasePassword

        The model defined in huaweicloud sdk

        :param name: 数据库用户名。
        :type name: str
        :param host: 主机地址。
        :type host: str
        :param password: 数据库用户密码，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_&#x3D;+?,()&amp;组成，长度8~32个字符。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险
        :type password: str
        """
        
        

        self._name = None
        self._host = None
        self._password = None
        self.discriminator = None

        self.name = name
        if host is not None:
            self.host = host
        self.password = password

    @property
    def name(self):
        """Gets the name of this ResetDatabasePassword.

        数据库用户名。

        :return: The name of this ResetDatabasePassword.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResetDatabasePassword.

        数据库用户名。

        :param name: The name of this ResetDatabasePassword.
        :type name: str
        """
        self._name = name

    @property
    def host(self):
        """Gets the host of this ResetDatabasePassword.

        主机地址。

        :return: The host of this ResetDatabasePassword.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ResetDatabasePassword.

        主机地址。

        :param host: The host of this ResetDatabasePassword.
        :type host: str
        """
        self._host = host

    @property
    def password(self):
        """Gets the password of this ResetDatabasePassword.

        数据库用户密码，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险

        :return: The password of this ResetDatabasePassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ResetDatabasePassword.

        数据库用户密码，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险

        :param password: The password of this ResetDatabasePassword.
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
        if not isinstance(other, ResetDatabasePassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
