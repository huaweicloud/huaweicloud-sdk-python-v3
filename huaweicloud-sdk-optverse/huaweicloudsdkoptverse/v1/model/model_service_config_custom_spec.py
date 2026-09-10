# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelServiceConfigCustomSpec:

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
        'ascend': 'str',
        'memory': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'gpu': 'gpu',
        'ascend': 'ascend',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, gpu=None, ascend=None, memory=None):
        r"""ModelServiceConfigCustomSpec

        The model defined in huaweicloud sdk

        :param cpu: CPU核数
        :type cpu: str
        :param gpu: GPU个数
        :type gpu: str
        :param ascend: 昇腾芯片个数
        :type ascend: str
        :param memory: 内存大小
        :type memory: str
        """
        
        

        self._cpu = None
        self._gpu = None
        self._ascend = None
        self._memory = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if gpu is not None:
            self.gpu = gpu
        if ascend is not None:
            self.ascend = ascend
        if memory is not None:
            self.memory = memory

    @property
    def cpu(self):
        r"""Gets the cpu of this ModelServiceConfigCustomSpec.

        CPU核数

        :return: The cpu of this ModelServiceConfigCustomSpec.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ModelServiceConfigCustomSpec.

        CPU核数

        :param cpu: The cpu of this ModelServiceConfigCustomSpec.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def gpu(self):
        r"""Gets the gpu of this ModelServiceConfigCustomSpec.

        GPU个数

        :return: The gpu of this ModelServiceConfigCustomSpec.
        :rtype: str
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this ModelServiceConfigCustomSpec.

        GPU个数

        :param gpu: The gpu of this ModelServiceConfigCustomSpec.
        :type gpu: str
        """
        self._gpu = gpu

    @property
    def ascend(self):
        r"""Gets the ascend of this ModelServiceConfigCustomSpec.

        昇腾芯片个数

        :return: The ascend of this ModelServiceConfigCustomSpec.
        :rtype: str
        """
        return self._ascend

    @ascend.setter
    def ascend(self, ascend):
        r"""Sets the ascend of this ModelServiceConfigCustomSpec.

        昇腾芯片个数

        :param ascend: The ascend of this ModelServiceConfigCustomSpec.
        :type ascend: str
        """
        self._ascend = ascend

    @property
    def memory(self):
        r"""Gets the memory of this ModelServiceConfigCustomSpec.

        内存大小

        :return: The memory of this ModelServiceConfigCustomSpec.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ModelServiceConfigCustomSpec.

        内存大小

        :param memory: The memory of this ModelServiceConfigCustomSpec.
        :type memory: str
        """
        self._memory = memory

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
        if not isinstance(other, ModelServiceConfigCustomSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
