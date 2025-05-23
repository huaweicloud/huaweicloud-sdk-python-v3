# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCompletionRateResponseV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_status': 'IssueStatusResponseV4',
        'tracker_id': 'int'
    }

    attribute_map = {
        'issue_status': 'issue_status',
        'tracker_id': 'tracker_id'
    }

    def __init__(self, issue_status=None, tracker_id=None):
        r"""IssueCompletionRateResponseV4

        The model defined in huaweicloud sdk

        :param issue_status: 
        :type issue_status: :class:`huaweicloudsdkprojectman.v4.IssueStatusResponseV4`
        :param tracker_id: 工作项类型,2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story
        :type tracker_id: int
        """
        
        

        self._issue_status = None
        self._tracker_id = None
        self.discriminator = None

        if issue_status is not None:
            self.issue_status = issue_status
        if tracker_id is not None:
            self.tracker_id = tracker_id

    @property
    def issue_status(self):
        r"""Gets the issue_status of this IssueCompletionRateResponseV4.

        :return: The issue_status of this IssueCompletionRateResponseV4.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueStatusResponseV4`
        """
        return self._issue_status

    @issue_status.setter
    def issue_status(self, issue_status):
        r"""Sets the issue_status of this IssueCompletionRateResponseV4.

        :param issue_status: The issue_status of this IssueCompletionRateResponseV4.
        :type issue_status: :class:`huaweicloudsdkprojectman.v4.IssueStatusResponseV4`
        """
        self._issue_status = issue_status

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this IssueCompletionRateResponseV4.

        工作项类型,2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :return: The tracker_id of this IssueCompletionRateResponseV4.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this IssueCompletionRateResponseV4.

        工作项类型,2任务/Task,3缺陷/Bug,5Epic,6Feature,7Story

        :param tracker_id: The tracker_id of this IssueCompletionRateResponseV4.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

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
        if not isinstance(other, IssueCompletionRateResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
