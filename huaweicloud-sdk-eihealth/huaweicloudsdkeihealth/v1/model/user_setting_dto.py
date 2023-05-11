# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_quota': 'int',
        'job_timeout': 'int',
        'cpu_quota': 'int',
        'mem_quota': 'int',
        'projects_per_user': 'int'
    }

    attribute_map = {
        'job_quota': 'job_quota',
        'job_timeout': 'job_timeout',
        'cpu_quota': 'cpu_quota',
        'mem_quota': 'mem_quota',
        'projects_per_user': 'projects_per_user'
    }

    def __init__(self, job_quota=None, job_timeout=None, cpu_quota=None, mem_quota=None, projects_per_user=None):
        """UserSettingDto

        The model defined in huaweicloud sdk

        :param job_quota: 允许同时运行的作业数
        :type job_quota: int
        :param job_timeout: 作业执行超时时长，单位天
        :type job_timeout: int
        :param cpu_quota: 作业的CPU资源配额，单位核
        :type cpu_quota: int
        :param mem_quota: 作业的内存资源配额，单位GB
        :type mem_quota: int
        :param projects_per_user: 用户可创建项目数配额
        :type projects_per_user: int
        """
        
        

        self._job_quota = None
        self._job_timeout = None
        self._cpu_quota = None
        self._mem_quota = None
        self._projects_per_user = None
        self.discriminator = None

        self.job_quota = job_quota
        self.job_timeout = job_timeout
        self.cpu_quota = cpu_quota
        self.mem_quota = mem_quota
        if projects_per_user is not None:
            self.projects_per_user = projects_per_user

    @property
    def job_quota(self):
        """Gets the job_quota of this UserSettingDto.

        允许同时运行的作业数

        :return: The job_quota of this UserSettingDto.
        :rtype: int
        """
        return self._job_quota

    @job_quota.setter
    def job_quota(self, job_quota):
        """Sets the job_quota of this UserSettingDto.

        允许同时运行的作业数

        :param job_quota: The job_quota of this UserSettingDto.
        :type job_quota: int
        """
        self._job_quota = job_quota

    @property
    def job_timeout(self):
        """Gets the job_timeout of this UserSettingDto.

        作业执行超时时长，单位天

        :return: The job_timeout of this UserSettingDto.
        :rtype: int
        """
        return self._job_timeout

    @job_timeout.setter
    def job_timeout(self, job_timeout):
        """Sets the job_timeout of this UserSettingDto.

        作业执行超时时长，单位天

        :param job_timeout: The job_timeout of this UserSettingDto.
        :type job_timeout: int
        """
        self._job_timeout = job_timeout

    @property
    def cpu_quota(self):
        """Gets the cpu_quota of this UserSettingDto.

        作业的CPU资源配额，单位核

        :return: The cpu_quota of this UserSettingDto.
        :rtype: int
        """
        return self._cpu_quota

    @cpu_quota.setter
    def cpu_quota(self, cpu_quota):
        """Sets the cpu_quota of this UserSettingDto.

        作业的CPU资源配额，单位核

        :param cpu_quota: The cpu_quota of this UserSettingDto.
        :type cpu_quota: int
        """
        self._cpu_quota = cpu_quota

    @property
    def mem_quota(self):
        """Gets the mem_quota of this UserSettingDto.

        作业的内存资源配额，单位GB

        :return: The mem_quota of this UserSettingDto.
        :rtype: int
        """
        return self._mem_quota

    @mem_quota.setter
    def mem_quota(self, mem_quota):
        """Sets the mem_quota of this UserSettingDto.

        作业的内存资源配额，单位GB

        :param mem_quota: The mem_quota of this UserSettingDto.
        :type mem_quota: int
        """
        self._mem_quota = mem_quota

    @property
    def projects_per_user(self):
        """Gets the projects_per_user of this UserSettingDto.

        用户可创建项目数配额

        :return: The projects_per_user of this UserSettingDto.
        :rtype: int
        """
        return self._projects_per_user

    @projects_per_user.setter
    def projects_per_user(self, projects_per_user):
        """Sets the projects_per_user of this UserSettingDto.

        用户可创建项目数配额

        :param projects_per_user: The projects_per_user of this UserSettingDto.
        :type projects_per_user: int
        """
        self._projects_per_user = projects_per_user

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
        if not isinstance(other, UserSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
