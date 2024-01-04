# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DependJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[str]',
        'depend_period': 'str',
        'depend_fail_policy': 'str',
        'same_work_space_jobs': 'list[DependWorkSpaceJob]',
        'other_work_space_jobs': 'list[DependWorkSpaceJob]'
    }

    attribute_map = {
        'jobs': 'jobs',
        'depend_period': 'dependPeriod',
        'depend_fail_policy': 'dependFailPolicy',
        'same_work_space_jobs': 'sameWorkSpaceJobs',
        'other_work_space_jobs': 'otherWorkSpaceJobs'
    }

    def __init__(self, jobs=None, depend_period=None, depend_fail_policy=None, same_work_space_jobs=None, other_work_space_jobs=None):
        """DependJob

        The model defined in huaweicloud sdk

        :param jobs: 依赖的作业名称列表，必须依赖已存在的作业.
        :type jobs: list[str]
        :param depend_period: 依赖周期
        :type depend_period: str
        :param depend_fail_policy: 依赖作业任务执行失败处理策略
        :type depend_fail_policy: str
        :param same_work_space_jobs: 依赖本工作空间的作业名称列表
        :type same_work_space_jobs: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        :param other_work_space_jobs: 依赖其他工作空间的作业名称列表
        :type other_work_space_jobs: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        """
        
        

        self._jobs = None
        self._depend_period = None
        self._depend_fail_policy = None
        self._same_work_space_jobs = None
        self._other_work_space_jobs = None
        self.discriminator = None

        self.jobs = jobs
        if depend_period is not None:
            self.depend_period = depend_period
        if depend_fail_policy is not None:
            self.depend_fail_policy = depend_fail_policy
        if same_work_space_jobs is not None:
            self.same_work_space_jobs = same_work_space_jobs
        if other_work_space_jobs is not None:
            self.other_work_space_jobs = other_work_space_jobs

    @property
    def jobs(self):
        """Gets the jobs of this DependJob.

        依赖的作业名称列表，必须依赖已存在的作业.

        :return: The jobs of this DependJob.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this DependJob.

        依赖的作业名称列表，必须依赖已存在的作业.

        :param jobs: The jobs of this DependJob.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def depend_period(self):
        """Gets the depend_period of this DependJob.

        依赖周期

        :return: The depend_period of this DependJob.
        :rtype: str
        """
        return self._depend_period

    @depend_period.setter
    def depend_period(self, depend_period):
        """Sets the depend_period of this DependJob.

        依赖周期

        :param depend_period: The depend_period of this DependJob.
        :type depend_period: str
        """
        self._depend_period = depend_period

    @property
    def depend_fail_policy(self):
        """Gets the depend_fail_policy of this DependJob.

        依赖作业任务执行失败处理策略

        :return: The depend_fail_policy of this DependJob.
        :rtype: str
        """
        return self._depend_fail_policy

    @depend_fail_policy.setter
    def depend_fail_policy(self, depend_fail_policy):
        """Sets the depend_fail_policy of this DependJob.

        依赖作业任务执行失败处理策略

        :param depend_fail_policy: The depend_fail_policy of this DependJob.
        :type depend_fail_policy: str
        """
        self._depend_fail_policy = depend_fail_policy

    @property
    def same_work_space_jobs(self):
        """Gets the same_work_space_jobs of this DependJob.

        依赖本工作空间的作业名称列表

        :return: The same_work_space_jobs of this DependJob.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        """
        return self._same_work_space_jobs

    @same_work_space_jobs.setter
    def same_work_space_jobs(self, same_work_space_jobs):
        """Sets the same_work_space_jobs of this DependJob.

        依赖本工作空间的作业名称列表

        :param same_work_space_jobs: The same_work_space_jobs of this DependJob.
        :type same_work_space_jobs: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        """
        self._same_work_space_jobs = same_work_space_jobs

    @property
    def other_work_space_jobs(self):
        """Gets the other_work_space_jobs of this DependJob.

        依赖其他工作空间的作业名称列表

        :return: The other_work_space_jobs of this DependJob.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        """
        return self._other_work_space_jobs

    @other_work_space_jobs.setter
    def other_work_space_jobs(self, other_work_space_jobs):
        """Sets the other_work_space_jobs of this DependJob.

        依赖其他工作空间的作业名称列表

        :param other_work_space_jobs: The other_work_space_jobs of this DependJob.
        :type other_work_space_jobs: list[:class:`huaweicloudsdkdlf.v1.DependWorkSpaceJob`]
        """
        self._other_work_space_jobs = other_work_space_jobs

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
        if not isinstance(other, DependJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
