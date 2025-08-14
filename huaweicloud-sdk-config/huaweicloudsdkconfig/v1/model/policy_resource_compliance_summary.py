# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyResourceComplianceSummary:

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
        'resource': 'PolicyResource',
        'results': 'PolicyComplianceSummaryResults'
    }

    attribute_map = {
        'compliance_state': 'compliance_state',
        'resource': 'resource',
        'results': 'results'
    }

    def __init__(self, compliance_state=None, resource=None, results=None):
        r"""PolicyResourceComplianceSummary

        The model defined in huaweicloud sdk

        :param compliance_state: 规则合规状态
        :type compliance_state: str
        :param resource: 
        :type resource: :class:`huaweicloudsdkconfig.v1.PolicyResource`
        :param results: 
        :type results: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        """
        
        

        self._compliance_state = None
        self._resource = None
        self._results = None
        self.discriminator = None

        if compliance_state is not None:
            self.compliance_state = compliance_state
        if resource is not None:
            self.resource = resource
        if results is not None:
            self.results = results

    @property
    def compliance_state(self):
        r"""Gets the compliance_state of this PolicyResourceComplianceSummary.

        规则合规状态

        :return: The compliance_state of this PolicyResourceComplianceSummary.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        r"""Sets the compliance_state of this PolicyResourceComplianceSummary.

        规则合规状态

        :param compliance_state: The compliance_state of this PolicyResourceComplianceSummary.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def resource(self):
        r"""Gets the resource of this PolicyResourceComplianceSummary.

        :return: The resource of this PolicyResourceComplianceSummary.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyResource`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this PolicyResourceComplianceSummary.

        :param resource: The resource of this PolicyResourceComplianceSummary.
        :type resource: :class:`huaweicloudsdkconfig.v1.PolicyResource`
        """
        self._resource = resource

    @property
    def results(self):
        r"""Gets the results of this PolicyResourceComplianceSummary.

        :return: The results of this PolicyResourceComplianceSummary.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this PolicyResourceComplianceSummary.

        :param results: The results of this PolicyResourceComplianceSummary.
        :type results: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        """
        self._results = results

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
        if not isinstance(other, PolicyResourceComplianceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
