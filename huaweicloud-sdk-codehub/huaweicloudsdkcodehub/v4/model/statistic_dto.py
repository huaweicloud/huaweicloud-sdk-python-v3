# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'project_id': 'int',
        'branch': 'str',
        'user_name': 'str',
        'add_lines': 'int',
        'delete_lines': 'int',
        'commit_count': 'int',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'branch': 'branch',
        'user_name': 'user_name',
        'add_lines': 'add_lines',
        'delete_lines': 'delete_lines',
        'commit_count': 'commit_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, branch=None, user_name=None, add_lines=None, delete_lines=None, commit_count=None, created_at=None, updated_at=None):
        r"""StatisticDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 统计ID。
        :type id: int
        :param project_id: **参数解释：** 仓库ID。
        :type project_id: int
        :param branch: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节
        :type branch: str
        :param user_name: 用户名
        :type user_name: str
        :param add_lines: **参数解释：** 增加行数。
        :type add_lines: int
        :param delete_lines: **参数解释：** 删除行数。
        :type delete_lines: int
        :param commit_count: **参数解释：** 总的提交数量。
        :type commit_count: int
        :param created_at: **参数解释：** 最早提交时间。
        :type created_at: str
        :param updated_at: **参数解释：** 最新更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._project_id = None
        self._branch = None
        self._user_name = None
        self._add_lines = None
        self._delete_lines = None
        self._commit_count = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if branch is not None:
            self.branch = branch
        if user_name is not None:
            self.user_name = user_name
        if add_lines is not None:
            self.add_lines = add_lines
        if delete_lines is not None:
            self.delete_lines = delete_lines
        if commit_count is not None:
            self.commit_count = commit_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this StatisticDto.

        **参数解释：** 统计ID。

        :return: The id of this StatisticDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StatisticDto.

        **参数解释：** 统计ID。

        :param id: The id of this StatisticDto.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this StatisticDto.

        **参数解释：** 仓库ID。

        :return: The project_id of this StatisticDto.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this StatisticDto.

        **参数解释：** 仓库ID。

        :param project_id: The project_id of this StatisticDto.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def branch(self):
        r"""Gets the branch of this StatisticDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :return: The branch of this StatisticDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this StatisticDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :param branch: The branch of this StatisticDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def user_name(self):
        r"""Gets the user_name of this StatisticDto.

        用户名

        :return: The user_name of this StatisticDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this StatisticDto.

        用户名

        :param user_name: The user_name of this StatisticDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def add_lines(self):
        r"""Gets the add_lines of this StatisticDto.

        **参数解释：** 增加行数。

        :return: The add_lines of this StatisticDto.
        :rtype: int
        """
        return self._add_lines

    @add_lines.setter
    def add_lines(self, add_lines):
        r"""Sets the add_lines of this StatisticDto.

        **参数解释：** 增加行数。

        :param add_lines: The add_lines of this StatisticDto.
        :type add_lines: int
        """
        self._add_lines = add_lines

    @property
    def delete_lines(self):
        r"""Gets the delete_lines of this StatisticDto.

        **参数解释：** 删除行数。

        :return: The delete_lines of this StatisticDto.
        :rtype: int
        """
        return self._delete_lines

    @delete_lines.setter
    def delete_lines(self, delete_lines):
        r"""Sets the delete_lines of this StatisticDto.

        **参数解释：** 删除行数。

        :param delete_lines: The delete_lines of this StatisticDto.
        :type delete_lines: int
        """
        self._delete_lines = delete_lines

    @property
    def commit_count(self):
        r"""Gets the commit_count of this StatisticDto.

        **参数解释：** 总的提交数量。

        :return: The commit_count of this StatisticDto.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this StatisticDto.

        **参数解释：** 总的提交数量。

        :param commit_count: The commit_count of this StatisticDto.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def created_at(self):
        r"""Gets the created_at of this StatisticDto.

        **参数解释：** 最早提交时间。

        :return: The created_at of this StatisticDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StatisticDto.

        **参数解释：** 最早提交时间。

        :param created_at: The created_at of this StatisticDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StatisticDto.

        **参数解释：** 最新更新时间。

        :return: The updated_at of this StatisticDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StatisticDto.

        **参数解释：** 最新更新时间。

        :param updated_at: The updated_at of this StatisticDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, StatisticDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
