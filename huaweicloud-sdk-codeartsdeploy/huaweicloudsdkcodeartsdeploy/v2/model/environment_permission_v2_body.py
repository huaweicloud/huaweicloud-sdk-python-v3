# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentPermissionV2Body:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'permission_name': 'str',
        'permission_value': 'bool'
    }

    attribute_map = {
        'role_id': 'role_id',
        'permission_name': 'permission_name',
        'permission_value': 'permission_value'
    }

    def __init__(self, role_id=None, permission_name=None, permission_value=None):
        r"""EnvironmentPermissionV2Body

        The model defined in huaweicloud sdk

        :param role_id: 角色id
        :type role_id: str
        :param permission_name: 权限名称，can_view：查看权限；can_edit：编辑权限；can_delete：删除权限；can_deploy：部署权限；can_manage：权限管理权限
        :type permission_name: str
        :param permission_value: true 有权限，false 无权限
        :type permission_value: bool
        """
        
        

        self._role_id = None
        self._permission_name = None
        self._permission_value = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if permission_name is not None:
            self.permission_name = permission_name
        if permission_value is not None:
            self.permission_value = permission_value

    @property
    def role_id(self):
        r"""Gets the role_id of this EnvironmentPermissionV2Body.

        角色id

        :return: The role_id of this EnvironmentPermissionV2Body.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this EnvironmentPermissionV2Body.

        角色id

        :param role_id: The role_id of this EnvironmentPermissionV2Body.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def permission_name(self):
        r"""Gets the permission_name of this EnvironmentPermissionV2Body.

        权限名称，can_view：查看权限；can_edit：编辑权限；can_delete：删除权限；can_deploy：部署权限；can_manage：权限管理权限

        :return: The permission_name of this EnvironmentPermissionV2Body.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        r"""Sets the permission_name of this EnvironmentPermissionV2Body.

        权限名称，can_view：查看权限；can_edit：编辑权限；can_delete：删除权限；can_deploy：部署权限；can_manage：权限管理权限

        :param permission_name: The permission_name of this EnvironmentPermissionV2Body.
        :type permission_name: str
        """
        self._permission_name = permission_name

    @property
    def permission_value(self):
        r"""Gets the permission_value of this EnvironmentPermissionV2Body.

        true 有权限，false 无权限

        :return: The permission_value of this EnvironmentPermissionV2Body.
        :rtype: bool
        """
        return self._permission_value

    @permission_value.setter
    def permission_value(self, permission_value):
        r"""Sets the permission_value of this EnvironmentPermissionV2Body.

        true 有权限，false 无权限

        :param permission_value: The permission_value of this EnvironmentPermissionV2Body.
        :type permission_value: bool
        """
        self._permission_value = permission_value

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
        if not isinstance(other, EnvironmentPermissionV2Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
