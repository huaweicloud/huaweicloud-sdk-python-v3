# coding: utf-8

import pprint
import re

import six





class MetricInfoForAlarm:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[MetricsDimension]',
        'metric_name': 'str',
        'namespace': 'str',
        'resource_group_id': 'str',
        'resource_group_name': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'resource_group_id': 'resource_group_id',
        'resource_group_name': 'resource_group_name'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None, resource_group_id=None, resource_group_name=None):
        """MetricInfoForAlarm - a model defined in huaweicloud sdk"""
        
        

        self._dimensions = None
        self._metric_name = None
        self._namespace = None
        self._resource_group_id = None
        self._resource_group_name = None
        self.discriminator = None

        self.dimensions = dimensions
        self.metric_name = metric_name
        self.namespace = namespace
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricInfoForAlarm.

        指标维度

        :return: The dimensions of this MetricInfoForAlarm.
        :rtype: list[MetricsDimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricInfoForAlarm.

        指标维度

        :param dimensions: The dimensions of this MetricInfoForAlarm.
        :type: list[MetricsDimension]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricInfoForAlarm.

        指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。  具体指标名请参见查询指标列表中查询出的指标名。

        :return: The metric_name of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricInfoForAlarm.

        指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。  具体指标名请参见查询指标列表中查询出的指标名。

        :param metric_name: The metric_name of this MetricInfoForAlarm.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this MetricInfoForAlarm.

        指标命名空间，，例如弹性云服务器命名空间。格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空。

        :return: The namespace of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetricInfoForAlarm.

        指标命名空间，，例如弹性云服务器命名空间。格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。说明： 当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为空。

        :param namespace: The namespace of this MetricInfoForAlarm.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this MetricInfoForAlarm.

        创建告警规则时选择的资源分组ID，如：rg1603786526428bWbVmk4rP

        :return: The resource_group_id of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this MetricInfoForAlarm.

        创建告警规则时选择的资源分组ID，如：rg1603786526428bWbVmk4rP

        :param resource_group_id: The resource_group_id of this MetricInfoForAlarm.
        :type: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this MetricInfoForAlarm.

        创建告警规则时选择的资源分组名称，如：Resource-Group-ECS-01

        :return: The resource_group_name of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this MetricInfoForAlarm.

        创建告警规则时选择的资源分组名称，如：Resource-Group-ECS-01

        :param resource_group_name: The resource_group_name of this MetricInfoForAlarm.
        :type: str
        """
        self._resource_group_name = resource_group_name

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
        if not isinstance(other, MetricInfoForAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
