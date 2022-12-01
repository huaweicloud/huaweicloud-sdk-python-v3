# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeFrame:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'str',
        'stop': 'str'
    }

    attribute_map = {
        'start': 'start',
        'stop': 'stop'
    }

    def __init__(self, start=None, stop=None):
        """TimeFrame

        The model defined in huaweicloud sdk

        :param start: 任务开始时间
        :type start: str
        :param stop: 任务结束时间
        :type stop: str
        """
        
        

        self._start = None
        self._stop = None
        self.discriminator = None

        self.start = start
        self.stop = stop

    @property
    def start(self):
        """Gets the start of this TimeFrame.

        任务开始时间

        :return: The start of this TimeFrame.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TimeFrame.

        任务开始时间

        :param start: The start of this TimeFrame.
        :type start: str
        """
        self._start = start

    @property
    def stop(self):
        """Gets the stop of this TimeFrame.

        任务结束时间

        :return: The stop of this TimeFrame.
        :rtype: str
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this TimeFrame.

        任务结束时间

        :param stop: The stop of this TimeFrame.
        :type stop: str
        """
        self._stop = stop

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
        if not isinstance(other, TimeFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
