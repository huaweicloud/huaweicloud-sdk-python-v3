# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerEventData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_serial': 'bool',
        'max_fetch_bytes': 'int',
        'polling_interval': 'int',
        'polling_unit': 'str'
    }

    attribute_map = {
        'is_serial': 'is_serial',
        'max_fetch_bytes': 'max_fetch_bytes',
        'polling_interval': 'polling_interval',
        'polling_unit': 'polling_unit'
    }

    def __init__(self, is_serial=None, max_fetch_bytes=None, polling_interval=None, polling_unit=None):
        """TriggerEventData

        The model defined in huaweicloud sdk

        :param is_serial: 串行处理数据
        :type is_serial: bool
        :param max_fetch_bytes: 最大字节数
        :type max_fetch_bytes: int
        :param polling_interval: 拉取周期
        :type polling_interval: int
        :param polling_unit: 拉取周期单位
        :type polling_unit: str
        """
        
        

        self._is_serial = None
        self._max_fetch_bytes = None
        self._polling_interval = None
        self._polling_unit = None
        self.discriminator = None

        if is_serial is not None:
            self.is_serial = is_serial
        if max_fetch_bytes is not None:
            self.max_fetch_bytes = max_fetch_bytes
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if polling_unit is not None:
            self.polling_unit = polling_unit

    @property
    def is_serial(self):
        """Gets the is_serial of this TriggerEventData.

        串行处理数据

        :return: The is_serial of this TriggerEventData.
        :rtype: bool
        """
        return self._is_serial

    @is_serial.setter
    def is_serial(self, is_serial):
        """Sets the is_serial of this TriggerEventData.

        串行处理数据

        :param is_serial: The is_serial of this TriggerEventData.
        :type is_serial: bool
        """
        self._is_serial = is_serial

    @property
    def max_fetch_bytes(self):
        """Gets the max_fetch_bytes of this TriggerEventData.

        最大字节数

        :return: The max_fetch_bytes of this TriggerEventData.
        :rtype: int
        """
        return self._max_fetch_bytes

    @max_fetch_bytes.setter
    def max_fetch_bytes(self, max_fetch_bytes):
        """Sets the max_fetch_bytes of this TriggerEventData.

        最大字节数

        :param max_fetch_bytes: The max_fetch_bytes of this TriggerEventData.
        :type max_fetch_bytes: int
        """
        self._max_fetch_bytes = max_fetch_bytes

    @property
    def polling_interval(self):
        """Gets the polling_interval of this TriggerEventData.

        拉取周期

        :return: The polling_interval of this TriggerEventData.
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this TriggerEventData.

        拉取周期

        :param polling_interval: The polling_interval of this TriggerEventData.
        :type polling_interval: int
        """
        self._polling_interval = polling_interval

    @property
    def polling_unit(self):
        """Gets the polling_unit of this TriggerEventData.

        拉取周期单位

        :return: The polling_unit of this TriggerEventData.
        :rtype: str
        """
        return self._polling_unit

    @polling_unit.setter
    def polling_unit(self, polling_unit):
        """Sets the polling_unit of this TriggerEventData.

        拉取周期单位

        :param polling_unit: The polling_unit of this TriggerEventData.
        :type polling_unit: str
        """
        self._polling_unit = polling_unit

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
        if not isinstance(other, TriggerEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
