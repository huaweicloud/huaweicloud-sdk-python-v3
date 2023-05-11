# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, name=None, value=None, unit=None):
        """Statistic

        The model defined in huaweicloud sdk

        :param name: 资源名称。 - cluster.total：总集群（个）。 - cluster.normal：可用集群（个）。 - instance.total：总节点（个）。 - instance.normal：可用节点（个）。 - storage.total：总容量（GB）。
        :type name: str
        :param value: 资源数量值。
        :type value: float
        :param unit: 资源数量单位。
        :type unit: str
        """
        
        

        self._name = None
        self._value = None
        self._unit = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.unit = unit

    @property
    def name(self):
        """Gets the name of this Statistic.

        资源名称。 - cluster.total：总集群（个）。 - cluster.normal：可用集群（个）。 - instance.total：总节点（个）。 - instance.normal：可用节点（个）。 - storage.total：总容量（GB）。

        :return: The name of this Statistic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Statistic.

        资源名称。 - cluster.total：总集群（个）。 - cluster.normal：可用集群（个）。 - instance.total：总节点（个）。 - instance.normal：可用节点（个）。 - storage.total：总容量（GB）。

        :param name: The name of this Statistic.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this Statistic.

        资源数量值。

        :return: The value of this Statistic.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Statistic.

        资源数量值。

        :param value: The value of this Statistic.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this Statistic.

        资源数量单位。

        :return: The unit of this Statistic.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Statistic.

        资源数量单位。

        :param unit: The unit of this Statistic.
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
        if not isinstance(other, Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
