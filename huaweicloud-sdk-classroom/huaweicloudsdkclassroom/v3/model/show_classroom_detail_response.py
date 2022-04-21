# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClassroomDetailResponse(SdkResponse):

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
        'description': 'str',
        'announcement': 'str',
        'announcement_time': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'teacher': 'str',
        'credit': 'float',
        'start_time': 'str',
        'end_time': 'str',
        'role': 'str',
        'school': 'str',
        'content_count': 'int',
        'courseware_count': 'int',
        'job_count': 'int',
        'member_count': 'int',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'announcement': 'announcement',
        'announcement_time': 'announcement_time',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'teacher': 'teacher',
        'credit': 'credit',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'role': 'role',
        'school': 'school',
        'content_count': 'content_count',
        'courseware_count': 'courseware_count',
        'job_count': 'job_count',
        'member_count': 'member_count',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, announcement=None, announcement_time=None, create_time=None, update_time=None, teacher=None, credit=None, start_time=None, end_time=None, role=None, school=None, content_count=None, courseware_count=None, job_count=None, member_count=None, status=None):
        """ShowClassroomDetailResponse

        The model defined in huaweicloud sdk

        :param name: 课堂名称
        :type name: str
        :param description: 课堂描述
        :type description: str
        :param announcement: 课堂公告
        :type announcement: str
        :param announcement_time: 课堂公告创建时间，日期格式：yyyy-MM-dd
        :type announcement_time: str
        :param create_time: 课堂创建时间，日期格式：yyyy-MM-dd HH:mm:ss
        :type create_time: str
        :param update_time: 课堂最新更新时间，日期格式：yyyy-MM-dd HH:mm:ss
        :type update_time: str
        :param teacher: 当前课堂的授课人
        :type teacher: str
        :param credit: 课堂学分
        :type credit: float
        :param start_time: 课堂开始时间，日期格式：yyyy-MM-dd HH:mm:ss
        :type start_time: str
        :param end_time: 课堂结束时间，日期格式：yyyy-MM-dd HH:mm:ss
        :type end_time: str
        :param role: 当前用户在课堂下角色，取值范围：teacher：老师，student：学生
        :type role: str
        :param school: 授课学校
        :type school: str
        :param content_count: 课堂下目录数量
        :type content_count: int
        :param courseware_count: 课堂下课件数量
        :type courseware_count: int
        :param job_count: 课堂下作业数量
        :type job_count: int
        :param member_count: 课堂下成员数量
        :type member_count: int
        :param status: 课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档
        :type status: str
        """
        
        super(ShowClassroomDetailResponse, self).__init__()

        self._name = None
        self._description = None
        self._announcement = None
        self._announcement_time = None
        self._create_time = None
        self._update_time = None
        self._teacher = None
        self._credit = None
        self._start_time = None
        self._end_time = None
        self._role = None
        self._school = None
        self._content_count = None
        self._courseware_count = None
        self._job_count = None
        self._member_count = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if announcement is not None:
            self.announcement = announcement
        if announcement_time is not None:
            self.announcement_time = announcement_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if teacher is not None:
            self.teacher = teacher
        if credit is not None:
            self.credit = credit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if role is not None:
            self.role = role
        if school is not None:
            self.school = school
        if content_count is not None:
            self.content_count = content_count
        if courseware_count is not None:
            self.courseware_count = courseware_count
        if job_count is not None:
            self.job_count = job_count
        if member_count is not None:
            self.member_count = member_count
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this ShowClassroomDetailResponse.

        课堂名称

        :return: The name of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowClassroomDetailResponse.

        课堂名称

        :param name: The name of this ShowClassroomDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowClassroomDetailResponse.

        课堂描述

        :return: The description of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowClassroomDetailResponse.

        课堂描述

        :param description: The description of this ShowClassroomDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def announcement(self):
        """Gets the announcement of this ShowClassroomDetailResponse.

        课堂公告

        :return: The announcement of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._announcement

    @announcement.setter
    def announcement(self, announcement):
        """Sets the announcement of this ShowClassroomDetailResponse.

        课堂公告

        :param announcement: The announcement of this ShowClassroomDetailResponse.
        :type announcement: str
        """
        self._announcement = announcement

    @property
    def announcement_time(self):
        """Gets the announcement_time of this ShowClassroomDetailResponse.

        课堂公告创建时间，日期格式：yyyy-MM-dd

        :return: The announcement_time of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._announcement_time

    @announcement_time.setter
    def announcement_time(self, announcement_time):
        """Sets the announcement_time of this ShowClassroomDetailResponse.

        课堂公告创建时间，日期格式：yyyy-MM-dd

        :param announcement_time: The announcement_time of this ShowClassroomDetailResponse.
        :type announcement_time: str
        """
        self._announcement_time = announcement_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowClassroomDetailResponse.

        课堂创建时间，日期格式：yyyy-MM-dd HH:mm:ss

        :return: The create_time of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowClassroomDetailResponse.

        课堂创建时间，日期格式：yyyy-MM-dd HH:mm:ss

        :param create_time: The create_time of this ShowClassroomDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowClassroomDetailResponse.

        课堂最新更新时间，日期格式：yyyy-MM-dd HH:mm:ss

        :return: The update_time of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowClassroomDetailResponse.

        课堂最新更新时间，日期格式：yyyy-MM-dd HH:mm:ss

        :param update_time: The update_time of this ShowClassroomDetailResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def teacher(self):
        """Gets the teacher of this ShowClassroomDetailResponse.

        当前课堂的授课人

        :return: The teacher of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        """Sets the teacher of this ShowClassroomDetailResponse.

        当前课堂的授课人

        :param teacher: The teacher of this ShowClassroomDetailResponse.
        :type teacher: str
        """
        self._teacher = teacher

    @property
    def credit(self):
        """Gets the credit of this ShowClassroomDetailResponse.

        课堂学分

        :return: The credit of this ShowClassroomDetailResponse.
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this ShowClassroomDetailResponse.

        课堂学分

        :param credit: The credit of this ShowClassroomDetailResponse.
        :type credit: float
        """
        self._credit = credit

    @property
    def start_time(self):
        """Gets the start_time of this ShowClassroomDetailResponse.

        课堂开始时间，日期格式：yyyy-MM-dd HH:mm:ss

        :return: The start_time of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowClassroomDetailResponse.

        课堂开始时间，日期格式：yyyy-MM-dd HH:mm:ss

        :param start_time: The start_time of this ShowClassroomDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowClassroomDetailResponse.

        课堂结束时间，日期格式：yyyy-MM-dd HH:mm:ss

        :return: The end_time of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowClassroomDetailResponse.

        课堂结束时间，日期格式：yyyy-MM-dd HH:mm:ss

        :param end_time: The end_time of this ShowClassroomDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def role(self):
        """Gets the role of this ShowClassroomDetailResponse.

        当前用户在课堂下角色，取值范围：teacher：老师，student：学生

        :return: The role of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ShowClassroomDetailResponse.

        当前用户在课堂下角色，取值范围：teacher：老师，student：学生

        :param role: The role of this ShowClassroomDetailResponse.
        :type role: str
        """
        self._role = role

    @property
    def school(self):
        """Gets the school of this ShowClassroomDetailResponse.

        授课学校

        :return: The school of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this ShowClassroomDetailResponse.

        授课学校

        :param school: The school of this ShowClassroomDetailResponse.
        :type school: str
        """
        self._school = school

    @property
    def content_count(self):
        """Gets the content_count of this ShowClassroomDetailResponse.

        课堂下目录数量

        :return: The content_count of this ShowClassroomDetailResponse.
        :rtype: int
        """
        return self._content_count

    @content_count.setter
    def content_count(self, content_count):
        """Sets the content_count of this ShowClassroomDetailResponse.

        课堂下目录数量

        :param content_count: The content_count of this ShowClassroomDetailResponse.
        :type content_count: int
        """
        self._content_count = content_count

    @property
    def courseware_count(self):
        """Gets the courseware_count of this ShowClassroomDetailResponse.

        课堂下课件数量

        :return: The courseware_count of this ShowClassroomDetailResponse.
        :rtype: int
        """
        return self._courseware_count

    @courseware_count.setter
    def courseware_count(self, courseware_count):
        """Sets the courseware_count of this ShowClassroomDetailResponse.

        课堂下课件数量

        :param courseware_count: The courseware_count of this ShowClassroomDetailResponse.
        :type courseware_count: int
        """
        self._courseware_count = courseware_count

    @property
    def job_count(self):
        """Gets the job_count of this ShowClassroomDetailResponse.

        课堂下作业数量

        :return: The job_count of this ShowClassroomDetailResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        """Sets the job_count of this ShowClassroomDetailResponse.

        课堂下作业数量

        :param job_count: The job_count of this ShowClassroomDetailResponse.
        :type job_count: int
        """
        self._job_count = job_count

    @property
    def member_count(self):
        """Gets the member_count of this ShowClassroomDetailResponse.

        课堂下成员数量

        :return: The member_count of this ShowClassroomDetailResponse.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this ShowClassroomDetailResponse.

        课堂下成员数量

        :param member_count: The member_count of this ShowClassroomDetailResponse.
        :type member_count: int
        """
        self._member_count = member_count

    @property
    def status(self):
        """Gets the status of this ShowClassroomDetailResponse.

        课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档

        :return: The status of this ShowClassroomDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClassroomDetailResponse.

        课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档

        :param status: The status of this ShowClassroomDetailResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowClassroomDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
