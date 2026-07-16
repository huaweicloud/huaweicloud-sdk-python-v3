# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AscendResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'npu': 'int',
        'npu_memory': 'str',
        'type': 'str',
        'ai_core': 'str',
        'ai_cpu': 'str'
    }

    attribute_map = {
        'npu': 'npu',
        'npu_memory': 'npu_memory',
        'type': 'type',
        'ai_core': 'ai_core',
        'ai_cpu': 'ai_cpu'
    }

    def __init__(self, npu=None, npu_memory=None, type=None, ai_core=None, ai_cpu=None):
        r"""AscendResource

        The model defined in huaweicloud sdk

        :param npu: **参数解释：** NPU数量。 **取值范围：** 不涉及。
        :type npu: int
        :param npu_memory: **参数解释：** NPU内存。 **取值范围：** 不涉及。
        :type npu_memory: str
        :param type: **参数解释：** NPU类型。 **取值范围：** 不涉及。
        :type type: str
        :param ai_core: **参数解释：** 切分规格中的ai_core。 **取值范围：** 不涉及。
        :type ai_core: str
        :param ai_cpu: **参数解释：** 切分规格中的ai_cpu。 **取值范围：** 不涉及。
        :type ai_cpu: str
        """
        
        

        self._npu = None
        self._npu_memory = None
        self._type = None
        self._ai_core = None
        self._ai_cpu = None
        self.discriminator = None

        if npu is not None:
            self.npu = npu
        if npu_memory is not None:
            self.npu_memory = npu_memory
        if type is not None:
            self.type = type
        if ai_core is not None:
            self.ai_core = ai_core
        if ai_cpu is not None:
            self.ai_cpu = ai_cpu

    @property
    def npu(self):
        r"""Gets the npu of this AscendResource.

        **参数解释：** NPU数量。 **取值范围：** 不涉及。

        :return: The npu of this AscendResource.
        :rtype: int
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this AscendResource.

        **参数解释：** NPU数量。 **取值范围：** 不涉及。

        :param npu: The npu of this AscendResource.
        :type npu: int
        """
        self._npu = npu

    @property
    def npu_memory(self):
        r"""Gets the npu_memory of this AscendResource.

        **参数解释：** NPU内存。 **取值范围：** 不涉及。

        :return: The npu_memory of this AscendResource.
        :rtype: str
        """
        return self._npu_memory

    @npu_memory.setter
    def npu_memory(self, npu_memory):
        r"""Sets the npu_memory of this AscendResource.

        **参数解释：** NPU内存。 **取值范围：** 不涉及。

        :param npu_memory: The npu_memory of this AscendResource.
        :type npu_memory: str
        """
        self._npu_memory = npu_memory

    @property
    def type(self):
        r"""Gets the type of this AscendResource.

        **参数解释：** NPU类型。 **取值范围：** 不涉及。

        :return: The type of this AscendResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AscendResource.

        **参数解释：** NPU类型。 **取值范围：** 不涉及。

        :param type: The type of this AscendResource.
        :type type: str
        """
        self._type = type

    @property
    def ai_core(self):
        r"""Gets the ai_core of this AscendResource.

        **参数解释：** 切分规格中的ai_core。 **取值范围：** 不涉及。

        :return: The ai_core of this AscendResource.
        :rtype: str
        """
        return self._ai_core

    @ai_core.setter
    def ai_core(self, ai_core):
        r"""Sets the ai_core of this AscendResource.

        **参数解释：** 切分规格中的ai_core。 **取值范围：** 不涉及。

        :param ai_core: The ai_core of this AscendResource.
        :type ai_core: str
        """
        self._ai_core = ai_core

    @property
    def ai_cpu(self):
        r"""Gets the ai_cpu of this AscendResource.

        **参数解释：** 切分规格中的ai_cpu。 **取值范围：** 不涉及。

        :return: The ai_cpu of this AscendResource.
        :rtype: str
        """
        return self._ai_cpu

    @ai_cpu.setter
    def ai_cpu(self, ai_cpu):
        r"""Sets the ai_cpu of this AscendResource.

        **参数解释：** 切分规格中的ai_cpu。 **取值范围：** 不涉及。

        :param ai_cpu: The ai_cpu of this AscendResource.
        :type ai_cpu: str
        """
        self._ai_cpu = ai_cpu

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
        if not isinstance(other, AscendResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
