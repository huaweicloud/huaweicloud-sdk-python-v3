# coding: utf-8

import pprint
import re

import six





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
        'job_id': 'str',
        'job_type': 'int',
        'job_status': 'int',
        'entities': 'list[Entity]',
        'sub_jobs': 'list[Job]',
        'begin_time': 'str',
        'end_time': 'str',
        'execute_code': 'str',
        'execute_message': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'job_type': 'jobType',
        'job_status': 'jobStatus',
        'entities': 'entities',
        'sub_jobs': 'subJobs',
        'begin_time': 'beginTime',
        'end_time': 'endTime',
        'execute_code': 'executeCode',
        'execute_message': 'executeMessage'
    }

    def __init__(self, job_id=None, job_type=None, job_status=None, entities=None, sub_jobs=None, begin_time=None, end_time=None, execute_code=None, execute_message=None):
        """Job - a model defined in huaweicloud sdk"""
        
        

        self._job_id = None
        self._job_type = None
        self._job_status = None
        self._entities = None
        self._sub_jobs = None
        self._begin_time = None
        self._end_time = None
        self._execute_code = None
        self._execute_message = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if job_status is not None:
            self.job_status = job_status
        if entities is not None:
            self.entities = entities
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if execute_code is not None:
            self.execute_code = execute_code
        if execute_message is not None:
            self.execute_message = execute_message

    @property
    def job_id(self):
        """Gets the job_id of this Job.

        任务Id

        :return: The job_id of this Job.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Job.

        任务Id

        :param job_id: The job_id of this Job.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this Job.

        任务类型

        :return: The job_type of this Job.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        任务类型

        :param job_type: The job_type of this Job.
        :type: int
        """
        self._job_type = job_type

    @property
    def job_status(self):
        """Gets the job_status of this Job.

        任务状态

        :return: The job_status of this Job.
        :rtype: int
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this Job.

        任务状态

        :param job_status: The job_status of this Job.
        :type: int
        """
        self._job_status = job_status

    @property
    def entities(self):
        """Gets the entities of this Job.

        实体列表

        :return: The entities of this Job.
        :rtype: list[Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this Job.

        实体列表

        :param entities: The entities of this Job.
        :type: list[Entity]
        """
        self._entities = entities

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this Job.

        子任务列表

        :return: The sub_jobs of this Job.
        :rtype: list[Job]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this Job.

        子任务列表

        :param sub_jobs: The sub_jobs of this Job.
        :type: list[Job]
        """
        self._sub_jobs = sub_jobs

    @property
    def begin_time(self):
        """Gets the begin_time of this Job.

        任务开始时间

        :return: The begin_time of this Job.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this Job.

        任务开始时间

        :param begin_time: The begin_time of this Job.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this Job.

        任务结束时间

        :return: The end_time of this Job.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Job.

        任务结束时间

        :param end_time: The end_time of this Job.
        :type: str
        """
        self._end_time = end_time

    @property
    def execute_code(self):
        """Gets the execute_code of this Job.

        任务运行代码

        :return: The execute_code of this Job.
        :rtype: str
        """
        return self._execute_code

    @execute_code.setter
    def execute_code(self, execute_code):
        """Sets the execute_code of this Job.

        任务运行代码

        :param execute_code: The execute_code of this Job.
        :type: str
        """
        self._execute_code = execute_code

    @property
    def execute_message(self):
        """Gets the execute_message of this Job.

        任务运行信息

        :return: The execute_message of this Job.
        :rtype: str
        """
        return self._execute_message

    @execute_message.setter
    def execute_message(self, execute_message):
        """Sets the execute_message of this Job.

        任务运行信息

        :param execute_message: The execute_message of this Job.
        :type: str
        """
        self._execute_message = execute_message

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
