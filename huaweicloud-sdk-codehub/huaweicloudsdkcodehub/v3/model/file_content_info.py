# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileContentInfo:

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
        'size': 'int',
        'encoding': 'str',
        'content_sha256': 'str',
        'ref': 'str',
        'blob_id': 'str',
        'commit_id': 'str',
        'last_commit_id': 'str',
        'content': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_path': 'file_path',
        'size': 'size',
        'encoding': 'encoding',
        'content_sha256': 'content_sha256',
        'ref': 'ref',
        'blob_id': 'blob_id',
        'commit_id': 'commit_id',
        'last_commit_id': 'last_commit_id',
        'content': 'content'
    }

    def __init__(self, file_name=None, file_path=None, size=None, encoding=None, content_sha256=None, ref=None, blob_id=None, commit_id=None, last_commit_id=None, content=None):
        r"""FileContentInfo

        The model defined in huaweicloud sdk

        :param file_name: 文件名
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param size: 文件大小
        :type size: int
        :param encoding: 文件编码
        :type encoding: str
        :param content_sha256: sha256编码的文件内容
        :type content_sha256: str
        :param ref: 分支名
        :type ref: str
        :param blob_id: blob sha
        :type blob_id: str
        :param commit_id: 提交对应的SHA id
        :type commit_id: str
        :param last_commit_id: 最后一个提交对应的SHA id
        :type last_commit_id: str
        :param content: base64编码的文件内容
        :type content: str
        """
        
        

        self._file_name = None
        self._file_path = None
        self._size = None
        self._encoding = None
        self._content_sha256 = None
        self._ref = None
        self._blob_id = None
        self._commit_id = None
        self._last_commit_id = None
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
        if content_sha256 is not None:
            self.content_sha256 = content_sha256
        if ref is not None:
            self.ref = ref
        if blob_id is not None:
            self.blob_id = blob_id
        if commit_id is not None:
            self.commit_id = commit_id
        if last_commit_id is not None:
            self.last_commit_id = last_commit_id
        if content is not None:
            self.content = content

    @property
    def file_name(self):
        r"""Gets the file_name of this FileContentInfo.

        文件名

        :return: The file_name of this FileContentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this FileContentInfo.

        文件名

        :param file_name: The file_name of this FileContentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this FileContentInfo.

        文件路径

        :return: The file_path of this FileContentInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this FileContentInfo.

        文件路径

        :param file_path: The file_path of this FileContentInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def size(self):
        r"""Gets the size of this FileContentInfo.

        文件大小

        :return: The size of this FileContentInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this FileContentInfo.

        文件大小

        :param size: The size of this FileContentInfo.
        :type size: int
        """
        self._size = size

    @property
    def encoding(self):
        r"""Gets the encoding of this FileContentInfo.

        文件编码

        :return: The encoding of this FileContentInfo.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this FileContentInfo.

        文件编码

        :param encoding: The encoding of this FileContentInfo.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def content_sha256(self):
        r"""Gets the content_sha256 of this FileContentInfo.

        sha256编码的文件内容

        :return: The content_sha256 of this FileContentInfo.
        :rtype: str
        """
        return self._content_sha256

    @content_sha256.setter
    def content_sha256(self, content_sha256):
        r"""Sets the content_sha256 of this FileContentInfo.

        sha256编码的文件内容

        :param content_sha256: The content_sha256 of this FileContentInfo.
        :type content_sha256: str
        """
        self._content_sha256 = content_sha256

    @property
    def ref(self):
        r"""Gets the ref of this FileContentInfo.

        分支名

        :return: The ref of this FileContentInfo.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this FileContentInfo.

        分支名

        :param ref: The ref of this FileContentInfo.
        :type ref: str
        """
        self._ref = ref

    @property
    def blob_id(self):
        r"""Gets the blob_id of this FileContentInfo.

        blob sha

        :return: The blob_id of this FileContentInfo.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this FileContentInfo.

        blob sha

        :param blob_id: The blob_id of this FileContentInfo.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def commit_id(self):
        r"""Gets the commit_id of this FileContentInfo.

        提交对应的SHA id

        :return: The commit_id of this FileContentInfo.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this FileContentInfo.

        提交对应的SHA id

        :param commit_id: The commit_id of this FileContentInfo.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def last_commit_id(self):
        r"""Gets the last_commit_id of this FileContentInfo.

        最后一个提交对应的SHA id

        :return: The last_commit_id of this FileContentInfo.
        :rtype: str
        """
        return self._last_commit_id

    @last_commit_id.setter
    def last_commit_id(self, last_commit_id):
        r"""Sets the last_commit_id of this FileContentInfo.

        最后一个提交对应的SHA id

        :param last_commit_id: The last_commit_id of this FileContentInfo.
        :type last_commit_id: str
        """
        self._last_commit_id = last_commit_id

    @property
    def content(self):
        r"""Gets the content of this FileContentInfo.

        base64编码的文件内容

        :return: The content of this FileContentInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this FileContentInfo.

        base64编码的文件内容

        :param content: The content of this FileContentInfo.
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
        if not isinstance(other, FileContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
