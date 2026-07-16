# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayQuota:

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
        r"""CoreGatewayQuota

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 配额类型。 **取值范围：** - &#x60;gateway_count&#x60;: 网关数量配额，当指定gateway id时，不返回该类型的配额详情。 - &#x60;target_count_per_gateway&#x60;: 每个网关的目标服务数量配额，仅当指定了gateway id时，才会返回该类型的配额详情。 
        :type type: str
        :param min: **参数解释：** 最小允许值。 **取值范围：** 取值为 1-10000个。 
        :type min: int
        :param max: **参数解释：** 最大允许值。 **取值范围：** 取值为 1-10000个。 
        :type max: int
        :param quota: **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。 
        :type quota: int
        :param used: **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。 
        :type used: int
        """
        
        

        self._type = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.min = min
        self.max = max
        self.quota = quota
        self.used = used

    @property
    def type(self):
        r"""Gets the type of this CoreGatewayQuota.

        **参数解释：** 配额类型。 **取值范围：** - `gateway_count`: 网关数量配额，当指定gateway id时，不返回该类型的配额详情。 - `target_count_per_gateway`: 每个网关的目标服务数量配额，仅当指定了gateway id时，才会返回该类型的配额详情。 

        :return: The type of this CoreGatewayQuota.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CoreGatewayQuota.

        **参数解释：** 配额类型。 **取值范围：** - `gateway_count`: 网关数量配额，当指定gateway id时，不返回该类型的配额详情。 - `target_count_per_gateway`: 每个网关的目标服务数量配额，仅当指定了gateway id时，才会返回该类型的配额详情。 

        :param type: The type of this CoreGatewayQuota.
        :type type: str
        """
        self._type = type

    @property
    def min(self):
        r"""Gets the min of this CoreGatewayQuota.

        **参数解释：** 最小允许值。 **取值范围：** 取值为 1-10000个。 

        :return: The min of this CoreGatewayQuota.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this CoreGatewayQuota.

        **参数解释：** 最小允许值。 **取值范围：** 取值为 1-10000个。 

        :param min: The min of this CoreGatewayQuota.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this CoreGatewayQuota.

        **参数解释：** 最大允许值。 **取值范围：** 取值为 1-10000个。 

        :return: The max of this CoreGatewayQuota.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this CoreGatewayQuota.

        **参数解释：** 最大允许值。 **取值范围：** 取值为 1-10000个。 

        :param max: The max of this CoreGatewayQuota.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this CoreGatewayQuota.

        **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。 

        :return: The quota of this CoreGatewayQuota.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this CoreGatewayQuota.

        **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。 

        :param quota: The quota of this CoreGatewayQuota.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this CoreGatewayQuota.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。 

        :return: The used of this CoreGatewayQuota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this CoreGatewayQuota.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。 

        :param used: The used of this CoreGatewayQuota.
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
        if not isinstance(other, CoreGatewayQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
