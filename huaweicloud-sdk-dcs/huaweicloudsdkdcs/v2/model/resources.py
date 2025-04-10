# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit': 'str',
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'used': 'int',
        'type': 'str'
    }

    attribute_map = {
        'unit': 'unit',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used',
        'type': 'type'
    }

    def __init__(self, unit=None, min=None, max=None, quota=None, used=None, type=None):
        r"""Resources

        The model defined in huaweicloud sdk

        :param unit: 资源的计数单位。 - 当type为instance时，无单位。 - 当type为ram时，单位为GB。 
        :type unit: str
        :param min: - 当type为instance时，表示可申请实例配额的最小值。 - 当type为ram时，表示可申请内存配额的最小值。 
        :type min: int
        :param max: - 当type为instance时，表示可申请实例配额的最大值。 - 当type为ram时，表示可申请内存配额的最大值。 
        :type max: int
        :param quota: 可以创建的实例最大数和总内存的配额限制。
        :type quota: int
        :param used: 已创建的实例个数和已使用的内存配额。
        :type used: int
        :param type: 支持instance、ram两种。 - instance表示实例配额。 - ram表示内存配额。 
        :type type: str
        """
        
        

        self._unit = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self._type = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if type is not None:
            self.type = type

    @property
    def unit(self):
        r"""Gets the unit of this Resources.

        资源的计数单位。 - 当type为instance时，无单位。 - 当type为ram时，单位为GB。 

        :return: The unit of this Resources.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Resources.

        资源的计数单位。 - 当type为instance时，无单位。 - 当type为ram时，单位为GB。 

        :param unit: The unit of this Resources.
        :type unit: str
        """
        self._unit = unit

    @property
    def min(self):
        r"""Gets the min of this Resources.

        - 当type为instance时，表示可申请实例配额的最小值。 - 当type为ram时，表示可申请内存配额的最小值。 

        :return: The min of this Resources.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this Resources.

        - 当type为instance时，表示可申请实例配额的最小值。 - 当type为ram时，表示可申请内存配额的最小值。 

        :param min: The min of this Resources.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this Resources.

        - 当type为instance时，表示可申请实例配额的最大值。 - 当type为ram时，表示可申请内存配额的最大值。 

        :return: The max of this Resources.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this Resources.

        - 当type为instance时，表示可申请实例配额的最大值。 - 当type为ram时，表示可申请内存配额的最大值。 

        :param max: The max of this Resources.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        r"""Gets the quota of this Resources.

        可以创建的实例最大数和总内存的配额限制。

        :return: The quota of this Resources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this Resources.

        可以创建的实例最大数和总内存的配额限制。

        :param quota: The quota of this Resources.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this Resources.

        已创建的实例个数和已使用的内存配额。

        :return: The used of this Resources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this Resources.

        已创建的实例个数和已使用的内存配额。

        :param used: The used of this Resources.
        :type used: int
        """
        self._used = used

    @property
    def type(self):
        r"""Gets the type of this Resources.

        支持instance、ram两种。 - instance表示实例配额。 - ram表示内存配额。 

        :return: The type of this Resources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Resources.

        支持instance、ram两种。 - instance表示实例配额。 - ram表示内存配额。 

        :param type: The type of this Resources.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
