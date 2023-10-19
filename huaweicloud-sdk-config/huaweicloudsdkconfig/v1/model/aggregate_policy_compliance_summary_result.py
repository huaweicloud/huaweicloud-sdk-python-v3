# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregatePolicyComplianceSummaryResult:

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
        'assignment_details': 'PolicyComplianceSummaryUnit',
        'group_name': 'str',
        'group_account_name': 'str'
    }

    attribute_map = {
        'resource_details': 'resource_details',
        'assignment_details': 'assignment_details',
        'group_name': 'group_name',
        'group_account_name': 'group_account_name'
    }

    def __init__(self, resource_details=None, assignment_details=None, group_name=None, group_account_name=None):
        """AggregatePolicyComplianceSummaryResult

        The model defined in huaweicloud sdk

        :param resource_details: 
        :type resource_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        :param assignment_details: 
        :type assignment_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        :param group_name: 分组名称
        :type group_name: str
        :param group_account_name: 帐号名称
        :type group_account_name: str
        """
        
        

        self._resource_details = None
        self._assignment_details = None
        self._group_name = None
        self._group_account_name = None
        self.discriminator = None

        if resource_details is not None:
            self.resource_details = resource_details
        if assignment_details is not None:
            self.assignment_details = assignment_details
        if group_name is not None:
            self.group_name = group_name
        if group_account_name is not None:
            self.group_account_name = group_account_name

    @property
    def resource_details(self):
        """Gets the resource_details of this AggregatePolicyComplianceSummaryResult.

        :return: The resource_details of this AggregatePolicyComplianceSummaryResult.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        """Sets the resource_details of this AggregatePolicyComplianceSummaryResult.

        :param resource_details: The resource_details of this AggregatePolicyComplianceSummaryResult.
        :type resource_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        self._resource_details = resource_details

    @property
    def assignment_details(self):
        """Gets the assignment_details of this AggregatePolicyComplianceSummaryResult.

        :return: The assignment_details of this AggregatePolicyComplianceSummaryResult.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        return self._assignment_details

    @assignment_details.setter
    def assignment_details(self, assignment_details):
        """Sets the assignment_details of this AggregatePolicyComplianceSummaryResult.

        :param assignment_details: The assignment_details of this AggregatePolicyComplianceSummaryResult.
        :type assignment_details: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryUnit`
        """
        self._assignment_details = assignment_details

    @property
    def group_name(self):
        """Gets the group_name of this AggregatePolicyComplianceSummaryResult.

        分组名称

        :return: The group_name of this AggregatePolicyComplianceSummaryResult.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AggregatePolicyComplianceSummaryResult.

        分组名称

        :param group_name: The group_name of this AggregatePolicyComplianceSummaryResult.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_account_name(self):
        """Gets the group_account_name of this AggregatePolicyComplianceSummaryResult.

        帐号名称

        :return: The group_account_name of this AggregatePolicyComplianceSummaryResult.
        :rtype: str
        """
        return self._group_account_name

    @group_account_name.setter
    def group_account_name(self, group_account_name):
        """Sets the group_account_name of this AggregatePolicyComplianceSummaryResult.

        帐号名称

        :param group_account_name: The group_account_name of this AggregatePolicyComplianceSummaryResult.
        :type group_account_name: str
        """
        self._group_account_name = group_account_name

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
        if not isinstance(other, AggregatePolicyComplianceSummaryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
