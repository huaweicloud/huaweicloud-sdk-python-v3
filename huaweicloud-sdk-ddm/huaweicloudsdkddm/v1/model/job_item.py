# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'created_time': 'str',
        'end_time': 'str',
        'process': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'jobs': 'list[str]',
        'database_name': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'created_time': 'created_time',
        'end_time': 'end_time',
        'process': 'process',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'jobs': 'jobs',
        'database_name': 'database_name',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, status=None, created_time=None, end_time=None, process=None, instance_name=None, instance_id=None, jobs=None, database_name=None, fail_reason=None):
        r"""JobItem

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param created_time: 开始时间。
        :type created_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param process: 过程。
        :type process: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param jobs: 操作。
        :type jobs: list[str]
        :param database_name: 逻辑库名称。
        :type database_name: str
        :param fail_reason: 失败原因。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._created_time = None
        self._end_time = None
        self._process = None
        self._instance_name = None
        self._instance_id = None
        self._jobs = None
        self._database_name = None
        self._fail_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if end_time is not None:
            self.end_time = end_time
        if process is not None:
            self.process = process
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if jobs is not None:
            self.jobs = jobs
        if database_name is not None:
            self.database_name = database_name
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        r"""Gets the id of this JobItem.

        任务id。

        :return: The id of this JobItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobItem.

        任务id。

        :param id: The id of this JobItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobItem.

        任务名称。

        :return: The name of this JobItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobItem.

        任务名称。

        :param name: The name of this JobItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this JobItem.

        任务状态。

        :return: The status of this JobItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobItem.

        任务状态。

        :param status: The status of this JobItem.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this JobItem.

        开始时间。

        :return: The created_time of this JobItem.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this JobItem.

        开始时间。

        :param created_time: The created_time of this JobItem.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobItem.

        结束时间。

        :return: The end_time of this JobItem.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobItem.

        结束时间。

        :param end_time: The end_time of this JobItem.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def process(self):
        r"""Gets the process of this JobItem.

        过程。

        :return: The process of this JobItem.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this JobItem.

        过程。

        :param process: The process of this JobItem.
        :type process: str
        """
        self._process = process

    @property
    def instance_name(self):
        r"""Gets the instance_name of this JobItem.

        实例名称。

        :return: The instance_name of this JobItem.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this JobItem.

        实例名称。

        :param instance_name: The instance_name of this JobItem.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this JobItem.

        实例id。

        :return: The instance_id of this JobItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this JobItem.

        实例id。

        :param instance_id: The instance_id of this JobItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def jobs(self):
        r"""Gets the jobs of this JobItem.

        操作。

        :return: The jobs of this JobItem.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this JobItem.

        操作。

        :param jobs: The jobs of this JobItem.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def database_name(self):
        r"""Gets the database_name of this JobItem.

        逻辑库名称。

        :return: The database_name of this JobItem.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this JobItem.

        逻辑库名称。

        :param database_name: The database_name of this JobItem.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this JobItem.

        失败原因。

        :return: The fail_reason of this JobItem.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this JobItem.

        失败原因。

        :param fail_reason: The fail_reason of this JobItem.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
