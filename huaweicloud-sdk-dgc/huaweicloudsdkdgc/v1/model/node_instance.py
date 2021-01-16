# coding: utf-8

import pprint
import re

import six





class NodeInstance:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'status': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'node_type': 'str',
        'retry_times': 'int',
        'instance_id': 'int',
        'input_row_count': 'int',
        'output_row_count': 'int',
        'log_path': 'str'
    }

    attribute_map = {
        'node_name': 'nodeName',
        'status': 'status',
        'plan_time': 'planTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'execute_time': 'executeTime',
        'node_type': 'nodeType',
        'retry_times': 'retryTimes',
        'instance_id': 'instanceId',
        'input_row_count': 'inputRowCount',
        'output_row_count': 'outputRowCount',
        'log_path': 'logPath'
    }

    def __init__(self, node_name=None, status=None, plan_time=None, start_time=None, end_time=None, execute_time=None, node_type=None, retry_times=None, instance_id=None, input_row_count=None, output_row_count=None, log_path=None):
        """NodeInstance - a model defined in huaweicloud sdk"""
        
        

        self._node_name = None
        self._status = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._node_type = None
        self._retry_times = None
        self._instance_id = None
        self._input_row_count = None
        self._output_row_count = None
        self._log_path = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
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
        if node_type is not None:
            self.node_type = node_type
        if retry_times is not None:
            self.retry_times = retry_times
        if instance_id is not None:
            self.instance_id = instance_id
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if output_row_count is not None:
            self.output_row_count = output_row_count
        if log_path is not None:
            self.log_path = log_path

    @property
    def node_name(self):
        """Gets the node_name of this NodeInstance.


        :return: The node_name of this NodeInstance.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this NodeInstance.


        :param node_name: The node_name of this NodeInstance.
        :type: str
        """
        self._node_name = node_name

    @property
    def status(self):
        """Gets the status of this NodeInstance.


        :return: The status of this NodeInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeInstance.


        :param status: The status of this NodeInstance.
        :type: str
        """
        self._status = status

    @property
    def plan_time(self):
        """Gets the plan_time of this NodeInstance.


        :return: The plan_time of this NodeInstance.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        """Sets the plan_time of this NodeInstance.


        :param plan_time: The plan_time of this NodeInstance.
        :type: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        """Gets the start_time of this NodeInstance.


        :return: The start_time of this NodeInstance.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NodeInstance.


        :param start_time: The start_time of this NodeInstance.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this NodeInstance.


        :return: The end_time of this NodeInstance.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this NodeInstance.


        :param end_time: The end_time of this NodeInstance.
        :type: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        """Gets the execute_time of this NodeInstance.


        :return: The execute_time of this NodeInstance.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this NodeInstance.


        :param execute_time: The execute_time of this NodeInstance.
        :type: int
        """
        self._execute_time = execute_time

    @property
    def node_type(self):
        """Gets the node_type of this NodeInstance.


        :return: The node_type of this NodeInstance.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodeInstance.


        :param node_type: The node_type of this NodeInstance.
        :type: str
        """
        self._node_type = node_type

    @property
    def retry_times(self):
        """Gets the retry_times of this NodeInstance.


        :return: The retry_times of this NodeInstance.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        """Sets the retry_times of this NodeInstance.


        :param retry_times: The retry_times of this NodeInstance.
        :type: int
        """
        self._retry_times = retry_times

    @property
    def instance_id(self):
        """Gets the instance_id of this NodeInstance.


        :return: The instance_id of this NodeInstance.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this NodeInstance.


        :param instance_id: The instance_id of this NodeInstance.
        :type: int
        """
        self._instance_id = instance_id

    @property
    def input_row_count(self):
        """Gets the input_row_count of this NodeInstance.


        :return: The input_row_count of this NodeInstance.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        """Sets the input_row_count of this NodeInstance.


        :param input_row_count: The input_row_count of this NodeInstance.
        :type: int
        """
        self._input_row_count = input_row_count

    @property
    def output_row_count(self):
        """Gets the output_row_count of this NodeInstance.


        :return: The output_row_count of this NodeInstance.
        :rtype: int
        """
        return self._output_row_count

    @output_row_count.setter
    def output_row_count(self, output_row_count):
        """Sets the output_row_count of this NodeInstance.


        :param output_row_count: The output_row_count of this NodeInstance.
        :type: int
        """
        self._output_row_count = output_row_count

    @property
    def log_path(self):
        """Gets the log_path of this NodeInstance.


        :return: The log_path of this NodeInstance.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this NodeInstance.


        :param log_path: The log_path of this NodeInstance.
        :type: str
        """
        self._log_path = log_path

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
        if not isinstance(other, NodeInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
