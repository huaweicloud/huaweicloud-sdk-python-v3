# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgencyEpPolicyAssignmentReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_assignments': 'list[CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments]'
    }

    attribute_map = {
        'role_assignments': 'role_assignments'
    }

    def __init__(self, role_assignments=None):
        """CreateAgencyEpPolicyAssignmentReqBody

        The model defined in huaweicloud sdk

        :param role_assignments: 委托在企业项目上的绑定关系，最多支持250条。
        :type role_assignments: list[:class:`huaweicloudsdkiam.v3.CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments`]
        """
        
        

        self._role_assignments = None
        self.discriminator = None

        self.role_assignments = role_assignments

    @property
    def role_assignments(self):
        """Gets the role_assignments of this CreateAgencyEpPolicyAssignmentReqBody.

        委托在企业项目上的绑定关系，最多支持250条。

        :return: The role_assignments of this CreateAgencyEpPolicyAssignmentReqBody.
        :rtype: list[:class:`huaweicloudsdkiam.v3.CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments`]
        """
        return self._role_assignments

    @role_assignments.setter
    def role_assignments(self, role_assignments):
        """Sets the role_assignments of this CreateAgencyEpPolicyAssignmentReqBody.

        委托在企业项目上的绑定关系，最多支持250条。

        :param role_assignments: The role_assignments of this CreateAgencyEpPolicyAssignmentReqBody.
        :type role_assignments: list[:class:`huaweicloudsdkiam.v3.CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments`]
        """
        self._role_assignments = role_assignments

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
        if not isinstance(other, CreateAgencyEpPolicyAssignmentReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
