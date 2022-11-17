# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilesResponseInfo:

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
        'file_path': 'str',
        'size': 'str',
        'encoding': 'str',
        'ref': 'str',
        'blob_id': 'str',
        'file_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_path': 'file_path',
        'size': 'size',
        'encoding': 'encoding',
        'ref': 'ref',
        'blob_id': 'blob_id',
        'file_type': 'file_type',
        'content': 'content'
    }

    def __init__(self, file_name=None, file_path=None, size=None, encoding=None, ref=None, blob_id=None, file_type=None, content=None):
        """FilesResponseInfo

        The model defined in huaweicloud sdk

        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param size: 文件大小
        :type size: str
        :param encoding: 编码类型
        :type encoding: str
        :param ref: 分支名称
        :type ref: str
        :param blob_id: 文件块id
        :type blob_id: str
        :param file_type: 文件类型
        :type file_type: str
        :param content: 文件内容
        :type content: str
        """
        
        

        self._file_name = None
        self._file_path = None
        self._size = None
        self._encoding = None
        self._ref = None
        self._blob_id = None
        self._file_type = None
        self._content = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if size is not None:
            self.size = size
        if encoding is not None:
            self.encoding = encoding
        if ref is not None:
            self.ref = ref
        if blob_id is not None:
            self.blob_id = blob_id
        if file_type is not None:
            self.file_type = file_type
        if content is not None:
            self.content = content

    @property
    def file_name(self):
        """Gets the file_name of this FilesResponseInfo.

        文件名称

        :return: The file_name of this FilesResponseInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FilesResponseInfo.

        文件名称

        :param file_name: The file_name of this FilesResponseInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        """Gets the file_path of this FilesResponseInfo.

        文件路径

        :return: The file_path of this FilesResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this FilesResponseInfo.

        文件路径

        :param file_path: The file_path of this FilesResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def size(self):
        """Gets the size of this FilesResponseInfo.

        文件大小

        :return: The size of this FilesResponseInfo.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FilesResponseInfo.

        文件大小

        :param size: The size of this FilesResponseInfo.
        :type size: str
        """
        self._size = size

    @property
    def encoding(self):
        """Gets the encoding of this FilesResponseInfo.

        编码类型

        :return: The encoding of this FilesResponseInfo.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this FilesResponseInfo.

        编码类型

        :param encoding: The encoding of this FilesResponseInfo.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def ref(self):
        """Gets the ref of this FilesResponseInfo.

        分支名称

        :return: The ref of this FilesResponseInfo.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this FilesResponseInfo.

        分支名称

        :param ref: The ref of this FilesResponseInfo.
        :type ref: str
        """
        self._ref = ref

    @property
    def blob_id(self):
        """Gets the blob_id of this FilesResponseInfo.

        文件块id

        :return: The blob_id of this FilesResponseInfo.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        """Sets the blob_id of this FilesResponseInfo.

        文件块id

        :param blob_id: The blob_id of this FilesResponseInfo.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def file_type(self):
        """Gets the file_type of this FilesResponseInfo.

        文件类型

        :return: The file_type of this FilesResponseInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FilesResponseInfo.

        文件类型

        :param file_type: The file_type of this FilesResponseInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def content(self):
        """Gets the content of this FilesResponseInfo.

        文件内容

        :return: The content of this FilesResponseInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FilesResponseInfo.

        文件内容

        :param content: The content of this FilesResponseInfo.
        :type content: str
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
        if not isinstance(other, FilesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
