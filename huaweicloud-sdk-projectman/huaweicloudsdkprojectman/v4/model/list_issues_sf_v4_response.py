# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssuesSfV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issues': 'list[IssueItemSfV4]',
        'total': 'int'
    }

    attribute_map = {
        'issues': 'issues',
        'total': 'total'
    }

    def __init__(self, issues=None, total=None):
        r"""ListIssuesSfV4Response

        The model defined in huaweicloud sdk

        :param issues: 工作项
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.IssueItemSfV4`]
        :param total: 总数
        :type total: int
        """
        
        super(ListIssuesSfV4Response, self).__init__()

        self._issues = None
        self._total = None
        self.discriminator = None

        if issues is not None:
            self.issues = issues
        if total is not None:
            self.total = total

    @property
    def issues(self):
        r"""Gets the issues of this ListIssuesSfV4Response.

        工作项

        :return: The issues of this ListIssuesSfV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueItemSfV4`]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        r"""Sets the issues of this ListIssuesSfV4Response.

        工作项

        :param issues: The issues of this ListIssuesSfV4Response.
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.IssueItemSfV4`]
        """
        self._issues = issues

    @property
    def total(self):
        r"""Gets the total of this ListIssuesSfV4Response.

        总数

        :return: The total of this ListIssuesSfV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListIssuesSfV4Response.

        总数

        :param total: The total of this ListIssuesSfV4Response.
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
        if not isinstance(other, ListIssuesSfV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
