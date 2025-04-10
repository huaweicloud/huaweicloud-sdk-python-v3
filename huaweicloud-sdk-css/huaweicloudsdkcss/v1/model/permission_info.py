# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionInfo:

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
        'permission_type': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'permission_type': 'permission_type',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, permission=None, permission_type=None, created_at=None):
        r"""PermissionInfo

        The model defined in huaweicloud sdk

        :param id: permission的ID。
        :type id: str
        :param permission: permission详情。
        :type permission: str
        :param permission_type: 终端节点服务白名单类型。
        :type permission_type: str
        :param created_at: 白名单的添加时间。
        :type created_at: str
        """
        
        

        self._id = None
        self._permission = None
        self._permission_type = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if permission_type is not None:
            self.permission_type = permission_type
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this PermissionInfo.

        permission的ID。

        :return: The id of this PermissionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PermissionInfo.

        permission的ID。

        :param id: The id of this PermissionInfo.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        r"""Gets the permission of this PermissionInfo.

        permission详情。

        :return: The permission of this PermissionInfo.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this PermissionInfo.

        permission详情。

        :param permission: The permission of this PermissionInfo.
        :type permission: str
        """
        self._permission = permission

    @property
    def permission_type(self):
        r"""Gets the permission_type of this PermissionInfo.

        终端节点服务白名单类型。

        :return: The permission_type of this PermissionInfo.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this PermissionInfo.

        终端节点服务白名单类型。

        :param permission_type: The permission_type of this PermissionInfo.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def created_at(self):
        r"""Gets the created_at of this PermissionInfo.

        白名单的添加时间。

        :return: The created_at of this PermissionInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PermissionInfo.

        白名单的添加时间。

        :param created_at: The created_at of this PermissionInfo.
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
        if not isinstance(other, PermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
