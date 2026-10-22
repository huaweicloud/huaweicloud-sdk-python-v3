# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkExecutorResourceSpec:

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
        'min_executor_numbers': 'int',
        'max_executor_numbers': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'min_executor_numbers': 'min_executor_numbers',
        'max_executor_numbers': 'max_executor_numbers'
    }

    def __init__(self, cpu=None, memory=None, min_executor_numbers=None, max_executor_numbers=None):
        r"""SparkExecutorResourceSpec

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：Spark Executor CPU，单位毫核。 **约束限制**：不涉及。 **取值范围**：1000~48000。 **默认取值**：不涉及。
        :type cpu: int
        :param memory: **参数解释**：Spark Executor内存大小，单位MB，1GB&#x3D;1024MB。 **约束限制**：不涉及。 **取值范围**：1024~393216。 **默认取值**：不涉及。
        :type memory: int
        :param min_executor_numbers: **参数解释**：Spark Executor最小数量。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。
        :type min_executor_numbers: int
        :param max_executor_numbers: **参数解释**：Spark Executor最大数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：不涉及。
        :type max_executor_numbers: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._min_executor_numbers = None
        self._max_executor_numbers = None
        self.discriminator = None

        self.cpu = cpu
        self.memory = memory
        self.min_executor_numbers = min_executor_numbers
        self.max_executor_numbers = max_executor_numbers

    @property
    def cpu(self):
        r"""Gets the cpu of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor CPU，单位毫核。 **约束限制**：不涉及。 **取值范围**：1000~48000。 **默认取值**：不涉及。

        :return: The cpu of this SparkExecutorResourceSpec.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor CPU，单位毫核。 **约束限制**：不涉及。 **取值范围**：1000~48000。 **默认取值**：不涉及。

        :param cpu: The cpu of this SparkExecutorResourceSpec.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor内存大小，单位MB，1GB=1024MB。 **约束限制**：不涉及。 **取值范围**：1024~393216。 **默认取值**：不涉及。

        :return: The memory of this SparkExecutorResourceSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor内存大小，单位MB，1GB=1024MB。 **约束限制**：不涉及。 **取值范围**：1024~393216。 **默认取值**：不涉及。

        :param memory: The memory of this SparkExecutorResourceSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def min_executor_numbers(self):
        r"""Gets the min_executor_numbers of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor最小数量。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :return: The min_executor_numbers of this SparkExecutorResourceSpec.
        :rtype: int
        """
        return self._min_executor_numbers

    @min_executor_numbers.setter
    def min_executor_numbers(self, min_executor_numbers):
        r"""Sets the min_executor_numbers of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor最小数量。 **约束限制**：不涉及。 **取值范围**：1~2147483647。 **默认取值**：不涉及。

        :param min_executor_numbers: The min_executor_numbers of this SparkExecutorResourceSpec.
        :type min_executor_numbers: int
        """
        self._min_executor_numbers = min_executor_numbers

    @property
    def max_executor_numbers(self):
        r"""Gets the max_executor_numbers of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor最大数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：不涉及。

        :return: The max_executor_numbers of this SparkExecutorResourceSpec.
        :rtype: int
        """
        return self._max_executor_numbers

    @max_executor_numbers.setter
    def max_executor_numbers(self, max_executor_numbers):
        r"""Sets the max_executor_numbers of this SparkExecutorResourceSpec.

        **参数解释**：Spark Executor最大数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：不涉及。

        :param max_executor_numbers: The max_executor_numbers of this SparkExecutorResourceSpec.
        :type max_executor_numbers: int
        """
        self._max_executor_numbers = max_executor_numbers

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
        if not isinstance(other, SparkExecutorResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
