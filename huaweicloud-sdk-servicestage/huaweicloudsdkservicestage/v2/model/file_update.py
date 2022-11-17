# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'content': 'str',
        'sha': 'str'
    }

    attribute_map = {
        'message': 'message',
        'content': 'content',
        'sha': 'sha'
    }

    def __init__(self, message=None, content=None, sha=None):
        """FileUpdate

        The model defined in huaweicloud sdk

        :param message: 提交描述。
        :type message: str
        :param content: 经base64编码的文件内容。
        :type content: str
        :param sha: 文件的sha值。
        :type sha: str
        """
        
        

        self._message = None
        self._content = None
        self._sha = None
        self.discriminator = None

        self.message = message
        self.content = content
        self.sha = sha

    @property
    def message(self):
        """Gets the message of this FileUpdate.

        提交描述。

        :return: The message of this FileUpdate.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FileUpdate.

        提交描述。

        :param message: The message of this FileUpdate.
        :type message: str
        """
        self._message = message

    @property
    def content(self):
        """Gets the content of this FileUpdate.

        经base64编码的文件内容。

        :return: The content of this FileUpdate.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FileUpdate.

        经base64编码的文件内容。

        :param content: The content of this FileUpdate.
        :type content: str
        """
        self._content = content

    @property
    def sha(self):
        """Gets the sha of this FileUpdate.

        文件的sha值。

        :return: The sha of this FileUpdate.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this FileUpdate.

        文件的sha值。

        :param sha: The sha of this FileUpdate.
        :type sha: str
        """
        self._sha = sha

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
        if not isinstance(other, FileUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
