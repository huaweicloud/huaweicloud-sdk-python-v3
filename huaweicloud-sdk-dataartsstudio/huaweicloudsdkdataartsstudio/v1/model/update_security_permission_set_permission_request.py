# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPermissionSetPermissionRequest:

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
        'permission_id': 'str',
        'workspace': 'str',
        'body': 'PermissionSetPermissionUpdateDTO'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'permission_id': 'permission_id',
        'workspace': 'workspace',
        'body': 'body'
    }

    def __init__(self, permission_set_id=None, permission_id=None, workspace=None, body=None):
        r"""UpdateSecurityPermissionSetPermissionRequest

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param permission_id: 权限id
        :type permission_id: str
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param body: Body of the UpdateSecurityPermissionSetPermissionRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetPermissionUpdateDTO`
        """
        
        

        self._permission_set_id = None
        self._permission_id = None
        self._workspace = None
        self._body = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.permission_id = permission_id
        self.workspace = workspace
        if body is not None:
            self.body = body

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this UpdateSecurityPermissionSetPermissionRequest.

        权限集id

        :return: The permission_set_id of this UpdateSecurityPermissionSetPermissionRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this UpdateSecurityPermissionSetPermissionRequest.

        权限集id

        :param permission_set_id: The permission_set_id of this UpdateSecurityPermissionSetPermissionRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def permission_id(self):
        r"""Gets the permission_id of this UpdateSecurityPermissionSetPermissionRequest.

        权限id

        :return: The permission_id of this UpdateSecurityPermissionSetPermissionRequest.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        r"""Sets the permission_id of this UpdateSecurityPermissionSetPermissionRequest.

        权限id

        :param permission_id: The permission_id of this UpdateSecurityPermissionSetPermissionRequest.
        :type permission_id: str
        """
        self._permission_id = permission_id

    @property
    def workspace(self):
        r"""Gets the workspace of this UpdateSecurityPermissionSetPermissionRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this UpdateSecurityPermissionSetPermissionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this UpdateSecurityPermissionSetPermissionRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this UpdateSecurityPermissionSetPermissionRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def body(self):
        r"""Gets the body of this UpdateSecurityPermissionSetPermissionRequest.

        :return: The body of this UpdateSecurityPermissionSetPermissionRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetPermissionUpdateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSecurityPermissionSetPermissionRequest.

        :param body: The body of this UpdateSecurityPermissionSetPermissionRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.PermissionSetPermissionUpdateDTO`
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
        if not isinstance(other, UpdateSecurityPermissionSetPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
