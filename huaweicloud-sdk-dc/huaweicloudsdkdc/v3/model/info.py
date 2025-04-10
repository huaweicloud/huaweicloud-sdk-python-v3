# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Info:

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
        'unit': 'str'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used',
        'unit': 'unit'
    }

    def __init__(self, type=None, quota=None, used=None, unit=None):
        r"""Info

        The model defined in huaweicloud sdk

        :param type: 配额类型
        :type type: str
        :param quota: 可用的配额数，-1 代表不受限制
        :type quota: int
        :param used: 已使用的配额数量
        :type used: int
        :param unit: 用量单位
        :type unit: str
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self._unit = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if unit is not None:
            self.unit = unit

    @property
    def type(self):
        r"""Gets the type of this Info.

        配额类型

        :return: The type of this Info.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Info.

        配额类型

        :param type: The type of this Info.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        r"""Gets the quota of this Info.

        可用的配额数，-1 代表不受限制

        :return: The quota of this Info.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this Info.

        可用的配额数，-1 代表不受限制

        :param quota: The quota of this Info.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this Info.

        已使用的配额数量

        :return: The used of this Info.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this Info.

        已使用的配额数量

        :param used: The used of this Info.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this Info.

        用量单位

        :return: The unit of this Info.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Info.

        用量单位

        :param unit: The unit of this Info.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, Info):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
