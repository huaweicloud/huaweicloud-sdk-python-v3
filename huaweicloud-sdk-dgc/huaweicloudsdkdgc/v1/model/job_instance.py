# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'status': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'instances_id': 'str'
    }

    attribute_map = {
        'job_name': 'jobName',
        'status': 'status',
        'plan_time': 'planTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'execute_time': 'executeTime',
        'instances_id': 'instancesId'
    }

    def __init__(self, job_name=None, status=None, plan_time=None, start_time=None, end_time=None, execute_time=None, instances_id=None):
        """JobInstance

        The model defined in huaweicloud sdk

        :param job_name: 
        :type job_name: str
        :param status: 
        :type status: str
        :param plan_time: 
        :type plan_time: int
        :param start_time: 
        :type start_time: int
        :param end_time: 
        :type end_time: int
        :param execute_time: 
        :type execute_time: int
        :param instances_id: 
        :type instances_id: str
        """
        
        

        self._job_name = None
        self._status = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._instances_id = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if status is not None:
            self.status = status
        if plan_time is not None:
            self.plan_time = plan_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if instances_id is not None:
            self.instances_id = instances_id

    @property
    def job_name(self):
        """Gets the job_name of this JobInstance.

        :return: The job_name of this JobInstance.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobInstance.

        :param job_name: The job_name of this JobInstance.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        """Gets the status of this JobInstance.

        :return: The status of this JobInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobInstance.

        :param status: The status of this JobInstance.
        :type status: str
        """
        self._status = status

    @property
    def plan_time(self):
        """Gets the plan_time of this JobInstance.

        :return: The plan_time of this JobInstance.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        """Sets the plan_time of this JobInstance.

        :param plan_time: The plan_time of this JobInstance.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        """Gets the start_time of this JobInstance.

        :return: The start_time of this JobInstance.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobInstance.

        :param start_time: The start_time of this JobInstance.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobInstance.

        :return: The end_time of this JobInstance.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobInstance.

        :param end_time: The end_time of this JobInstance.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        """Gets the execute_time of this JobInstance.

        :return: The execute_time of this JobInstance.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this JobInstance.

        :param execute_time: The execute_time of this JobInstance.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def instances_id(self):
        """Gets the instances_id of this JobInstance.

        :return: The instances_id of this JobInstance.
        :rtype: str
        """
        return self._instances_id

    @instances_id.setter
    def instances_id(self, instances_id):
        """Sets the instances_id of this JobInstance.

        :param instances_id: The instances_id of this JobInstance.
        :type instances_id: str
        """
        self._instances_id = instances_id

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
        if not isinstance(other, JobInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
