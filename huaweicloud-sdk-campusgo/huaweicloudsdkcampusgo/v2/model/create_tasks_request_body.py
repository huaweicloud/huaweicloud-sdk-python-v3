# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTasksRequestBody:

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
        'description': 'str',
        'input': 'TaskInput',
        'output': 'TaskOutput',
        'service_version': 'str',
        'edge_pool_id': 'str',
        'resource_order_id': 'str',
        'service_config': 'TaskServiceConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'input': 'input',
        'output': 'output',
        'service_version': 'service_version',
        'edge_pool_id': 'edge_pool_id',
        'resource_order_id': 'resource_order_id',
        'service_config': 'service_config'
    }

    def __init__(self, name=None, description=None, input=None, output=None, service_version=None, edge_pool_id=None, resource_order_id=None, service_config=None):
        """CreateTasksRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业的名称
        :type name: str
        :param description: 作业的描述
        :type description: str
        :param input: 
        :type input: :class:`huaweicloudsdkcampusgo.v2.TaskInput`
        :param output: 
        :type output: :class:`huaweicloudsdkcampusgo.v2.TaskOutput`
        :param service_version: 作业对应服务的版本号
        :type service_version: str
        :param edge_pool_id: 仅边缘作业需填且必填，作业运行指定的边缘运行池ID
        :type edge_pool_id: str
        :param resource_order_id: 作业指定的算法能力包包周期订单ID
        :type resource_order_id: str
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkcampusgo.v2.TaskServiceConfig`
        """
        
        

        self._name = None
        self._description = None
        self._input = None
        self._output = None
        self._service_version = None
        self._edge_pool_id = None
        self._resource_order_id = None
        self._service_config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.input = input
        self.output = output
        self.service_version = service_version
        if edge_pool_id is not None:
            self.edge_pool_id = edge_pool_id
        if resource_order_id is not None:
            self.resource_order_id = resource_order_id
        if service_config is not None:
            self.service_config = service_config

    @property
    def name(self):
        """Gets the name of this CreateTasksRequestBody.

        作业的名称

        :return: The name of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTasksRequestBody.

        作业的名称

        :param name: The name of this CreateTasksRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTasksRequestBody.

        作业的描述

        :return: The description of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTasksRequestBody.

        作业的描述

        :param description: The description of this CreateTasksRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def input(self):
        """Gets the input of this CreateTasksRequestBody.

        :return: The input of this CreateTasksRequestBody.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateTasksRequestBody.

        :param input: The input of this CreateTasksRequestBody.
        :type input: :class:`huaweicloudsdkcampusgo.v2.TaskInput`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateTasksRequestBody.

        :return: The output of this CreateTasksRequestBody.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskOutput`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateTasksRequestBody.

        :param output: The output of this CreateTasksRequestBody.
        :type output: :class:`huaweicloudsdkcampusgo.v2.TaskOutput`
        """
        self._output = output

    @property
    def service_version(self):
        """Gets the service_version of this CreateTasksRequestBody.

        作业对应服务的版本号

        :return: The service_version of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """Sets the service_version of this CreateTasksRequestBody.

        作业对应服务的版本号

        :param service_version: The service_version of this CreateTasksRequestBody.
        :type service_version: str
        """
        self._service_version = service_version

    @property
    def edge_pool_id(self):
        """Gets the edge_pool_id of this CreateTasksRequestBody.

        仅边缘作业需填且必填，作业运行指定的边缘运行池ID

        :return: The edge_pool_id of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._edge_pool_id

    @edge_pool_id.setter
    def edge_pool_id(self, edge_pool_id):
        """Sets the edge_pool_id of this CreateTasksRequestBody.

        仅边缘作业需填且必填，作业运行指定的边缘运行池ID

        :param edge_pool_id: The edge_pool_id of this CreateTasksRequestBody.
        :type edge_pool_id: str
        """
        self._edge_pool_id = edge_pool_id

    @property
    def resource_order_id(self):
        """Gets the resource_order_id of this CreateTasksRequestBody.

        作业指定的算法能力包包周期订单ID

        :return: The resource_order_id of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._resource_order_id

    @resource_order_id.setter
    def resource_order_id(self, resource_order_id):
        """Sets the resource_order_id of this CreateTasksRequestBody.

        作业指定的算法能力包包周期订单ID

        :param resource_order_id: The resource_order_id of this CreateTasksRequestBody.
        :type resource_order_id: str
        """
        self._resource_order_id = resource_order_id

    @property
    def service_config(self):
        """Gets the service_config of this CreateTasksRequestBody.

        :return: The service_config of this CreateTasksRequestBody.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """Sets the service_config of this CreateTasksRequestBody.

        :param service_config: The service_config of this CreateTasksRequestBody.
        :type service_config: :class:`huaweicloudsdkcampusgo.v2.TaskServiceConfig`
        """
        self._service_config = service_config

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
        if not isinstance(other, CreateTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
