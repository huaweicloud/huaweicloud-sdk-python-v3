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
        'spec_code': 'str',
        'cpu_resource': 'int',
        'memory_resource': 'int',
        'npu_resource': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'cpu_resource': 'cpu_resource',
        'memory_resource': 'memory_resource',
        'npu_resource': 'npu_resource'
    }

    def __init__(self, spec_code=None, cpu_resource=None, memory_resource=None, npu_resource=None):
        r"""ResourceSpec

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格，从规格列表查询获取。
        :type spec_code: str
        :param cpu_resource: **参数解释**：cpu核数量。 **约束限制**：不涉及。 **取值范围**：[0,192]。 **默认取值**：null。
        :type cpu_resource: int
        :param memory_resource: **参数解释**：内存大小。 **约束限制**：不涉及。 **取值范围**：[0,1536]。 **默认取值**：null。
        :type memory_resource: int
        :param npu_resource: **参数解释**：昇腾卡数量。 **约束限制**：不涉及。 **取值范围**：[0,8]。 **默认取值**：null。
        :type npu_resource: int
        """
        
        

        self._spec_code = None
        self._cpu_resource = None
        self._memory_resource = None
        self._npu_resource = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if cpu_resource is not None:
            self.cpu_resource = cpu_resource
        if memory_resource is not None:
            self.memory_resource = memory_resource
        if npu_resource is not None:
            self.npu_resource = npu_resource

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ResourceSpec.

        资源规格，从规格列表查询获取。

        :return: The spec_code of this ResourceSpec.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ResourceSpec.

        资源规格，从规格列表查询获取。

        :param spec_code: The spec_code of this ResourceSpec.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cpu_resource(self):
        r"""Gets the cpu_resource of this ResourceSpec.

        **参数解释**：cpu核数量。 **约束限制**：不涉及。 **取值范围**：[0,192]。 **默认取值**：null。

        :return: The cpu_resource of this ResourceSpec.
        :rtype: int
        """
        return self._cpu_resource

    @cpu_resource.setter
    def cpu_resource(self, cpu_resource):
        r"""Sets the cpu_resource of this ResourceSpec.

        **参数解释**：cpu核数量。 **约束限制**：不涉及。 **取值范围**：[0,192]。 **默认取值**：null。

        :param cpu_resource: The cpu_resource of this ResourceSpec.
        :type cpu_resource: int
        """
        self._cpu_resource = cpu_resource

    @property
    def memory_resource(self):
        r"""Gets the memory_resource of this ResourceSpec.

        **参数解释**：内存大小。 **约束限制**：不涉及。 **取值范围**：[0,1536]。 **默认取值**：null。

        :return: The memory_resource of this ResourceSpec.
        :rtype: int
        """
        return self._memory_resource

    @memory_resource.setter
    def memory_resource(self, memory_resource):
        r"""Sets the memory_resource of this ResourceSpec.

        **参数解释**：内存大小。 **约束限制**：不涉及。 **取值范围**：[0,1536]。 **默认取值**：null。

        :param memory_resource: The memory_resource of this ResourceSpec.
        :type memory_resource: int
        """
        self._memory_resource = memory_resource

    @property
    def npu_resource(self):
        r"""Gets the npu_resource of this ResourceSpec.

        **参数解释**：昇腾卡数量。 **约束限制**：不涉及。 **取值范围**：[0,8]。 **默认取值**：null。

        :return: The npu_resource of this ResourceSpec.
        :rtype: int
        """
        return self._npu_resource

    @npu_resource.setter
    def npu_resource(self, npu_resource):
        r"""Sets the npu_resource of this ResourceSpec.

        **参数解释**：昇腾卡数量。 **约束限制**：不涉及。 **取值范围**：[0,8]。 **默认取值**：null。

        :param npu_resource: The npu_resource of this ResourceSpec.
        :type npu_resource: int
        """
        self._npu_resource = npu_resource

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
