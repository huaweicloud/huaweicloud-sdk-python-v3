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
        'quota': 'str',
        'used': 'str',
        'unit': 'str',
        'min': 'str',
        'max': 'str'
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
        r"""QuotaResource

        The model defined in huaweicloud sdk

        :param type: 配额类型，取值范围： - cluster：集群类型配额 - clustergroup：容器舰队类型配额 - rule：规则类型配额 - federation：联邦类型配额
        :type type: str
        :param quota: 配额的总值
        :type quota: str
        :param used: 已使用配额
        :type used: str
        :param unit: 单位
        :type unit: str
        :param min: 最小值
        :type min: str
        :param max: 最大值
        :type max: str
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
        r"""Gets the type of this QuotaResource.

        配额类型，取值范围： - cluster：集群类型配额 - clustergroup：容器舰队类型配额 - rule：规则类型配额 - federation：联邦类型配额

        :return: The type of this QuotaResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuotaResource.

        配额类型，取值范围： - cluster：集群类型配额 - clustergroup：容器舰队类型配额 - rule：规则类型配额 - federation：联邦类型配额

        :param type: The type of this QuotaResource.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        r"""Gets the quota of this QuotaResource.

        配额的总值

        :return: The quota of this QuotaResource.
        :rtype: str
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this QuotaResource.

        配额的总值

        :param quota: The quota of this QuotaResource.
        :type quota: str
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this QuotaResource.

        已使用配额

        :return: The used of this QuotaResource.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this QuotaResource.

        已使用配额

        :param used: The used of this QuotaResource.
        :type used: str
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this QuotaResource.

        单位

        :return: The unit of this QuotaResource.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this QuotaResource.

        单位

        :param unit: The unit of this QuotaResource.
        :type unit: str
        """
        self._unit = unit

    @property
    def min(self):
        r"""Gets the min of this QuotaResource.

        最小值

        :return: The min of this QuotaResource.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this QuotaResource.

        最小值

        :param min: The min of this QuotaResource.
        :type min: str
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this QuotaResource.

        最大值

        :return: The max of this QuotaResource.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this QuotaResource.

        最大值

        :param max: The max of this QuotaResource.
        :type max: str
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
        if not isinstance(other, QuotaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
