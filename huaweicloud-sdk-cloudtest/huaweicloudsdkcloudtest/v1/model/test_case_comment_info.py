# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseCommentInfo:

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
        'notifier': 'list[str]',
        'version_uri': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'notifier': 'notifier',
        'version_uri': 'version_uri'
    }

    def __init__(self, comment=None, notifier=None, version_uri=None):
        r"""TestCaseCommentInfo

        The model defined in huaweicloud sdk

        :param comment: 评论
        :type comment: str
        :param notifier: 通知人列表
        :type notifier: list[str]
        :param version_uri: 分支uri/测试计划uri
        :type version_uri: str
        """
        
        

        self._comment = None
        self._notifier = None
        self._version_uri = None
        self.discriminator = None

        self.comment = comment
        if notifier is not None:
            self.notifier = notifier
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def comment(self):
        r"""Gets the comment of this TestCaseCommentInfo.

        评论

        :return: The comment of this TestCaseCommentInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this TestCaseCommentInfo.

        评论

        :param comment: The comment of this TestCaseCommentInfo.
        :type comment: str
        """
        self._comment = comment

    @property
    def notifier(self):
        r"""Gets the notifier of this TestCaseCommentInfo.

        通知人列表

        :return: The notifier of this TestCaseCommentInfo.
        :rtype: list[str]
        """
        return self._notifier

    @notifier.setter
    def notifier(self, notifier):
        r"""Sets the notifier of this TestCaseCommentInfo.

        通知人列表

        :param notifier: The notifier of this TestCaseCommentInfo.
        :type notifier: list[str]
        """
        self._notifier = notifier

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestCaseCommentInfo.

        分支uri/测试计划uri

        :return: The version_uri of this TestCaseCommentInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestCaseCommentInfo.

        分支uri/测试计划uri

        :param version_uri: The version_uri of this TestCaseCommentInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

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
        if not isinstance(other, TestCaseCommentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
