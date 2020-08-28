# coding: utf-8

import pprint
import re

import six





class IssueCommentV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'comment': 'str',
        'id': 'int',
        'created_time': 'str',
        'user': 'CommentUserV4'
    }

    attribute_map = {
        'comment': 'comment',
        'id': 'id',
        'created_time': 'created_time',
        'user': 'user'
    }

    def __init__(self, comment=None, id=None, created_time=None, user=None):
        """IssueCommentV4 - a model defined in huaweicloud sdk"""
        
        

        self._comment = None
        self._id = None
        self._created_time = None
        self._user = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if user is not None:
            self.user = user

    @property
    def comment(self):
        """Gets the comment of this IssueCommentV4.

        评论内容

        :return: The comment of this IssueCommentV4.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this IssueCommentV4.

        评论内容

        :param comment: The comment of this IssueCommentV4.
        :type: str
        """
        self._comment = comment

    @property
    def id(self):
        """Gets the id of this IssueCommentV4.

        评论id

        :return: The id of this IssueCommentV4.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueCommentV4.

        评论id

        :param id: The id of this IssueCommentV4.
        :type: int
        """
        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this IssueCommentV4.

        评论时间

        :return: The created_time of this IssueCommentV4.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this IssueCommentV4.

        评论时间

        :param created_time: The created_time of this IssueCommentV4.
        :type: str
        """
        self._created_time = created_time

    @property
    def user(self):
        """Gets the user of this IssueCommentV4.


        :return: The user of this IssueCommentV4.
        :rtype: CommentUserV4
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IssueCommentV4.


        :param user: The user of this IssueCommentV4.
        :type: CommentUserV4
        """
        self._user = user

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
        if not isinstance(other, IssueCommentV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
