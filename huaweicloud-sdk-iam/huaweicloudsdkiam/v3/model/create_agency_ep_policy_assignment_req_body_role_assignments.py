# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_id': 'str',
        'enterprise_project_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'agency_id': 'agency_id',
        'enterprise_project_id': 'enterprise_project_id',
        'role_id': 'role_id'
    }

    def __init__(self, agency_id=None, enterprise_project_id=None, role_id=None):
        r"""CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments

        The model defined in huaweicloud sdk

        :param agency_id: 委托id
        :type agency_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param role_id: 策略id
        :type role_id: str
        """
        
        

        self._agency_id = None
        self._enterprise_project_id = None
        self._role_id = None
        self.discriminator = None

        self.agency_id = agency_id
        self.enterprise_project_id = enterprise_project_id
        self.role_id = role_id

    @property
    def agency_id(self):
        r"""Gets the agency_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        委托id

        :return: The agency_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        委托id

        :param agency_id: The agency_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        企业项目id

        :return: The enterprise_project_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def role_id(self):
        r"""Gets the role_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        策略id

        :return: The role_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.

        策略id

        :param role_id: The role_id of this CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments.
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
        if not isinstance(other, CreateAgencyEpPolicyAssignmentReqBodyRoleAssignments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
