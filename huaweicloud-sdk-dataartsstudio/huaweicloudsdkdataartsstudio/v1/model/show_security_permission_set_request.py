# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityPermissionSetRequest:

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
        'workspace': 'str'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'workspace': 'workspace'
    }

    def __init__(self, permission_set_id=None, workspace=None):
        r"""ShowSecurityPermissionSetRequest

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        """
        
        

        self._permission_set_id = None
        self._workspace = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.workspace = workspace

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this ShowSecurityPermissionSetRequest.

        权限集id

        :return: The permission_set_id of this ShowSecurityPermissionSetRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this ShowSecurityPermissionSetRequest.

        权限集id

        :param permission_set_id: The permission_set_id of this ShowSecurityPermissionSetRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowSecurityPermissionSetRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowSecurityPermissionSetRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowSecurityPermissionSetRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowSecurityPermissionSetRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ShowSecurityPermissionSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
