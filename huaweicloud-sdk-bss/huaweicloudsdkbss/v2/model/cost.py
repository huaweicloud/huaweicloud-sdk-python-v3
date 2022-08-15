# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time_dimension_value': 'str',
        'time_measure_id': 'int',
        'amount': 'str',
        'official_amount': 'str'
    }

    attribute_map = {
        'time_dimension_value': 'time_dimension_value',
        'time_measure_id': 'time_measure_id',
        'amount': 'amount',
        'official_amount': 'official_amount'
    }

    def __init__(self, time_dimension_value=None, time_measure_id=None, amount=None, official_amount=None):
        """Cost

        The model defined in huaweicloud sdk

        :param time_dimension_value: 时间维度值。 如按天维度，该值为yyyy-mm-dd如按月维度，该值为yyyy-mm
        :type time_dimension_value: str
        :param time_measure_id: 时间单位。 1：天2：月
        :type time_measure_id: int
        :param amount: 应付或实付的成本金额或均摊金额，具体取决于请求参数。
        :type amount: str
        :param official_amount: 官网价金额。
        :type official_amount: str
        """
        
        

        self._time_dimension_value = None
        self._time_measure_id = None
        self._amount = None
        self._official_amount = None
        self.discriminator = None

        if time_dimension_value is not None:
            self.time_dimension_value = time_dimension_value
        if time_measure_id is not None:
            self.time_measure_id = time_measure_id
        if amount is not None:
            self.amount = amount
        if official_amount is not None:
            self.official_amount = official_amount

    @property
    def time_dimension_value(self):
        """Gets the time_dimension_value of this Cost.

        时间维度值。 如按天维度，该值为yyyy-mm-dd如按月维度，该值为yyyy-mm

        :return: The time_dimension_value of this Cost.
        :rtype: str
        """
        return self._time_dimension_value

    @time_dimension_value.setter
    def time_dimension_value(self, time_dimension_value):
        """Sets the time_dimension_value of this Cost.

        时间维度值。 如按天维度，该值为yyyy-mm-dd如按月维度，该值为yyyy-mm

        :param time_dimension_value: The time_dimension_value of this Cost.
        :type time_dimension_value: str
        """
        self._time_dimension_value = time_dimension_value

    @property
    def time_measure_id(self):
        """Gets the time_measure_id of this Cost.

        时间单位。 1：天2：月

        :return: The time_measure_id of this Cost.
        :rtype: int
        """
        return self._time_measure_id

    @time_measure_id.setter
    def time_measure_id(self, time_measure_id):
        """Sets the time_measure_id of this Cost.

        时间单位。 1：天2：月

        :param time_measure_id: The time_measure_id of this Cost.
        :type time_measure_id: int
        """
        self._time_measure_id = time_measure_id

    @property
    def amount(self):
        """Gets the amount of this Cost.

        应付或实付的成本金额或均摊金额，具体取决于请求参数。

        :return: The amount of this Cost.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Cost.

        应付或实付的成本金额或均摊金额，具体取决于请求参数。

        :param amount: The amount of this Cost.
        :type amount: str
        """
        self._amount = amount

    @property
    def official_amount(self):
        """Gets the official_amount of this Cost.

        官网价金额。

        :return: The official_amount of this Cost.
        :rtype: str
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this Cost.

        官网价金额。

        :param official_amount: The official_amount of this Cost.
        :type official_amount: str
        """
        self._official_amount = official_amount

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
        if not isinstance(other, Cost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
