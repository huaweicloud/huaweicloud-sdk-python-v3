# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShadowValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_name': 'str',
        'property_value': 'str',
        'property_updated_date': 'int'
    }

    attribute_map = {
        'property_name': 'property_name',
        'property_value': 'property_value',
        'property_updated_date': 'property_updated_date'
    }

    def __init__(self, property_name=None, property_value=None, property_updated_date=None):
        r"""ShadowValue

        The model defined in huaweicloud sdk

        :param property_name: 属性名称
        :type property_name: str
        :param property_value: 属性最后一次上报值
        :type property_value: str
        :param property_updated_date: 属性最后一次上报时间，格式timestamp(ms)，使用UTC时区
        :type property_updated_date: int
        """
        
        

        self._property_name = None
        self._property_value = None
        self._property_updated_date = None
        self.discriminator = None

        if property_name is not None:
            self.property_name = property_name
        if property_value is not None:
            self.property_value = property_value
        if property_updated_date is not None:
            self.property_updated_date = property_updated_date

    @property
    def property_name(self):
        r"""Gets the property_name of this ShadowValue.

        属性名称

        :return: The property_name of this ShadowValue.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        r"""Sets the property_name of this ShadowValue.

        属性名称

        :param property_name: The property_name of this ShadowValue.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def property_value(self):
        r"""Gets the property_value of this ShadowValue.

        属性最后一次上报值

        :return: The property_value of this ShadowValue.
        :rtype: str
        """
        return self._property_value

    @property_value.setter
    def property_value(self, property_value):
        r"""Sets the property_value of this ShadowValue.

        属性最后一次上报值

        :param property_value: The property_value of this ShadowValue.
        :type property_value: str
        """
        self._property_value = property_value

    @property
    def property_updated_date(self):
        r"""Gets the property_updated_date of this ShadowValue.

        属性最后一次上报时间，格式timestamp(ms)，使用UTC时区

        :return: The property_updated_date of this ShadowValue.
        :rtype: int
        """
        return self._property_updated_date

    @property_updated_date.setter
    def property_updated_date(self, property_updated_date):
        r"""Sets the property_updated_date of this ShadowValue.

        属性最后一次上报时间，格式timestamp(ms)，使用UTC时区

        :param property_updated_date: The property_updated_date of this ShadowValue.
        :type property_updated_date: int
        """
        self._property_updated_date = property_updated_date

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
        if not isinstance(other, ShadowValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
