# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comment_title': 'str',
        'comment_message': 'str',
        'attachment_name': 'list[str]'
    }

    attribute_map = {
        'comment_title': 'comment_title',
        'comment_message': 'comment_message',
        'attachment_name': 'attachment_name'
    }

    def __init__(self, comment_title=None, comment_message=None, attachment_name=None):
        r"""CommentData

        The model defined in huaweicloud sdk

        :param comment_title: 标题。
        :type comment_title: str
        :param comment_message: 消息。
        :type comment_message: str
        :param attachment_name: 附件名字
        :type attachment_name: list[str]
        """
        
        

        self._comment_title = None
        self._comment_message = None
        self._attachment_name = None
        self.discriminator = None

        if comment_title is not None:
            self.comment_title = comment_title
        if comment_message is not None:
            self.comment_message = comment_message
        if attachment_name is not None:
            self.attachment_name = attachment_name

    @property
    def comment_title(self):
        r"""Gets the comment_title of this CommentData.

        标题。

        :return: The comment_title of this CommentData.
        :rtype: str
        """
        return self._comment_title

    @comment_title.setter
    def comment_title(self, comment_title):
        r"""Sets the comment_title of this CommentData.

        标题。

        :param comment_title: The comment_title of this CommentData.
        :type comment_title: str
        """
        self._comment_title = comment_title

    @property
    def comment_message(self):
        r"""Gets the comment_message of this CommentData.

        消息。

        :return: The comment_message of this CommentData.
        :rtype: str
        """
        return self._comment_message

    @comment_message.setter
    def comment_message(self, comment_message):
        r"""Sets the comment_message of this CommentData.

        消息。

        :param comment_message: The comment_message of this CommentData.
        :type comment_message: str
        """
        self._comment_message = comment_message

    @property
    def attachment_name(self):
        r"""Gets the attachment_name of this CommentData.

        附件名字

        :return: The attachment_name of this CommentData.
        :rtype: list[str]
        """
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, attachment_name):
        r"""Sets the attachment_name of this CommentData.

        附件名字

        :param attachment_name: The attachment_name of this CommentData.
        :type attachment_name: list[str]
        """
        self._attachment_name = attachment_name

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
        if not isinstance(other, CommentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
