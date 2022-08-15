# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function': 'str',
        '_as': 'str',
        'default_value': 'str',
        'trace': 'bool',
        'precision': 'int',
        'unit': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'function': 'function',
        '_as': 'as',
        'default_value': 'default_value',
        'trace': 'trace',
        'precision': 'precision',
        'unit': 'unit',
        'visible': 'visible'
    }

    def __init__(self, function=None, _as=None, default_value=None, trace=None, precision=None, unit=None, visible=None):
        """FieldItem

        The model defined in huaweicloud sdk

        :param function: 表达式
        :type function: str
        :param _as: 作为
        :type _as: str
        :param default_value: 默认值
        :type default_value: str
        :param trace: 是否是trace
        :type trace: bool
        :param precision: 百分比
        :type precision: int
        :param unit: 单位
        :type unit: str
        :param visible: 是否可见
        :type visible: bool
        """
        
        

        self._function = None
        self.__as = None
        self._default_value = None
        self._trace = None
        self._precision = None
        self._unit = None
        self._visible = None
        self.discriminator = None

        if function is not None:
            self.function = function
        if _as is not None:
            self._as = _as
        if default_value is not None:
            self.default_value = default_value
        if trace is not None:
            self.trace = trace
        if precision is not None:
            self.precision = precision
        if unit is not None:
            self.unit = unit
        if visible is not None:
            self.visible = visible

    @property
    def function(self):
        """Gets the function of this FieldItem.

        表达式

        :return: The function of this FieldItem.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this FieldItem.

        表达式

        :param function: The function of this FieldItem.
        :type function: str
        """
        self._function = function

    @property
    def _as(self):
        """Gets the _as of this FieldItem.

        作为

        :return: The _as of this FieldItem.
        :rtype: str
        """
        return self.__as

    @_as.setter
    def _as(self, _as):
        """Sets the _as of this FieldItem.

        作为

        :param _as: The _as of this FieldItem.
        :type _as: str
        """
        self.__as = _as

    @property
    def default_value(self):
        """Gets the default_value of this FieldItem.

        默认值

        :return: The default_value of this FieldItem.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldItem.

        默认值

        :param default_value: The default_value of this FieldItem.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def trace(self):
        """Gets the trace of this FieldItem.

        是否是trace

        :return: The trace of this FieldItem.
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this FieldItem.

        是否是trace

        :param trace: The trace of this FieldItem.
        :type trace: bool
        """
        self._trace = trace

    @property
    def precision(self):
        """Gets the precision of this FieldItem.

        百分比

        :return: The precision of this FieldItem.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this FieldItem.

        百分比

        :param precision: The precision of this FieldItem.
        :type precision: int
        """
        self._precision = precision

    @property
    def unit(self):
        """Gets the unit of this FieldItem.

        单位

        :return: The unit of this FieldItem.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this FieldItem.

        单位

        :param unit: The unit of this FieldItem.
        :type unit: str
        """
        self._unit = unit

    @property
    def visible(self):
        """Gets the visible of this FieldItem.

        是否可见

        :return: The visible of this FieldItem.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this FieldItem.

        是否可见

        :param visible: The visible of this FieldItem.
        :type visible: bool
        """
        self._visible = visible

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
        if not isinstance(other, FieldItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
