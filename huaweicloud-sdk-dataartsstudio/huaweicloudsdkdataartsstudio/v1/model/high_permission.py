# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HighPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'DiagnoseResult',
        'workspace_admin': 'str',
        'security_administrator': 'str'
    }

    attribute_map = {
        'result': 'result',
        'workspace_admin': 'workspace_admin',
        'security_administrator': 'security_administrator'
    }

    def __init__(self, result=None, workspace_admin=None, security_administrator=None):
        r"""HighPermission

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        :param workspace_admin: 空间管理员用户列表。
        :type workspace_admin: str
        :param security_administrator: 安全管理员用户列表。
        :type security_administrator: str
        """
        
        

        self._result = None
        self._workspace_admin = None
        self._security_administrator = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if workspace_admin is not None:
            self.workspace_admin = workspace_admin
        if security_administrator is not None:
            self.security_administrator = security_administrator

    @property
    def result(self):
        r"""Gets the result of this HighPermission.

        :return: The result of this HighPermission.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this HighPermission.

        :param result: The result of this HighPermission.
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        self._result = result

    @property
    def workspace_admin(self):
        r"""Gets the workspace_admin of this HighPermission.

        空间管理员用户列表。

        :return: The workspace_admin of this HighPermission.
        :rtype: str
        """
        return self._workspace_admin

    @workspace_admin.setter
    def workspace_admin(self, workspace_admin):
        r"""Sets the workspace_admin of this HighPermission.

        空间管理员用户列表。

        :param workspace_admin: The workspace_admin of this HighPermission.
        :type workspace_admin: str
        """
        self._workspace_admin = workspace_admin

    @property
    def security_administrator(self):
        r"""Gets the security_administrator of this HighPermission.

        安全管理员用户列表。

        :return: The security_administrator of this HighPermission.
        :rtype: str
        """
        return self._security_administrator

    @security_administrator.setter
    def security_administrator(self, security_administrator):
        r"""Sets the security_administrator of this HighPermission.

        安全管理员用户列表。

        :param security_administrator: The security_administrator of this HighPermission.
        :type security_administrator: str
        """
        self._security_administrator = security_administrator

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
        if not isinstance(other, HighPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
