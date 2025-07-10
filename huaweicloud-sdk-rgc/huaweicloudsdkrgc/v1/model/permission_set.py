# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set_id': 'str',
        'permission_set_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'permission_set_name': 'permission_set_name',
        'description': 'description'
    }

    def __init__(self, permission_set_id=None, permission_set_name=None, description=None):
        r"""PermissionSet

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集ID。
        :type permission_set_id: str
        :param permission_set_name: 权限集名称。
        :type permission_set_name: str
        :param description: 权限集描述。
        :type description: str
        """
        
        

        self._permission_set_id = None
        self._permission_set_name = None
        self._description = None
        self.discriminator = None

        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if permission_set_name is not None:
            self.permission_set_name = permission_set_name
        if description is not None:
            self.description = description

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this PermissionSet.

        权限集ID。

        :return: The permission_set_id of this PermissionSet.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this PermissionSet.

        权限集ID。

        :param permission_set_id: The permission_set_id of this PermissionSet.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def permission_set_name(self):
        r"""Gets the permission_set_name of this PermissionSet.

        权限集名称。

        :return: The permission_set_name of this PermissionSet.
        :rtype: str
        """
        return self._permission_set_name

    @permission_set_name.setter
    def permission_set_name(self, permission_set_name):
        r"""Sets the permission_set_name of this PermissionSet.

        权限集名称。

        :param permission_set_name: The permission_set_name of this PermissionSet.
        :type permission_set_name: str
        """
        self._permission_set_name = permission_set_name

    @property
    def description(self):
        r"""Gets the description of this PermissionSet.

        权限集描述。

        :return: The description of this PermissionSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PermissionSet.

        权限集描述。

        :param description: The description of this PermissionSet.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, PermissionSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
