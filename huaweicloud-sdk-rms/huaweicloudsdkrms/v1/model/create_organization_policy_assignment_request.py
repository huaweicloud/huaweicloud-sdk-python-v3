# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrganizationPolicyAssignmentRequest:

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
        'body': 'OrganizationPolicyAssignmentRequest'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'body': 'body'
    }

    def __init__(self, organization_id=None, body=None):
        """CreateOrganizationPolicyAssignmentRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param body: Body of the CreateOrganizationPolicyAssignmentRequest
        :type body: :class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentRequest`
        """
        
        

        self._organization_id = None
        self._body = None
        self.discriminator = None

        self.organization_id = organization_id
        if body is not None:
            self.body = body

    @property
    def organization_id(self):
        """Gets the organization_id of this CreateOrganizationPolicyAssignmentRequest.

        组织ID。

        :return: The organization_id of this CreateOrganizationPolicyAssignmentRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CreateOrganizationPolicyAssignmentRequest.

        组织ID。

        :param organization_id: The organization_id of this CreateOrganizationPolicyAssignmentRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def body(self):
        """Gets the body of this CreateOrganizationPolicyAssignmentRequest.

        :return: The body of this CreateOrganizationPolicyAssignmentRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateOrganizationPolicyAssignmentRequest.

        :param body: The body of this CreateOrganizationPolicyAssignmentRequest.
        :type body: :class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentRequest`
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
        if not isinstance(other, CreateOrganizationPolicyAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
