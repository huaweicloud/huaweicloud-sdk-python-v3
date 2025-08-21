# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticEventsDto:

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
        'user_id': 'int',
        'project_id': 'int',
        'branch': 'str',
        'status': 'str',
        'stat_date': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'project_id': 'project_id',
        'branch': 'branch',
        'status': 'status',
        'stat_date': 'stat_date',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, user_id=None, project_id=None, branch=None, status=None, stat_date=None, created_at=None, updated_at=None):
        r"""StatisticEventsDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 统计ID。
        :type id: int
        :param user_id: **参数解释：** 用户ID。
        :type user_id: int
        :param project_id: **参数解释：** 仓库ID。
        :type project_id: int
        :param branch: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节
        :type branch: str
        :param status: **参数解释：** 统计状态。
        :type status: str
        :param stat_date: **参数解释：** 统计时间。
        :type stat_date: str
        :param created_at: **参数解释：** 统计创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 统计更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._user_id = None
        self._project_id = None
        self._branch = None
        self._status = None
        self._stat_date = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id
        if branch is not None:
            self.branch = branch
        if status is not None:
            self.status = status
        if stat_date is not None:
            self.stat_date = stat_date
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this StatisticEventsDto.

        **参数解释：** 统计ID。

        :return: The id of this StatisticEventsDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StatisticEventsDto.

        **参数解释：** 统计ID。

        :param id: The id of this StatisticEventsDto.
        :type id: int
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this StatisticEventsDto.

        **参数解释：** 用户ID。

        :return: The user_id of this StatisticEventsDto.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this StatisticEventsDto.

        **参数解释：** 用户ID。

        :param user_id: The user_id of this StatisticEventsDto.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def project_id(self):
        r"""Gets the project_id of this StatisticEventsDto.

        **参数解释：** 仓库ID。

        :return: The project_id of this StatisticEventsDto.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this StatisticEventsDto.

        **参数解释：** 仓库ID。

        :param project_id: The project_id of this StatisticEventsDto.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def branch(self):
        r"""Gets the branch of this StatisticEventsDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :return: The branch of this StatisticEventsDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this StatisticEventsDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节

        :param branch: The branch of this StatisticEventsDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def status(self):
        r"""Gets the status of this StatisticEventsDto.

        **参数解释：** 统计状态。

        :return: The status of this StatisticEventsDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StatisticEventsDto.

        **参数解释：** 统计状态。

        :param status: The status of this StatisticEventsDto.
        :type status: str
        """
        self._status = status

    @property
    def stat_date(self):
        r"""Gets the stat_date of this StatisticEventsDto.

        **参数解释：** 统计时间。

        :return: The stat_date of this StatisticEventsDto.
        :rtype: str
        """
        return self._stat_date

    @stat_date.setter
    def stat_date(self, stat_date):
        r"""Sets the stat_date of this StatisticEventsDto.

        **参数解释：** 统计时间。

        :param stat_date: The stat_date of this StatisticEventsDto.
        :type stat_date: str
        """
        self._stat_date = stat_date

    @property
    def created_at(self):
        r"""Gets the created_at of this StatisticEventsDto.

        **参数解释：** 统计创建时间。

        :return: The created_at of this StatisticEventsDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StatisticEventsDto.

        **参数解释：** 统计创建时间。

        :param created_at: The created_at of this StatisticEventsDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StatisticEventsDto.

        **参数解释：** 统计更新时间。

        :return: The updated_at of this StatisticEventsDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StatisticEventsDto.

        **参数解释：** 统计更新时间。

        :param updated_at: The updated_at of this StatisticEventsDto.
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
        if not isinstance(other, StatisticEventsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
