# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'size': 'int',
        'content_type': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'size': 'size',
        'content_type': 'content_type'
    }

    def __init__(self, file_name=None, size=None, content_type=None):
        r"""FileInfo

        The model defined in huaweicloud sdk

        :param file_name: 文件名称。
        :type file_name: str
        :param size: 文件大小。
        :type size: int
        :param content_type: 文件的MIME类型。
        :type content_type: str
        """
        
        

        self._file_name = None
        self._size = None
        self._content_type = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if size is not None:
            self.size = size
        if content_type is not None:
            self.content_type = content_type

    @property
    def file_name(self):
        r"""Gets the file_name of this FileInfo.

        文件名称。

        :return: The file_name of this FileInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this FileInfo.

        文件名称。

        :param file_name: The file_name of this FileInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def size(self):
        r"""Gets the size of this FileInfo.

        文件大小。

        :return: The size of this FileInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this FileInfo.

        文件大小。

        :param size: The size of this FileInfo.
        :type size: int
        """
        self._size = size

    @property
    def content_type(self):
        r"""Gets the content_type of this FileInfo.

        文件的MIME类型。

        :return: The content_type of this FileInfo.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this FileInfo.

        文件的MIME类型。

        :param content_type: The content_type of this FileInfo.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, FileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
