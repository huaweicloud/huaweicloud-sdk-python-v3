# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkResourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_slot': 'int',
        'parallel_number': 'int',
        'jobmanager_resource_spec': 'ResourceSpec',
        'taskmanager_resource_spec': 'ResourceSpec'
    }

    attribute_map = {
        'max_slot': 'max_slot',
        'parallel_number': 'parallel_number',
        'jobmanager_resource_spec': 'jobmanager_resource_spec',
        'taskmanager_resource_spec': 'taskmanager_resource_spec'
    }

    def __init__(self, max_slot=None, parallel_number=None, jobmanager_resource_spec=None, taskmanager_resource_spec=None):
        """FlinkResourceConfig

        The model defined in huaweicloud sdk

        :param max_slot: 最大的 slot 数。
        :type max_slot: int
        :param parallel_number: 用户设置的作业并行数目。默认值为1。
        :type parallel_number: int
        :param jobmanager_resource_spec: 
        :type jobmanager_resource_spec: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        :param taskmanager_resource_spec: 
        :type taskmanager_resource_spec: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        """
        
        

        self._max_slot = None
        self._parallel_number = None
        self._jobmanager_resource_spec = None
        self._taskmanager_resource_spec = None
        self.discriminator = None

        if max_slot is not None:
            self.max_slot = max_slot
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if jobmanager_resource_spec is not None:
            self.jobmanager_resource_spec = jobmanager_resource_spec
        if taskmanager_resource_spec is not None:
            self.taskmanager_resource_spec = taskmanager_resource_spec

    @property
    def max_slot(self):
        """Gets the max_slot of this FlinkResourceConfig.

        最大的 slot 数。

        :return: The max_slot of this FlinkResourceConfig.
        :rtype: int
        """
        return self._max_slot

    @max_slot.setter
    def max_slot(self, max_slot):
        """Sets the max_slot of this FlinkResourceConfig.

        最大的 slot 数。

        :param max_slot: The max_slot of this FlinkResourceConfig.
        :type max_slot: int
        """
        self._max_slot = max_slot

    @property
    def parallel_number(self):
        """Gets the parallel_number of this FlinkResourceConfig.

        用户设置的作业并行数目。默认值为1。

        :return: The parallel_number of this FlinkResourceConfig.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        """Sets the parallel_number of this FlinkResourceConfig.

        用户设置的作业并行数目。默认值为1。

        :param parallel_number: The parallel_number of this FlinkResourceConfig.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def jobmanager_resource_spec(self):
        """Gets the jobmanager_resource_spec of this FlinkResourceConfig.

        :return: The jobmanager_resource_spec of this FlinkResourceConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        """
        return self._jobmanager_resource_spec

    @jobmanager_resource_spec.setter
    def jobmanager_resource_spec(self, jobmanager_resource_spec):
        """Sets the jobmanager_resource_spec of this FlinkResourceConfig.

        :param jobmanager_resource_spec: The jobmanager_resource_spec of this FlinkResourceConfig.
        :type jobmanager_resource_spec: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        """
        self._jobmanager_resource_spec = jobmanager_resource_spec

    @property
    def taskmanager_resource_spec(self):
        """Gets the taskmanager_resource_spec of this FlinkResourceConfig.

        :return: The taskmanager_resource_spec of this FlinkResourceConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        """
        return self._taskmanager_resource_spec

    @taskmanager_resource_spec.setter
    def taskmanager_resource_spec(self, taskmanager_resource_spec):
        """Sets the taskmanager_resource_spec of this FlinkResourceConfig.

        :param taskmanager_resource_spec: The taskmanager_resource_spec of this FlinkResourceConfig.
        :type taskmanager_resource_spec: :class:`huaweicloudsdkdli.v1.ResourceSpec`
        """
        self._taskmanager_resource_spec = taskmanager_resource_spec

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
        if not isinstance(other, FlinkResourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
