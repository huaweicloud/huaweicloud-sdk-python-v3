# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoStatisticsEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'branch': 'str',
        'created_at': 'datetime',
        'date': 'str',
        'id': 'int',
        'project_id': 'int',
        'status': 'str',
        'updated_at': 'datetime',
        'user_id': 'int'
    }

    attribute_map = {
        'branch': 'branch',
        'created_at': 'created_at',
        'date': 'date',
        'id': 'id',
        'project_id': 'project_id',
        'status': 'status',
        'updated_at': 'updated_at',
        'user_id': 'user_id'
    }

    def __init__(self, branch=None, created_at=None, date=None, id=None, project_id=None, status=None, updated_at=None, user_id=None):
        """RepoStatisticsEvent

        The model defined in huaweicloud sdk

        :param branch: 分支名
        :type branch: str
        :param created_at: 仓库统计创建的时间
        :type created_at: datetime
        :param date: 仓库统计的日期
        :type date: str
        :param id: 仓库统计事件的id
        :type id: int
        :param project_id: 仓库id
        :type project_id: int
        :param status: 仓库统计的状态: 等待统计waiting  正在统计active  完成统计finish
        :type status: str
        :param updated_at: 仓库统计更新的时间
        :type updated_at: datetime
        :param user_id: 用户id
        :type user_id: int
        """
        
        

        self._branch = None
        self._created_at = None
        self._date = None
        self._id = None
        self._project_id = None
        self._status = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if created_at is not None:
            self.created_at = created_at
        if date is not None:
            self.date = date
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def branch(self):
        """Gets the branch of this RepoStatisticsEvent.

        分支名

        :return: The branch of this RepoStatisticsEvent.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this RepoStatisticsEvent.

        分支名

        :param branch: The branch of this RepoStatisticsEvent.
        :type branch: str
        """
        self._branch = branch

    @property
    def created_at(self):
        """Gets the created_at of this RepoStatisticsEvent.

        仓库统计创建的时间

        :return: The created_at of this RepoStatisticsEvent.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RepoStatisticsEvent.

        仓库统计创建的时间

        :param created_at: The created_at of this RepoStatisticsEvent.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def date(self):
        """Gets the date of this RepoStatisticsEvent.

        仓库统计的日期

        :return: The date of this RepoStatisticsEvent.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RepoStatisticsEvent.

        仓库统计的日期

        :param date: The date of this RepoStatisticsEvent.
        :type date: str
        """
        self._date = date

    @property
    def id(self):
        """Gets the id of this RepoStatisticsEvent.

        仓库统计事件的id

        :return: The id of this RepoStatisticsEvent.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepoStatisticsEvent.

        仓库统计事件的id

        :param id: The id of this RepoStatisticsEvent.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this RepoStatisticsEvent.

        仓库id

        :return: The project_id of this RepoStatisticsEvent.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepoStatisticsEvent.

        仓库id

        :param project_id: The project_id of this RepoStatisticsEvent.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this RepoStatisticsEvent.

        仓库统计的状态: 等待统计waiting  正在统计active  完成统计finish

        :return: The status of this RepoStatisticsEvent.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RepoStatisticsEvent.

        仓库统计的状态: 等待统计waiting  正在统计active  完成统计finish

        :param status: The status of this RepoStatisticsEvent.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this RepoStatisticsEvent.

        仓库统计更新的时间

        :return: The updated_at of this RepoStatisticsEvent.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RepoStatisticsEvent.

        仓库统计更新的时间

        :param updated_at: The updated_at of this RepoStatisticsEvent.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this RepoStatisticsEvent.

        用户id

        :return: The user_id of this RepoStatisticsEvent.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RepoStatisticsEvent.

        用户id

        :param user_id: The user_id of this RepoStatisticsEvent.
        :type user_id: int
        """
        self._user_id = user_id

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
        if not isinstance(other, RepoStatisticsEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
