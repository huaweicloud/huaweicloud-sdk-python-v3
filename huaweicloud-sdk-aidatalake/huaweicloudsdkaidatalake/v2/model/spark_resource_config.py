# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkResourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_resource_spec': 'ResourceSpec',
        'executor_number': 'int',
        'executor_resource_spec': 'ResourceSpec'
    }

    attribute_map = {
        'driver_resource_spec': 'driver_resource_spec',
        'executor_number': 'executor_number',
        'executor_resource_spec': 'executor_resource_spec'
    }

    def __init__(self, driver_resource_spec=None, executor_number=None, executor_resource_spec=None):
        r"""SparkResourceConfig

        The model defined in huaweicloud sdk

        :param driver_resource_spec: 
        :type driver_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        :param executor_number: **参数解释**：Executor数量，用于指定Spark作业的最大Executor个数。如果配置此参数，则表示启用动态资源分配，动态资源分配最小Executor数为1，初始Executor数为1，最大Executor数为配置值。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：不涉及。
        :type executor_number: int
        :param executor_resource_spec: 
        :type executor_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        """
        
        

        self._driver_resource_spec = None
        self._executor_number = None
        self._executor_resource_spec = None
        self.discriminator = None

        if driver_resource_spec is not None:
            self.driver_resource_spec = driver_resource_spec
        if executor_number is not None:
            self.executor_number = executor_number
        if executor_resource_spec is not None:
            self.executor_resource_spec = executor_resource_spec

    @property
    def driver_resource_spec(self):
        r"""Gets the driver_resource_spec of this SparkResourceConfig.

        :return: The driver_resource_spec of this SparkResourceConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        """
        return self._driver_resource_spec

    @driver_resource_spec.setter
    def driver_resource_spec(self, driver_resource_spec):
        r"""Sets the driver_resource_spec of this SparkResourceConfig.

        :param driver_resource_spec: The driver_resource_spec of this SparkResourceConfig.
        :type driver_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        """
        self._driver_resource_spec = driver_resource_spec

    @property
    def executor_number(self):
        r"""Gets the executor_number of this SparkResourceConfig.

        **参数解释**：Executor数量，用于指定Spark作业的最大Executor个数。如果配置此参数，则表示启用动态资源分配，动态资源分配最小Executor数为1，初始Executor数为1，最大Executor数为配置值。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：不涉及。

        :return: The executor_number of this SparkResourceConfig.
        :rtype: int
        """
        return self._executor_number

    @executor_number.setter
    def executor_number(self, executor_number):
        r"""Sets the executor_number of this SparkResourceConfig.

        **参数解释**：Executor数量，用于指定Spark作业的最大Executor个数。如果配置此参数，则表示启用动态资源分配，动态资源分配最小Executor数为1，初始Executor数为1，最大Executor数为配置值。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：不涉及。

        :param executor_number: The executor_number of this SparkResourceConfig.
        :type executor_number: int
        """
        self._executor_number = executor_number

    @property
    def executor_resource_spec(self):
        r"""Gets the executor_resource_spec of this SparkResourceConfig.

        :return: The executor_resource_spec of this SparkResourceConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        """
        return self._executor_resource_spec

    @executor_resource_spec.setter
    def executor_resource_spec(self, executor_resource_spec):
        r"""Sets the executor_resource_spec of this SparkResourceConfig.

        :param executor_resource_spec: The executor_resource_spec of this SparkResourceConfig.
        :type executor_resource_spec: :class:`huaweicloudsdkaidatalake.v2.ResourceSpec`
        """
        self._executor_resource_spec = executor_resource_spec

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
        if not isinstance(other, SparkResourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
