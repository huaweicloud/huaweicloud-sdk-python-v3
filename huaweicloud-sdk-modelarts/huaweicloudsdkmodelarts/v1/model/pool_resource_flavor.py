# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolResourceFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'count': 'int',
        'max_count': 'int',
        'extend_params': 'PoolResourceFlavorExtendParams',
        'os': 'Os'
    }

    attribute_map = {
        'flavor': 'flavor',
        'count': 'count',
        'max_count': 'maxCount',
        'extend_params': 'extendParams',
        'os': 'os'
    }

    def __init__(self, flavor=None, count=None, max_count=None, extend_params=None, os=None):
        r"""PoolResourceFlavor

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格，比如：modelarts.vm.gpu.tnt004。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param count: **参数解释**：资源规格的保障资源量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type count: int
        :param max_count: **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type max_count: int
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorExtendParams`
        :param os: 
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        
        

        self._flavor = None
        self._count = None
        self._max_count = None
        self._extend_params = None
        self._os = None
        self.discriminator = None

        self.flavor = flavor
        self.count = count
        if max_count is not None:
            self.max_count = max_count
        if extend_params is not None:
            self.extend_params = extend_params
        if os is not None:
            self.os = os

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolResourceFlavor.

        **参数解释**：资源规格，比如：modelarts.vm.gpu.tnt004。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this PoolResourceFlavor.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolResourceFlavor.

        **参数解释**：资源规格，比如：modelarts.vm.gpu.tnt004。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this PoolResourceFlavor.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def count(self):
        r"""Gets the count of this PoolResourceFlavor.

        **参数解释**：资源规格的保障资源量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The count of this PoolResourceFlavor.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolResourceFlavor.

        **参数解释**：资源规格的保障资源量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param count: The count of this PoolResourceFlavor.
        :type count: int
        """
        self._count = count

    @property
    def max_count(self):
        r"""Gets the max_count of this PoolResourceFlavor.

        **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The max_count of this PoolResourceFlavor.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        r"""Sets the max_count of this PoolResourceFlavor.

        **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param max_count: The max_count of this PoolResourceFlavor.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def extend_params(self):
        r"""Gets the extend_params of this PoolResourceFlavor.

        :return: The extend_params of this PoolResourceFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this PoolResourceFlavor.

        :param extend_params: The extend_params of this PoolResourceFlavor.
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavorExtendParams`
        """
        self._extend_params = extend_params

    @property
    def os(self):
        r"""Gets the os of this PoolResourceFlavor.

        :return: The os of this PoolResourceFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this PoolResourceFlavor.

        :param os: The os of this PoolResourceFlavor.
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        self._os = os

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
        if not isinstance(other, PoolResourceFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
