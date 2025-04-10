# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_type': 'str',
        'permission_types': 'list[str]',
        'permission_actions': 'list[PermissionActions]'
    }

    attribute_map = {
        'datasource_type': 'datasource_type',
        'permission_types': 'permission_types',
        'permission_actions': 'permission_actions'
    }

    def __init__(self, datasource_type=None, permission_types=None, permission_actions=None):
        r"""PermissionConfiguration

        The model defined in huaweicloud sdk

        :param datasource_type: 数据源类型
        :type datasource_type: str
        :param permission_types: 数据源操作权限类型
        :type permission_types: list[str]
        :param permission_actions: 数据源支持的权限操作列表
        :type permission_actions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        
        

        self._datasource_type = None
        self._permission_types = None
        self._permission_actions = None
        self.discriminator = None

        if datasource_type is not None:
            self.datasource_type = datasource_type
        if permission_types is not None:
            self.permission_types = permission_types
        if permission_actions is not None:
            self.permission_actions = permission_actions

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this PermissionConfiguration.

        数据源类型

        :return: The datasource_type of this PermissionConfiguration.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this PermissionConfiguration.

        数据源类型

        :param datasource_type: The datasource_type of this PermissionConfiguration.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def permission_types(self):
        r"""Gets the permission_types of this PermissionConfiguration.

        数据源操作权限类型

        :return: The permission_types of this PermissionConfiguration.
        :rtype: list[str]
        """
        return self._permission_types

    @permission_types.setter
    def permission_types(self, permission_types):
        r"""Sets the permission_types of this PermissionConfiguration.

        数据源操作权限类型

        :param permission_types: The permission_types of this PermissionConfiguration.
        :type permission_types: list[str]
        """
        self._permission_types = permission_types

    @property
    def permission_actions(self):
        r"""Gets the permission_actions of this PermissionConfiguration.

        数据源支持的权限操作列表

        :return: The permission_actions of this PermissionConfiguration.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        r"""Sets the permission_actions of this PermissionConfiguration.

        数据源支持的权限操作列表

        :param permission_actions: The permission_actions of this PermissionConfiguration.
        :type permission_actions: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionActions`]
        """
        self._permission_actions = permission_actions

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
        if not isinstance(other, PermissionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
