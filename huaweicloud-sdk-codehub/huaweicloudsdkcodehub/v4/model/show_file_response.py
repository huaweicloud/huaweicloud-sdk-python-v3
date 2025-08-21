# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'path': 'str',
        'size': 'int',
        'encoding': 'str',
        'ref': 'str',
        'blob_id': 'str',
        'file_type': 'str',
        'commit': 'RepositoryCommitDto',
        'content': 'str',
        'is_limited': 'bool',
        'content_sha256': 'str',
        'last_commit_id': 'str',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str',
        'x_total': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'size': 'size',
        'encoding': 'encoding',
        'ref': 'ref',
        'blob_id': 'blob_id',
        'file_type': 'file_type',
        'commit': 'commit',
        'content': 'content',
        'is_limited': 'is_limited',
        'content_sha256': 'content_sha256',
        'last_commit_id': 'last_commit_id',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name',
        'x_total': 'X-Total'
    }

    def __init__(self, name=None, path=None, size=None, encoding=None, ref=None, blob_id=None, file_type=None, commit=None, content=None, is_limited=None, content_sha256=None, last_commit_id=None, nick_name=None, tenant_name=None, user_name=None, x_total=None):
        r"""ShowFileResponse

        The model defined in huaweicloud sdk

        :param name: 文件名称
        :type name: str
        :param path: 文件路径
        :type path: str
        :param size: 文件大小
        :type size: int
        :param encoding: 文件编码方式
        :type encoding: str
        :param ref: 分支名称、tag名称或者commitid
        :type ref: str
        :param blob_id: 文件标识
        :type blob_id: str
        :param file_type: 文件类型
        :type file_type: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        :param content: 文件内容
        :type content: str
        :param is_limited: **参数解释：** 文件是否受限。 **取值范围：** - false, 不受限。 - true, 受限。
        :type is_limited: bool
        :param content_sha256: sha256值
        :type content_sha256: str
        :param last_commit_id: 最新提交commitid
        :type last_commit_id: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param user_name: 用户名称
        :type user_name: str
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowFileResponse, self).__init__()

        self._name = None
        self._path = None
        self._size = None
        self._encoding = None
        self._ref = None
        self._blob_id = None
        self._file_type = None
        self._commit = None
        self._content = None
        self._is_limited = None
        self._content_sha256 = None
        self._last_commit_id = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self._x_total = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
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
        if commit is not None:
            self.commit = commit
        if content is not None:
            self.content = content
        if is_limited is not None:
            self.is_limited = is_limited
        if content_sha256 is not None:
            self.content_sha256 = content_sha256
        if last_commit_id is not None:
            self.last_commit_id = last_commit_id
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name
        if x_total is not None:
            self.x_total = x_total

    @property
    def name(self):
        r"""Gets the name of this ShowFileResponse.

        文件名称

        :return: The name of this ShowFileResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFileResponse.

        文件名称

        :param name: The name of this ShowFileResponse.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this ShowFileResponse.

        文件路径

        :return: The path of this ShowFileResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowFileResponse.

        文件路径

        :param path: The path of this ShowFileResponse.
        :type path: str
        """
        self._path = path

    @property
    def size(self):
        r"""Gets the size of this ShowFileResponse.

        文件大小

        :return: The size of this ShowFileResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowFileResponse.

        文件大小

        :param size: The size of this ShowFileResponse.
        :type size: int
        """
        self._size = size

    @property
    def encoding(self):
        r"""Gets the encoding of this ShowFileResponse.

        文件编码方式

        :return: The encoding of this ShowFileResponse.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this ShowFileResponse.

        文件编码方式

        :param encoding: The encoding of this ShowFileResponse.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def ref(self):
        r"""Gets the ref of this ShowFileResponse.

        分支名称、tag名称或者commitid

        :return: The ref of this ShowFileResponse.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this ShowFileResponse.

        分支名称、tag名称或者commitid

        :param ref: The ref of this ShowFileResponse.
        :type ref: str
        """
        self._ref = ref

    @property
    def blob_id(self):
        r"""Gets the blob_id of this ShowFileResponse.

        文件标识

        :return: The blob_id of this ShowFileResponse.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this ShowFileResponse.

        文件标识

        :param blob_id: The blob_id of this ShowFileResponse.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def file_type(self):
        r"""Gets the file_type of this ShowFileResponse.

        文件类型

        :return: The file_type of this ShowFileResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ShowFileResponse.

        文件类型

        :param file_type: The file_type of this ShowFileResponse.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def commit(self):
        r"""Gets the commit of this ShowFileResponse.

        :return: The commit of this ShowFileResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this ShowFileResponse.

        :param commit: The commit of this ShowFileResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        """
        self._commit = commit

    @property
    def content(self):
        r"""Gets the content of this ShowFileResponse.

        文件内容

        :return: The content of this ShowFileResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowFileResponse.

        文件内容

        :param content: The content of this ShowFileResponse.
        :type content: str
        """
        self._content = content

    @property
    def is_limited(self):
        r"""Gets the is_limited of this ShowFileResponse.

        **参数解释：** 文件是否受限。 **取值范围：** - false, 不受限。 - true, 受限。

        :return: The is_limited of this ShowFileResponse.
        :rtype: bool
        """
        return self._is_limited

    @is_limited.setter
    def is_limited(self, is_limited):
        r"""Sets the is_limited of this ShowFileResponse.

        **参数解释：** 文件是否受限。 **取值范围：** - false, 不受限。 - true, 受限。

        :param is_limited: The is_limited of this ShowFileResponse.
        :type is_limited: bool
        """
        self._is_limited = is_limited

    @property
    def content_sha256(self):
        r"""Gets the content_sha256 of this ShowFileResponse.

        sha256值

        :return: The content_sha256 of this ShowFileResponse.
        :rtype: str
        """
        return self._content_sha256

    @content_sha256.setter
    def content_sha256(self, content_sha256):
        r"""Sets the content_sha256 of this ShowFileResponse.

        sha256值

        :param content_sha256: The content_sha256 of this ShowFileResponse.
        :type content_sha256: str
        """
        self._content_sha256 = content_sha256

    @property
    def last_commit_id(self):
        r"""Gets the last_commit_id of this ShowFileResponse.

        最新提交commitid

        :return: The last_commit_id of this ShowFileResponse.
        :rtype: str
        """
        return self._last_commit_id

    @last_commit_id.setter
    def last_commit_id(self, last_commit_id):
        r"""Sets the last_commit_id of this ShowFileResponse.

        最新提交commitid

        :param last_commit_id: The last_commit_id of this ShowFileResponse.
        :type last_commit_id: str
        """
        self._last_commit_id = last_commit_id

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ShowFileResponse.

        用户昵称

        :return: The nick_name of this ShowFileResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ShowFileResponse.

        用户昵称

        :param nick_name: The nick_name of this ShowFileResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ShowFileResponse.

        租户名称

        :return: The tenant_name of this ShowFileResponse.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ShowFileResponse.

        租户名称

        :param tenant_name: The tenant_name of this ShowFileResponse.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowFileResponse.

        用户名称

        :return: The user_name of this ShowFileResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowFileResponse.

        用户名称

        :param user_name: The user_name of this ShowFileResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowFileResponse.

        :return: The x_total of this ShowFileResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowFileResponse.

        :param x_total: The x_total of this ShowFileResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
