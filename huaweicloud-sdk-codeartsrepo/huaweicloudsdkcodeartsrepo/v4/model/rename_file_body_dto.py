# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenameFileBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'branch_name': 'str',
        'commit_message': 'str',
        'start_branch': 'str',
        'author_email': 'str',
        'author_name': 'str',
        'previous_path': 'str',
        'infer_content': 'bool',
        'content': 'str',
        'encoding': 'str',
        'last_commit_id': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'branch_name': 'branch_name',
        'commit_message': 'commit_message',
        'start_branch': 'start_branch',
        'author_email': 'author_email',
        'author_name': 'author_name',
        'previous_path': 'previous_path',
        'infer_content': 'infer_content',
        'content': 'content',
        'encoding': 'encoding',
        'last_commit_id': 'last_commit_id'
    }

    def __init__(self, file_path=None, branch_name=None, commit_message=None, start_branch=None, author_email=None, author_name=None, previous_path=None, infer_content=None, content=None, encoding=None, last_commit_id=None):
        r"""RenameFileBodyDto

        The model defined in huaweicloud sdk

        :param file_path: **参数解释：** 文件路径 **取值范围：** 不涉及。
        :type file_path: str
        :param branch_name: **参数解释：** 分支名 **取值范围：** 不涉及。
        :type branch_name: str
        :param commit_message: **参数解释：** 提交信息 **取值范围：** 不涉及。
        :type commit_message: str
        :param start_branch: **参数解释：** 基于分支名（即基于某分支，向其他分支进行推送） **取值范围：** 不涉及。
        :type start_branch: str
        :param author_email: **参数解释：** 作者邮箱 **取值范围：** 不涉及。
        :type author_email: str
        :param author_name: **参数解释：** 作者名称 **取值范围：** 不涉及。
        :type author_name: str
        :param previous_path: **参数解释：** 改名前地址 **取值范围：** 不涉及。
        :type previous_path: str
        :param infer_content: **参数解释：** 是否迁移内容（与content字段不能同时为空） **取值范围：** 不涉及。
        :type infer_content: bool
        :param content: **参数解释：** 文件内容（与infer_content字段不能同时为空） **取值范围：** 不涉及。
        :type content: str
        :param encoding: **参数解释：** 编码方式。 **取值范围：** - text。 - base64.
        :type encoding: str
        :param last_commit_id: **参数解释：** 上次已知的文件提交ID。 **取值范围：** 不涉及。
        :type last_commit_id: str
        """
        
        

        self._file_path = None
        self._branch_name = None
        self._commit_message = None
        self._start_branch = None
        self._author_email = None
        self._author_name = None
        self._previous_path = None
        self._infer_content = None
        self._content = None
        self._encoding = None
        self._last_commit_id = None
        self.discriminator = None

        self.file_path = file_path
        self.branch_name = branch_name
        self.commit_message = commit_message
        if start_branch is not None:
            self.start_branch = start_branch
        if author_email is not None:
            self.author_email = author_email
        if author_name is not None:
            self.author_name = author_name
        self.previous_path = previous_path
        if infer_content is not None:
            self.infer_content = infer_content
        if content is not None:
            self.content = content
        if encoding is not None:
            self.encoding = encoding
        if last_commit_id is not None:
            self.last_commit_id = last_commit_id

    @property
    def file_path(self):
        r"""Gets the file_path of this RenameFileBodyDto.

        **参数解释：** 文件路径 **取值范围：** 不涉及。

        :return: The file_path of this RenameFileBodyDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this RenameFileBodyDto.

        **参数解释：** 文件路径 **取值范围：** 不涉及。

        :param file_path: The file_path of this RenameFileBodyDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def branch_name(self):
        r"""Gets the branch_name of this RenameFileBodyDto.

        **参数解释：** 分支名 **取值范围：** 不涉及。

        :return: The branch_name of this RenameFileBodyDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this RenameFileBodyDto.

        **参数解释：** 分支名 **取值范围：** 不涉及。

        :param branch_name: The branch_name of this RenameFileBodyDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def commit_message(self):
        r"""Gets the commit_message of this RenameFileBodyDto.

        **参数解释：** 提交信息 **取值范围：** 不涉及。

        :return: The commit_message of this RenameFileBodyDto.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this RenameFileBodyDto.

        **参数解释：** 提交信息 **取值范围：** 不涉及。

        :param commit_message: The commit_message of this RenameFileBodyDto.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def start_branch(self):
        r"""Gets the start_branch of this RenameFileBodyDto.

        **参数解释：** 基于分支名（即基于某分支，向其他分支进行推送） **取值范围：** 不涉及。

        :return: The start_branch of this RenameFileBodyDto.
        :rtype: str
        """
        return self._start_branch

    @start_branch.setter
    def start_branch(self, start_branch):
        r"""Sets the start_branch of this RenameFileBodyDto.

        **参数解释：** 基于分支名（即基于某分支，向其他分支进行推送） **取值范围：** 不涉及。

        :param start_branch: The start_branch of this RenameFileBodyDto.
        :type start_branch: str
        """
        self._start_branch = start_branch

    @property
    def author_email(self):
        r"""Gets the author_email of this RenameFileBodyDto.

        **参数解释：** 作者邮箱 **取值范围：** 不涉及。

        :return: The author_email of this RenameFileBodyDto.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this RenameFileBodyDto.

        **参数解释：** 作者邮箱 **取值范围：** 不涉及。

        :param author_email: The author_email of this RenameFileBodyDto.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def author_name(self):
        r"""Gets the author_name of this RenameFileBodyDto.

        **参数解释：** 作者名称 **取值范围：** 不涉及。

        :return: The author_name of this RenameFileBodyDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this RenameFileBodyDto.

        **参数解释：** 作者名称 **取值范围：** 不涉及。

        :param author_name: The author_name of this RenameFileBodyDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def previous_path(self):
        r"""Gets the previous_path of this RenameFileBodyDto.

        **参数解释：** 改名前地址 **取值范围：** 不涉及。

        :return: The previous_path of this RenameFileBodyDto.
        :rtype: str
        """
        return self._previous_path

    @previous_path.setter
    def previous_path(self, previous_path):
        r"""Sets the previous_path of this RenameFileBodyDto.

        **参数解释：** 改名前地址 **取值范围：** 不涉及。

        :param previous_path: The previous_path of this RenameFileBodyDto.
        :type previous_path: str
        """
        self._previous_path = previous_path

    @property
    def infer_content(self):
        r"""Gets the infer_content of this RenameFileBodyDto.

        **参数解释：** 是否迁移内容（与content字段不能同时为空） **取值范围：** 不涉及。

        :return: The infer_content of this RenameFileBodyDto.
        :rtype: bool
        """
        return self._infer_content

    @infer_content.setter
    def infer_content(self, infer_content):
        r"""Sets the infer_content of this RenameFileBodyDto.

        **参数解释：** 是否迁移内容（与content字段不能同时为空） **取值范围：** 不涉及。

        :param infer_content: The infer_content of this RenameFileBodyDto.
        :type infer_content: bool
        """
        self._infer_content = infer_content

    @property
    def content(self):
        r"""Gets the content of this RenameFileBodyDto.

        **参数解释：** 文件内容（与infer_content字段不能同时为空） **取值范围：** 不涉及。

        :return: The content of this RenameFileBodyDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this RenameFileBodyDto.

        **参数解释：** 文件内容（与infer_content字段不能同时为空） **取值范围：** 不涉及。

        :param content: The content of this RenameFileBodyDto.
        :type content: str
        """
        self._content = content

    @property
    def encoding(self):
        r"""Gets the encoding of this RenameFileBodyDto.

        **参数解释：** 编码方式。 **取值范围：** - text。 - base64.

        :return: The encoding of this RenameFileBodyDto.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this RenameFileBodyDto.

        **参数解释：** 编码方式。 **取值范围：** - text。 - base64.

        :param encoding: The encoding of this RenameFileBodyDto.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def last_commit_id(self):
        r"""Gets the last_commit_id of this RenameFileBodyDto.

        **参数解释：** 上次已知的文件提交ID。 **取值范围：** 不涉及。

        :return: The last_commit_id of this RenameFileBodyDto.
        :rtype: str
        """
        return self._last_commit_id

    @last_commit_id.setter
    def last_commit_id(self, last_commit_id):
        r"""Sets the last_commit_id of this RenameFileBodyDto.

        **参数解释：** 上次已知的文件提交ID。 **取值范围：** 不涉及。

        :param last_commit_id: The last_commit_id of this RenameFileBodyDto.
        :type last_commit_id: str
        """
        self._last_commit_id = last_commit_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenameFileBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
