# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInput:

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
        'property_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'property_name': 'property_name'
    }

    def __init__(self, name=None, property_name=None):
        r"""MetricInput

        The model defined in huaweicloud sdk

        :param name: 指标计算表达式的入参名称
        :type name: str
        :param property_name: 入参所对应的资产属性名称
        :type property_name: str
        """
        
        

        self._name = None
        self._property_name = None
        self.discriminator = None

        self.name = name
        self.property_name = property_name

    @property
    def name(self):
        r"""Gets the name of this MetricInput.

        指标计算表达式的入参名称

        :return: The name of this MetricInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MetricInput.

        指标计算表达式的入参名称

        :param name: The name of this MetricInput.
        :type name: str
        """
        self._name = name

    @property
    def property_name(self):
        r"""Gets the property_name of this MetricInput.

        入参所对应的资产属性名称

        :return: The property_name of this MetricInput.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        r"""Sets the property_name of this MetricInput.

        入参所对应的资产属性名称

        :param property_name: The property_name of this MetricInput.
        :type property_name: str
        """
        self._property_name = property_name

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
        if not isinstance(other, MetricInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
