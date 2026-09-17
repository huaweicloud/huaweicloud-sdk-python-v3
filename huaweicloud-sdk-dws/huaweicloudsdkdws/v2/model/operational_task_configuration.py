# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationalTaskConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parallel_min': 'int',
        'parallel_max': 'int',
        'small_cu_rows_limit': 'int',
        'small_cu_percentage': 'float'
    }

    attribute_map = {
        'parallel_min': 'parallel_min',
        'parallel_max': 'parallel_max',
        'small_cu_rows_limit': 'small_cu_rows_limit',
        'small_cu_percentage': 'small_cu_percentage'
    }

    def __init__(self, parallel_min=None, parallel_max=None, small_cu_rows_limit=None, small_cu_percentage=None):
        r"""OperationalTaskConfiguration

        The model defined in huaweicloud sdk

        :param parallel_min: **参数解释**： 用户表VacuumFull运维任务最小并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。
        :type parallel_min: int
        :param parallel_max: **参数解释**： 用户表VacuumFull运维任务最大并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。
        :type parallel_max: int
        :param small_cu_rows_limit: **参数解释**： 小CU阈值。 **约束限制**： 不涉及。 **取值范围**： 0~1000。 **默认取值**： 不涉及。
        :type small_cu_rows_limit: int
        :param small_cu_percentage: **参数解释**： 小CU占比。 **约束限制**： 不涉及。 **取值范围**： 0.01~99.99。 **默认取值**： 不涉及。
        :type small_cu_percentage: float
        """
        
        

        self._parallel_min = None
        self._parallel_max = None
        self._small_cu_rows_limit = None
        self._small_cu_percentage = None
        self.discriminator = None

        if parallel_min is not None:
            self.parallel_min = parallel_min
        if parallel_max is not None:
            self.parallel_max = parallel_max
        if small_cu_rows_limit is not None:
            self.small_cu_rows_limit = small_cu_rows_limit
        if small_cu_percentage is not None:
            self.small_cu_percentage = small_cu_percentage

    @property
    def parallel_min(self):
        r"""Gets the parallel_min of this OperationalTaskConfiguration.

        **参数解释**： 用户表VacuumFull运维任务最小并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。

        :return: The parallel_min of this OperationalTaskConfiguration.
        :rtype: int
        """
        return self._parallel_min

    @parallel_min.setter
    def parallel_min(self, parallel_min):
        r"""Sets the parallel_min of this OperationalTaskConfiguration.

        **参数解释**： 用户表VacuumFull运维任务最小并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。

        :param parallel_min: The parallel_min of this OperationalTaskConfiguration.
        :type parallel_min: int
        """
        self._parallel_min = parallel_min

    @property
    def parallel_max(self):
        r"""Gets the parallel_max of this OperationalTaskConfiguration.

        **参数解释**： 用户表VacuumFull运维任务最大并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。

        :return: The parallel_max of this OperationalTaskConfiguration.
        :rtype: int
        """
        return self._parallel_max

    @parallel_max.setter
    def parallel_max(self, parallel_max):
        r"""Sets the parallel_max of this OperationalTaskConfiguration.

        **参数解释**： 用户表VacuumFull运维任务最大并发数。 **约束限制**： 不涉及。 **取值范围**： 1~24 **默认取值**： 不涉及。

        :param parallel_max: The parallel_max of this OperationalTaskConfiguration.
        :type parallel_max: int
        """
        self._parallel_max = parallel_max

    @property
    def small_cu_rows_limit(self):
        r"""Gets the small_cu_rows_limit of this OperationalTaskConfiguration.

        **参数解释**： 小CU阈值。 **约束限制**： 不涉及。 **取值范围**： 0~1000。 **默认取值**： 不涉及。

        :return: The small_cu_rows_limit of this OperationalTaskConfiguration.
        :rtype: int
        """
        return self._small_cu_rows_limit

    @small_cu_rows_limit.setter
    def small_cu_rows_limit(self, small_cu_rows_limit):
        r"""Sets the small_cu_rows_limit of this OperationalTaskConfiguration.

        **参数解释**： 小CU阈值。 **约束限制**： 不涉及。 **取值范围**： 0~1000。 **默认取值**： 不涉及。

        :param small_cu_rows_limit: The small_cu_rows_limit of this OperationalTaskConfiguration.
        :type small_cu_rows_limit: int
        """
        self._small_cu_rows_limit = small_cu_rows_limit

    @property
    def small_cu_percentage(self):
        r"""Gets the small_cu_percentage of this OperationalTaskConfiguration.

        **参数解释**： 小CU占比。 **约束限制**： 不涉及。 **取值范围**： 0.01~99.99。 **默认取值**： 不涉及。

        :return: The small_cu_percentage of this OperationalTaskConfiguration.
        :rtype: float
        """
        return self._small_cu_percentage

    @small_cu_percentage.setter
    def small_cu_percentage(self, small_cu_percentage):
        r"""Sets the small_cu_percentage of this OperationalTaskConfiguration.

        **参数解释**： 小CU占比。 **约束限制**： 不涉及。 **取值范围**： 0.01~99.99。 **默认取值**： 不涉及。

        :param small_cu_percentage: The small_cu_percentage of this OperationalTaskConfiguration.
        :type small_cu_percentage: float
        """
        self._small_cu_percentage = small_cu_percentage

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
        if not isinstance(other, OperationalTaskConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
