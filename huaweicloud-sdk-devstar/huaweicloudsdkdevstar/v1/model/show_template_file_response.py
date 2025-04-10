# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'encoding': 'str',
        'file_name': 'str',
        'file_path': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'content': 'content',
        'encoding': 'encoding',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'file_type': 'file_type'
    }

    def __init__(self, content=None, encoding=None, file_name=None, file_path=None, file_type=None):
        r"""ShowTemplateFileResponse

        The model defined in huaweicloud sdk

        :param content: 文件内容（返回的文件内容为encoding指定的编码格式编码后的内容）。
        :type content: str
        :param encoding: 内容编码格式(固定base64)。
        :type encoding: str
        :param file_name: 文件名。
        :type file_name: str
        :param file_path: 文件相对路径。
        :type file_path: str
        :param file_type: 文件类型。
        :type file_type: str
        """
        
        super(ShowTemplateFileResponse, self).__init__()

        self._content = None
        self._encoding = None
        self._file_name = None
        self._file_path = None
        self._file_type = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if encoding is not None:
            self.encoding = encoding
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type

    @property
    def content(self):
        r"""Gets the content of this ShowTemplateFileResponse.

        文件内容（返回的文件内容为encoding指定的编码格式编码后的内容）。

        :return: The content of this ShowTemplateFileResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowTemplateFileResponse.

        文件内容（返回的文件内容为encoding指定的编码格式编码后的内容）。

        :param content: The content of this ShowTemplateFileResponse.
        :type content: str
        """
        self._content = content

    @property
    def encoding(self):
        r"""Gets the encoding of this ShowTemplateFileResponse.

        内容编码格式(固定base64)。

        :return: The encoding of this ShowTemplateFileResponse.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this ShowTemplateFileResponse.

        内容编码格式(固定base64)。

        :param encoding: The encoding of this ShowTemplateFileResponse.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowTemplateFileResponse.

        文件名。

        :return: The file_name of this ShowTemplateFileResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowTemplateFileResponse.

        文件名。

        :param file_name: The file_name of this ShowTemplateFileResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowTemplateFileResponse.

        文件相对路径。

        :return: The file_path of this ShowTemplateFileResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowTemplateFileResponse.

        文件相对路径。

        :param file_path: The file_path of this ShowTemplateFileResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this ShowTemplateFileResponse.

        文件类型。

        :return: The file_type of this ShowTemplateFileResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ShowTemplateFileResponse.

        文件类型。

        :param file_type: The file_type of this ShowTemplateFileResponse.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, ShowTemplateFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
