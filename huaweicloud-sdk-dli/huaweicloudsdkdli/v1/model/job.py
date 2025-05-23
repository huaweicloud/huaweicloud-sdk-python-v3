# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'status': 'str',
        'create_time': 'int',
        'exceptions': 'str',
        'metrics': 'str',
        'plan': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'create_time': 'create_time',
        'exceptions': 'exceptions',
        'metrics': 'metrics',
        'plan': 'plan'
    }

    def __init__(self, job_id=None, status=None, create_time=None, exceptions=None, metrics=None, plan=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: int
        :param status: 作业状态
        :type status: str
        :param create_time: 时间戳
        :type create_time: int
        :param exceptions: 作业异常信息
        :type exceptions: str
        :param metrics: 作业指标信息
        :type metrics: str
        :param plan: 作业执行计划
        :type plan: str
        """
        
        

        self._job_id = None
        self._status = None
        self._create_time = None
        self._exceptions = None
        self._metrics = None
        self._plan = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        self.status = status
        self.create_time = create_time
        if exceptions is not None:
            self.exceptions = exceptions
        if metrics is not None:
            self.metrics = metrics
        if plan is not None:
            self.plan = plan

    @property
    def job_id(self):
        r"""Gets the job_id of this Job.

        作业ID

        :return: The job_id of this Job.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Job.

        作业ID

        :param job_id: The job_id of this Job.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this Job.

        作业状态

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Job.

        作业状态

        :param status: The status of this Job.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this Job.

        时间戳

        :return: The create_time of this Job.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Job.

        时间戳

        :param create_time: The create_time of this Job.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def exceptions(self):
        r"""Gets the exceptions of this Job.

        作业异常信息

        :return: The exceptions of this Job.
        :rtype: str
        """
        return self._exceptions

    @exceptions.setter
    def exceptions(self, exceptions):
        r"""Sets the exceptions of this Job.

        作业异常信息

        :param exceptions: The exceptions of this Job.
        :type exceptions: str
        """
        self._exceptions = exceptions

    @property
    def metrics(self):
        r"""Gets the metrics of this Job.

        作业指标信息

        :return: The metrics of this Job.
        :rtype: str
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this Job.

        作业指标信息

        :param metrics: The metrics of this Job.
        :type metrics: str
        """
        self._metrics = metrics

    @property
    def plan(self):
        r"""Gets the plan of this Job.

        作业执行计划

        :return: The plan of this Job.
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        r"""Sets the plan of this Job.

        作业执行计划

        :param plan: The plan of this Job.
        :type plan: str
        """
        self._plan = plan

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
