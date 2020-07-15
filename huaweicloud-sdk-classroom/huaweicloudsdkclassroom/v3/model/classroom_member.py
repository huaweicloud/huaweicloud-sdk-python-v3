# coding: utf-8

import pprint
import re

import six





class ClassroomMember:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'member_id': 'str',
        'name': 'str',
        'number': 'str',
        'class_name': 'str',
        'user_name': 'str',
        'join_time': 'str',
        'job_received_count': 'int',
        'job_finished_count': 'int',
        'job_finished_rate': 'float'
    }

    attribute_map = {
        'member_id': 'member_id',
        'name': 'name',
        'number': 'number',
        'class_name': 'class_name',
        'user_name': 'user_name',
        'join_time': 'join_time',
        'job_received_count': 'job_received_count',
        'job_finished_count': 'job_finished_count',
        'job_finished_rate': 'job_finished_rate'
    }

    def __init__(self, member_id=None, name=None, number=None, class_name=None, user_name=None, join_time=None, job_received_count=None, job_finished_count=None, job_finished_rate=None):
        """ClassroomMember - a model defined in huaweicloud sdk"""
        
        

        self._member_id = None
        self._name = None
        self._number = None
        self._class_name = None
        self._user_name = None
        self._join_time = None
        self._job_received_count = None
        self._job_finished_count = None
        self._job_finished_rate = None
        self.discriminator = None

        self.member_id = member_id
        self.name = name
        self.number = number
        self.class_name = class_name
        self.user_name = user_name
        self.join_time = join_time
        self.job_received_count = job_received_count
        self.job_finished_count = job_finished_count
        self.job_finished_rate = job_finished_rate

    @property
    def member_id(self):
        """Gets the member_id of this ClassroomMember.

        成员ID

        :return: The member_id of this ClassroomMember.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ClassroomMember.

        成员ID

        :param member_id: The member_id of this ClassroomMember.
        :type: str
        """
        self._member_id = member_id

    @property
    def name(self):
        """Gets the name of this ClassroomMember.

        成员名称

        :return: The name of this ClassroomMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClassroomMember.

        成员名称

        :param name: The name of this ClassroomMember.
        :type: str
        """
        self._name = name

    @property
    def number(self):
        """Gets the number of this ClassroomMember.

        成员学号/工号

        :return: The number of this ClassroomMember.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ClassroomMember.

        成员学号/工号

        :param number: The number of this ClassroomMember.
        :type: str
        """
        self._number = number

    @property
    def class_name(self):
        """Gets the class_name of this ClassroomMember.

        成员所在班级的名字

        :return: The class_name of this ClassroomMember.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this ClassroomMember.

        成员所在班级的名字

        :param class_name: The class_name of this ClassroomMember.
        :type: str
        """
        self._class_name = class_name

    @property
    def user_name(self):
        """Gets the user_name of this ClassroomMember.

        成员用户名

        :return: The user_name of this ClassroomMember.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ClassroomMember.

        成员用户名

        :param user_name: The user_name of this ClassroomMember.
        :type: str
        """
        self._user_name = user_name

    @property
    def join_time(self):
        """Gets the join_time of this ClassroomMember.

        成员加入课堂时间，日期格式：yyyy-MM-dd HH:mm:ss

        :return: The join_time of this ClassroomMember.
        :rtype: str
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this ClassroomMember.

        成员加入课堂时间，日期格式：yyyy-MM-dd HH:mm:ss

        :param join_time: The join_time of this ClassroomMember.
        :type: str
        """
        self._join_time = join_time

    @property
    def job_received_count(self):
        """Gets the job_received_count of this ClassroomMember.

        该成员已接收到的作业数量

        :return: The job_received_count of this ClassroomMember.
        :rtype: int
        """
        return self._job_received_count

    @job_received_count.setter
    def job_received_count(self, job_received_count):
        """Sets the job_received_count of this ClassroomMember.

        该成员已接收到的作业数量

        :param job_received_count: The job_received_count of this ClassroomMember.
        :type: int
        """
        self._job_received_count = job_received_count

    @property
    def job_finished_count(self):
        """Gets the job_finished_count of this ClassroomMember.

        该成员已完成的作业数量

        :return: The job_finished_count of this ClassroomMember.
        :rtype: int
        """
        return self._job_finished_count

    @job_finished_count.setter
    def job_finished_count(self, job_finished_count):
        """Sets the job_finished_count of this ClassroomMember.

        该成员已完成的作业数量

        :param job_finished_count: The job_finished_count of this ClassroomMember.
        :type: int
        """
        self._job_finished_count = job_finished_count

    @property
    def job_finished_rate(self):
        """Gets the job_finished_rate of this ClassroomMember.

        该成员作业完成率

        :return: The job_finished_rate of this ClassroomMember.
        :rtype: float
        """
        return self._job_finished_rate

    @job_finished_rate.setter
    def job_finished_rate(self, job_finished_rate):
        """Sets the job_finished_rate of this ClassroomMember.

        该成员作业完成率

        :param job_finished_rate: The job_finished_rate of this ClassroomMember.
        :type: float
        """
        self._job_finished_rate = job_finished_rate

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClassroomMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
