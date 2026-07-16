# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Capacity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'Value',
        'max_value': 'Value',
        'timestamp': 'str',
        'window': 'str'
    }

    attribute_map = {
        'value': 'value',
        'max_value': 'maxValue',
        'timestamp': 'timestamp',
        'window': 'window'
    }

    def __init__(self, value=None, max_value=None, timestamp=None, window=None):
        r"""Capacity

        The model defined in huaweicloud sdk

        :param value: 
        :type value: :class:`huaweicloudsdkmodelarts.v1.Value`
        :param max_value: 
        :type max_value: :class:`huaweicloudsdkmodelarts.v1.Value`
        :param timestamp: UTC时间，格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。
        :type timestamp: str
        :param window: 统计间隔，1s表示1秒，1m表示1分钟，1h为1小时。
        :type window: str
        """
        
        

        self._value = None
        self._max_value = None
        self._timestamp = None
        self._window = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if max_value is not None:
            self.max_value = max_value
        if timestamp is not None:
            self.timestamp = timestamp
        if window is not None:
            self.window = window

    @property
    def value(self):
        r"""Gets the value of this Capacity.

        :return: The value of this Capacity.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Value`
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Capacity.

        :param value: The value of this Capacity.
        :type value: :class:`huaweicloudsdkmodelarts.v1.Value`
        """
        self._value = value

    @property
    def max_value(self):
        r"""Gets the max_value of this Capacity.

        :return: The max_value of this Capacity.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Value`
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this Capacity.

        :param max_value: The max_value of this Capacity.
        :type max_value: :class:`huaweicloudsdkmodelarts.v1.Value`
        """
        self._max_value = max_value

    @property
    def timestamp(self):
        r"""Gets the timestamp of this Capacity.

        UTC时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :return: The timestamp of this Capacity.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this Capacity.

        UTC时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :param timestamp: The timestamp of this Capacity.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def window(self):
        r"""Gets the window of this Capacity.

        统计间隔，1s表示1秒，1m表示1分钟，1h为1小时。

        :return: The window of this Capacity.
        :rtype: str
        """
        return self._window

    @window.setter
    def window(self, window):
        r"""Sets the window of this Capacity.

        统计间隔，1s表示1秒，1m表示1分钟，1h为1小时。

        :param window: The window of this Capacity.
        :type window: str
        """
        self._window = window

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
        if not isinstance(other, Capacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
