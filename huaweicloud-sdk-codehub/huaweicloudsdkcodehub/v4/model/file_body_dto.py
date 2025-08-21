# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileBodyDto:

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
        'file_path': 'str',
        'branch': 'str',
        'commit_message': 'str',
        'author_email': 'str',
        'author_name': 'str',
        'content': 'str',
        'encoding': 'str'
    }

    attribute_map = {
        'name': 'name',
        'file_path': 'file_path',
        'branch': 'branch',
        'commit_message': 'commit_message',
        'author_email': 'author_email',
        'author_name': 'author_name',
        'content': 'content',
        'encoding': 'encoding'
    }

    def __init__(self, name=None, file_path=None, branch=None, commit_message=None, author_email=None, author_name=None, content=None, encoding=None):
        r"""FileBodyDto

        The model defined in huaweicloud sdk

        :param name: 用户名
        :type name: str
        :param file_path: 文件路径
        :type file_path: str
        :param branch: 分支名
        :type branch: str
        :param commit_message: 提交信息
        :type commit_message: str
        :param author_email: 作者邮箱
        :type author_email: str
        :param author_name: 作者名称
        :type author_name: str
        :param content: 文件内容
        :type content: str
        :param encoding: 编码方式
        :type encoding: str
        """
        
        

        self._name = None
        self._file_path = None
        self._branch = None
        self._commit_message = None
        self._author_email = None
        self._author_name = None
        self._content = None
        self._encoding = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.file_path = file_path
        self.branch = branch
        self.commit_message = commit_message
        if author_email is not None:
            self.author_email = author_email
        if author_name is not None:
            self.author_name = author_name
        self.content = content
        if encoding is not None:
            self.encoding = encoding

    @property
    def name(self):
        r"""Gets the name of this FileBodyDto.

        用户名

        :return: The name of this FileBodyDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FileBodyDto.

        用户名

        :param name: The name of this FileBodyDto.
        :type name: str
        """
        self._name = name

    @property
    def file_path(self):
        r"""Gets the file_path of this FileBodyDto.

        文件路径

        :return: The file_path of this FileBodyDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this FileBodyDto.

        文件路径

        :param file_path: The file_path of this FileBodyDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def branch(self):
        r"""Gets the branch of this FileBodyDto.

        分支名

        :return: The branch of this FileBodyDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this FileBodyDto.

        分支名

        :param branch: The branch of this FileBodyDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_message(self):
        r"""Gets the commit_message of this FileBodyDto.

        提交信息

        :return: The commit_message of this FileBodyDto.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this FileBodyDto.

        提交信息

        :param commit_message: The commit_message of this FileBodyDto.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def author_email(self):
        r"""Gets the author_email of this FileBodyDto.

        作者邮箱

        :return: The author_email of this FileBodyDto.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this FileBodyDto.

        作者邮箱

        :param author_email: The author_email of this FileBodyDto.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def author_name(self):
        r"""Gets the author_name of this FileBodyDto.

        作者名称

        :return: The author_name of this FileBodyDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this FileBodyDto.

        作者名称

        :param author_name: The author_name of this FileBodyDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def content(self):
        r"""Gets the content of this FileBodyDto.

        文件内容

        :return: The content of this FileBodyDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this FileBodyDto.

        文件内容

        :param content: The content of this FileBodyDto.
        :type content: str
        """
        self._content = content

    @property
    def encoding(self):
        r"""Gets the encoding of this FileBodyDto.

        编码方式

        :return: The encoding of this FileBodyDto.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this FileBodyDto.

        编码方式

        :param encoding: The encoding of this FileBodyDto.
        :type encoding: str
        """
        self._encoding = encoding

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
        if not isinstance(other, FileBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
