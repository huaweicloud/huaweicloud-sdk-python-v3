# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageKpiItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comparison': 'str',
        'value': 'int'
    }

    attribute_map = {
        'comparison': 'comparison',
        'value': 'value'
    }

    def __init__(self, comparison=None, value=None):
        """StageKpiItem

        The model defined in huaweicloud sdk

        :param comparison: 比较符
        :type comparison: str
        :param value: 比较值
        :type value: int
        """
        
        

        self._comparison = None
        self._value = None
        self.discriminator = None

        if comparison is not None:
            self.comparison = comparison
        if value is not None:
            self.value = value

    @property
    def comparison(self):
        """Gets the comparison of this StageKpiItem.

        比较符

        :return: The comparison of this StageKpiItem.
        :rtype: str
        """
        return self._comparison

    @comparison.setter
    def comparison(self, comparison):
        """Sets the comparison of this StageKpiItem.

        比较符

        :param comparison: The comparison of this StageKpiItem.
        :type comparison: str
        """
        self._comparison = comparison

    @property
    def value(self):
        """Gets the value of this StageKpiItem.

        比较值

        :return: The value of this StageKpiItem.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StageKpiItem.

        比较值

        :param value: The value of this StageKpiItem.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, StageKpiItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
