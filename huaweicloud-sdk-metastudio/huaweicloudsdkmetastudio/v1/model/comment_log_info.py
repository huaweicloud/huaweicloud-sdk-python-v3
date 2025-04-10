# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_time': 'str',
        'comment_type': 'str',
        'comment_title': 'str',
        'comment_message': 'str',
        'attachment_download_url': 'list[str]'
    }

    attribute_map = {
        'operate_time': 'operate_time',
        'comment_type': 'comment_type',
        'comment_title': 'comment_title',
        'comment_message': 'comment_message',
        'attachment_download_url': 'attachment_download_url'
    }

    def __init__(self, operate_time=None, comment_type=None, comment_title=None, comment_message=None, attachment_download_url=None):
        r"""CommentLogInfo

        The model defined in huaweicloud sdk

        :param operate_time: 操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”
        :type operate_time: str
        :param comment_type: * USER_REJECT：用户驳回 * USER_COMMENT：用户评论 * ADMIN_COMMENT：管理员评论
        :type comment_type: str
        :param comment_title: 标题。
        :type comment_title: str
        :param comment_message: 消息。
        :type comment_message: str
        :param attachment_download_url: 附件下载地址
        :type attachment_download_url: list[str]
        """
        
        

        self._operate_time = None
        self._comment_type = None
        self._comment_title = None
        self._comment_message = None
        self._attachment_download_url = None
        self.discriminator = None

        if operate_time is not None:
            self.operate_time = operate_time
        if comment_type is not None:
            self.comment_type = comment_type
        if comment_title is not None:
            self.comment_title = comment_title
        if comment_message is not None:
            self.comment_message = comment_message
        if attachment_download_url is not None:
            self.attachment_download_url = attachment_download_url

    @property
    def operate_time(self):
        r"""Gets the operate_time of this CommentLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The operate_time of this CommentLogInfo.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this CommentLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param operate_time: The operate_time of this CommentLogInfo.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def comment_type(self):
        r"""Gets the comment_type of this CommentLogInfo.

        * USER_REJECT：用户驳回 * USER_COMMENT：用户评论 * ADMIN_COMMENT：管理员评论

        :return: The comment_type of this CommentLogInfo.
        :rtype: str
        """
        return self._comment_type

    @comment_type.setter
    def comment_type(self, comment_type):
        r"""Sets the comment_type of this CommentLogInfo.

        * USER_REJECT：用户驳回 * USER_COMMENT：用户评论 * ADMIN_COMMENT：管理员评论

        :param comment_type: The comment_type of this CommentLogInfo.
        :type comment_type: str
        """
        self._comment_type = comment_type

    @property
    def comment_title(self):
        r"""Gets the comment_title of this CommentLogInfo.

        标题。

        :return: The comment_title of this CommentLogInfo.
        :rtype: str
        """
        return self._comment_title

    @comment_title.setter
    def comment_title(self, comment_title):
        r"""Sets the comment_title of this CommentLogInfo.

        标题。

        :param comment_title: The comment_title of this CommentLogInfo.
        :type comment_title: str
        """
        self._comment_title = comment_title

    @property
    def comment_message(self):
        r"""Gets the comment_message of this CommentLogInfo.

        消息。

        :return: The comment_message of this CommentLogInfo.
        :rtype: str
        """
        return self._comment_message

    @comment_message.setter
    def comment_message(self, comment_message):
        r"""Sets the comment_message of this CommentLogInfo.

        消息。

        :param comment_message: The comment_message of this CommentLogInfo.
        :type comment_message: str
        """
        self._comment_message = comment_message

    @property
    def attachment_download_url(self):
        r"""Gets the attachment_download_url of this CommentLogInfo.

        附件下载地址

        :return: The attachment_download_url of this CommentLogInfo.
        :rtype: list[str]
        """
        return self._attachment_download_url

    @attachment_download_url.setter
    def attachment_download_url(self, attachment_download_url):
        r"""Sets the attachment_download_url of this CommentLogInfo.

        附件下载地址

        :param attachment_download_url: The attachment_download_url of this CommentLogInfo.
        :type attachment_download_url: list[str]
        """
        self._attachment_download_url = attachment_download_url

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
        if not isinstance(other, CommentLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
