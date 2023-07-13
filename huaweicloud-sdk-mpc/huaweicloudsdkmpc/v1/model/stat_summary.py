# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'float',
        'date': 'str'
    }

    attribute_map = {
        'value': 'value',
        'date': 'date'
    }

    def __init__(self, value=None, date=None):
        """StatSummary

        The model defined in huaweicloud sdk

        :param value: 精确到小数点后两位。 
        :type value: float
        :param date: 日期,精确到天,格式样例：2018/03/01。 
        :type date: str
        """
        
        

        self._value = None
        self._date = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if date is not None:
            self.date = date

    @property
    def value(self):
        """Gets the value of this StatSummary.

        精确到小数点后两位。 

        :return: The value of this StatSummary.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StatSummary.

        精确到小数点后两位。 

        :param value: The value of this StatSummary.
        :type value: float
        """
        self._value = value

    @property
    def date(self):
        """Gets the date of this StatSummary.

        日期,精确到天,格式样例：2018/03/01。 

        :return: The date of this StatSummary.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this StatSummary.

        日期,精确到天,格式样例：2018/03/01。 

        :param date: The date of this StatSummary.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, StatSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
