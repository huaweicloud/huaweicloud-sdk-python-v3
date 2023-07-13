# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchIssuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_list': 'list[WorkTableIssuseListResponseBodyIssueList]',
        'total': 'int'
    }

    attribute_map = {
        'issue_list': 'issue_list',
        'total': 'total'
    }

    def __init__(self, issue_list=None, total=None):
        """SearchIssuesResponse

        The model defined in huaweicloud sdk

        :param issue_list: 工作项信息列表
        :type issue_list: list[:class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyIssueList`]
        :param total: 工作项总数
        :type total: int
        """
        
        super(SearchIssuesResponse, self).__init__()

        self._issue_list = None
        self._total = None
        self.discriminator = None

        if issue_list is not None:
            self.issue_list = issue_list
        if total is not None:
            self.total = total

    @property
    def issue_list(self):
        """Gets the issue_list of this SearchIssuesResponse.

        工作项信息列表

        :return: The issue_list of this SearchIssuesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyIssueList`]
        """
        return self._issue_list

    @issue_list.setter
    def issue_list(self, issue_list):
        """Sets the issue_list of this SearchIssuesResponse.

        工作项信息列表

        :param issue_list: The issue_list of this SearchIssuesResponse.
        :type issue_list: list[:class:`huaweicloudsdkprojectman.v4.WorkTableIssuseListResponseBodyIssueList`]
        """
        self._issue_list = issue_list

    @property
    def total(self):
        """Gets the total of this SearchIssuesResponse.

        工作项总数

        :return: The total of this SearchIssuesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchIssuesResponse.

        工作项总数

        :param total: The total of this SearchIssuesResponse.
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
        if not isinstance(other, SearchIssuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
