# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeSize:

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
        'mem': 'int',
        'accelerator': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'mem': 'mem',
        'accelerator': 'accelerator'
    }

    def __init__(self, cpu=None, mem=None, accelerator=None):
        r"""ComputeSize

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：cpu总量，单位毫核。 **取值范围**：等于资源池该规格cpu大小。 
        :type cpu: int
        :param mem: **参数解释**：内存总量，单位MB。 **取值范围**：等于资源池该规格内存大小。 
        :type mem: int
        :param accelerator: **参数解释**：显卡总量，单位卡。 **取值范围**：等于资源池该规格显卡数量大小。 
        :type accelerator: int
        """
        
        

        self._cpu = None
        self._mem = None
        self._accelerator = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if accelerator is not None:
            self.accelerator = accelerator

    @property
    def cpu(self):
        r"""Gets the cpu of this ComputeSize.

        **参数解释**：cpu总量，单位毫核。 **取值范围**：等于资源池该规格cpu大小。 

        :return: The cpu of this ComputeSize.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ComputeSize.

        **参数解释**：cpu总量，单位毫核。 **取值范围**：等于资源池该规格cpu大小。 

        :param cpu: The cpu of this ComputeSize.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this ComputeSize.

        **参数解释**：内存总量，单位MB。 **取值范围**：等于资源池该规格内存大小。 

        :return: The mem of this ComputeSize.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this ComputeSize.

        **参数解释**：内存总量，单位MB。 **取值范围**：等于资源池该规格内存大小。 

        :param mem: The mem of this ComputeSize.
        :type mem: int
        """
        self._mem = mem

    @property
    def accelerator(self):
        r"""Gets the accelerator of this ComputeSize.

        **参数解释**：显卡总量，单位卡。 **取值范围**：等于资源池该规格显卡数量大小。 

        :return: The accelerator of this ComputeSize.
        :rtype: int
        """
        return self._accelerator

    @accelerator.setter
    def accelerator(self, accelerator):
        r"""Sets the accelerator of this ComputeSize.

        **参数解释**：显卡总量，单位卡。 **取值范围**：等于资源池该规格显卡数量大小。 

        :param accelerator: The accelerator of this ComputeSize.
        :type accelerator: int
        """
        self._accelerator = accelerator

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
        if not isinstance(other, ComputeSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
