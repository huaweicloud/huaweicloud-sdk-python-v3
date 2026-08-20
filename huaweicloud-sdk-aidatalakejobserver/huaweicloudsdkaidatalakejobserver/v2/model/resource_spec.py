# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'memory': 'int',
        'disk': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'disk': 'disk'
    }

    def __init__(self, cpu=None, memory=None, disk=None):
        r"""ResourceSpec

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：CPU核数，单位为毫核，用于指定作业运行所需的CPU资源。 **约束限制**：不涉及。 **取值范围**：最小值为1000，最大值为48000。 **默认取值**：1000。 
        :type cpu: int
        :param memory: **参数解释**：内存大小，单位为MB，用于指定作业运行所需的内存资源。 **约束限制**：不涉及。 **取值范围**：最小值为1024，最大值为393216。 **默认取值**：4096。 
        :type memory: int
        :param disk: **参数解释**：本地磁盘大小，用于指定Spark作业Driver和Executor的本地磁盘资源。 **约束限制**：不涉及。 **取值范围**：单位为GB，最小值为0，最大值为994。 **默认取值**：不涉及。 
        :type disk: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._disk = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk

    @property
    def cpu(self):
        r"""Gets the cpu of this ResourceSpec.

        **参数解释**：CPU核数，单位为毫核，用于指定作业运行所需的CPU资源。 **约束限制**：不涉及。 **取值范围**：最小值为1000，最大值为48000。 **默认取值**：1000。 

        :return: The cpu of this ResourceSpec.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResourceSpec.

        **参数解释**：CPU核数，单位为毫核，用于指定作业运行所需的CPU资源。 **约束限制**：不涉及。 **取值范围**：最小值为1000，最大值为48000。 **默认取值**：1000。 

        :param cpu: The cpu of this ResourceSpec.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ResourceSpec.

        **参数解释**：内存大小，单位为MB，用于指定作业运行所需的内存资源。 **约束限制**：不涉及。 **取值范围**：最小值为1024，最大值为393216。 **默认取值**：4096。 

        :return: The memory of this ResourceSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ResourceSpec.

        **参数解释**：内存大小，单位为MB，用于指定作业运行所需的内存资源。 **约束限制**：不涉及。 **取值范围**：最小值为1024，最大值为393216。 **默认取值**：4096。 

        :param memory: The memory of this ResourceSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def disk(self):
        r"""Gets the disk of this ResourceSpec.

        **参数解释**：本地磁盘大小，用于指定Spark作业Driver和Executor的本地磁盘资源。 **约束限制**：不涉及。 **取值范围**：单位为GB，最小值为0，最大值为994。 **默认取值**：不涉及。 

        :return: The disk of this ResourceSpec.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this ResourceSpec.

        **参数解释**：本地磁盘大小，用于指定Spark作业Driver和Executor的本地磁盘资源。 **约束限制**：不涉及。 **取值范围**：单位为GB，最小值为0，最大值为994。 **默认取值**：不涉及。 

        :param disk: The disk of this ResourceSpec.
        :type disk: int
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
        if not isinstance(other, ResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
