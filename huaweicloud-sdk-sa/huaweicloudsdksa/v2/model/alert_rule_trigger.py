# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertRuleTrigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'operator': 'str',
        'expression': 'str',
        'severity': 'str',
        'accumulated_times': 'int'
    }

    attribute_map = {
        'mode': 'mode',
        'operator': 'operator',
        'expression': 'expression',
        'severity': 'severity',
        'accumulated_times': 'accumulated_times'
    }

    def __init__(self, mode=None, operator=None, expression=None, severity=None, accumulated_times=None):
        """AlertRuleTrigger

        The model defined in huaweicloud sdk

        :param mode: mode. COUNT.
        :type mode: str
        :param operator: operator. EQ equal, NE not equal, GT greater than, LT less than.
        :type operator: str
        :param expression: expression
        :type expression: str
        :param severity: severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: str
        :param accumulated_times: accumulated_times
        :type accumulated_times: int
        """
        
        

        self._mode = None
        self._operator = None
        self._expression = None
        self._severity = None
        self._accumulated_times = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if operator is not None:
            self.operator = operator
        self.expression = expression
        if severity is not None:
            self.severity = severity
        if accumulated_times is not None:
            self.accumulated_times = accumulated_times

    @property
    def mode(self):
        """Gets the mode of this AlertRuleTrigger.

        mode. COUNT.

        :return: The mode of this AlertRuleTrigger.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AlertRuleTrigger.

        mode. COUNT.

        :param mode: The mode of this AlertRuleTrigger.
        :type mode: str
        """
        self._mode = mode

    @property
    def operator(self):
        """Gets the operator of this AlertRuleTrigger.

        operator. EQ equal, NE not equal, GT greater than, LT less than.

        :return: The operator of this AlertRuleTrigger.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this AlertRuleTrigger.

        operator. EQ equal, NE not equal, GT greater than, LT less than.

        :param operator: The operator of this AlertRuleTrigger.
        :type operator: str
        """
        self._operator = operator

    @property
    def expression(self):
        """Gets the expression of this AlertRuleTrigger.

        expression

        :return: The expression of this AlertRuleTrigger.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this AlertRuleTrigger.

        expression

        :param expression: The expression of this AlertRuleTrigger.
        :type expression: str
        """
        self._expression = expression

    @property
    def severity(self):
        """Gets the severity of this AlertRuleTrigger.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this AlertRuleTrigger.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertRuleTrigger.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this AlertRuleTrigger.
        :type severity: str
        """
        self._severity = severity

    @property
    def accumulated_times(self):
        """Gets the accumulated_times of this AlertRuleTrigger.

        accumulated_times

        :return: The accumulated_times of this AlertRuleTrigger.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        """Sets the accumulated_times of this AlertRuleTrigger.

        accumulated_times

        :param accumulated_times: The accumulated_times of this AlertRuleTrigger.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

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
        if not isinstance(other, AlertRuleTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
