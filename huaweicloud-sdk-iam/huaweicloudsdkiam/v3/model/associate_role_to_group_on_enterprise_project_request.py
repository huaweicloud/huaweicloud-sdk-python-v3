# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRoleToGroupOnEnterpriseProjectRequest:

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
        'group_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'group_id': 'group_id',
        'role_id': 'role_id'
    }

    def __init__(self, enterprise_project_id=None, group_id=None, role_id=None):
        """AssociateRoleToGroupOnEnterpriseProjectRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param group_id: 用户组ID。
        :type group_id: str
        :param role_id: 权限ID。
        :type role_id: str
        """
        
        

        self._enterprise_project_id = None
        self._group_id = None
        self._role_id = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.group_id = group_id
        self.role_id = role_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        企业项目ID。

        :return: The enterprise_project_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def group_id(self):
        """Gets the group_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        用户组ID。

        :return: The group_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        用户组ID。

        :param group_id: The group_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def role_id(self):
        """Gets the role_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        权限ID。

        :return: The role_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.

        权限ID。

        :param role_id: The role_id of this AssociateRoleToGroupOnEnterpriseProjectRequest.
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
        if not isinstance(other, AssociateRoleToGroupOnEnterpriseProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
