# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedIssuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issues': 'list[AssociateIssueDetail]',
        'total': 'int'
    }

    attribute_map = {
        'issues': 'issues',
        'total': 'total'
    }

    def __init__(self, issues=None, total=None):
        """ListAssociatedIssuesResponse

        The model defined in huaweicloud sdk

        :param issues: 关联的工作项列表
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        :param total: 总数
        :type total: int
        """
        
        super(ListAssociatedIssuesResponse, self).__init__()

        self._issues = None
        self._total = None
        self.discriminator = None

        if issues is not None:
            self.issues = issues
        if total is not None:
            self.total = total

    @property
    def issues(self):
        """Gets the issues of this ListAssociatedIssuesResponse.

        关联的工作项列表

        :return: The issues of this ListAssociatedIssuesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this ListAssociatedIssuesResponse.

        关联的工作项列表

        :param issues: The issues of this ListAssociatedIssuesResponse.
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        """
        self._issues = issues

    @property
    def total(self):
        """Gets the total of this ListAssociatedIssuesResponse.

        总数

        :return: The total of this ListAssociatedIssuesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAssociatedIssuesResponse.

        总数

        :param total: The total of this ListAssociatedIssuesResponse.
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
        if not isinstance(other, ListAssociatedIssuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
