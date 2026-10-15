# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, min=None, max=None, quota=None, used=None):
        r"""QuotaResource

        The model defined in huaweicloud sdk

        :param type: **参数解释**：  配额类型，用于标识不同维度的资源配额。  **约束限制**：  不涉及。  **取值范围**：  - instances：实例的数量配额  **默认取值**：  不涉及
        :type type: str
        :param min: **参数解释**：  配额允许的最小值，表示该资源配额的下限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type min: int
        :param max: **参数解释**：  配额允许的最大值，表示该资源配额的上限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type max: int
        :param quota: **参数解释**：  用户当前配额的实际值，即系统为该用户分配的配额数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type quota: int
        :param used: **参数解释**：  用户已使用的配额值，表示当前已占用的资源数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type used: int
        """
        
        

        self._type = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def type(self):
        r"""Gets the type of this QuotaResource.

        **参数解释**：  配额类型，用于标识不同维度的资源配额。  **约束限制**：  不涉及。  **取值范围**：  - instances：实例的数量配额  **默认取值**：  不涉及

        :return: The type of this QuotaResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuotaResource.

        **参数解释**：  配额类型，用于标识不同维度的资源配额。  **约束限制**：  不涉及。  **取值范围**：  - instances：实例的数量配额  **默认取值**：  不涉及

        :param type: The type of this QuotaResource.
        :type type: str
        """
        self._type = type

    @property
    def min(self):
        r"""Gets the min of this QuotaResource.

        **参数解释**：  配额允许的最小值，表示该资源配额的下限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The min of this QuotaResource.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this QuotaResource.

        **参数解释**：  配额允许的最小值，表示该资源配额的下限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param min: The min of this QuotaResource.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this QuotaResource.

        **参数解释**：  配额允许的最大值，表示该资源配额的上限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The max of this QuotaResource.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this QuotaResource.

        **参数解释**：  配额允许的最大值，表示该资源配额的上限。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param max: The max of this QuotaResource.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this QuotaResource.

        **参数解释**：  用户当前配额的实际值，即系统为该用户分配的配额数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The quota of this QuotaResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this QuotaResource.

        **参数解释**：  用户当前配额的实际值，即系统为该用户分配的配额数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param quota: The quota of this QuotaResource.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this QuotaResource.

        **参数解释**：  用户已使用的配额值，表示当前已占用的资源数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The used of this QuotaResource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this QuotaResource.

        **参数解释**：  用户已使用的配额值，表示当前已占用的资源数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param used: The used of this QuotaResource.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, QuotaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
