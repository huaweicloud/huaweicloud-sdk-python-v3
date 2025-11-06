# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceQuotasResp:

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
        'used': 'int',
        'unit': 'str',
        'quota': 'int',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'unit': 'unit',
        'quota': 'quota',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, type=None, used=None, unit=None, quota=None, min=None, max=None):
        r"""ResourceQuotasResp

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 配额类型。 **取值范围**： 枚举值说明：   - alarm：告警规则 
        :type type: str
        :param used: **参数解释**： 已使用配额数。 **取值范围**： 不涉及。 
        :type used: int
        :param unit: **参数解释**： 单位。 **取值范围**： 长度为[0,32]个字符。 
        :type unit: str
        :param quota: **参数解释**： 配额总数。 **取值范围**： 不涉及。 
        :type quota: int
        :param min: **参数解释**： 最小值。 **取值范围**： 不涉及。 
        :type min: int
        :param max: **参数解释**： 最大值。 **取值范围**： 不涉及。 
        :type max: int
        """
        
        

        self._type = None
        self._used = None
        self._unit = None
        self._quota = None
        self._min = None
        self._max = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.unit = unit
        self.quota = quota
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def type(self):
        r"""Gets the type of this ResourceQuotasResp.

        **参数解释**： 配额类型。 **取值范围**： 枚举值说明：   - alarm：告警规则 

        :return: The type of this ResourceQuotasResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceQuotasResp.

        **参数解释**： 配额类型。 **取值范围**： 枚举值说明：   - alarm：告警规则 

        :param type: The type of this ResourceQuotasResp.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        r"""Gets the used of this ResourceQuotasResp.

        **参数解释**： 已使用配额数。 **取值范围**： 不涉及。 

        :return: The used of this ResourceQuotasResp.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ResourceQuotasResp.

        **参数解释**： 已使用配额数。 **取值范围**： 不涉及。 

        :param used: The used of this ResourceQuotasResp.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this ResourceQuotasResp.

        **参数解释**： 单位。 **取值范围**： 长度为[0,32]个字符。 

        :return: The unit of this ResourceQuotasResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ResourceQuotasResp.

        **参数解释**： 单位。 **取值范围**： 长度为[0,32]个字符。 

        :param unit: The unit of this ResourceQuotasResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def quota(self):
        r"""Gets the quota of this ResourceQuotasResp.

        **参数解释**： 配额总数。 **取值范围**： 不涉及。 

        :return: The quota of this ResourceQuotasResp.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ResourceQuotasResp.

        **参数解释**： 配额总数。 **取值范围**： 不涉及。 

        :param quota: The quota of this ResourceQuotasResp.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        r"""Gets the min of this ResourceQuotasResp.

        **参数解释**： 最小值。 **取值范围**： 不涉及。 

        :return: The min of this ResourceQuotasResp.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this ResourceQuotasResp.

        **参数解释**： 最小值。 **取值范围**： 不涉及。 

        :param min: The min of this ResourceQuotasResp.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this ResourceQuotasResp.

        **参数解释**： 最大值。 **取值范围**： 不涉及。 

        :return: The max of this ResourceQuotasResp.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this ResourceQuotasResp.

        **参数解释**： 最大值。 **取值范围**： 不涉及。 

        :param max: The max of this ResourceQuotasResp.
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
        if not isinstance(other, ResourceQuotasResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
