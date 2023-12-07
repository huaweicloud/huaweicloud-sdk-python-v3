# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPermissionSetRequest:

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
        'workspace': 'str',
        'body': 'PermissionSetCreateDTO'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'workspace': 'workspace',
        'body': 'body'
    }

    def __init__(self, permission_set_id=None, workspace=None, body=None):
        """UpdateSecurityPermissionSetRequest

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param workspace: workspace 信息
        :type workspace: str
        :param body: Body of the UpdateSecurityPermissionSetRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetCreateDTO`
        """
        
        

        self._permission_set_id = None
        self._workspace = None
        self._body = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.workspace = workspace
        if body is not None:
            self.body = body

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this UpdateSecurityPermissionSetRequest.

        权限集id

        :return: The permission_set_id of this UpdateSecurityPermissionSetRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this UpdateSecurityPermissionSetRequest.

        权限集id

        :param permission_set_id: The permission_set_id of this UpdateSecurityPermissionSetRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def workspace(self):
        """Gets the workspace of this UpdateSecurityPermissionSetRequest.

        workspace 信息

        :return: The workspace of this UpdateSecurityPermissionSetRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this UpdateSecurityPermissionSetRequest.

        workspace 信息

        :param workspace: The workspace of this UpdateSecurityPermissionSetRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def body(self):
        """Gets the body of this UpdateSecurityPermissionSetRequest.

        :return: The body of this UpdateSecurityPermissionSetRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetCreateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSecurityPermissionSetRequest.

        :param body: The body of this UpdateSecurityPermissionSetRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetCreateDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateSecurityPermissionSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
