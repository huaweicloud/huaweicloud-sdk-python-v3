# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvalidVpnUser:

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
        'description': 'str',
        'user_group_name': 'str',
        'cause': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'user_group_name': 'user_group_name',
        'cause': 'cause'
    }

    def __init__(self, name=None, description=None, user_group_name=None, cause=None):
        """InvalidVpnUser

        The model defined in huaweicloud sdk

        :param name: 用户名
        :type name: str
        :param description: 用户描述，0-64字符，中文、英文、数字包含下划线
        :type description: str
        :param user_group_name: 所属用户组名称
        :type user_group_name: str
        :param cause: 失败原因
        :type cause: str
        """
        
        

        self._name = None
        self._description = None
        self._user_group_name = None
        self._cause = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if cause is not None:
            self.cause = cause

    @property
    def name(self):
        """Gets the name of this InvalidVpnUser.

        用户名

        :return: The name of this InvalidVpnUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvalidVpnUser.

        用户名

        :param name: The name of this InvalidVpnUser.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this InvalidVpnUser.

        用户描述，0-64字符，中文、英文、数字包含下划线

        :return: The description of this InvalidVpnUser.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvalidVpnUser.

        用户描述，0-64字符，中文、英文、数字包含下划线

        :param description: The description of this InvalidVpnUser.
        :type description: str
        """
        self._description = description

    @property
    def user_group_name(self):
        """Gets the user_group_name of this InvalidVpnUser.

        所属用户组名称

        :return: The user_group_name of this InvalidVpnUser.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this InvalidVpnUser.

        所属用户组名称

        :param user_group_name: The user_group_name of this InvalidVpnUser.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def cause(self):
        """Gets the cause of this InvalidVpnUser.

        失败原因

        :return: The cause of this InvalidVpnUser.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this InvalidVpnUser.

        失败原因

        :param cause: The cause of this InvalidVpnUser.
        :type cause: str
        """
        self._cause = cause

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
        if not isinstance(other, InvalidVpnUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
