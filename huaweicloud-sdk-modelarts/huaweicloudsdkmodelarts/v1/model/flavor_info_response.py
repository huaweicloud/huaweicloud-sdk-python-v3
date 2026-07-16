# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_num': 'int',
        'cpu': 'Cpu',
        'gpu': 'Gpu',
        'npu': 'Npu',
        'memory': 'Memory',
        'disk': 'DiskResponse'
    }

    attribute_map = {
        'max_num': 'max_num',
        'cpu': 'cpu',
        'gpu': 'gpu',
        'npu': 'npu',
        'memory': 'memory',
        'disk': 'disk'
    }

    def __init__(self, max_num=None, cpu=None, gpu=None, npu=None, memory=None, disk=None):
        r"""FlavorInfoResponse

        The model defined in huaweicloud sdk

        :param max_num: 可以选择的最大节点数量（max_num，为1代表不支持分布式）。
        :type max_num: int
        :param cpu: 
        :type cpu: :class:`huaweicloudsdkmodelarts.v1.Cpu`
        :param gpu: 
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.Gpu`
        :param npu: 
        :type npu: :class:`huaweicloudsdkmodelarts.v1.Npu`
        :param memory: 
        :type memory: :class:`huaweicloudsdkmodelarts.v1.Memory`
        :param disk: 
        :type disk: :class:`huaweicloudsdkmodelarts.v1.DiskResponse`
        """
        
        

        self._max_num = None
        self._cpu = None
        self._gpu = None
        self._npu = None
        self._memory = None
        self._disk = None
        self.discriminator = None

        if max_num is not None:
            self.max_num = max_num
        if cpu is not None:
            self.cpu = cpu
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk

    @property
    def max_num(self):
        r"""Gets the max_num of this FlavorInfoResponse.

        可以选择的最大节点数量（max_num，为1代表不支持分布式）。

        :return: The max_num of this FlavorInfoResponse.
        :rtype: int
        """
        return self._max_num

    @max_num.setter
    def max_num(self, max_num):
        r"""Sets the max_num of this FlavorInfoResponse.

        可以选择的最大节点数量（max_num，为1代表不支持分布式）。

        :param max_num: The max_num of this FlavorInfoResponse.
        :type max_num: int
        """
        self._max_num = max_num

    @property
    def cpu(self):
        r"""Gets the cpu of this FlavorInfoResponse.

        :return: The cpu of this FlavorInfoResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Cpu`
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this FlavorInfoResponse.

        :param cpu: The cpu of this FlavorInfoResponse.
        :type cpu: :class:`huaweicloudsdkmodelarts.v1.Cpu`
        """
        self._cpu = cpu

    @property
    def gpu(self):
        r"""Gets the gpu of this FlavorInfoResponse.

        :return: The gpu of this FlavorInfoResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Gpu`
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this FlavorInfoResponse.

        :param gpu: The gpu of this FlavorInfoResponse.
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.Gpu`
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this FlavorInfoResponse.

        :return: The npu of this FlavorInfoResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Npu`
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this FlavorInfoResponse.

        :param npu: The npu of this FlavorInfoResponse.
        :type npu: :class:`huaweicloudsdkmodelarts.v1.Npu`
        """
        self._npu = npu

    @property
    def memory(self):
        r"""Gets the memory of this FlavorInfoResponse.

        :return: The memory of this FlavorInfoResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Memory`
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this FlavorInfoResponse.

        :param memory: The memory of this FlavorInfoResponse.
        :type memory: :class:`huaweicloudsdkmodelarts.v1.Memory`
        """
        self._memory = memory

    @property
    def disk(self):
        r"""Gets the disk of this FlavorInfoResponse.

        :return: The disk of this FlavorInfoResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DiskResponse`
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this FlavorInfoResponse.

        :param disk: The disk of this FlavorInfoResponse.
        :type disk: :class:`huaweicloudsdkmodelarts.v1.DiskResponse`
        """
        self._disk = disk

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FlavorInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
