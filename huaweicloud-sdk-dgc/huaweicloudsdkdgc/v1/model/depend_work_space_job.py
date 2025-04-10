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
        'work_space_id': 'str',
        'work_space': 'str',
        'depend_type': 'str',
        'depend_on_last_n_period_value': 'int'
    }

    attribute_map = {
        'depend_on_last_period': 'dependOnLastPeriod',
        'job_name': 'jobName',
        'work_space_id': 'workSpaceId',
        'work_space': 'workSpace',
        'depend_type': 'dependType',
        'depend_on_last_n_period_value': 'dependOnLastNPeriodValue'
    }

    def __init__(self, depend_on_last_period=None, job_name=None, work_space_id=None, work_space=None, depend_type=None, depend_on_last_n_period_value=None):
        r"""DependWorkSpaceJob

        The model defined in huaweicloud sdk

        :param depend_on_last_period: 是否依赖最近一个周期
        :type depend_on_last_period: bool
        :param job_name: 作业名
        :type job_name: str
        :param work_space_id: 工作空间名ID
        :type work_space_id: str
        :param work_space: 工作空间名
        :type work_space: str
        :param depend_type: 依赖的规则
        :type depend_type: str
        :param depend_on_last_n_period_value: 依赖上N个周期
        :type depend_on_last_n_period_value: int
        """
        
        

        self._depend_on_last_period = None
        self._job_name = None
        self._work_space_id = None
        self._work_space = None
        self._depend_type = None
        self._depend_on_last_n_period_value = None
        self.discriminator = None

        if depend_on_last_period is not None:
            self.depend_on_last_period = depend_on_last_period
        if job_name is not None:
            self.job_name = job_name
        if work_space_id is not None:
            self.work_space_id = work_space_id
        if work_space is not None:
            self.work_space = work_space
        if depend_type is not None:
            self.depend_type = depend_type
        if depend_on_last_n_period_value is not None:
            self.depend_on_last_n_period_value = depend_on_last_n_period_value

    @property
    def depend_on_last_period(self):
        r"""Gets the depend_on_last_period of this DependWorkSpaceJob.

        是否依赖最近一个周期

        :return: The depend_on_last_period of this DependWorkSpaceJob.
        :rtype: bool
        """
        return self._depend_on_last_period

    @depend_on_last_period.setter
    def depend_on_last_period(self, depend_on_last_period):
        r"""Sets the depend_on_last_period of this DependWorkSpaceJob.

        是否依赖最近一个周期

        :param depend_on_last_period: The depend_on_last_period of this DependWorkSpaceJob.
        :type depend_on_last_period: bool
        """
        self._depend_on_last_period = depend_on_last_period

    @property
    def job_name(self):
        r"""Gets the job_name of this DependWorkSpaceJob.

        作业名

        :return: The job_name of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this DependWorkSpaceJob.

        作业名

        :param job_name: The job_name of this DependWorkSpaceJob.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def work_space_id(self):
        r"""Gets the work_space_id of this DependWorkSpaceJob.

        工作空间名ID

        :return: The work_space_id of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._work_space_id

    @work_space_id.setter
    def work_space_id(self, work_space_id):
        r"""Sets the work_space_id of this DependWorkSpaceJob.

        工作空间名ID

        :param work_space_id: The work_space_id of this DependWorkSpaceJob.
        :type work_space_id: str
        """
        self._work_space_id = work_space_id

    @property
    def work_space(self):
        r"""Gets the work_space of this DependWorkSpaceJob.

        工作空间名

        :return: The work_space of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._work_space

    @work_space.setter
    def work_space(self, work_space):
        r"""Sets the work_space of this DependWorkSpaceJob.

        工作空间名

        :param work_space: The work_space of this DependWorkSpaceJob.
        :type work_space: str
        """
        self._work_space = work_space

    @property
    def depend_type(self):
        r"""Gets the depend_type of this DependWorkSpaceJob.

        依赖的规则

        :return: The depend_type of this DependWorkSpaceJob.
        :rtype: str
        """
        return self._depend_type

    @depend_type.setter
    def depend_type(self, depend_type):
        r"""Sets the depend_type of this DependWorkSpaceJob.

        依赖的规则

        :param depend_type: The depend_type of this DependWorkSpaceJob.
        :type depend_type: str
        """
        self._depend_type = depend_type

    @property
    def depend_on_last_n_period_value(self):
        r"""Gets the depend_on_last_n_period_value of this DependWorkSpaceJob.

        依赖上N个周期

        :return: The depend_on_last_n_period_value of this DependWorkSpaceJob.
        :rtype: int
        """
        return self._depend_on_last_n_period_value

    @depend_on_last_n_period_value.setter
    def depend_on_last_n_period_value(self, depend_on_last_n_period_value):
        r"""Sets the depend_on_last_n_period_value of this DependWorkSpaceJob.

        依赖上N个周期

        :param depend_on_last_n_period_value: The depend_on_last_n_period_value of this DependWorkSpaceJob.
        :type depend_on_last_n_period_value: int
        """
        self._depend_on_last_n_period_value = depend_on_last_n_period_value

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
