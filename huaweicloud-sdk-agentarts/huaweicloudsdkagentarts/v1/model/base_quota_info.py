# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseQuotaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, min=None, max=None, quota=None, used=None):
        r"""BaseQuotaInfo

        The model defined in huaweicloud sdk

        :param min: **参数解释：** 最小允许值。 **取值范围：** 1~10000 
        :type min: int
        :param max: **参数解释：** 最大允许值。 **取值范围：** 1~10000 
        :type max: int
        :param quota: **参数解释：** 当前配置的配额值。 **取值范围：** 1~10000 
        :type quota: int
        :param used: **参数解释：** 已使用数量（实时计算）。 **取值范围：** 0~10000 
        :type used: int
        """
        
        

        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def min(self):
        r"""Gets the min of this BaseQuotaInfo.

        **参数解释：** 最小允许值。 **取值范围：** 1~10000 

        :return: The min of this BaseQuotaInfo.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this BaseQuotaInfo.

        **参数解释：** 最小允许值。 **取值范围：** 1~10000 

        :param min: The min of this BaseQuotaInfo.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this BaseQuotaInfo.

        **参数解释：** 最大允许值。 **取值范围：** 1~10000 

        :return: The max of this BaseQuotaInfo.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this BaseQuotaInfo.

        **参数解释：** 最大允许值。 **取值范围：** 1~10000 

        :param max: The max of this BaseQuotaInfo.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this BaseQuotaInfo.

        **参数解释：** 当前配置的配额值。 **取值范围：** 1~10000 

        :return: The quota of this BaseQuotaInfo.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this BaseQuotaInfo.

        **参数解释：** 当前配置的配额值。 **取值范围：** 1~10000 

        :param quota: The quota of this BaseQuotaInfo.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this BaseQuotaInfo.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 0~10000 

        :return: The used of this BaseQuotaInfo.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this BaseQuotaInfo.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 0~10000 

        :param used: The used of this BaseQuotaInfo.
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
        if not isinstance(other, BaseQuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
