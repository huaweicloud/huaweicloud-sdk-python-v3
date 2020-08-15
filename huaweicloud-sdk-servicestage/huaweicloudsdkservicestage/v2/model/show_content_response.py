# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowContentResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'sha': 'str',
        'encoding': 'str',
        'content': 'str'
    }

    attribute_map = {
        'path': 'path',
        'sha': 'sha',
        'encoding': 'encoding',
        'content': 'content'
    }

    def __init__(self, path=None, sha=None, encoding=None, content=None):
        """ShowContentResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._path = None
        self._sha = None
        self._encoding = None
        self._content = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if sha is not None:
            self.sha = sha
        if encoding is not None:
            self.encoding = encoding
        if content is not None:
            self.content = content

    @property
    def path(self):
        """Gets the path of this ShowContentResponse.

        文件路径。

        :return: The path of this ShowContentResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowContentResponse.

        文件路径。

        :param path: The path of this ShowContentResponse.
        :type: str
        """
        self._path = path

    @property
    def sha(self):
        """Gets the sha of this ShowContentResponse.

        commit 哈希。

        :return: The sha of this ShowContentResponse.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ShowContentResponse.

        commit 哈希。

        :param sha: The sha of this ShowContentResponse.
        :type: str
        """
        self._sha = sha

    @property
    def encoding(self):
        """Gets the encoding of this ShowContentResponse.

        编码方式：base64或者text/plain。

        :return: The encoding of this ShowContentResponse.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ShowContentResponse.

        编码方式：base64或者text/plain。

        :param encoding: The encoding of this ShowContentResponse.
        :type: str
        """
        self._encoding = encoding

    @property
    def content(self):
        """Gets the content of this ShowContentResponse.

        文件内容。

        :return: The content of this ShowContentResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowContentResponse.

        文件内容。

        :param content: The content of this ShowContentResponse.
        :type: str
        """
        self._content = content

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
        if not isinstance(other, ShowContentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
