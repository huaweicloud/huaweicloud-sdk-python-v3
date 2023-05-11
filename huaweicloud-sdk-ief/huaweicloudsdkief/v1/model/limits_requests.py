# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LimitsRequests:

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
        'memory': 'float',
        'gpu': 'float',
        'npu': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'npu': 'npu'
    }

    def __init__(self, cpu=None, memory=None, gpu=None, npu=None):
        """LimitsRequests

        The model defined in huaweicloud sdk

        :param cpu: cpu核数，大于等于0.01，最大1000；请求不需要带单位
        :type cpu: float
        :param memory: 内存大小，单位兆，大于等于0.01，最大1024000。注意：内存的limits值最小为4；请求不需要带单位
        :type memory: float
        :param gpu: Gpu显存大小，单位兆，大于等于0.01，最大1024000；请求不需要带单位
        :type gpu: float
        :param npu: Npu个数，大于0，最大1000；请求不需要带单位
        :type npu: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._gpu = None
        self._npu = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu

    @property
    def cpu(self):
        """Gets the cpu of this LimitsRequests.

        cpu核数，大于等于0.01，最大1000；请求不需要带单位

        :return: The cpu of this LimitsRequests.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this LimitsRequests.

        cpu核数，大于等于0.01，最大1000；请求不需要带单位

        :param cpu: The cpu of this LimitsRequests.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this LimitsRequests.

        内存大小，单位兆，大于等于0.01，最大1024000。注意：内存的limits值最小为4；请求不需要带单位

        :return: The memory of this LimitsRequests.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this LimitsRequests.

        内存大小，单位兆，大于等于0.01，最大1024000。注意：内存的limits值最小为4；请求不需要带单位

        :param memory: The memory of this LimitsRequests.
        :type memory: float
        """
        self._memory = memory

    @property
    def gpu(self):
        """Gets the gpu of this LimitsRequests.

        Gpu显存大小，单位兆，大于等于0.01，最大1024000；请求不需要带单位

        :return: The gpu of this LimitsRequests.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this LimitsRequests.

        Gpu显存大小，单位兆，大于等于0.01，最大1024000；请求不需要带单位

        :param gpu: The gpu of this LimitsRequests.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def npu(self):
        """Gets the npu of this LimitsRequests.

        Npu个数，大于0，最大1000；请求不需要带单位

        :return: The npu of this LimitsRequests.
        :rtype: int
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        """Sets the npu of this LimitsRequests.

        Npu个数，大于0，最大1000；请求不需要带单位

        :param npu: The npu of this LimitsRequests.
        :type npu: int
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
        if not isinstance(other, LimitsRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
