# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueRange2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lower': 'float',
        'upper': 'float'
    }

    attribute_map = {
        'lower': 'lower',
        'upper': 'upper'
    }

    def __init__(self, lower=None, upper=None):
        """ValueRange2

        The model defined in huaweicloud sdk

        :param lower: 值域下限
        :type lower: float
        :param upper: 值域上限
        :type upper: float
        """
        
        

        self._lower = None
        self._upper = None
        self.discriminator = None

        if lower is not None:
            self.lower = lower
        if upper is not None:
            self.upper = upper

    @property
    def lower(self):
        """Gets the lower of this ValueRange2.

        值域下限

        :return: The lower of this ValueRange2.
        :rtype: float
        """
        return self._lower

    @lower.setter
    def lower(self, lower):
        """Sets the lower of this ValueRange2.

        值域下限

        :param lower: The lower of this ValueRange2.
        :type lower: float
        """
        self._lower = lower

    @property
    def upper(self):
        """Gets the upper of this ValueRange2.

        值域上限

        :return: The upper of this ValueRange2.
        :rtype: float
        """
        return self._upper

    @upper.setter
    def upper(self, upper):
        """Sets the upper of this ValueRange2.

        值域上限

        :param upper: The upper of this ValueRange2.
        :type upper: float
        """
        self._upper = upper

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
        if not isinstance(other, ValueRange2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
