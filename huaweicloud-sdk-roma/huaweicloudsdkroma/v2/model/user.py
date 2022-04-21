# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class User:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'roles': 'roles'
    }

    def __init__(self, id=None, roles=None):
        """User

        The model defined in huaweicloud sdk

        :param id: 用户ID
        :type id: str
        :param roles: 应用权限角色 - read：应用下资源只读权限，至少要存在此权限，包括API调试 - access：应用下资源的访问管理权限 - delete：应用下资源的删除权限 - modify：应用下资源的修改权限，包括API发布、下线 - admin：应用和应用下资源的权限 - 仅提供admin时，会自动应用其它所有权限 - 未提供read时会自动应用read权限
        :type roles: list[str]
        """
        
        

        self._id = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        """Gets the id of this User.

        用户ID

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        用户ID

        :param id: The id of this User.
        :type id: str
        """
        self._id = id

    @property
    def roles(self):
        """Gets the roles of this User.

        应用权限角色 - read：应用下资源只读权限，至少要存在此权限，包括API调试 - access：应用下资源的访问管理权限 - delete：应用下资源的删除权限 - modify：应用下资源的修改权限，包括API发布、下线 - admin：应用和应用下资源的权限 - 仅提供admin时，会自动应用其它所有权限 - 未提供read时会自动应用read权限

        :return: The roles of this User.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

        应用权限角色 - read：应用下资源只读权限，至少要存在此权限，包括API调试 - access：应用下资源的访问管理权限 - delete：应用下资源的删除权限 - modify：应用下资源的修改权限，包括API发布、下线 - admin：应用和应用下资源的权限 - 仅提供admin时，会自动应用其它所有权限 - 未提供read时会自动应用read权限

        :param roles: The roles of this User.
        :type roles: list[str]
        """
        self._roles = roles

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
