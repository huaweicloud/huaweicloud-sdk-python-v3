# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Log:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'raw_message': 'str'
    }

    attribute_map = {
        'time': 'time',
        'raw_message': 'raw_message'
    }

    def __init__(self, time=None, raw_message=None):
        r"""Log

        The model defined in huaweicloud sdk

        :param time: 时间戳
        :type time: int
        :param raw_message: 日志信息
        :type raw_message: str
        """
        
        

        self._time = None
        self._raw_message = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if raw_message is not None:
            self.raw_message = raw_message

    @property
    def time(self):
        r"""Gets the time of this Log.

        时间戳

        :return: The time of this Log.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Log.

        时间戳

        :param time: The time of this Log.
        :type time: int
        """
        self._time = time

    @property
    def raw_message(self):
        r"""Gets the raw_message of this Log.

        日志信息

        :return: The raw_message of this Log.
        :rtype: str
        """
        return self._raw_message

    @raw_message.setter
    def raw_message(self, raw_message):
        r"""Sets the raw_message of this Log.

        日志信息

        :param raw_message: The raw_message of this Log.
        :type raw_message: str
        """
        self._raw_message = raw_message

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
        if not isinstance(other, Log):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
