# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterQuotaResource:

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
        'quota': 'int',
        'used': 'int',
        'unit': 'str',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used',
        'unit': 'unit',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, type=None, quota=None, used=None, unit=None, min=None, max=None):
        r"""ClusterQuotaResource

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 资源类型 **约束限制**： 不涉及 **取值范围**： - cluster：Standard/Turbo集群 - autopilot_cluster：Autopilot集群  **默认取值**： 不涉及 
        :type type: str
        :param quota: **参数解释**： 总配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type quota: int
        :param used: **参数解释**： 配额已使用数量 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type used: int
        :param unit: **参数解释**： 单位 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type unit: str
        :param min: **参数解释**： 配额最小值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type min: int
        :param max: **参数解释**： 配额最大值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type max: int
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self._unit = None
        self._min = None
        self._max = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if unit is not None:
            self.unit = unit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def type(self):
        r"""Gets the type of this ClusterQuotaResource.

        **参数解释**： 资源类型 **约束限制**： 不涉及 **取值范围**： - cluster：Standard/Turbo集群 - autopilot_cluster：Autopilot集群  **默认取值**： 不涉及 

        :return: The type of this ClusterQuotaResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterQuotaResource.

        **参数解释**： 资源类型 **约束限制**： 不涉及 **取值范围**： - cluster：Standard/Turbo集群 - autopilot_cluster：Autopilot集群  **默认取值**： 不涉及 

        :param type: The type of this ClusterQuotaResource.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        r"""Gets the quota of this ClusterQuotaResource.

        **参数解释**： 总配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The quota of this ClusterQuotaResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ClusterQuotaResource.

        **参数解释**： 总配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param quota: The quota of this ClusterQuotaResource.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this ClusterQuotaResource.

        **参数解释**： 配额已使用数量 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The used of this ClusterQuotaResource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ClusterQuotaResource.

        **参数解释**： 配额已使用数量 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param used: The used of this ClusterQuotaResource.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this ClusterQuotaResource.

        **参数解释**： 单位 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The unit of this ClusterQuotaResource.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ClusterQuotaResource.

        **参数解释**： 单位 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param unit: The unit of this ClusterQuotaResource.
        :type unit: str
        """
        self._unit = unit

    @property
    def min(self):
        r"""Gets the min of this ClusterQuotaResource.

        **参数解释**： 配额最小值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The min of this ClusterQuotaResource.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this ClusterQuotaResource.

        **参数解释**： 配额最小值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param min: The min of this ClusterQuotaResource.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this ClusterQuotaResource.

        **参数解释**： 配额最大值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The max of this ClusterQuotaResource.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this ClusterQuotaResource.

        **参数解释**： 配额最大值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param max: The max of this ClusterQuotaResource.
        :type max: int
        """
        self._max = max

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
        if not isinstance(other, ClusterQuotaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
