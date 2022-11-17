# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:

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
        'gpu': 'float',
        'memory': 'float'
    }

    attribute_map = {
        'cpu': 'cpu',
        'gpu': 'gpu',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, gpu=None, memory=None):
        """FlavorInfo

        The model defined in huaweicloud sdk

        :param cpu: notebook占用的cpu,0.1核为100m,单位为\&quot;C\&quot;
        :type cpu: float
        :param gpu: notebook占用的gpu，0.1为使用单卡10%，1为占满单个显卡，1+为使用多个显卡
        :type gpu: float
        :param memory: notebook占用的内存,单位为\&quot;G\&quot;
        :type memory: float
        """
        
        

        self._cpu = None
        self._gpu = None
        self._memory = None
        self.discriminator = None

        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this FlavorInfo.

        notebook占用的cpu,0.1核为100m,单位为\"C\"

        :return: The cpu of this FlavorInfo.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this FlavorInfo.

        notebook占用的cpu,0.1核为100m,单位为\"C\"

        :param cpu: The cpu of this FlavorInfo.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def gpu(self):
        """Gets the gpu of this FlavorInfo.

        notebook占用的gpu，0.1为使用单卡10%，1为占满单个显卡，1+为使用多个显卡

        :return: The gpu of this FlavorInfo.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this FlavorInfo.

        notebook占用的gpu，0.1为使用单卡10%，1为占满单个显卡，1+为使用多个显卡

        :param gpu: The gpu of this FlavorInfo.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def memory(self):
        """Gets the memory of this FlavorInfo.

        notebook占用的内存,单位为\"G\"

        :return: The memory of this FlavorInfo.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this FlavorInfo.

        notebook占用的内存,单位为\"G\"

        :param memory: The memory of this FlavorInfo.
        :type memory: float
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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
