# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyComplianceSummaryResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_details': 'PolicyComplianceSummaryUnit',
        'assignment_details': 'PolicyComplianceSummaryUnit'
    }

    attribute_map = {
        'resource_details': 'resource_details',
        'assignment_details': 'assignment_details'
    }

    def __init__(self, resource_details=None, assignment_details=None):
        r"""PolicyComplianceSummaryResults

        The model defined in huaweicloud sdk

        :param resource_details: 
        :type resource_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        :param assignment_details: 
        :type assignment_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        
        

        self._resource_details = None
        self._assignment_details = None
        self.discriminator = None

        if resource_details is not None:
            self.resource_details = resource_details
        if assignment_details is not None:
            self.assignment_details = assignment_details

    @property
    def resource_details(self):
        r"""Gets the resource_details of this PolicyComplianceSummaryResults.

        :return: The resource_details of this PolicyComplianceSummaryResults.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        r"""Sets the resource_details of this PolicyComplianceSummaryResults.

        :param resource_details: The resource_details of this PolicyComplianceSummaryResults.
        :type resource_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        self._resource_details = resource_details

    @property
    def assignment_details(self):
        r"""Gets the assignment_details of this PolicyComplianceSummaryResults.

        :return: The assignment_details of this PolicyComplianceSummaryResults.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        return self._assignment_details

    @assignment_details.setter
    def assignment_details(self, assignment_details):
        r"""Sets the assignment_details of this PolicyComplianceSummaryResults.

        :param assignment_details: The assignment_details of this PolicyComplianceSummaryResults.
        :type assignment_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        self._assignment_details = assignment_details

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
        if not isinstance(other, PolicyComplianceSummaryResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
