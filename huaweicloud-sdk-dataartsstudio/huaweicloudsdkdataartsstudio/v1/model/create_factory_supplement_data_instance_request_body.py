# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFactorySupplementDataInstanceRequestBody:

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
        'depend_jobs': 'list[CreateFactorySupplementDataInstanceRequestBodyDependJobs]',
        'is_day_granularity': 'bool',
        'priority': 'int',
        'is_stop_when_fail': 'bool',
        'reverse_order': 'int',
        'supplement_data_run_time': 'CreateFactorySupplementDataInstanceRequestBodySupplementDataRunTime',
        'supplement_data_instance_time': 'CreateFactorySupplementDataInstanceRequestBodySupplementDataInstanceTime',
        'force': 'str'
    }

    attribute_map = {
        'name': 'name',
        'job_name': 'job_name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'parallel': 'parallel',
        'depend_jobs': 'depend_jobs',
        'is_day_granularity': 'is_day_granularity',
        'priority': 'priority',
        'is_stop_when_fail': 'is_stop_when_fail',
        'reverse_order': 'reverse_order',
        'supplement_data_run_time': 'supplement_data_run_time',
        'supplement_data_instance_time': 'supplement_data_instance_time',
        'force': 'force'
    }

    def __init__(self, name=None, job_name=None, start_date=None, end_date=None, parallel=None, depend_jobs=None, is_day_granularity=None, priority=None, is_stop_when_fail=None, reverse_order=None, supplement_data_run_time=None, supplement_data_instance_time=None, force=None):
        """CreateFactorySupplementDataInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 补数据实例名称
        :type name: str
        :param job_name: 作业名称
        :type job_name: str
        :param start_date: 补数据开始时间
        :type start_date: str
        :param end_date: 补数据结束时间
        :type end_date: str
        :param parallel: 并行周期数
        :type parallel: int
        :param depend_jobs: 依赖作业信息
        :type depend_jobs: list[:class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodyDependJobs`]
        :param is_day_granularity: 是否按天粒度补数据
        :type is_day_granularity: bool
        :param priority: 优先级
        :type priority: int
        :param is_stop_when_fail: 失败时作业是否停止
        :type is_stop_when_fail: bool
        :param reverse_order: 按照时间倒序补跑
        :type reverse_order: int
        :param supplement_data_run_time: 
        :type supplement_data_run_time: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataRunTime`
        :param supplement_data_instance_time: 
        :type supplement_data_instance_time: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataInstanceTime`
        :param force: 当前有补数据实例在运行时，是否强制补数据
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
        self._supplement_data_run_time = None
        self._supplement_data_instance_time = None
        self._force = None
        self.discriminator = None

        self.name = name
        self.job_name = job_name
        self.start_date = start_date
        self.end_date = end_date
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
        if supplement_data_run_time is not None:
            self.supplement_data_run_time = supplement_data_run_time
        if supplement_data_instance_time is not None:
            self.supplement_data_instance_time = supplement_data_instance_time
        if force is not None:
            self.force = force

    @property
    def name(self):
        """Gets the name of this CreateFactorySupplementDataInstanceRequestBody.

        补数据实例名称

        :return: The name of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFactorySupplementDataInstanceRequestBody.

        补数据实例名称

        :param name: The name of this CreateFactorySupplementDataInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def job_name(self):
        """Gets the job_name of this CreateFactorySupplementDataInstanceRequestBody.

        作业名称

        :return: The job_name of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CreateFactorySupplementDataInstanceRequestBody.

        作业名称

        :param job_name: The job_name of this CreateFactorySupplementDataInstanceRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def start_date(self):
        """Gets the start_date of this CreateFactorySupplementDataInstanceRequestBody.

        补数据开始时间

        :return: The start_date of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateFactorySupplementDataInstanceRequestBody.

        补数据开始时间

        :param start_date: The start_date of this CreateFactorySupplementDataInstanceRequestBody.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreateFactorySupplementDataInstanceRequestBody.

        补数据结束时间

        :return: The end_date of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreateFactorySupplementDataInstanceRequestBody.

        补数据结束时间

        :param end_date: The end_date of this CreateFactorySupplementDataInstanceRequestBody.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def parallel(self):
        """Gets the parallel of this CreateFactorySupplementDataInstanceRequestBody.

        并行周期数

        :return: The parallel of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: int
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this CreateFactorySupplementDataInstanceRequestBody.

        并行周期数

        :param parallel: The parallel of this CreateFactorySupplementDataInstanceRequestBody.
        :type parallel: int
        """
        self._parallel = parallel

    @property
    def depend_jobs(self):
        """Gets the depend_jobs of this CreateFactorySupplementDataInstanceRequestBody.

        依赖作业信息

        :return: The depend_jobs of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodyDependJobs`]
        """
        return self._depend_jobs

    @depend_jobs.setter
    def depend_jobs(self, depend_jobs):
        """Sets the depend_jobs of this CreateFactorySupplementDataInstanceRequestBody.

        依赖作业信息

        :param depend_jobs: The depend_jobs of this CreateFactorySupplementDataInstanceRequestBody.
        :type depend_jobs: list[:class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodyDependJobs`]
        """
        self._depend_jobs = depend_jobs

    @property
    def is_day_granularity(self):
        """Gets the is_day_granularity of this CreateFactorySupplementDataInstanceRequestBody.

        是否按天粒度补数据

        :return: The is_day_granularity of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: bool
        """
        return self._is_day_granularity

    @is_day_granularity.setter
    def is_day_granularity(self, is_day_granularity):
        """Sets the is_day_granularity of this CreateFactorySupplementDataInstanceRequestBody.

        是否按天粒度补数据

        :param is_day_granularity: The is_day_granularity of this CreateFactorySupplementDataInstanceRequestBody.
        :type is_day_granularity: bool
        """
        self._is_day_granularity = is_day_granularity

    @property
    def priority(self):
        """Gets the priority of this CreateFactorySupplementDataInstanceRequestBody.

        优先级

        :return: The priority of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateFactorySupplementDataInstanceRequestBody.

        优先级

        :param priority: The priority of this CreateFactorySupplementDataInstanceRequestBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def is_stop_when_fail(self):
        """Gets the is_stop_when_fail of this CreateFactorySupplementDataInstanceRequestBody.

        失败时作业是否停止

        :return: The is_stop_when_fail of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: bool
        """
        return self._is_stop_when_fail

    @is_stop_when_fail.setter
    def is_stop_when_fail(self, is_stop_when_fail):
        """Sets the is_stop_when_fail of this CreateFactorySupplementDataInstanceRequestBody.

        失败时作业是否停止

        :param is_stop_when_fail: The is_stop_when_fail of this CreateFactorySupplementDataInstanceRequestBody.
        :type is_stop_when_fail: bool
        """
        self._is_stop_when_fail = is_stop_when_fail

    @property
    def reverse_order(self):
        """Gets the reverse_order of this CreateFactorySupplementDataInstanceRequestBody.

        按照时间倒序补跑

        :return: The reverse_order of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: int
        """
        return self._reverse_order

    @reverse_order.setter
    def reverse_order(self, reverse_order):
        """Sets the reverse_order of this CreateFactorySupplementDataInstanceRequestBody.

        按照时间倒序补跑

        :param reverse_order: The reverse_order of this CreateFactorySupplementDataInstanceRequestBody.
        :type reverse_order: int
        """
        self._reverse_order = reverse_order

    @property
    def supplement_data_run_time(self):
        """Gets the supplement_data_run_time of this CreateFactorySupplementDataInstanceRequestBody.

        :return: The supplement_data_run_time of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataRunTime`
        """
        return self._supplement_data_run_time

    @supplement_data_run_time.setter
    def supplement_data_run_time(self, supplement_data_run_time):
        """Sets the supplement_data_run_time of this CreateFactorySupplementDataInstanceRequestBody.

        :param supplement_data_run_time: The supplement_data_run_time of this CreateFactorySupplementDataInstanceRequestBody.
        :type supplement_data_run_time: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataRunTime`
        """
        self._supplement_data_run_time = supplement_data_run_time

    @property
    def supplement_data_instance_time(self):
        """Gets the supplement_data_instance_time of this CreateFactorySupplementDataInstanceRequestBody.

        :return: The supplement_data_instance_time of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataInstanceTime`
        """
        return self._supplement_data_instance_time

    @supplement_data_instance_time.setter
    def supplement_data_instance_time(self, supplement_data_instance_time):
        """Sets the supplement_data_instance_time of this CreateFactorySupplementDataInstanceRequestBody.

        :param supplement_data_instance_time: The supplement_data_instance_time of this CreateFactorySupplementDataInstanceRequestBody.
        :type supplement_data_instance_time: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequestBodySupplementDataInstanceTime`
        """
        self._supplement_data_instance_time = supplement_data_instance_time

    @property
    def force(self):
        """Gets the force of this CreateFactorySupplementDataInstanceRequestBody.

        当前有补数据实例在运行时，是否强制补数据

        :return: The force of this CreateFactorySupplementDataInstanceRequestBody.
        :rtype: str
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this CreateFactorySupplementDataInstanceRequestBody.

        当前有补数据实例在运行时，是否强制补数据

        :param force: The force of this CreateFactorySupplementDataInstanceRequestBody.
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
        if not isinstance(other, CreateFactorySupplementDataInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
