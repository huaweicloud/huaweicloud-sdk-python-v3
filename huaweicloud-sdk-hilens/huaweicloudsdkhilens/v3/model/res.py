# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Res:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'str',
        'gpu': 'str',
        'memory': 'str',
        'npu': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'gpu': 'gpu',
        'memory': 'memory',
        'npu': 'npu'
    }

    def __init__(self, cpu=None, gpu=None, memory=None, npu=None):
        """Res

        The model defined in huaweicloud sdk

        :param cpu: cpu数量，字符串所对应的数值在0.01到1000之间
        :type cpu: str
        :param gpu: gpu数量，值在0到1000
        :type gpu: str
        :param memory: 内存数量，如果是资源限制，其值范围在4到1024000之间，否则在0.01到1024000之间
        :type memory: str
        :param npu: npu数量，字符串所对应的数值在0.到1000之间
        :type npu: str
        """
        
        

        self._cpu = None
        self._gpu = None
        self._memory = None
        self._npu = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if gpu is not None:
            self.gpu = gpu
        if memory is not None:
            self.memory = memory
        if npu is not None:
            self.npu = npu

    @property
    def cpu(self):
        """Gets the cpu of this Res.

        cpu数量，字符串所对应的数值在0.01到1000之间

        :return: The cpu of this Res.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Res.

        cpu数量，字符串所对应的数值在0.01到1000之间

        :param cpu: The cpu of this Res.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def gpu(self):
        """Gets the gpu of this Res.

        gpu数量，值在0到1000

        :return: The gpu of this Res.
        :rtype: str
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this Res.

        gpu数量，值在0到1000

        :param gpu: The gpu of this Res.
        :type gpu: str
        """
        self._gpu = gpu

    @property
    def memory(self):
        """Gets the memory of this Res.

        内存数量，如果是资源限制，其值范围在4到1024000之间，否则在0.01到1024000之间

        :return: The memory of this Res.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Res.

        内存数量，如果是资源限制，其值范围在4到1024000之间，否则在0.01到1024000之间

        :param memory: The memory of this Res.
        :type memory: str
        """
        self._memory = memory

    @property
    def npu(self):
        """Gets the npu of this Res.

        npu数量，字符串所对应的数值在0.到1000之间

        :return: The npu of this Res.
        :rtype: str
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        """Sets the npu of this Res.

        npu数量，字符串所对应的数值在0.到1000之间

        :param npu: The npu of this Res.
        :type npu: str
        """
        self._npu = npu

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
        if not isinstance(other, Res):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
