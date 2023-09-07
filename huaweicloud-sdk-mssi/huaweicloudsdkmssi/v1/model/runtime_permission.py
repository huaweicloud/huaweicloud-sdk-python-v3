# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimePermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'action_list': 'list[str]',
        'name': 'str',
        'permission_name': 'str',
        'permission_type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'action_list': 'action_list',
        'name': 'name',
        'permission_name': 'permission_name',
        'permission_type': 'permission_type'
    }

    def __init__(self, action=None, action_list=None, name=None, permission_name=None, permission_type=None):
        """RuntimePermission

        The model defined in huaweicloud sdk

        :param action: 动作列表
        :type action: str
        :param action_list: 动作列表
        :type action_list: list[str]
        :param name: 权限名称
        :type name: str
        :param permission_name: 权限名称
        :type permission_name: str
        :param permission_type: 权限类型
        :type permission_type: str
        """
        
        

        self._action = None
        self._action_list = None
        self._name = None
        self._permission_name = None
        self._permission_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_list is not None:
            self.action_list = action_list
        if name is not None:
            self.name = name
        if permission_name is not None:
            self.permission_name = permission_name
        if permission_type is not None:
            self.permission_type = permission_type

    @property
    def action(self):
        """Gets the action of this RuntimePermission.

        动作列表

        :return: The action of this RuntimePermission.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RuntimePermission.

        动作列表

        :param action: The action of this RuntimePermission.
        :type action: str
        """
        self._action = action

    @property
    def action_list(self):
        """Gets the action_list of this RuntimePermission.

        动作列表

        :return: The action_list of this RuntimePermission.
        :rtype: list[str]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """Sets the action_list of this RuntimePermission.

        动作列表

        :param action_list: The action_list of this RuntimePermission.
        :type action_list: list[str]
        """
        self._action_list = action_list

    @property
    def name(self):
        """Gets the name of this RuntimePermission.

        权限名称

        :return: The name of this RuntimePermission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuntimePermission.

        权限名称

        :param name: The name of this RuntimePermission.
        :type name: str
        """
        self._name = name

    @property
    def permission_name(self):
        """Gets the permission_name of this RuntimePermission.

        权限名称

        :return: The permission_name of this RuntimePermission.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        """Sets the permission_name of this RuntimePermission.

        权限名称

        :param permission_name: The permission_name of this RuntimePermission.
        :type permission_name: str
        """
        self._permission_name = permission_name

    @property
    def permission_type(self):
        """Gets the permission_type of this RuntimePermission.

        权限类型

        :return: The permission_type of this RuntimePermission.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this RuntimePermission.

        权限类型

        :param permission_type: The permission_type of this RuntimePermission.
        :type permission_type: str
        """
        self._permission_type = permission_type

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
        if not isinstance(other, RuntimePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
