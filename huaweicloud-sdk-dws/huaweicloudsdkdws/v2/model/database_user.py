# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUser:

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
        'login': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'login': 'login'
    }

    def __init__(self, name=None, login=None):
        """DatabaseUser

        The model defined in huaweicloud sdk

        :param name: 用户名
        :type name: str
        :param login: 是否可以登陆
        :type login: bool
        """
        
        

        self._name = None
        self._login = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if login is not None:
            self.login = login

    @property
    def name(self):
        """Gets the name of this DatabaseUser.

        用户名

        :return: The name of this DatabaseUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseUser.

        用户名

        :param name: The name of this DatabaseUser.
        :type name: str
        """
        self._name = name

    @property
    def login(self):
        """Gets the login of this DatabaseUser.

        是否可以登陆

        :return: The login of this DatabaseUser.
        :rtype: bool
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this DatabaseUser.

        是否可以登陆

        :param login: The login of this DatabaseUser.
        :type login: bool
        """
        self._login = login

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
        if not isinstance(other, DatabaseUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
