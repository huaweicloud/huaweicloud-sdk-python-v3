# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionGroupDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'can_view': 'bool',
        'can_edit': 'bool',
        'can_delete': 'bool',
        'can_add_host': 'bool',
        'can_manage': 'bool'
    }

    attribute_map = {
        'can_view': 'can_view',
        'can_edit': 'can_edit',
        'can_delete': 'can_delete',
        'can_add_host': 'can_add_host',
        'can_manage': 'can_manage'
    }

    def __init__(self, can_view=None, can_edit=None, can_delete=None, can_add_host=None, can_manage=None):
        """PermissionGroupDetail

        The model defined in huaweicloud sdk

        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_edit: 是否有编辑权限
        :type can_edit: bool
        :param can_delete: 是否有删除权限
        :type can_delete: bool
        :param can_add_host: 是否有添加主机权限
        :type can_add_host: bool
        :param can_manage: 是否有管理权限
        :type can_manage: bool
        """
        
        

        self._can_view = None
        self._can_edit = None
        self._can_delete = None
        self._can_add_host = None
        self._can_manage = None
        self.discriminator = None

        if can_view is not None:
            self.can_view = can_view
        if can_edit is not None:
            self.can_edit = can_edit
        if can_delete is not None:
            self.can_delete = can_delete
        if can_add_host is not None:
            self.can_add_host = can_add_host
        if can_manage is not None:
            self.can_manage = can_manage

    @property
    def can_view(self):
        """Gets the can_view of this PermissionGroupDetail.

        是否有查看权限

        :return: The can_view of this PermissionGroupDetail.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this PermissionGroupDetail.

        是否有查看权限

        :param can_view: The can_view of this PermissionGroupDetail.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_edit(self):
        """Gets the can_edit of this PermissionGroupDetail.

        是否有编辑权限

        :return: The can_edit of this PermissionGroupDetail.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this PermissionGroupDetail.

        是否有编辑权限

        :param can_edit: The can_edit of this PermissionGroupDetail.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_delete(self):
        """Gets the can_delete of this PermissionGroupDetail.

        是否有删除权限

        :return: The can_delete of this PermissionGroupDetail.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this PermissionGroupDetail.

        是否有删除权限

        :param can_delete: The can_delete of this PermissionGroupDetail.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_add_host(self):
        """Gets the can_add_host of this PermissionGroupDetail.

        是否有添加主机权限

        :return: The can_add_host of this PermissionGroupDetail.
        :rtype: bool
        """
        return self._can_add_host

    @can_add_host.setter
    def can_add_host(self, can_add_host):
        """Sets the can_add_host of this PermissionGroupDetail.

        是否有添加主机权限

        :param can_add_host: The can_add_host of this PermissionGroupDetail.
        :type can_add_host: bool
        """
        self._can_add_host = can_add_host

    @property
    def can_manage(self):
        """Gets the can_manage of this PermissionGroupDetail.

        是否有管理权限

        :return: The can_manage of this PermissionGroupDetail.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        """Sets the can_manage of this PermissionGroupDetail.

        是否有管理权限

        :param can_manage: The can_manage of this PermissionGroupDetail.
        :type can_manage: bool
        """
        self._can_manage = can_manage

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
        if not isinstance(other, PermissionGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
