# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectSummaryV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bug_statistics': 'list[BugStatisticResponseV4]',
        'demand_statistics': 'list[DemandStatisticResponseV4]',
        'issue_completion_rates': 'list[IssueCompletionRateResponseV4]',
        'project_id': 'str'
    }

    attribute_map = {
        'bug_statistics': 'bug_statistics',
        'demand_statistics': 'demand_statistics',
        'issue_completion_rates': 'issue_completion_rates',
        'project_id': 'project_id'
    }

    def __init__(self, bug_statistics=None, demand_statistics=None, issue_completion_rates=None, project_id=None):
        """ShowProjectSummaryV4Response

        The model defined in huaweicloud sdk

        :param bug_statistics: bug统计列表
        :type bug_statistics: list[:class:`huaweicloudsdkprojectman.v4.BugStatisticResponseV4`]
        :param demand_statistics: 按模块统计列表
        :type demand_statistics: list[:class:`huaweicloudsdkprojectman.v4.DemandStatisticResponseV4`]
        :param issue_completion_rates: 按工作项类型统计列表
        :type issue_completion_rates: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateResponseV4`]
        :param project_id: 项目id
        :type project_id: str
        """
        
        super(ShowProjectSummaryV4Response, self).__init__()

        self._bug_statistics = None
        self._demand_statistics = None
        self._issue_completion_rates = None
        self._project_id = None
        self.discriminator = None

        if bug_statistics is not None:
            self.bug_statistics = bug_statistics
        if demand_statistics is not None:
            self.demand_statistics = demand_statistics
        if issue_completion_rates is not None:
            self.issue_completion_rates = issue_completion_rates
        if project_id is not None:
            self.project_id = project_id

    @property
    def bug_statistics(self):
        """Gets the bug_statistics of this ShowProjectSummaryV4Response.

        bug统计列表

        :return: The bug_statistics of this ShowProjectSummaryV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.BugStatisticResponseV4`]
        """
        return self._bug_statistics

    @bug_statistics.setter
    def bug_statistics(self, bug_statistics):
        """Sets the bug_statistics of this ShowProjectSummaryV4Response.

        bug统计列表

        :param bug_statistics: The bug_statistics of this ShowProjectSummaryV4Response.
        :type bug_statistics: list[:class:`huaweicloudsdkprojectman.v4.BugStatisticResponseV4`]
        """
        self._bug_statistics = bug_statistics

    @property
    def demand_statistics(self):
        """Gets the demand_statistics of this ShowProjectSummaryV4Response.

        按模块统计列表

        :return: The demand_statistics of this ShowProjectSummaryV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.DemandStatisticResponseV4`]
        """
        return self._demand_statistics

    @demand_statistics.setter
    def demand_statistics(self, demand_statistics):
        """Sets the demand_statistics of this ShowProjectSummaryV4Response.

        按模块统计列表

        :param demand_statistics: The demand_statistics of this ShowProjectSummaryV4Response.
        :type demand_statistics: list[:class:`huaweicloudsdkprojectman.v4.DemandStatisticResponseV4`]
        """
        self._demand_statistics = demand_statistics

    @property
    def issue_completion_rates(self):
        """Gets the issue_completion_rates of this ShowProjectSummaryV4Response.

        按工作项类型统计列表

        :return: The issue_completion_rates of this ShowProjectSummaryV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateResponseV4`]
        """
        return self._issue_completion_rates

    @issue_completion_rates.setter
    def issue_completion_rates(self, issue_completion_rates):
        """Sets the issue_completion_rates of this ShowProjectSummaryV4Response.

        按工作项类型统计列表

        :param issue_completion_rates: The issue_completion_rates of this ShowProjectSummaryV4Response.
        :type issue_completion_rates: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateResponseV4`]
        """
        self._issue_completion_rates = issue_completion_rates

    @property
    def project_id(self):
        """Gets the project_id of this ShowProjectSummaryV4Response.

        项目id

        :return: The project_id of this ShowProjectSummaryV4Response.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowProjectSummaryV4Response.

        项目id

        :param project_id: The project_id of this ShowProjectSummaryV4Response.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ShowProjectSummaryV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
