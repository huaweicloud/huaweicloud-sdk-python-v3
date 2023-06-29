# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOrganizationPolicyAssignmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_id': 'str',
        'organization_policy_assignment_id': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'organization_policy_assignment_id': 'organization_policy_assignment_id'
    }

    def __init__(self, organization_id=None, organization_policy_assignment_id=None):
        """DeleteOrganizationPolicyAssignmentRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param organization_policy_assignment_id: 组织合规规则ID。
        :type organization_policy_assignment_id: str
        """
        
        

        self._organization_id = None
        self._organization_policy_assignment_id = None
        self.discriminator = None

        self.organization_id = organization_id
        self.organization_policy_assignment_id = organization_policy_assignment_id

    @property
    def organization_id(self):
        """Gets the organization_id of this DeleteOrganizationPolicyAssignmentRequest.

        组织ID。

        :return: The organization_id of this DeleteOrganizationPolicyAssignmentRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this DeleteOrganizationPolicyAssignmentRequest.

        组织ID。

        :param organization_id: The organization_id of this DeleteOrganizationPolicyAssignmentRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def organization_policy_assignment_id(self):
        """Gets the organization_policy_assignment_id of this DeleteOrganizationPolicyAssignmentRequest.

        组织合规规则ID。

        :return: The organization_policy_assignment_id of this DeleteOrganizationPolicyAssignmentRequest.
        :rtype: str
        """
        return self._organization_policy_assignment_id

    @organization_policy_assignment_id.setter
    def organization_policy_assignment_id(self, organization_policy_assignment_id):
        """Sets the organization_policy_assignment_id of this DeleteOrganizationPolicyAssignmentRequest.

        组织合规规则ID。

        :param organization_policy_assignment_id: The organization_policy_assignment_id of this DeleteOrganizationPolicyAssignmentRequest.
        :type organization_policy_assignment_id: str
        """
        self._organization_policy_assignment_id = organization_policy_assignment_id

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
        if not isinstance(other, DeleteOrganizationPolicyAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
