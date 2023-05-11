# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSubMetricsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail_num': 'int',
        'retry_success_num': 'int',
        'retry_fail_num': 'int',
        'retry_times': 'int',
        'timestamp': 'int',
        'num': 'int',
        'success_num': 'int',
        'process_time': 'int',
        'invoke_time': 'int'
    }

    attribute_map = {
        'fail_num': 'fail_num',
        'retry_success_num': 'retry_success_num',
        'retry_fail_num': 'retry_fail_num',
        'retry_times': 'retry_times',
        'timestamp': 'timestamp',
        'num': 'num',
        'success_num': 'success_num',
        'process_time': 'process_time',
        'invoke_time': 'invoke_time'
    }

    def __init__(self, fail_num=None, retry_success_num=None, retry_fail_num=None, retry_times=None, timestamp=None, num=None, success_num=None, process_time=None, invoke_time=None):
        """EventSubMetricsItem

        The model defined in huaweicloud sdk

        :param fail_num: 失败数
        :type fail_num: int
        :param retry_success_num: 重试成功数
        :type retry_success_num: int
        :param retry_fail_num: 重试失败数
        :type retry_fail_num: int
        :param retry_times: 重试数
        :type retry_times: int
        :param timestamp: 时间戳
        :type timestamp: int
        :param num: 调用数
        :type num: int
        :param success_num: 调用成功数
        :type success_num: int
        :param process_time: 处理时间
        :type process_time: int
        :param invoke_time: 调用时间
        :type invoke_time: int
        """
        
        

        self._fail_num = None
        self._retry_success_num = None
        self._retry_fail_num = None
        self._retry_times = None
        self._timestamp = None
        self._num = None
        self._success_num = None
        self._process_time = None
        self._invoke_time = None
        self.discriminator = None

        if fail_num is not None:
            self.fail_num = fail_num
        if retry_success_num is not None:
            self.retry_success_num = retry_success_num
        if retry_fail_num is not None:
            self.retry_fail_num = retry_fail_num
        if retry_times is not None:
            self.retry_times = retry_times
        if timestamp is not None:
            self.timestamp = timestamp
        if num is not None:
            self.num = num
        if success_num is not None:
            self.success_num = success_num
        if process_time is not None:
            self.process_time = process_time
        if invoke_time is not None:
            self.invoke_time = invoke_time

    @property
    def fail_num(self):
        """Gets the fail_num of this EventSubMetricsItem.

        失败数

        :return: The fail_num of this EventSubMetricsItem.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        """Sets the fail_num of this EventSubMetricsItem.

        失败数

        :param fail_num: The fail_num of this EventSubMetricsItem.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def retry_success_num(self):
        """Gets the retry_success_num of this EventSubMetricsItem.

        重试成功数

        :return: The retry_success_num of this EventSubMetricsItem.
        :rtype: int
        """
        return self._retry_success_num

    @retry_success_num.setter
    def retry_success_num(self, retry_success_num):
        """Sets the retry_success_num of this EventSubMetricsItem.

        重试成功数

        :param retry_success_num: The retry_success_num of this EventSubMetricsItem.
        :type retry_success_num: int
        """
        self._retry_success_num = retry_success_num

    @property
    def retry_fail_num(self):
        """Gets the retry_fail_num of this EventSubMetricsItem.

        重试失败数

        :return: The retry_fail_num of this EventSubMetricsItem.
        :rtype: int
        """
        return self._retry_fail_num

    @retry_fail_num.setter
    def retry_fail_num(self, retry_fail_num):
        """Sets the retry_fail_num of this EventSubMetricsItem.

        重试失败数

        :param retry_fail_num: The retry_fail_num of this EventSubMetricsItem.
        :type retry_fail_num: int
        """
        self._retry_fail_num = retry_fail_num

    @property
    def retry_times(self):
        """Gets the retry_times of this EventSubMetricsItem.

        重试数

        :return: The retry_times of this EventSubMetricsItem.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        """Sets the retry_times of this EventSubMetricsItem.

        重试数

        :param retry_times: The retry_times of this EventSubMetricsItem.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def timestamp(self):
        """Gets the timestamp of this EventSubMetricsItem.

        时间戳

        :return: The timestamp of this EventSubMetricsItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EventSubMetricsItem.

        时间戳

        :param timestamp: The timestamp of this EventSubMetricsItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def num(self):
        """Gets the num of this EventSubMetricsItem.

        调用数

        :return: The num of this EventSubMetricsItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this EventSubMetricsItem.

        调用数

        :param num: The num of this EventSubMetricsItem.
        :type num: int
        """
        self._num = num

    @property
    def success_num(self):
        """Gets the success_num of this EventSubMetricsItem.

        调用成功数

        :return: The success_num of this EventSubMetricsItem.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this EventSubMetricsItem.

        调用成功数

        :param success_num: The success_num of this EventSubMetricsItem.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def process_time(self):
        """Gets the process_time of this EventSubMetricsItem.

        处理时间

        :return: The process_time of this EventSubMetricsItem.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this EventSubMetricsItem.

        处理时间

        :param process_time: The process_time of this EventSubMetricsItem.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def invoke_time(self):
        """Gets the invoke_time of this EventSubMetricsItem.

        调用时间

        :return: The invoke_time of this EventSubMetricsItem.
        :rtype: int
        """
        return self._invoke_time

    @invoke_time.setter
    def invoke_time(self, invoke_time):
        """Sets the invoke_time of this EventSubMetricsItem.

        调用时间

        :param invoke_time: The invoke_time of this EventSubMetricsItem.
        :type invoke_time: int
        """
        self._invoke_time = invoke_time

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
        if not isinstance(other, EventSubMetricsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
