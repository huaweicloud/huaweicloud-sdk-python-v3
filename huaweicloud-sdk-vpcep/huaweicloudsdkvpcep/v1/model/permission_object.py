# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionObject:

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
        'permission': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, permission=None, created_at=None):
        """PermissionObject

        The model defined in huaweicloud sdk

        :param id: permission的ID，唯一标识。
        :type id: str
        :param permission: permission列表。 权限格式为“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。
        :type permission: str
        :param created_at: 白名单的添加时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ
        :type created_at: str
        """
        
        

        self._id = None
        self._permission = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this PermissionObject.

        permission的ID，唯一标识。

        :return: The id of this PermissionObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PermissionObject.

        permission的ID，唯一标识。

        :param id: The id of this PermissionObject.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        """Gets the permission of this PermissionObject.

        permission列表。 权限格式为“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。

        :return: The permission of this PermissionObject.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this PermissionObject.

        permission列表。 权限格式为“iam:domain::6e9dfd51d1124e8d8498dce894923a0d”或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。

        :param permission: The permission of this PermissionObject.
        :type permission: str
        """
        self._permission = permission

    @property
    def created_at(self):
        """Gets the created_at of this PermissionObject.

        白名单的添加时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :return: The created_at of this PermissionObject.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PermissionObject.

        白名单的添加时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :param created_at: The created_at of this PermissionObject.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, PermissionObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
