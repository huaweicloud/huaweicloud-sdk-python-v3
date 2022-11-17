# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

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
        """ShowJobResponse

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param nodes: 
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.Node`]
        :param schedule: 
        :type schedule: :class:`huaweicloudsdkdgc.v1.Schedule`
        :param params: 
        :type params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        :param directory: 
        :type directory: str
        :param job_type: 
        :type job_type: str
        :param basic_config: 
        :type basic_config: :class:`huaweicloudsdkdgc.v1.BasicInfo`
        """
        
        super(ShowJobResponse, self).__init__()

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
        """Gets the name of this ShowJobResponse.

        :return: The name of this ShowJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowJobResponse.

        :param name: The name of this ShowJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def nodes(self):
        """Gets the nodes of this ShowJobResponse.

        :return: The nodes of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowJobResponse.

        :param nodes: The nodes of this ShowJobResponse.
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        self._nodes = nodes

    @property
    def schedule(self):
        """Gets the schedule of this ShowJobResponse.

        :return: The schedule of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ShowJobResponse.

        :param schedule: The schedule of this ShowJobResponse.
        :type schedule: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def params(self):
        """Gets the params of this ShowJobResponse.

        :return: The params of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ShowJobResponse.

        :param params: The params of this ShowJobResponse.
        :type params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        self._params = params

    @property
    def directory(self):
        """Gets the directory of this ShowJobResponse.

        :return: The directory of this ShowJobResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ShowJobResponse.

        :param directory: The directory of this ShowJobResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobResponse.

        :return: The job_type of this ShowJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobResponse.

        :param job_type: The job_type of this ShowJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def basic_config(self):
        """Gets the basic_config of this ShowJobResponse.

        :return: The basic_config of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkdgc.v1.BasicInfo`
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        """Sets the basic_config of this ShowJobResponse.

        :param basic_config: The basic_config of this ShowJobResponse.
        :type basic_config: :class:`huaweicloudsdkdgc.v1.BasicInfo`
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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
