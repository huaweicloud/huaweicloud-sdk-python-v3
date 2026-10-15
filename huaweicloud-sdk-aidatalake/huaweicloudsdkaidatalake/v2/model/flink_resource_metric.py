# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkResourceMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_memory': 'int',
        'total_cpu': 'int',
        'total_disk': 'int'
    }

    attribute_map = {
        'total_memory': 'total_memory',
        'total_cpu': 'total_cpu',
        'total_disk': 'total_disk'
    }

    def __init__(self, total_memory=None, total_cpu=None, total_disk=None):
        r"""FlinkResourceMetric

        The model defined in huaweicloud sdk

        :param total_memory: **参数解释**：总内存，单位MB。 **取值范围**：0~9223372036854775807。 
        :type total_memory: int
        :param total_cpu: **参数解释**：总CPU，单位毫核。 **取值范围**：0~9223372036854775807。 
        :type total_cpu: int
        :param total_disk: **参数解释**：总磁盘容量，单位GB。 **取值范围**：0~9223372036854775807。 
        :type total_disk: int
        """
        
        

        self._total_memory = None
        self._total_cpu = None
        self._total_disk = None
        self.discriminator = None

        if total_memory is not None:
            self.total_memory = total_memory
        if total_cpu is not None:
            self.total_cpu = total_cpu
        if total_disk is not None:
            self.total_disk = total_disk

    @property
    def total_memory(self):
        r"""Gets the total_memory of this FlinkResourceMetric.

        **参数解释**：总内存，单位MB。 **取值范围**：0~9223372036854775807。 

        :return: The total_memory of this FlinkResourceMetric.
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        r"""Sets the total_memory of this FlinkResourceMetric.

        **参数解释**：总内存，单位MB。 **取值范围**：0~9223372036854775807。 

        :param total_memory: The total_memory of this FlinkResourceMetric.
        :type total_memory: int
        """
        self._total_memory = total_memory

    @property
    def total_cpu(self):
        r"""Gets the total_cpu of this FlinkResourceMetric.

        **参数解释**：总CPU，单位毫核。 **取值范围**：0~9223372036854775807。 

        :return: The total_cpu of this FlinkResourceMetric.
        :rtype: int
        """
        return self._total_cpu

    @total_cpu.setter
    def total_cpu(self, total_cpu):
        r"""Sets the total_cpu of this FlinkResourceMetric.

        **参数解释**：总CPU，单位毫核。 **取值范围**：0~9223372036854775807。 

        :param total_cpu: The total_cpu of this FlinkResourceMetric.
        :type total_cpu: int
        """
        self._total_cpu = total_cpu

    @property
    def total_disk(self):
        r"""Gets the total_disk of this FlinkResourceMetric.

        **参数解释**：总磁盘容量，单位GB。 **取值范围**：0~9223372036854775807。 

        :return: The total_disk of this FlinkResourceMetric.
        :rtype: int
        """
        return self._total_disk

    @total_disk.setter
    def total_disk(self, total_disk):
        r"""Sets the total_disk of this FlinkResourceMetric.

        **参数解释**：总磁盘容量，单位GB。 **取值范围**：0~9223372036854775807。 

        :param total_disk: The total_disk of this FlinkResourceMetric.
        :type total_disk: int
        """
        self._total_disk = total_disk

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
        if not isinstance(other, FlinkResourceMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
