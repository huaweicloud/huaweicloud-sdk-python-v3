# coding: utf-8

import pprint
import re

import six





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
        """IssueCompletionRateResponseV4 - a model defined in huaweicloud sdk"""
        
        

        self._issue_status = None
        self._tracker_id = None
        self.discriminator = None

        if issue_status is not None:
            self.issue_status = issue_status
        if tracker_id is not None:
            self.tracker_id = tracker_id

    @property
    def issue_status(self):
        """Gets the issue_status of this IssueCompletionRateResponseV4.


        :return: The issue_status of this IssueCompletionRateResponseV4.
        :rtype: IssueStatusResponseV4
        """
        return self._issue_status

    @issue_status.setter
    def issue_status(self, issue_status):
        """Sets the issue_status of this IssueCompletionRateResponseV4.


        :param issue_status: The issue_status of this IssueCompletionRateResponseV4.
        :type: IssueStatusResponseV4
        """
        self._issue_status = issue_status

    @property
    def tracker_id(self):
        """Gets the tracker_id of this IssueCompletionRateResponseV4.

        工作项类型,2任务/task,3缺陷/bug,5epic,6feature,7story

        :return: The tracker_id of this IssueCompletionRateResponseV4.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this IssueCompletionRateResponseV4.

        工作项类型,2任务/task,3缺陷/bug,5epic,6feature,7story

        :param tracker_id: The tracker_id of this IssueCompletionRateResponseV4.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueCompletionRateResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
