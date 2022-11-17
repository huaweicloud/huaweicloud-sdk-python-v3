# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScrumProjectStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'issue_statuses': 'list[IssueStatus]'
    }

    attribute_map = {
        'total': 'total',
        'issue_statuses': 'issue_statuses'
    }

    def __init__(self, total=None, issue_statuses=None):
        """ListScrumProjectStatusesResponse

        The model defined in huaweicloud sdk

        :param total: 状态总数
        :type total: int
        :param issue_statuses: 状态列表
        :type issue_statuses: list[:class:`huaweicloudsdkprojectman.v4.IssueStatus`]
        """
        
        super(ListScrumProjectStatusesResponse, self).__init__()

        self._total = None
        self._issue_statuses = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if issue_statuses is not None:
            self.issue_statuses = issue_statuses

    @property
    def total(self):
        """Gets the total of this ListScrumProjectStatusesResponse.

        状态总数

        :return: The total of this ListScrumProjectStatusesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListScrumProjectStatusesResponse.

        状态总数

        :param total: The total of this ListScrumProjectStatusesResponse.
        :type total: int
        """
        self._total = total

    @property
    def issue_statuses(self):
        """Gets the issue_statuses of this ListScrumProjectStatusesResponse.

        状态列表

        :return: The issue_statuses of this ListScrumProjectStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueStatus`]
        """
        return self._issue_statuses

    @issue_statuses.setter
    def issue_statuses(self, issue_statuses):
        """Sets the issue_statuses of this ListScrumProjectStatusesResponse.

        状态列表

        :param issue_statuses: The issue_statuses of this ListScrumProjectStatusesResponse.
        :type issue_statuses: list[:class:`huaweicloudsdkprojectman.v4.IssueStatus`]
        """
        self._issue_statuses = issue_statuses

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
        if not isinstance(other, ListScrumProjectStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
