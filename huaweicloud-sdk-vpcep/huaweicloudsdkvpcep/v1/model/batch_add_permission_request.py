# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddPermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[EpsAddPermissionRequest]',
        'permission_type': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'permission_type': 'permission_type'
    }

    def __init__(self, permissions=None, permission_type=None):
        """BatchAddPermissionRequest

        The model defined in huaweicloud sdk

        :param permissions: 终端节点服务白名单列表
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.EpsAddPermissionRequest`]
        :param permission_type: 终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。
        :type permission_type: str
        """
        
        

        self._permissions = None
        self._permission_type = None
        self.discriminator = None

        self.permissions = permissions
        if permission_type is not None:
            self.permission_type = permission_type

    @property
    def permissions(self):
        """Gets the permissions of this BatchAddPermissionRequest.

        终端节点服务白名单列表

        :return: The permissions of this BatchAddPermissionRequest.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.EpsAddPermissionRequest`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this BatchAddPermissionRequest.

        终端节点服务白名单列表

        :param permissions: The permissions of this BatchAddPermissionRequest.
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.EpsAddPermissionRequest`]
        """
        self._permissions = permissions

    @property
    def permission_type(self):
        """Gets the permission_type of this BatchAddPermissionRequest.

        终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。

        :return: The permission_type of this BatchAddPermissionRequest.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this BatchAddPermissionRequest.

        终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。

        :param permission_type: The permission_type of this BatchAddPermissionRequest.
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
        if not isinstance(other, BatchAddPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
