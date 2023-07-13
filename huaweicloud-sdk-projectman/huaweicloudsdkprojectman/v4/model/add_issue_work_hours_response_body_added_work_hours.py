# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddIssueWorkHoursResponseBodyAddedWorkHours:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_hours_id': 'str',
        'issue_id': 'int',
        'user_name': 'str',
        'user_nick_name': 'str',
        'work_date': 'str',
        'work_hours': 'str',
        'work_hours_type_name': 'str'
    }

    attribute_map = {
        'work_hours_id': 'work_hours_id',
        'issue_id': 'issue_id',
        'user_name': 'user_name',
        'user_nick_name': 'user_nick_name',
        'work_date': 'work_date',
        'work_hours': 'work_hours',
        'work_hours_type_name': 'work_hours_type_name'
    }

    def __init__(self, work_hours_id=None, issue_id=None, user_name=None, user_nick_name=None, work_date=None, work_hours=None, work_hours_type_name=None):
        """AddIssueWorkHoursResponseBodyAddedWorkHours

        The model defined in huaweicloud sdk

        :param work_hours_id: 工时id
        :type work_hours_id: str
        :param issue_id: 工作项id
        :type issue_id: int
        :param user_name: 用户名
        :type user_name: str
        :param user_nick_name: 用户昵称
        :type user_nick_name: str
        :param work_date: 工时日期
        :type work_date: str
        :param work_hours: 工时数
        :type work_hours: str
        :param work_hours_type_name: 工时类型名称
        :type work_hours_type_name: str
        """
        
        

        self._work_hours_id = None
        self._issue_id = None
        self._user_name = None
        self._user_nick_name = None
        self._work_date = None
        self._work_hours = None
        self._work_hours_type_name = None
        self.discriminator = None

        if work_hours_id is not None:
            self.work_hours_id = work_hours_id
        if issue_id is not None:
            self.issue_id = issue_id
        if user_name is not None:
            self.user_name = user_name
        if user_nick_name is not None:
            self.user_nick_name = user_nick_name
        if work_date is not None:
            self.work_date = work_date
        if work_hours is not None:
            self.work_hours = work_hours
        if work_hours_type_name is not None:
            self.work_hours_type_name = work_hours_type_name

    @property
    def work_hours_id(self):
        """Gets the work_hours_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时id

        :return: The work_hours_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._work_hours_id

    @work_hours_id.setter
    def work_hours_id(self, work_hours_id):
        """Sets the work_hours_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时id

        :param work_hours_id: The work_hours_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type work_hours_id: str
        """
        self._work_hours_id = work_hours_id

    @property
    def issue_id(self):
        """Gets the issue_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工作项id

        :return: The issue_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工作项id

        :param issue_id: The issue_id of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def user_name(self):
        """Gets the user_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        用户名

        :return: The user_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        用户名

        :param user_name: The user_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_nick_name(self):
        """Gets the user_nick_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        用户昵称

        :return: The user_nick_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._user_nick_name

    @user_nick_name.setter
    def user_nick_name(self, user_nick_name):
        """Sets the user_nick_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        用户昵称

        :param user_nick_name: The user_nick_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type user_nick_name: str
        """
        self._user_nick_name = user_nick_name

    @property
    def work_date(self):
        """Gets the work_date of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时日期

        :return: The work_date of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._work_date

    @work_date.setter
    def work_date(self, work_date):
        """Sets the work_date of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时日期

        :param work_date: The work_date of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type work_date: str
        """
        self._work_date = work_date

    @property
    def work_hours(self):
        """Gets the work_hours of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时数

        :return: The work_hours of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        """Sets the work_hours of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时数

        :param work_hours: The work_hours of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type work_hours: str
        """
        self._work_hours = work_hours

    @property
    def work_hours_type_name(self):
        """Gets the work_hours_type_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时类型名称

        :return: The work_hours_type_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :rtype: str
        """
        return self._work_hours_type_name

    @work_hours_type_name.setter
    def work_hours_type_name(self, work_hours_type_name):
        """Sets the work_hours_type_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.

        工时类型名称

        :param work_hours_type_name: The work_hours_type_name of this AddIssueWorkHoursResponseBodyAddedWorkHours.
        :type work_hours_type_name: str
        """
        self._work_hours_type_name = work_hours_type_name

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
        if not isinstance(other, AddIssueWorkHoursResponseBodyAddedWorkHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
