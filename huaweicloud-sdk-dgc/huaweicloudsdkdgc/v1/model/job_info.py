# coding: utf-8

import pprint
import re

import six





class JobInfo:


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
        'nodes': 'list[Node]',
        'schedule': 'Schedule',
        'params': 'list[JobParam]',
        'directory': 'str',
        'job_type': 'str',
        'basic_config': 'BasicInfo'
    }

    attribute_map = {
        'name': 'name',
        'nodes': 'nodes',
        'schedule': 'schedule',
        'params': 'params',
        'directory': 'directory',
        'job_type': 'jobType',
        'basic_config': 'basicConfig'
    }

    def __init__(self, name=None, nodes=None, schedule=None, params=None, directory=None, job_type=None, basic_config=None):
        """JobInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._nodes = None
        self._schedule = None
        self._params = None
        self._directory = None
        self._job_type = None
        self._basic_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if nodes is not None:
            self.nodes = nodes
        if schedule is not None:
            self.schedule = schedule
        if params is not None:
            self.params = params
        if directory is not None:
            self.directory = directory
        if job_type is not None:
            self.job_type = job_type
        if basic_config is not None:
            self.basic_config = basic_config

    @property
    def name(self):
        """Gets the name of this JobInfo.


        :return: The name of this JobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobInfo.


        :param name: The name of this JobInfo.
        :type: str
        """
        self._name = name

    @property
    def nodes(self):
        """Gets the nodes of this JobInfo.


        :return: The nodes of this JobInfo.
        :rtype: list[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this JobInfo.


        :param nodes: The nodes of this JobInfo.
        :type: list[Node]
        """
        self._nodes = nodes

    @property
    def schedule(self):
        """Gets the schedule of this JobInfo.


        :return: The schedule of this JobInfo.
        :rtype: Schedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this JobInfo.


        :param schedule: The schedule of this JobInfo.
        :type: Schedule
        """
        self._schedule = schedule

    @property
    def params(self):
        """Gets the params of this JobInfo.


        :return: The params of this JobInfo.
        :rtype: list[JobParam]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this JobInfo.


        :param params: The params of this JobInfo.
        :type: list[JobParam]
        """
        self._params = params

    @property
    def directory(self):
        """Gets the directory of this JobInfo.


        :return: The directory of this JobInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this JobInfo.


        :param directory: The directory of this JobInfo.
        :type: str
        """
        self._directory = directory

    @property
    def job_type(self):
        """Gets the job_type of this JobInfo.


        :return: The job_type of this JobInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobInfo.


        :param job_type: The job_type of this JobInfo.
        :type: str
        """
        self._job_type = job_type

    @property
    def basic_config(self):
        """Gets the basic_config of this JobInfo.


        :return: The basic_config of this JobInfo.
        :rtype: BasicInfo
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        """Sets the basic_config of this JobInfo.


        :param basic_config: The basic_config of this JobInfo.
        :type: BasicInfo
        """
        self._basic_config = basic_config

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
