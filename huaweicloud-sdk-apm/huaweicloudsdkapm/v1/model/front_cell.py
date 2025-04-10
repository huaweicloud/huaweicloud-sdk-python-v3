# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrontCell:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_type': 'str',
        'function': 'str',
        'trace': 'bool',
        'span': 'bool',
        'span_field': 'str',
        'precision': 'int',
        'text': 'str',
        'unit': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'data_type': 'data_type',
        'function': 'function',
        'trace': 'trace',
        'span': 'span',
        'span_field': 'span_field',
        'precision': 'precision',
        'text': 'text',
        'unit': 'unit',
        'visible': 'visible'
    }

    def __init__(self, data_type=None, function=None, trace=None, span=None, span_field=None, precision=None, text=None, unit=None, visible=None):
        r"""FrontCell

        The model defined in huaweicloud sdk

        :param data_type: 数据类型。
        :type data_type: str
        :param function: 函数。
        :type function: str
        :param trace: 是否调用链。
        :type trace: bool
        :param span: 是否是span信息，如果是就跳到调用链搜索页面。
        :type span: bool
        :param span_field: span字段。
        :type span_field: str
        :param precision: 小数点位数。
        :type precision: int
        :param text: 文本信息。
        :type text: str
        :param unit: 单位。
        :type unit: str
        :param visible: 是否可见。
        :type visible: bool
        """
        
        

        self._data_type = None
        self._function = None
        self._trace = None
        self._span = None
        self._span_field = None
        self._precision = None
        self._text = None
        self._unit = None
        self._visible = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if function is not None:
            self.function = function
        if trace is not None:
            self.trace = trace
        if span is not None:
            self.span = span
        if span_field is not None:
            self.span_field = span_field
        if precision is not None:
            self.precision = precision
        if text is not None:
            self.text = text
        if unit is not None:
            self.unit = unit
        if visible is not None:
            self.visible = visible

    @property
    def data_type(self):
        r"""Gets the data_type of this FrontCell.

        数据类型。

        :return: The data_type of this FrontCell.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this FrontCell.

        数据类型。

        :param data_type: The data_type of this FrontCell.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def function(self):
        r"""Gets the function of this FrontCell.

        函数。

        :return: The function of this FrontCell.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        r"""Sets the function of this FrontCell.

        函数。

        :param function: The function of this FrontCell.
        :type function: str
        """
        self._function = function

    @property
    def trace(self):
        r"""Gets the trace of this FrontCell.

        是否调用链。

        :return: The trace of this FrontCell.
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        r"""Sets the trace of this FrontCell.

        是否调用链。

        :param trace: The trace of this FrontCell.
        :type trace: bool
        """
        self._trace = trace

    @property
    def span(self):
        r"""Gets the span of this FrontCell.

        是否是span信息，如果是就跳到调用链搜索页面。

        :return: The span of this FrontCell.
        :rtype: bool
        """
        return self._span

    @span.setter
    def span(self, span):
        r"""Sets the span of this FrontCell.

        是否是span信息，如果是就跳到调用链搜索页面。

        :param span: The span of this FrontCell.
        :type span: bool
        """
        self._span = span

    @property
    def span_field(self):
        r"""Gets the span_field of this FrontCell.

        span字段。

        :return: The span_field of this FrontCell.
        :rtype: str
        """
        return self._span_field

    @span_field.setter
    def span_field(self, span_field):
        r"""Sets the span_field of this FrontCell.

        span字段。

        :param span_field: The span_field of this FrontCell.
        :type span_field: str
        """
        self._span_field = span_field

    @property
    def precision(self):
        r"""Gets the precision of this FrontCell.

        小数点位数。

        :return: The precision of this FrontCell.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        r"""Sets the precision of this FrontCell.

        小数点位数。

        :param precision: The precision of this FrontCell.
        :type precision: int
        """
        self._precision = precision

    @property
    def text(self):
        r"""Gets the text of this FrontCell.

        文本信息。

        :return: The text of this FrontCell.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this FrontCell.

        文本信息。

        :param text: The text of this FrontCell.
        :type text: str
        """
        self._text = text

    @property
    def unit(self):
        r"""Gets the unit of this FrontCell.

        单位。

        :return: The unit of this FrontCell.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this FrontCell.

        单位。

        :param unit: The unit of this FrontCell.
        :type unit: str
        """
        self._unit = unit

    @property
    def visible(self):
        r"""Gets the visible of this FrontCell.

        是否可见。

        :return: The visible of this FrontCell.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this FrontCell.

        是否可见。

        :param visible: The visible of this FrontCell.
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
        if not isinstance(other, FrontCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
