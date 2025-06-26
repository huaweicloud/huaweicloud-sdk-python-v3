# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'execution_id': 'int',
        'repository': 'str',
        'job_id': 'str',
        'status': 'str',
        'status_code': 'int',
        'status_revision': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'total': 'int',
        'retained': 'int'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'repository': 'repository',
        'job_id': 'job_id',
        'status': 'status',
        'status_code': 'status_code',
        'status_revision': 'status_revision',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'total': 'total',
        'retained': 'retained'
    }

    def __init__(self, id=None, execution_id=None, repository=None, job_id=None, status=None, status_code=None, status_revision=None, start_time=None, end_time=None, total=None, retained=None):
        r"""Task

        The model defined in huaweicloud sdk

        :param id: 老化策略执行记录任务ID
        :type id: int
        :param execution_id: 老化策略执行记录ID
        :type execution_id: int
        :param repository: 制品仓库名称
        :type repository: str
        :param job_id: 任务名称
        :type job_id: str
        :param status: 执行状态
        :type status: str
        :param status_code: 状态码
        :type status_code: int
        :param status_revision: 状态修订
        :type status_revision: int
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param total: 版本总数
        :type total: int
        :param retained: 保留版本总数
        :type retained: int
        """
        
        

        self._id = None
        self._execution_id = None
        self._repository = None
        self._job_id = None
        self._status = None
        self._status_code = None
        self._status_revision = None
        self._start_time = None
        self._end_time = None
        self._total = None
        self._retained = None
        self.discriminator = None

        self.id = id
        self.execution_id = execution_id
        self.repository = repository
        self.job_id = job_id
        self.status = status
        self.status_code = status_code
        self.status_revision = status_revision
        self.start_time = start_time
        self.end_time = end_time
        self.total = total
        self.retained = retained

    @property
    def id(self):
        r"""Gets the id of this Task.

        老化策略执行记录任务ID

        :return: The id of this Task.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Task.

        老化策略执行记录任务ID

        :param id: The id of this Task.
        :type id: int
        """
        self._id = id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this Task.

        老化策略执行记录ID

        :return: The execution_id of this Task.
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this Task.

        老化策略执行记录ID

        :param execution_id: The execution_id of this Task.
        :type execution_id: int
        """
        self._execution_id = execution_id

    @property
    def repository(self):
        r"""Gets the repository of this Task.

        制品仓库名称

        :return: The repository of this Task.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this Task.

        制品仓库名称

        :param repository: The repository of this Task.
        :type repository: str
        """
        self._repository = repository

    @property
    def job_id(self):
        r"""Gets the job_id of this Task.

        任务名称

        :return: The job_id of this Task.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Task.

        任务名称

        :param job_id: The job_id of this Task.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this Task.

        执行状态

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Task.

        执行状态

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

    @property
    def status_code(self):
        r"""Gets the status_code of this Task.

        状态码

        :return: The status_code of this Task.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this Task.

        状态码

        :param status_code: The status_code of this Task.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def status_revision(self):
        r"""Gets the status_revision of this Task.

        状态修订

        :return: The status_revision of this Task.
        :rtype: int
        """
        return self._status_revision

    @status_revision.setter
    def status_revision(self, status_revision):
        r"""Sets the status_revision of this Task.

        状态修订

        :param status_revision: The status_revision of this Task.
        :type status_revision: int
        """
        self._status_revision = status_revision

    @property
    def start_time(self):
        r"""Gets the start_time of this Task.

        开始时间

        :return: The start_time of this Task.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this Task.

        开始时间

        :param start_time: The start_time of this Task.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Task.

        结束时间

        :return: The end_time of this Task.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Task.

        结束时间

        :param end_time: The end_time of this Task.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def total(self):
        r"""Gets the total of this Task.

        版本总数

        :return: The total of this Task.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Task.

        版本总数

        :param total: The total of this Task.
        :type total: int
        """
        self._total = total

    @property
    def retained(self):
        r"""Gets the retained of this Task.

        保留版本总数

        :return: The retained of this Task.
        :rtype: int
        """
        return self._retained

    @retained.setter
    def retained(self, retained):
        r"""Sets the retained of this Task.

        保留版本总数

        :param retained: The retained of this Task.
        :type retained: int
        """
        self._retained = retained

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
