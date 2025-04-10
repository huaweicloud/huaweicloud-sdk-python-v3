# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatedPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_id': 'str',
        'permission_name': 'str',
        'resource_type': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'permission_id': 'permission_id',
        'permission_name': 'permission_name',
        'resource_type': 'resource_type',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, permission_id=None, permission_name=None, resource_type=None, status=None, created_at=None, updated_at=None):
        r"""AssociatedPermission

        The model defined in huaweicloud sdk

        :param permission_id: 权限的ID。
        :type permission_id: str
        :param permission_name: 共享资源权限的名称。
        :type permission_name: str
        :param resource_type: 权限适用的资源类型。
        :type resource_type: str
        :param status: 权限的当前状态。
        :type status: str
        :param created_at: 创建权限的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新权限的时间。
        :type updated_at: datetime
        """
        
        

        self._permission_id = None
        self._permission_name = None
        self._resource_type = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if permission_id is not None:
            self.permission_id = permission_id
        if permission_name is not None:
            self.permission_name = permission_name
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def permission_id(self):
        r"""Gets the permission_id of this AssociatedPermission.

        权限的ID。

        :return: The permission_id of this AssociatedPermission.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        r"""Sets the permission_id of this AssociatedPermission.

        权限的ID。

        :param permission_id: The permission_id of this AssociatedPermission.
        :type permission_id: str
        """
        self._permission_id = permission_id

    @property
    def permission_name(self):
        r"""Gets the permission_name of this AssociatedPermission.

        共享资源权限的名称。

        :return: The permission_name of this AssociatedPermission.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        r"""Sets the permission_name of this AssociatedPermission.

        共享资源权限的名称。

        :param permission_name: The permission_name of this AssociatedPermission.
        :type permission_name: str
        """
        self._permission_name = permission_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AssociatedPermission.

        权限适用的资源类型。

        :return: The resource_type of this AssociatedPermission.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AssociatedPermission.

        权限适用的资源类型。

        :param resource_type: The resource_type of this AssociatedPermission.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def status(self):
        r"""Gets the status of this AssociatedPermission.

        权限的当前状态。

        :return: The status of this AssociatedPermission.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssociatedPermission.

        权限的当前状态。

        :param status: The status of this AssociatedPermission.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this AssociatedPermission.

        创建权限的时间。

        :return: The created_at of this AssociatedPermission.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AssociatedPermission.

        创建权限的时间。

        :param created_at: The created_at of this AssociatedPermission.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AssociatedPermission.

        最后一次更新权限的时间。

        :return: The updated_at of this AssociatedPermission.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AssociatedPermission.

        最后一次更新权限的时间。

        :param updated_at: The updated_at of this AssociatedPermission.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, AssociatedPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
