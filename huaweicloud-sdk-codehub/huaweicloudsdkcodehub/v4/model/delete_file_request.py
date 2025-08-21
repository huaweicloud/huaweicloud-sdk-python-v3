# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'file_path': 'str',
        'author_name': 'str',
        'branch': 'str',
        'commit_message': 'str',
        'author_email': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'file_path': 'file_path',
        'author_name': 'author_name',
        'branch': 'branch',
        'commit_message': 'commit_message',
        'author_email': 'author_email'
    }

    def __init__(self, repository_id=None, file_path=None, author_name=None, branch=None, commit_message=None, author_email=None):
        r"""DeleteFileRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param file_path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type file_path: str
        :param author_name: **参数解释：** 作者名称
        :type author_name: str
        :param branch: **参数解释：** 分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type branch: str
        :param commit_message: **参数解释：** 删除描述。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type commit_message: str
        :param author_email: **参数解释：** 作者邮箱。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type author_email: str
        """
        
        

        self._repository_id = None
        self._file_path = None
        self._author_name = None
        self._branch = None
        self._commit_message = None
        self._author_email = None
        self.discriminator = None

        self.repository_id = repository_id
        self.file_path = file_path
        if author_name is not None:
            self.author_name = author_name
        self.branch = branch
        self.commit_message = commit_message
        if author_email is not None:
            self.author_email = author_email

    @property
    def repository_id(self):
        r"""Gets the repository_id of this DeleteFileRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this DeleteFileRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this DeleteFileRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this DeleteFileRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def file_path(self):
        r"""Gets the file_path of this DeleteFileRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The file_path of this DeleteFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this DeleteFileRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param file_path: The file_path of this DeleteFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def author_name(self):
        r"""Gets the author_name of this DeleteFileRequest.

        **参数解释：** 作者名称

        :return: The author_name of this DeleteFileRequest.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this DeleteFileRequest.

        **参数解释：** 作者名称

        :param author_name: The author_name of this DeleteFileRequest.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def branch(self):
        r"""Gets the branch of this DeleteFileRequest.

        **参数解释：** 分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The branch of this DeleteFileRequest.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this DeleteFileRequest.

        **参数解释：** 分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param branch: The branch of this DeleteFileRequest.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_message(self):
        r"""Gets the commit_message of this DeleteFileRequest.

        **参数解释：** 删除描述。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The commit_message of this DeleteFileRequest.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this DeleteFileRequest.

        **参数解释：** 删除描述。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param commit_message: The commit_message of this DeleteFileRequest.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def author_email(self):
        r"""Gets the author_email of this DeleteFileRequest.

        **参数解释：** 作者邮箱。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The author_email of this DeleteFileRequest.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this DeleteFileRequest.

        **参数解释：** 作者邮箱。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param author_email: The author_email of this DeleteFileRequest.
        :type author_email: str
        """
        self._author_email = author_email

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
        if not isinstance(other, DeleteFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
