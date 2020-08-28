# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListIssueCommentsV4Response(SdkResponse):


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
        'comments': 'list[IssueCommentV4]'
    }

    attribute_map = {
        'total': 'total',
        'comments': 'comments'
    }

    def __init__(self, total=None, comments=None):
        """ListIssueCommentsV4Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._comments = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if comments is not None:
            self.comments = comments

    @property
    def total(self):
        """Gets the total of this ListIssueCommentsV4Response.

        评论总数

        :return: The total of this ListIssueCommentsV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListIssueCommentsV4Response.

        评论总数

        :param total: The total of this ListIssueCommentsV4Response.
        :type: int
        """
        self._total = total

    @property
    def comments(self):
        """Gets the comments of this ListIssueCommentsV4Response.

        品论列表

        :return: The comments of this ListIssueCommentsV4Response.
        :rtype: list[IssueCommentV4]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ListIssueCommentsV4Response.

        品论列表

        :param comments: The comments of this ListIssueCommentsV4Response.
        :type: list[IssueCommentV4]
        """
        self._comments = comments

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
        if not isinstance(other, ListIssueCommentsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
