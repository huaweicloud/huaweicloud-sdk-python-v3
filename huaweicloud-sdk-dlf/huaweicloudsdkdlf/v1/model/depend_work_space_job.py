# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DependWorkSpaceJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'depend_on_last_period': 'bool',
        'job_name': 'str',
        'work_space': 'str'
    }

    attribute_map = {
        'depend_on_last_period': 'dependOnLastPeriod',
        'job_name': 'jobName',
        'work_space': 'workSpace'
    }

    def __init__(self, depend_on_last_period=None, job_name=None, work_space=None):
        """DependWorkSpaceJob

        The model defined in huaweicloud sdk

        :param depend_on_last_period: 是否依赖最近一个周期
        :type depend_on_last_period: bool
        :param job_name: 作业名
        :type job_name: str
        :param work_space: 工作空间名
        :type work_space: str
        """
        
        

        self._depend_on_last_period = None
        self._job_name = None
        self._work_space = None
        self.discriminator = None

        if depend_on_last_period is not None:
            self.depend_on_last_period = depend_on_last_period
        if job_name is not None:
            self.job_name = job_name
        if work_space is not None:
            self.work_space = work_space

    @property
    def depend_on_last_period(self):
        """Gets the depend_on_last_period of this DependWorkSpaceJob.

        是否依赖最近一个周期

        :return: The depend_on_last_period of this DependWorkSpaceJob.
        :rtype: bool
        """
        return self._depend_on_last_period

    @depend_on_last_period.setter
    def depend_on_last_period(self, depend_on_last_period):
        """Sets the depend_on_last_period of this DependWorkSpaceJob.

        是否依赖最近一个周期

        :param depend_on_last_period: The depend_on_last_period of this DependWorkSpaceJob.
        :type depend_on_last_period: bool
        """
        self._depend_on_last_period = depend_on_last_period

    @property
    def job_name(self):
        """Gets the job_name of this DependWorkSpaceJob.

        作业名

        :return: The job_name of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this DependWorkSpaceJob.

        作业名

        :param job_name: The job_name of this DependWorkSpaceJob.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def work_space(self):
        """Gets the work_space of this DependWorkSpaceJob.

        工作空间名

        :return: The work_space of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._work_space

    @work_space.setter
    def work_space(self, work_space):
        """Sets the work_space of this DependWorkSpaceJob.

        工作空间名

        :param work_space: The work_space of this DependWorkSpaceJob.
        :type work_space: str
        """
        self._work_space = work_space

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
        if not isinstance(other, DependWorkSpaceJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
