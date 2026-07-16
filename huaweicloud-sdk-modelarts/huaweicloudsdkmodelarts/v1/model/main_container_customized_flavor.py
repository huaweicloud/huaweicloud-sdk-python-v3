# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MainContainerCustomizedFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_core_num': 'float',
        'mem_size': 'float',
        'accelerator_num': 'float'
    }

    attribute_map = {
        'cpu_core_num': 'cpu_core_num',
        'mem_size': 'mem_size',
        'accelerator_num': 'accelerator_num'
    }

    def __init__(self, cpu_core_num=None, mem_size=None, accelerator_num=None):
        r"""MainContainerCustomizedFlavor

        The model defined in huaweicloud sdk

        :param cpu_core_num: **参数解释**：cpu核数。 **取值范围**：大于零。
        :type cpu_core_num: float
        :param mem_size: **参数解释**：内存大小。 **取值范围**：大于零。
        :type mem_size: float
        :param accelerator_num: **参数解释**：加速卡卡数。 **取值范围**：大于等于零。
        :type accelerator_num: float
        """
        
        

        self._cpu_core_num = None
        self._mem_size = None
        self._accelerator_num = None
        self.discriminator = None

        if cpu_core_num is not None:
            self.cpu_core_num = cpu_core_num
        if mem_size is not None:
            self.mem_size = mem_size
        if accelerator_num is not None:
            self.accelerator_num = accelerator_num

    @property
    def cpu_core_num(self):
        r"""Gets the cpu_core_num of this MainContainerCustomizedFlavor.

        **参数解释**：cpu核数。 **取值范围**：大于零。

        :return: The cpu_core_num of this MainContainerCustomizedFlavor.
        :rtype: float
        """
        return self._cpu_core_num

    @cpu_core_num.setter
    def cpu_core_num(self, cpu_core_num):
        r"""Sets the cpu_core_num of this MainContainerCustomizedFlavor.

        **参数解释**：cpu核数。 **取值范围**：大于零。

        :param cpu_core_num: The cpu_core_num of this MainContainerCustomizedFlavor.
        :type cpu_core_num: float
        """
        self._cpu_core_num = cpu_core_num

    @property
    def mem_size(self):
        r"""Gets the mem_size of this MainContainerCustomizedFlavor.

        **参数解释**：内存大小。 **取值范围**：大于零。

        :return: The mem_size of this MainContainerCustomizedFlavor.
        :rtype: float
        """
        return self._mem_size

    @mem_size.setter
    def mem_size(self, mem_size):
        r"""Sets the mem_size of this MainContainerCustomizedFlavor.

        **参数解释**：内存大小。 **取值范围**：大于零。

        :param mem_size: The mem_size of this MainContainerCustomizedFlavor.
        :type mem_size: float
        """
        self._mem_size = mem_size

    @property
    def accelerator_num(self):
        r"""Gets the accelerator_num of this MainContainerCustomizedFlavor.

        **参数解释**：加速卡卡数。 **取值范围**：大于等于零。

        :return: The accelerator_num of this MainContainerCustomizedFlavor.
        :rtype: float
        """
        return self._accelerator_num

    @accelerator_num.setter
    def accelerator_num(self, accelerator_num):
        r"""Sets the accelerator_num of this MainContainerCustomizedFlavor.

        **参数解释**：加速卡卡数。 **取值范围**：大于等于零。

        :param accelerator_num: The accelerator_num of this MainContainerCustomizedFlavor.
        :type accelerator_num: float
        """
        self._accelerator_num = accelerator_num

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
        if not isinstance(other, MainContainerCustomizedFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
