# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DependJobs:

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
        'depend_fail_policy': 'str'
    }

    attribute_map = {
        'jobs': 'jobs',
        'depend_period': 'dependPeriod',
        'depend_fail_policy': 'dependFailPolicy'
    }

    def __init__(self, jobs=None, depend_period=None, depend_fail_policy=None):
        """DependJobs

        The model defined in huaweicloud sdk

        :param jobs: 依赖的作业名称列表，必须依赖已存在的作业.
        :type jobs: list[str]
        :param depend_period: 依赖周期
        :type depend_period: str
        :param depend_fail_policy: 依赖作业任务执行失败处理策略
        :type depend_fail_policy: str
        """
        
        

        self._jobs = None
        self._depend_period = None
        self._depend_fail_policy = None
        self.discriminator = None

        self.jobs = jobs
        if depend_period is not None:
            self.depend_period = depend_period
        if depend_fail_policy is not None:
            self.depend_fail_policy = depend_fail_policy

    @property
    def jobs(self):
        """Gets the jobs of this DependJobs.

        依赖的作业名称列表，必须依赖已存在的作业.

        :return: The jobs of this DependJobs.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this DependJobs.

        依赖的作业名称列表，必须依赖已存在的作业.

        :param jobs: The jobs of this DependJobs.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def depend_period(self):
        """Gets the depend_period of this DependJobs.

        依赖周期

        :return: The depend_period of this DependJobs.
        :rtype: str
        """
        return self._depend_period

    @depend_period.setter
    def depend_period(self, depend_period):
        """Sets the depend_period of this DependJobs.

        依赖周期

        :param depend_period: The depend_period of this DependJobs.
        :type depend_period: str
        """
        self._depend_period = depend_period

    @property
    def depend_fail_policy(self):
        """Gets the depend_fail_policy of this DependJobs.

        依赖作业任务执行失败处理策略

        :return: The depend_fail_policy of this DependJobs.
        :rtype: str
        """
        return self._depend_fail_policy

    @depend_fail_policy.setter
    def depend_fail_policy(self, depend_fail_policy):
        """Sets the depend_fail_policy of this DependJobs.

        依赖作业任务执行失败处理策略

        :param depend_fail_policy: The depend_fail_policy of this DependJobs.
        :type depend_fail_policy: str
        """
        self._depend_fail_policy = depend_fail_policy

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
        if not isinstance(other, DependJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
