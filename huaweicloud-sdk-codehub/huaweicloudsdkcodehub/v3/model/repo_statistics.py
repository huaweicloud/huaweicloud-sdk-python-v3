# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_lines': 'int',
        'branch': 'str',
        'commit_count': 'int',
        'created_at': 'datetime',
        'delete_lines': 'int',
        'id': 'int',
        'project_id': 'int',
        'updated_at': 'datetime',
        'user_name': 'str'
    }

    attribute_map = {
        'add_lines': 'add_lines',
        'branch': 'branch',
        'commit_count': 'commit_count',
        'created_at': 'created_at',
        'delete_lines': 'delete_lines',
        'id': 'id',
        'project_id': 'project_id',
        'updated_at': 'updated_at',
        'user_name': 'user_name'
    }

    def __init__(self, add_lines=None, branch=None, commit_count=None, created_at=None, delete_lines=None, id=None, project_id=None, updated_at=None, user_name=None):
        r"""RepoStatistics

        The model defined in huaweicloud sdk

        :param add_lines: 添加代码行
        :type add_lines: int
        :param branch: 分支名
        :type branch: str
        :param commit_count: 提交次数
        :type commit_count: int
        :param created_at: 仓库统计创建的时间
        :type created_at: datetime
        :param delete_lines: 删除代码行
        :type delete_lines: int
        :param id: 仓库统计记录id
        :type id: int
        :param project_id: 仓库id
        :type project_id: int
        :param updated_at: 仓库统计更新的时间
        :type updated_at: datetime
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._add_lines = None
        self._branch = None
        self._commit_count = None
        self._created_at = None
        self._delete_lines = None
        self._id = None
        self._project_id = None
        self._updated_at = None
        self._user_name = None
        self.discriminator = None

        if add_lines is not None:
            self.add_lines = add_lines
        if branch is not None:
            self.branch = branch
        if commit_count is not None:
            self.commit_count = commit_count
        if created_at is not None:
            self.created_at = created_at
        if delete_lines is not None:
            self.delete_lines = delete_lines
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if updated_at is not None:
            self.updated_at = updated_at
        if user_name is not None:
            self.user_name = user_name

    @property
    def add_lines(self):
        r"""Gets the add_lines of this RepoStatistics.

        添加代码行

        :return: The add_lines of this RepoStatistics.
        :rtype: int
        """
        return self._add_lines

    @add_lines.setter
    def add_lines(self, add_lines):
        r"""Sets the add_lines of this RepoStatistics.

        添加代码行

        :param add_lines: The add_lines of this RepoStatistics.
        :type add_lines: int
        """
        self._add_lines = add_lines

    @property
    def branch(self):
        r"""Gets the branch of this RepoStatistics.

        分支名

        :return: The branch of this RepoStatistics.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this RepoStatistics.

        分支名

        :param branch: The branch of this RepoStatistics.
        :type branch: str
        """
        self._branch = branch

    @property
    def commit_count(self):
        r"""Gets the commit_count of this RepoStatistics.

        提交次数

        :return: The commit_count of this RepoStatistics.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this RepoStatistics.

        提交次数

        :param commit_count: The commit_count of this RepoStatistics.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def created_at(self):
        r"""Gets the created_at of this RepoStatistics.

        仓库统计创建的时间

        :return: The created_at of this RepoStatistics.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RepoStatistics.

        仓库统计创建的时间

        :param created_at: The created_at of this RepoStatistics.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def delete_lines(self):
        r"""Gets the delete_lines of this RepoStatistics.

        删除代码行

        :return: The delete_lines of this RepoStatistics.
        :rtype: int
        """
        return self._delete_lines

    @delete_lines.setter
    def delete_lines(self, delete_lines):
        r"""Sets the delete_lines of this RepoStatistics.

        删除代码行

        :param delete_lines: The delete_lines of this RepoStatistics.
        :type delete_lines: int
        """
        self._delete_lines = delete_lines

    @property
    def id(self):
        r"""Gets the id of this RepoStatistics.

        仓库统计记录id

        :return: The id of this RepoStatistics.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepoStatistics.

        仓库统计记录id

        :param id: The id of this RepoStatistics.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this RepoStatistics.

        仓库id

        :return: The project_id of this RepoStatistics.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepoStatistics.

        仓库id

        :param project_id: The project_id of this RepoStatistics.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RepoStatistics.

        仓库统计更新的时间

        :return: The updated_at of this RepoStatistics.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RepoStatistics.

        仓库统计更新的时间

        :param updated_at: The updated_at of this RepoStatistics.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def user_name(self):
        r"""Gets the user_name of this RepoStatistics.

        用户名

        :return: The user_name of this RepoStatistics.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RepoStatistics.

        用户名

        :param user_name: The user_name of this RepoStatistics.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, RepoStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
