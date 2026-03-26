# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkerGroupSpecV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'limits': 'ResourceSpec',
        'requests': 'ResourceSpec'
    }

    attribute_map = {
        'name': 'name',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas',
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, name=None, min_replicas=None, max_replicas=None, limits=None, requests=None):
        r"""WorkerGroupSpecV2

        The model defined in huaweicloud sdk

        :param name: **参数解释**：名称。 **约束限制**：不涉及。 **取值范围**：长度[0,128]字母、数字、下划线(_)、中划线(-)的组合。 **默认取值**：不涉及。
        :type name: str
        :param min_replicas: **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,10000]。 **默认取值**：不涉及。
        :type min_replicas: int
        :param max_replicas: **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,10000]。 **默认取值**：不涉及。
        :type max_replicas: int
        :param limits: 
        :type limits: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        :param requests: 
        :type requests: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        """
        
        

        self._name = None
        self._min_replicas = None
        self._max_replicas = None
        self._limits = None
        self._requests = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def name(self):
        r"""Gets the name of this WorkerGroupSpecV2.

        **参数解释**：名称。 **约束限制**：不涉及。 **取值范围**：长度[0,128]字母、数字、下划线(_)、中划线(-)的组合。 **默认取值**：不涉及。

        :return: The name of this WorkerGroupSpecV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkerGroupSpecV2.

        **参数解释**：名称。 **约束限制**：不涉及。 **取值范围**：长度[0,128]字母、数字、下划线(_)、中划线(-)的组合。 **默认取值**：不涉及。

        :param name: The name of this WorkerGroupSpecV2.
        :type name: str
        """
        self._name = name

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this WorkerGroupSpecV2.

        **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,10000]。 **默认取值**：不涉及。

        :return: The min_replicas of this WorkerGroupSpecV2.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this WorkerGroupSpecV2.

        **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,10000]。 **默认取值**：不涉及。

        :param min_replicas: The min_replicas of this WorkerGroupSpecV2.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this WorkerGroupSpecV2.

        **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,10000]。 **默认取值**：不涉及。

        :return: The max_replicas of this WorkerGroupSpecV2.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this WorkerGroupSpecV2.

        **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,10000]。 **默认取值**：不涉及。

        :param max_replicas: The max_replicas of this WorkerGroupSpecV2.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def limits(self):
        r"""Gets the limits of this WorkerGroupSpecV2.

        :return: The limits of this WorkerGroupSpecV2.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this WorkerGroupSpecV2.

        :param limits: The limits of this WorkerGroupSpecV2.
        :type limits: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        """
        self._limits = limits

    @property
    def requests(self):
        r"""Gets the requests of this WorkerGroupSpecV2.

        :return: The requests of this WorkerGroupSpecV2.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        r"""Sets the requests of this WorkerGroupSpecV2.

        :param requests: The requests of this WorkerGroupSpecV2.
        :type requests: :class:`huaweicloudsdkdataartsfabric.v1.ResourceSpec`
        """
        self._requests = requests

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
        if not isinstance(other, WorkerGroupSpecV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
