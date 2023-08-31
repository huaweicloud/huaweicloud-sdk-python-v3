# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceQuotas:

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
        'quota': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'unit': 'unit',
        'quota': 'quota'
    }

    def __init__(self, type=None, used=None, unit=None, quota=None):
        """ResourceQuotas

        The model defined in huaweicloud sdk

        :param type: 配额类型。  枚举值说明：  alarm，告警规则
        :type type: str
        :param used: 已使用配额数。
        :type used: int
        :param unit: 单位。
        :type unit: str
        :param quota: 配额总数。
        :type quota: int
        """
        
        

        self._type = None
        self._used = None
        self._unit = None
        self._quota = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.unit = unit
        self.quota = quota

    @property
    def type(self):
        """Gets the type of this ResourceQuotas.

        配额类型。  枚举值说明：  alarm，告警规则

        :return: The type of this ResourceQuotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceQuotas.

        配额类型。  枚举值说明：  alarm，告警规则

        :param type: The type of this ResourceQuotas.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this ResourceQuotas.

        已使用配额数。

        :return: The used of this ResourceQuotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ResourceQuotas.

        已使用配额数。

        :param used: The used of this ResourceQuotas.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        """Gets the unit of this ResourceQuotas.

        单位。

        :return: The unit of this ResourceQuotas.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ResourceQuotas.

        单位。

        :param unit: The unit of this ResourceQuotas.
        :type unit: str
        """
        self._unit = unit

    @property
    def quota(self):
        """Gets the quota of this ResourceQuotas.

        配额总数。

        :return: The quota of this ResourceQuotas.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ResourceQuotas.

        配额总数。

        :param quota: The quota of this ResourceQuotas.
        :type quota: int
        """
        self._quota = quota

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
