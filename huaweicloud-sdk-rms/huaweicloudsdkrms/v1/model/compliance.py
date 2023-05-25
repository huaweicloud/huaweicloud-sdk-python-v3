# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Compliance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliance_state': 'str',
        'resource_details': 'PolicyComplianceSummaryUnit'
    }

    attribute_map = {
        'compliance_state': 'compliance_state',
        'resource_details': 'resource_details'
    }

    def __init__(self, compliance_state=None, resource_details=None):
        """Compliance

        The model defined in huaweicloud sdk

        :param compliance_state: 合规结果。
        :type compliance_state: str
        :param resource_details: 
        :type resource_details: :class:`huaweicloudsdkrms.v1.PolicyComplianceSummaryUnit`
        """
        
        

        self._compliance_state = None
        self._resource_details = None
        self.discriminator = None

        if compliance_state is not None:
            self.compliance_state = compliance_state
        if resource_details is not None:
            self.resource_details = resource_details

    @property
    def compliance_state(self):
        """Gets the compliance_state of this Compliance.

        合规结果。

        :return: The compliance_state of this Compliance.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this Compliance.

        合规结果。

        :param compliance_state: The compliance_state of this Compliance.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def resource_details(self):
        """Gets the resource_details of this Compliance.

        :return: The resource_details of this Compliance.
        :rtype: :class:`huaweicloudsdkrms.v1.PolicyComplianceSummaryUnit`
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        """Sets the resource_details of this Compliance.

        :param resource_details: The resource_details of this Compliance.
        :type resource_details: :class:`huaweicloudsdkrms.v1.PolicyComplianceSummaryUnit`
        """
        self._resource_details = resource_details

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
        if not isinstance(other, Compliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
