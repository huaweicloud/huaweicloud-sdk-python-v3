# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""ListIssueCommentsV4Response

        The model defined in huaweicloud sdk

        :param total: 评论总数
        :type total: int
        :param comments: 品论列表
        :type comments: list[:class:`huaweicloudsdkprojectman.v4.IssueCommentV4`]
        """
        
        super(ListIssueCommentsV4Response, self).__init__()

        self._total = None
        self._comments = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if comments is not None:
            self.comments = comments

    @property
    def total(self):
        r"""Gets the total of this ListIssueCommentsV4Response.

        评论总数

        :return: The total of this ListIssueCommentsV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListIssueCommentsV4Response.

        评论总数

        :param total: The total of this ListIssueCommentsV4Response.
        :type total: int
        """
        self._total = total

    @property
    def comments(self):
        r"""Gets the comments of this ListIssueCommentsV4Response.

        品论列表

        :return: The comments of this ListIssueCommentsV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueCommentV4`]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this ListIssueCommentsV4Response.

        品论列表

        :param comments: The comments of this ListIssueCommentsV4Response.
        :type comments: list[:class:`huaweicloudsdkprojectman.v4.IssueCommentV4`]
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
        if not isinstance(other, ListIssueCommentsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
