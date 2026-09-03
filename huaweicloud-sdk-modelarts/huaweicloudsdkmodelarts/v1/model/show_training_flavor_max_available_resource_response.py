# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingFlavorMaxAvailableResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_core_num': 'int',
        'mem_size': 'int'
    }

    attribute_map = {
        'cpu_core_num': 'cpu_core_num',
        'mem_size': 'mem_size'
    }

    def __init__(self, cpu_core_num=None, mem_size=None):
        r"""ShowTrainingFlavorMaxAvailableResourceResponse

        The model defined in huaweicloud sdk

        :param cpu_core_num: **参数解释**：最大可用CPU核数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type cpu_core_num: int
        :param mem_size: **参数解释**：最大可用内存大小，单位为GB。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type mem_size: int
        """
        
        super().__init__()

        self._cpu_core_num = None
        self._mem_size = None
        self.discriminator = None

        if cpu_core_num is not None:
            self.cpu_core_num = cpu_core_num
        if mem_size is not None:
            self.mem_size = mem_size

    @property
    def cpu_core_num(self):
        r"""Gets the cpu_core_num of this ShowTrainingFlavorMaxAvailableResourceResponse.

        **参数解释**：最大可用CPU核数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The cpu_core_num of this ShowTrainingFlavorMaxAvailableResourceResponse.
        :rtype: int
        """
        return self._cpu_core_num

    @cpu_core_num.setter
    def cpu_core_num(self, cpu_core_num):
        r"""Sets the cpu_core_num of this ShowTrainingFlavorMaxAvailableResourceResponse.

        **参数解释**：最大可用CPU核数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param cpu_core_num: The cpu_core_num of this ShowTrainingFlavorMaxAvailableResourceResponse.
        :type cpu_core_num: int
        """
        self._cpu_core_num = cpu_core_num

    @property
    def mem_size(self):
        r"""Gets the mem_size of this ShowTrainingFlavorMaxAvailableResourceResponse.

        **参数解释**：最大可用内存大小，单位为GB。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The mem_size of this ShowTrainingFlavorMaxAvailableResourceResponse.
        :rtype: int
        """
        return self._mem_size

    @mem_size.setter
    def mem_size(self, mem_size):
        r"""Sets the mem_size of this ShowTrainingFlavorMaxAvailableResourceResponse.

        **参数解释**：最大可用内存大小，单位为GB。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param mem_size: The mem_size of this ShowTrainingFlavorMaxAvailableResourceResponse.
        :type mem_size: int
        """
        self._mem_size = mem_size

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrainingFlavorMaxAvailableResourceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrainingFlavorMaxAvailableResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
