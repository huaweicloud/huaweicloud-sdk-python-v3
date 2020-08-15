# coding: utf-8

import pprint
import re

import six





class Role:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'c_role': 'str',
        'id': 'str',
        'role': 'str',
        'role_actionses': 'list[RoleAction]'
    }

    attribute_map = {
        'c_role': 'c_role',
        'id': 'id',
        'role': 'role',
        'role_actionses': 'role_actionses'
    }

    def __init__(self, c_role=None, id=None, role=None, role_actionses=None):
        """Role - a model defined in huaweicloud sdk"""
        
        

        self._c_role = None
        self._id = None
        self._role = None
        self._role_actionses = None
        self.discriminator = None

        if c_role is not None:
            self.c_role = c_role
        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if role_actionses is not None:
            self.role_actionses = role_actionses

    @property
    def c_role(self):
        """Gets the c_role of this Role.

        子角色

        :return: The c_role of this Role.
        :rtype: str
        """
        return self._c_role

    @c_role.setter
    def c_role(self, c_role):
        """Sets the c_role of this Role.

        子角色

        :param c_role: The c_role of this Role.
        :type: str
        """
        self._c_role = c_role

    @property
    def id(self):
        """Gets the id of this Role.

        id

        :return: The id of this Role.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

        id

        :param id: The id of this Role.
        :type: str
        """
        self._id = id

    @property
    def role(self):
        """Gets the role of this Role.

        角色

        :return: The role of this Role.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Role.

        角色

        :param role: The role of this Role.
        :type: str
        """
        self._role = role

    @property
    def role_actionses(self):
        """Gets the role_actionses of this Role.

        角色执行操作列表

        :return: The role_actionses of this Role.
        :rtype: list[RoleAction]
        """
        return self._role_actionses

    @role_actionses.setter
    def role_actionses(self, role_actionses):
        """Sets the role_actionses of this Role.

        角色执行操作列表

        :param role_actionses: The role_actionses of this Role.
        :type: list[RoleAction]
        """
        self._role_actionses = role_actionses

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
