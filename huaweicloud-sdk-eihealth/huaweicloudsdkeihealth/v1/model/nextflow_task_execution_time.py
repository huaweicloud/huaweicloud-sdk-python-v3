# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowTaskExecutionTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'submit': 'str',
        'start': 'str',
        'complete': 'str',
        'duration': 'int',
        'realtime': 'int'
    }

    attribute_map = {
        'submit': 'submit',
        'start': 'start',
        'complete': 'complete',
        'duration': 'duration',
        'realtime': 'realtime'
    }

    def __init__(self, submit=None, start=None, complete=None, duration=None, realtime=None):
        """NextflowTaskExecutionTime

        The model defined in huaweicloud sdk

        :param submit: 提交时间
        :type submit: str
        :param start: 开始时间
        :type start: str
        :param complete: 完成时间
        :type complete: str
        :param duration: 总时间
        :type duration: int
        :param realtime: 实际运行时间
        :type realtime: int
        """
        
        

        self._submit = None
        self._start = None
        self._complete = None
        self._duration = None
        self._realtime = None
        self.discriminator = None

        if submit is not None:
            self.submit = submit
        if start is not None:
            self.start = start
        if complete is not None:
            self.complete = complete
        if duration is not None:
            self.duration = duration
        if realtime is not None:
            self.realtime = realtime

    @property
    def submit(self):
        """Gets the submit of this NextflowTaskExecutionTime.

        提交时间

        :return: The submit of this NextflowTaskExecutionTime.
        :rtype: str
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        """Sets the submit of this NextflowTaskExecutionTime.

        提交时间

        :param submit: The submit of this NextflowTaskExecutionTime.
        :type submit: str
        """
        self._submit = submit

    @property
    def start(self):
        """Gets the start of this NextflowTaskExecutionTime.

        开始时间

        :return: The start of this NextflowTaskExecutionTime.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this NextflowTaskExecutionTime.

        开始时间

        :param start: The start of this NextflowTaskExecutionTime.
        :type start: str
        """
        self._start = start

    @property
    def complete(self):
        """Gets the complete of this NextflowTaskExecutionTime.

        完成时间

        :return: The complete of this NextflowTaskExecutionTime.
        :rtype: str
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this NextflowTaskExecutionTime.

        完成时间

        :param complete: The complete of this NextflowTaskExecutionTime.
        :type complete: str
        """
        self._complete = complete

    @property
    def duration(self):
        """Gets the duration of this NextflowTaskExecutionTime.

        总时间

        :return: The duration of this NextflowTaskExecutionTime.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this NextflowTaskExecutionTime.

        总时间

        :param duration: The duration of this NextflowTaskExecutionTime.
        :type duration: int
        """
        self._duration = duration

    @property
    def realtime(self):
        """Gets the realtime of this NextflowTaskExecutionTime.

        实际运行时间

        :return: The realtime of this NextflowTaskExecutionTime.
        :rtype: int
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        """Sets the realtime of this NextflowTaskExecutionTime.

        实际运行时间

        :param realtime: The realtime of this NextflowTaskExecutionTime.
        :type realtime: int
        """
        self._realtime = realtime

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
        if not isinstance(other, NextflowTaskExecutionTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
