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
        'quota': 'int',
        'used': 'int',
        'type': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'used': 'used',
        'type': 'type',
        'unit': 'unit'
    }

    def __init__(self, quota=None, used=None, type=None, unit=None):
        """Resources

        The model defined in huaweicloud sdk

        :param quota: 函数配额限制。
        :type quota: int
        :param used: 已使用的配额。
        :type used: int
        :param type: “资源类型”
        :type type: str
        :param unit: 资源的计数单位。fgs_func_code_size,单位为MB,其他场景无单位
        :type unit: str
        """
        
        

        self._quota = None
        self._used = None
        self._type = None
        self._unit = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit

    @property
    def quota(self):
        """Gets the quota of this Resources.

        函数配额限制。

        :return: The quota of this Resources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Resources.

        函数配额限制。

        :param quota: The quota of this Resources.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this Resources.

        已使用的配额。

        :return: The used of this Resources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Resources.

        已使用的配额。

        :param used: The used of this Resources.
        :type used: int
        """
        self._used = used

    @property
    def type(self):
        """Gets the type of this Resources.

        “资源类型”

        :return: The type of this Resources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resources.

        “资源类型”

        :param type: The type of this Resources.
        :type type: str
        """
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this Resources.

        资源的计数单位。fgs_func_code_size,单位为MB,其他场景无单位

        :return: The unit of this Resources.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Resources.

        资源的计数单位。fgs_func_code_size,单位为MB,其他场景无单位

        :param unit: The unit of this Resources.
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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
