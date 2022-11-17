# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceUsersEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'role': 'str',
        'default_app': 'bool',
        'created_time': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'role': 'role',
        'default_app': 'default_app',
        'created_time': 'created_time'
    }

    def __init__(self, user_name=None, role=None, default_app=None, created_time=None):
        """ShowInstanceUsersEntity

        The model defined in huaweicloud sdk

        :param user_name: 用户名称。
        :type user_name: str
        :param role: 用户角色。
        :type role: str
        :param default_app: 是否为默认应用。
        :type default_app: bool
        :param created_time: 创建时间。
        :type created_time: int
        """
        
        

        self._user_name = None
        self._role = None
        self._default_app = None
        self._created_time = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if role is not None:
            self.role = role
        if default_app is not None:
            self.default_app = default_app
        if created_time is not None:
            self.created_time = created_time

    @property
    def user_name(self):
        """Gets the user_name of this ShowInstanceUsersEntity.

        用户名称。

        :return: The user_name of this ShowInstanceUsersEntity.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowInstanceUsersEntity.

        用户名称。

        :param user_name: The user_name of this ShowInstanceUsersEntity.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """Gets the role of this ShowInstanceUsersEntity.

        用户角色。

        :return: The role of this ShowInstanceUsersEntity.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ShowInstanceUsersEntity.

        用户角色。

        :param role: The role of this ShowInstanceUsersEntity.
        :type role: str
        """
        self._role = role

    @property
    def default_app(self):
        """Gets the default_app of this ShowInstanceUsersEntity.

        是否为默认应用。

        :return: The default_app of this ShowInstanceUsersEntity.
        :rtype: bool
        """
        return self._default_app

    @default_app.setter
    def default_app(self, default_app):
        """Sets the default_app of this ShowInstanceUsersEntity.

        是否为默认应用。

        :param default_app: The default_app of this ShowInstanceUsersEntity.
        :type default_app: bool
        """
        self._default_app = default_app

    @property
    def created_time(self):
        """Gets the created_time of this ShowInstanceUsersEntity.

        创建时间。

        :return: The created_time of this ShowInstanceUsersEntity.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowInstanceUsersEntity.

        创建时间。

        :param created_time: The created_time of this ShowInstanceUsersEntity.
        :type created_time: int
        """
        self._created_time = created_time

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
        if not isinstance(other, ShowInstanceUsersEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
