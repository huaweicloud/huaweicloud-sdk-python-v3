# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListProjectBugStaticsV4Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bug_statistics': 'list[BugStatisticResponseV4]'
    }

    attribute_map = {
        'bug_statistics': 'bug_statistics'
    }

    def __init__(self, bug_statistics=None):
        """ListProjectBugStaticsV4Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bug_statistics = None
        self.discriminator = None

        if bug_statistics is not None:
            self.bug_statistics = bug_statistics

    @property
    def bug_statistics(self):
        """Gets the bug_statistics of this ListProjectBugStaticsV4Response.

        bug统计

        :return: The bug_statistics of this ListProjectBugStaticsV4Response.
        :rtype: list[BugStatisticResponseV4]
        """
        return self._bug_statistics

    @bug_statistics.setter
    def bug_statistics(self, bug_statistics):
        """Sets the bug_statistics of this ListProjectBugStaticsV4Response.

        bug统计

        :param bug_statistics: The bug_statistics of this ListProjectBugStaticsV4Response.
        :type: list[BugStatisticResponseV4]
        """
        self._bug_statistics = bug_statistics

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
        if not isinstance(other, ListProjectBugStaticsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
