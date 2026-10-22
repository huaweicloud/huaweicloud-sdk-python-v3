# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceLimit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'spec_code': 'str',
        'compute_allocatable': 'ComputeAllocatable',
        'compute_size': 'ComputeSize',
        'worker_sizes': 'list[WorkerSizeInfo]'
    }

    attribute_map = {
        'type': 'type',
        'spec_code': 'spec_code',
        'compute_allocatable': 'compute_allocatable',
        'compute_size': 'compute_size',
        'worker_sizes': 'worker_sizes'
    }

    def __init__(self, type=None, spec_code=None, compute_allocatable=None, compute_size=None, worker_sizes=None):
        r"""ResourceLimit

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源类型。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 
        :type type: str
        :param spec_code: **参数解释**：资源规格编码，标识资源池中具体的资源规格，由系统生成，例如\&quot;aidatalake.cpu.x86.general.1c2g\&quot;。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 
        :type spec_code: str
        :param compute_allocatable: 
        :type compute_allocatable: :class:`huaweicloudsdkaidatalake.v2.ComputeAllocatable`
        :param compute_size: 
        :type compute_size: :class:`huaweicloudsdkaidatalake.v2.ComputeSize`
        :param worker_sizes: **参数解释**：可选的资源配置枚举列表。
        :type worker_sizes: list[:class:`huaweicloudsdkaidatalake.v2.WorkerSizeInfo`]
        """
        
        

        self._type = None
        self._spec_code = None
        self._compute_allocatable = None
        self._compute_size = None
        self._worker_sizes = None
        self.discriminator = None

        self.type = type
        self.spec_code = spec_code
        if compute_allocatable is not None:
            self.compute_allocatable = compute_allocatable
        if compute_size is not None:
            self.compute_size = compute_size
        if worker_sizes is not None:
            self.worker_sizes = worker_sizes

    @property
    def type(self):
        r"""Gets the type of this ResourceLimit.

        **参数解释**：资源类型。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 

        :return: The type of this ResourceLimit.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceLimit.

        **参数解释**：资源类型。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 

        :param type: The type of this ResourceLimit.
        :type type: str
        """
        self._type = type

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ResourceLimit.

        **参数解释**：资源规格编码，标识资源池中具体的资源规格，由系统生成，例如\"aidatalake.cpu.x86.general.1c2g\"。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 

        :return: The spec_code of this ResourceLimit.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ResourceLimit.

        **参数解释**：资源规格编码，标识资源池中具体的资源规格，由系统生成，例如\"aidatalake.cpu.x86.general.1c2g\"。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 

        :param spec_code: The spec_code of this ResourceLimit.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def compute_allocatable(self):
        r"""Gets the compute_allocatable of this ResourceLimit.

        :return: The compute_allocatable of this ResourceLimit.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ComputeAllocatable`
        """
        return self._compute_allocatable

    @compute_allocatable.setter
    def compute_allocatable(self, compute_allocatable):
        r"""Sets the compute_allocatable of this ResourceLimit.

        :param compute_allocatable: The compute_allocatable of this ResourceLimit.
        :type compute_allocatable: :class:`huaweicloudsdkaidatalake.v2.ComputeAllocatable`
        """
        self._compute_allocatable = compute_allocatable

    @property
    def compute_size(self):
        r"""Gets the compute_size of this ResourceLimit.

        :return: The compute_size of this ResourceLimit.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ComputeSize`
        """
        return self._compute_size

    @compute_size.setter
    def compute_size(self, compute_size):
        r"""Sets the compute_size of this ResourceLimit.

        :param compute_size: The compute_size of this ResourceLimit.
        :type compute_size: :class:`huaweicloudsdkaidatalake.v2.ComputeSize`
        """
        self._compute_size = compute_size

    @property
    def worker_sizes(self):
        r"""Gets the worker_sizes of this ResourceLimit.

        **参数解释**：可选的资源配置枚举列表。

        :return: The worker_sizes of this ResourceLimit.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.WorkerSizeInfo`]
        """
        return self._worker_sizes

    @worker_sizes.setter
    def worker_sizes(self, worker_sizes):
        r"""Sets the worker_sizes of this ResourceLimit.

        **参数解释**：可选的资源配置枚举列表。

        :param worker_sizes: The worker_sizes of this ResourceLimit.
        :type worker_sizes: list[:class:`huaweicloudsdkaidatalake.v2.WorkerSizeInfo`]
        """
        self._worker_sizes = worker_sizes

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
        if not isinstance(other, ResourceLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
