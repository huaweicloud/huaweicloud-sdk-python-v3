# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupplementDataInfo:

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
        'job_name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'parallel': 'int',
        'depend_jobs': 'list[JobInfo]',
        'is_day_granularity': 'bool',
        'priority': 'int',
        'is_stop_when_fail': 'bool',
        'reverse_order': 'int',
        'force': 'str'
    }

    attribute_map = {
        'name': 'name',
        'job_name': 'jobName',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'parallel': 'parallel',
        'depend_jobs': 'dependJobs',
        'is_day_granularity': 'isDayGranularity',
        'priority': 'priority',
        'is_stop_when_fail': 'is_stop_when_fail',
        'reverse_order': 'reverseOrder',
        'force': 'force'
    }

    def __init__(self, name=None, job_name=None, start_date=None, end_date=None, parallel=None, depend_jobs=None, is_day_granularity=None, priority=None, is_stop_when_fail=None, reverse_order=None, force=None):
        """SupplementDataInfo

        The model defined in huaweicloud sdk

        :param name: 补数据实例名称
        :type name: str
        :param job_name: 补数据依赖的作业名称
        :type job_name: str
        :param start_date: 开始补数据时间
        :type start_date: str
        :param end_date: 截止补数据时间
        :type end_date: str
        :param parallel: 优先级
        :type parallel: int
        :param depend_jobs: 依赖的作业信息
        :type depend_jobs: list[:class:`huaweicloudsdkdgc.v1.JobInfo`]
        :param is_day_granularity: 
        :type is_day_granularity: bool
        :param priority: 
        :type priority: int
        :param is_stop_when_fail: 
        :type is_stop_when_fail: bool
        :param reverse_order: 
        :type reverse_order: int
        :param force: 
        :type force: str
        """
        
        

        self._name = None
        self._job_name = None
        self._start_date = None
        self._end_date = None
        self._parallel = None
        self._depend_jobs = None
        self._is_day_granularity = None
        self._priority = None
        self._is_stop_when_fail = None
        self._reverse_order = None
        self._force = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if job_name is not None:
            self.job_name = job_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if parallel is not None:
            self.parallel = parallel
        if depend_jobs is not None:
            self.depend_jobs = depend_jobs
        if is_day_granularity is not None:
            self.is_day_granularity = is_day_granularity
        if priority is not None:
            self.priority = priority
        if is_stop_when_fail is not None:
            self.is_stop_when_fail = is_stop_when_fail
        if reverse_order is not None:
            self.reverse_order = reverse_order
        if force is not None:
            self.force = force

    @property
    def name(self):
        """Gets the name of this SupplementDataInfo.

        补数据实例名称

        :return: The name of this SupplementDataInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupplementDataInfo.

        补数据实例名称

        :param name: The name of this SupplementDataInfo.
        :type name: str
        """
        self._name = name

    @property
    def job_name(self):
        """Gets the job_name of this SupplementDataInfo.

        补数据依赖的作业名称

        :return: The job_name of this SupplementDataInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this SupplementDataInfo.

        补数据依赖的作业名称

        :param job_name: The job_name of this SupplementDataInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def start_date(self):
        """Gets the start_date of this SupplementDataInfo.

        开始补数据时间

        :return: The start_date of this SupplementDataInfo.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SupplementDataInfo.

        开始补数据时间

        :param start_date: The start_date of this SupplementDataInfo.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SupplementDataInfo.

        截止补数据时间

        :return: The end_date of this SupplementDataInfo.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SupplementDataInfo.

        截止补数据时间

        :param end_date: The end_date of this SupplementDataInfo.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def parallel(self):
        """Gets the parallel of this SupplementDataInfo.

        优先级

        :return: The parallel of this SupplementDataInfo.
        :rtype: int
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this SupplementDataInfo.

        优先级

        :param parallel: The parallel of this SupplementDataInfo.
        :type parallel: int
        """
        self._parallel = parallel

    @property
    def depend_jobs(self):
        """Gets the depend_jobs of this SupplementDataInfo.

        依赖的作业信息

        :return: The depend_jobs of this SupplementDataInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobInfo`]
        """
        return self._depend_jobs

    @depend_jobs.setter
    def depend_jobs(self, depend_jobs):
        """Sets the depend_jobs of this SupplementDataInfo.

        依赖的作业信息

        :param depend_jobs: The depend_jobs of this SupplementDataInfo.
        :type depend_jobs: list[:class:`huaweicloudsdkdgc.v1.JobInfo`]
        """
        self._depend_jobs = depend_jobs

    @property
    def is_day_granularity(self):
        """Gets the is_day_granularity of this SupplementDataInfo.

        :return: The is_day_granularity of this SupplementDataInfo.
        :rtype: bool
        """
        return self._is_day_granularity

    @is_day_granularity.setter
    def is_day_granularity(self, is_day_granularity):
        """Sets the is_day_granularity of this SupplementDataInfo.

        :param is_day_granularity: The is_day_granularity of this SupplementDataInfo.
        :type is_day_granularity: bool
        """
        self._is_day_granularity = is_day_granularity

    @property
    def priority(self):
        """Gets the priority of this SupplementDataInfo.

        :return: The priority of this SupplementDataInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SupplementDataInfo.

        :param priority: The priority of this SupplementDataInfo.
        :type priority: int
        """
        self._priority = priority

    @property
    def is_stop_when_fail(self):
        """Gets the is_stop_when_fail of this SupplementDataInfo.

        :return: The is_stop_when_fail of this SupplementDataInfo.
        :rtype: bool
        """
        return self._is_stop_when_fail

    @is_stop_when_fail.setter
    def is_stop_when_fail(self, is_stop_when_fail):
        """Sets the is_stop_when_fail of this SupplementDataInfo.

        :param is_stop_when_fail: The is_stop_when_fail of this SupplementDataInfo.
        :type is_stop_when_fail: bool
        """
        self._is_stop_when_fail = is_stop_when_fail

    @property
    def reverse_order(self):
        """Gets the reverse_order of this SupplementDataInfo.

        :return: The reverse_order of this SupplementDataInfo.
        :rtype: int
        """
        return self._reverse_order

    @reverse_order.setter
    def reverse_order(self, reverse_order):
        """Sets the reverse_order of this SupplementDataInfo.

        :param reverse_order: The reverse_order of this SupplementDataInfo.
        :type reverse_order: int
        """
        self._reverse_order = reverse_order

    @property
    def force(self):
        """Gets the force of this SupplementDataInfo.

        :return: The force of this SupplementDataInfo.
        :rtype: str
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this SupplementDataInfo.

        :param force: The force of this SupplementDataInfo.
        :type force: str
        """
        self._force = force

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
        if not isinstance(other, SupplementDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
