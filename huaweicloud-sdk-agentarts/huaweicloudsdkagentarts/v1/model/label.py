# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Label:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'span_id': 'str',
        'start': 'int',
        'last_update_time': 'int',
        'label_name': 'str',
        'string_value': 'str',
        'float_value': 'str'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'span_id': 'span_id',
        'start': 'start',
        'last_update_time': 'last_update_time',
        'label_name': 'label_name',
        'string_value': 'string_value',
        'float_value': 'float_value'
    }

    def __init__(self, trace_id=None, span_id=None, start=None, last_update_time=None, label_name=None, string_value=None, float_value=None):
        r"""Label

        The model defined in huaweicloud sdk

        :param trace_id: 调用链id
        :type trace_id: str
        :param span_id: span id
        :type span_id: str
        :param start: 起始时间
        :type start: int
        :param last_update_time: 更新时间
        :type last_update_time: int
        :param label_name: 标签名称
        :type label_name: str
        :param string_value: 标签值
        :type string_value: str
        :param float_value: 标签值
        :type float_value: str
        """
        
        

        self._trace_id = None
        self._span_id = None
        self._start = None
        self._last_update_time = None
        self._label_name = None
        self._string_value = None
        self._float_value = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if span_id is not None:
            self.span_id = span_id
        if start is not None:
            self.start = start
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if label_name is not None:
            self.label_name = label_name
        if string_value is not None:
            self.string_value = string_value
        if float_value is not None:
            self.float_value = float_value

    @property
    def trace_id(self):
        r"""Gets the trace_id of this Label.

        调用链id

        :return: The trace_id of this Label.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this Label.

        调用链id

        :param trace_id: The trace_id of this Label.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        r"""Gets the span_id of this Label.

        span id

        :return: The span_id of this Label.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this Label.

        span id

        :param span_id: The span_id of this Label.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def start(self):
        r"""Gets the start of this Label.

        起始时间

        :return: The start of this Label.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this Label.

        起始时间

        :param start: The start of this Label.
        :type start: int
        """
        self._start = start

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this Label.

        更新时间

        :return: The last_update_time of this Label.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this Label.

        更新时间

        :param last_update_time: The last_update_time of this Label.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def label_name(self):
        r"""Gets the label_name of this Label.

        标签名称

        :return: The label_name of this Label.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this Label.

        标签名称

        :param label_name: The label_name of this Label.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def string_value(self):
        r"""Gets the string_value of this Label.

        标签值

        :return: The string_value of this Label.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        r"""Sets the string_value of this Label.

        标签值

        :param string_value: The string_value of this Label.
        :type string_value: str
        """
        self._string_value = string_value

    @property
    def float_value(self):
        r"""Gets the float_value of this Label.

        标签值

        :return: The float_value of this Label.
        :rtype: str
        """
        return self._float_value

    @float_value.setter
    def float_value(self, float_value):
        r"""Sets the float_value of this Label.

        标签值

        :param float_value: The float_value of this Label.
        :type float_value: str
        """
        self._float_value = float_value

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
