# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RevokeRoleFromUserOnEnterpriseProjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'user_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'user_id': 'user_id',
        'role_id': 'role_id'
    }

    def __init__(self, enterprise_project_id=None, user_id=None, role_id=None):
        """RevokeRoleFromUserOnEnterpriseProjectRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param user_id: 用户ID。
        :type user_id: str
        :param role_id: 权限ID。
        :type role_id: str
        """
        
        

        self._enterprise_project_id = None
        self._user_id = None
        self._role_id = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.user_id = user_id
        self.role_id = role_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        企业项目ID。

        :return: The enterprise_project_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def user_id(self):
        """Gets the user_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        用户ID。

        :return: The user_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        用户ID。

        :param user_id: The user_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def role_id(self):
        """Gets the role_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        权限ID。

        :return: The role_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.

        权限ID。

        :param role_id: The role_id of this RevokeRoleFromUserOnEnterpriseProjectRequest.
        :type role_id: str
        """
        self._role_id = role_id

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
        if not isinstance(other, RevokeRoleFromUserOnEnterpriseProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
