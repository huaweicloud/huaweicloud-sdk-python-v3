# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIssueCompletionRateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'issue_completion_rates': 'list[IssueCompletionRateV4IssueCompletionRates]',
        'total': 'int'
    }

    attribute_map = {
        'issue_completion_rates': 'issue_completion_rates',
        'total': 'total'
    }

    def __init__(self, issue_completion_rates=None, total=None):
        """ShowIssueCompletionRateResponse

        The model defined in huaweicloud sdk

        :param issue_completion_rates: 不同类型的工作项完成率
        :type issue_completion_rates: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateV4IssueCompletionRates`]
        :param total: 总数
        :type total: int
        """
        
        super(ShowIssueCompletionRateResponse, self).__init__()

        self._issue_completion_rates = None
        self._total = None
        self.discriminator = None

        if issue_completion_rates is not None:
            self.issue_completion_rates = issue_completion_rates
        if total is not None:
            self.total = total

    @property
    def issue_completion_rates(self):
        """Gets the issue_completion_rates of this ShowIssueCompletionRateResponse.

        不同类型的工作项完成率

        :return: The issue_completion_rates of this ShowIssueCompletionRateResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateV4IssueCompletionRates`]
        """
        return self._issue_completion_rates

    @issue_completion_rates.setter
    def issue_completion_rates(self, issue_completion_rates):
        """Sets the issue_completion_rates of this ShowIssueCompletionRateResponse.

        不同类型的工作项完成率

        :param issue_completion_rates: The issue_completion_rates of this ShowIssueCompletionRateResponse.
        :type issue_completion_rates: list[:class:`huaweicloudsdkprojectman.v4.IssueCompletionRateV4IssueCompletionRates`]
        """
        self._issue_completion_rates = issue_completion_rates

    @property
    def total(self):
        """Gets the total of this ShowIssueCompletionRateResponse.

        总数

        :return: The total of this ShowIssueCompletionRateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowIssueCompletionRateResponse.

        总数

        :param total: The total of this ShowIssueCompletionRateResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowIssueCompletionRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
