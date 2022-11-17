# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectWorkHoursResponseBodyWorkHours:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_name': 'str',
        'nick_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'work_date': 'str',
        'work_hours_num': 'str',
        'summary': 'str',
        'work_hours_type_name': 'str',
        'issue_id': 'int',
        'issue_type': 'str',
        'subject': 'str',
        'created_time': 'str',
        'closed_time': 'str'
    }

    attribute_map = {
        'project_name': 'project_name',
        'nick_name': 'nick_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'work_date': 'work_date',
        'work_hours_num': 'work_hours_num',
        'summary': 'summary',
        'work_hours_type_name': 'work_hours_type_name',
        'issue_id': 'issue_id',
        'issue_type': 'issue_type',
        'subject': 'subject',
        'created_time': 'created_time',
        'closed_time': 'closed_time'
    }

    def __init__(self, project_name=None, nick_name=None, user_id=None, user_name=None, work_date=None, work_hours_num=None, summary=None, work_hours_type_name=None, issue_id=None, issue_type=None, subject=None, created_time=None, closed_time=None):
        """ShowProjectWorkHoursResponseBodyWorkHours

        The model defined in huaweicloud sdk

        :param project_name: 项目名称
        :type project_name: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param work_date: 工时日期
        :type work_date: str
        :param work_hours_num: 工时花费
        :type work_hours_num: str
        :param summary: 工时内容
        :type summary: str
        :param work_hours_type_name: 工时类型
        :type work_hours_type_name: str
        :param issue_id: 工作项id
        :type issue_id: int
        :param issue_type: 工作项类型
        :type issue_type: str
        :param subject: 工作项标题
        :type subject: str
        :param created_time: 工作项创建时间
        :type created_time: str
        :param closed_time: 工作项结束时间
        :type closed_time: str
        """
        
        

        self._project_name = None
        self._nick_name = None
        self._user_id = None
        self._user_name = None
        self._work_date = None
        self._work_hours_num = None
        self._summary = None
        self._work_hours_type_name = None
        self._issue_id = None
        self._issue_type = None
        self._subject = None
        self._created_time = None
        self._closed_time = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if nick_name is not None:
            self.nick_name = nick_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if work_date is not None:
            self.work_date = work_date
        if work_hours_num is not None:
            self.work_hours_num = work_hours_num
        if summary is not None:
            self.summary = summary
        if work_hours_type_name is not None:
            self.work_hours_type_name = work_hours_type_name
        if issue_id is not None:
            self.issue_id = issue_id
        if issue_type is not None:
            self.issue_type = issue_type
        if subject is not None:
            self.subject = subject
        if created_time is not None:
            self.created_time = created_time
        if closed_time is not None:
            self.closed_time = closed_time

    @property
    def project_name(self):
        """Gets the project_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        项目名称

        :return: The project_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        项目名称

        :param project_name: The project_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def nick_name(self):
        """Gets the nick_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户昵称

        :return: The nick_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户昵称

        :param nick_name: The nick_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def user_id(self):
        """Gets the user_id of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户id

        :return: The user_id of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户id

        :param user_id: The user_id of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户名

        :return: The user_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        用户名

        :param user_name: The user_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def work_date(self):
        """Gets the work_date of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时日期

        :return: The work_date of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._work_date

    @work_date.setter
    def work_date(self, work_date):
        """Sets the work_date of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时日期

        :param work_date: The work_date of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type work_date: str
        """
        self._work_date = work_date

    @property
    def work_hours_num(self):
        """Gets the work_hours_num of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时花费

        :return: The work_hours_num of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._work_hours_num

    @work_hours_num.setter
    def work_hours_num(self, work_hours_num):
        """Sets the work_hours_num of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时花费

        :param work_hours_num: The work_hours_num of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type work_hours_num: str
        """
        self._work_hours_num = work_hours_num

    @property
    def summary(self):
        """Gets the summary of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时内容

        :return: The summary of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时内容

        :param summary: The summary of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type summary: str
        """
        self._summary = summary

    @property
    def work_hours_type_name(self):
        """Gets the work_hours_type_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时类型

        :return: The work_hours_type_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._work_hours_type_name

    @work_hours_type_name.setter
    def work_hours_type_name(self, work_hours_type_name):
        """Sets the work_hours_type_name of this ShowProjectWorkHoursResponseBodyWorkHours.

        工时类型

        :param work_hours_type_name: The work_hours_type_name of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type work_hours_type_name: str
        """
        self._work_hours_type_name = work_hours_type_name

    @property
    def issue_id(self):
        """Gets the issue_id of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项id

        :return: The issue_id of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项id

        :param issue_id: The issue_id of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def issue_type(self):
        """Gets the issue_type of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项类型

        :return: The issue_type of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        """Sets the issue_type of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项类型

        :param issue_type: The issue_type of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type issue_type: str
        """
        self._issue_type = issue_type

    @property
    def subject(self):
        """Gets the subject of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项标题

        :return: The subject of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项标题

        :param subject: The subject of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type subject: str
        """
        self._subject = subject

    @property
    def created_time(self):
        """Gets the created_time of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项创建时间

        :return: The created_time of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项创建时间

        :param created_time: The created_time of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def closed_time(self):
        """Gets the closed_time of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项结束时间

        :return: The closed_time of this ShowProjectWorkHoursResponseBodyWorkHours.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        """Sets the closed_time of this ShowProjectWorkHoursResponseBodyWorkHours.

        工作项结束时间

        :param closed_time: The closed_time of this ShowProjectWorkHoursResponseBodyWorkHours.
        :type closed_time: str
        """
        self._closed_time = closed_time

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
        if not isinstance(other, ShowProjectWorkHoursResponseBodyWorkHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
