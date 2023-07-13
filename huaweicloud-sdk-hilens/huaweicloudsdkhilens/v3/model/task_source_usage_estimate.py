# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskSourceUsageEstimate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'float',
        'memory': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, memory=None):
        """TaskSourceUsageEstimate

        The model defined in huaweicloud sdk

        :param cpu: cpu消耗
        :type cpu: float
        :param memory: 内存消耗
        :type memory: int
        """
        
        

        self._cpu = None
        self._memory = None
        self.discriminator = None

        self.cpu = cpu
        self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this TaskSourceUsageEstimate.

        cpu消耗

        :return: The cpu of this TaskSourceUsageEstimate.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this TaskSourceUsageEstimate.

        cpu消耗

        :param cpu: The cpu of this TaskSourceUsageEstimate.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this TaskSourceUsageEstimate.

        内存消耗

        :return: The memory of this TaskSourceUsageEstimate.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this TaskSourceUsageEstimate.

        内存消耗

        :param memory: The memory of this TaskSourceUsageEstimate.
        :type memory: int
        """
        self._memory = memory

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
        if not isinstance(other, TaskSourceUsageEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
