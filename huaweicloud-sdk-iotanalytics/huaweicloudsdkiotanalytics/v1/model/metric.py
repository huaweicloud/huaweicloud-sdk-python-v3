# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metric:

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
        'type': 'str',
        'description': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'unit': 'unit'
    }

    def __init__(self, name=None, type=None, description=None, unit=None):
        """Metric

        The model defined in huaweicloud sdk

        :param name: 指标名称
        :type name: str
        :param type: 指标值类型
        :type type: str
        :param description: 指标描述
        :type description: str
        :param unit: 指标单位
        :type unit: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._unit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if unit is not None:
            self.unit = unit

    @property
    def name(self):
        """Gets the name of this Metric.

        指标名称

        :return: The name of this Metric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metric.

        指标名称

        :param name: The name of this Metric.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Metric.

        指标值类型

        :return: The type of this Metric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Metric.

        指标值类型

        :param type: The type of this Metric.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this Metric.

        指标描述

        :return: The description of this Metric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Metric.

        指标描述

        :param description: The description of this Metric.
        :type description: str
        """
        self._description = description

    @property
    def unit(self):
        """Gets the unit of this Metric.

        指标单位

        :return: The unit of this Metric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Metric.

        指标单位

        :param unit: The unit of this Metric.
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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
