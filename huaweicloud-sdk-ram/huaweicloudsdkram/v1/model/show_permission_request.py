# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPermissionRequest:

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
        'permission_version': 'int'
    }

    attribute_map = {
        'permission_id': 'permission_id',
        'permission_version': 'permission_version'
    }

    def __init__(self, permission_id=None, permission_version=None):
        """ShowPermissionRequest

        The model defined in huaweicloud sdk

        :param permission_id: 共享资源权限的ID。
        :type permission_id: str
        :param permission_version: 资源权限版本。
        :type permission_version: int
        """
        
        

        self._permission_id = None
        self._permission_version = None
        self.discriminator = None

        self.permission_id = permission_id
        if permission_version is not None:
            self.permission_version = permission_version

    @property
    def permission_id(self):
        """Gets the permission_id of this ShowPermissionRequest.

        共享资源权限的ID。

        :return: The permission_id of this ShowPermissionRequest.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        """Sets the permission_id of this ShowPermissionRequest.

        共享资源权限的ID。

        :param permission_id: The permission_id of this ShowPermissionRequest.
        :type permission_id: str
        """
        self._permission_id = permission_id

    @property
    def permission_version(self):
        """Gets the permission_version of this ShowPermissionRequest.

        资源权限版本。

        :return: The permission_version of this ShowPermissionRequest.
        :rtype: int
        """
        return self._permission_version

    @permission_version.setter
    def permission_version(self, permission_version):
        """Sets the permission_version of this ShowPermissionRequest.

        资源权限版本。

        :param permission_version: The permission_version of this ShowPermissionRequest.
        :type permission_version: int
        """
        self._permission_version = permission_version

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
        if not isinstance(other, ShowPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
