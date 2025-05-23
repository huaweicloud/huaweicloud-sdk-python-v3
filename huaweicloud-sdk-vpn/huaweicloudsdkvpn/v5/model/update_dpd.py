# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDpd:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval': 'int',
        'timeout': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'timeout': 'timeout',
        'msg': 'msg'
    }

    def __init__(self, interval=None, timeout=None, msg=None):
        r"""UpdateDpd

        The model defined in huaweicloud sdk

        :param interval: 对等体存活检测空闲时间
        :type interval: int
        :param timeout: 对等体存活检测报文重传间隔
        :type timeout: int
        :param msg: 对等体存活检测报文格式
        :type msg: str
        """
        
        

        self._interval = None
        self._timeout = None
        self._msg = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if msg is not None:
            self.msg = msg

    @property
    def interval(self):
        r"""Gets the interval of this UpdateDpd.

        对等体存活检测空闲时间

        :return: The interval of this UpdateDpd.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this UpdateDpd.

        对等体存活检测空闲时间

        :param interval: The interval of this UpdateDpd.
        :type interval: int
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this UpdateDpd.

        对等体存活检测报文重传间隔

        :return: The timeout of this UpdateDpd.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this UpdateDpd.

        对等体存活检测报文重传间隔

        :param timeout: The timeout of this UpdateDpd.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def msg(self):
        r"""Gets the msg of this UpdateDpd.

        对等体存活检测报文格式

        :return: The msg of this UpdateDpd.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this UpdateDpd.

        对等体存活检测报文格式

        :param msg: The msg of this UpdateDpd.
        :type msg: str
        """
        self._msg = msg

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
        if not isinstance(other, UpdateDpd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
