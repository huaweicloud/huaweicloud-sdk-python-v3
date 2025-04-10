# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertStatisticsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'block_alert_count': 'int',
        'exception_alert_count': 'int',
        'fail_alert_count': 'int',
        'service_id': 'str',
        'statistics_time': 'int',
        'timeout_alert_count': 'int'
    }

    attribute_map = {
        'block_alert_count': 'block_alert_count',
        'exception_alert_count': 'exception_alert_count',
        'fail_alert_count': 'fail_alert_count',
        'service_id': 'service_id',
        'statistics_time': 'statistics_time',
        'timeout_alert_count': 'timeout_alert_count'
    }

    def __init__(self, block_alert_count=None, exception_alert_count=None, fail_alert_count=None, service_id=None, statistics_time=None, timeout_alert_count=None):
        r"""AlertStatisticsDto

        The model defined in huaweicloud sdk

        :param block_alert_count: 阻塞告警次数
        :type block_alert_count: int
        :param exception_alert_count: 异常告警次数
        :type exception_alert_count: int
        :param fail_alert_count: 失败告警次数
        :type fail_alert_count: int
        :param service_id: 服务id
        :type service_id: str
        :param statistics_time: 统计时间
        :type statistics_time: int
        :param timeout_alert_count: 超时告警次数
        :type timeout_alert_count: int
        """
        
        

        self._block_alert_count = None
        self._exception_alert_count = None
        self._fail_alert_count = None
        self._service_id = None
        self._statistics_time = None
        self._timeout_alert_count = None
        self.discriminator = None

        if block_alert_count is not None:
            self.block_alert_count = block_alert_count
        if exception_alert_count is not None:
            self.exception_alert_count = exception_alert_count
        if fail_alert_count is not None:
            self.fail_alert_count = fail_alert_count
        if service_id is not None:
            self.service_id = service_id
        if statistics_time is not None:
            self.statistics_time = statistics_time
        if timeout_alert_count is not None:
            self.timeout_alert_count = timeout_alert_count

    @property
    def block_alert_count(self):
        r"""Gets the block_alert_count of this AlertStatisticsDto.

        阻塞告警次数

        :return: The block_alert_count of this AlertStatisticsDto.
        :rtype: int
        """
        return self._block_alert_count

    @block_alert_count.setter
    def block_alert_count(self, block_alert_count):
        r"""Sets the block_alert_count of this AlertStatisticsDto.

        阻塞告警次数

        :param block_alert_count: The block_alert_count of this AlertStatisticsDto.
        :type block_alert_count: int
        """
        self._block_alert_count = block_alert_count

    @property
    def exception_alert_count(self):
        r"""Gets the exception_alert_count of this AlertStatisticsDto.

        异常告警次数

        :return: The exception_alert_count of this AlertStatisticsDto.
        :rtype: int
        """
        return self._exception_alert_count

    @exception_alert_count.setter
    def exception_alert_count(self, exception_alert_count):
        r"""Sets the exception_alert_count of this AlertStatisticsDto.

        异常告警次数

        :param exception_alert_count: The exception_alert_count of this AlertStatisticsDto.
        :type exception_alert_count: int
        """
        self._exception_alert_count = exception_alert_count

    @property
    def fail_alert_count(self):
        r"""Gets the fail_alert_count of this AlertStatisticsDto.

        失败告警次数

        :return: The fail_alert_count of this AlertStatisticsDto.
        :rtype: int
        """
        return self._fail_alert_count

    @fail_alert_count.setter
    def fail_alert_count(self, fail_alert_count):
        r"""Sets the fail_alert_count of this AlertStatisticsDto.

        失败告警次数

        :param fail_alert_count: The fail_alert_count of this AlertStatisticsDto.
        :type fail_alert_count: int
        """
        self._fail_alert_count = fail_alert_count

    @property
    def service_id(self):
        r"""Gets the service_id of this AlertStatisticsDto.

        服务id

        :return: The service_id of this AlertStatisticsDto.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this AlertStatisticsDto.

        服务id

        :param service_id: The service_id of this AlertStatisticsDto.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def statistics_time(self):
        r"""Gets the statistics_time of this AlertStatisticsDto.

        统计时间

        :return: The statistics_time of this AlertStatisticsDto.
        :rtype: int
        """
        return self._statistics_time

    @statistics_time.setter
    def statistics_time(self, statistics_time):
        r"""Sets the statistics_time of this AlertStatisticsDto.

        统计时间

        :param statistics_time: The statistics_time of this AlertStatisticsDto.
        :type statistics_time: int
        """
        self._statistics_time = statistics_time

    @property
    def timeout_alert_count(self):
        r"""Gets the timeout_alert_count of this AlertStatisticsDto.

        超时告警次数

        :return: The timeout_alert_count of this AlertStatisticsDto.
        :rtype: int
        """
        return self._timeout_alert_count

    @timeout_alert_count.setter
    def timeout_alert_count(self, timeout_alert_count):
        r"""Sets the timeout_alert_count of this AlertStatisticsDto.

        超时告警次数

        :param timeout_alert_count: The timeout_alert_count of this AlertStatisticsDto.
        :type timeout_alert_count: int
        """
        self._timeout_alert_count = timeout_alert_count

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
        if not isinstance(other, AlertStatisticsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
