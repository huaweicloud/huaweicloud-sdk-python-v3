# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSpaceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'int',
        'used_size': 'int',
        'data_size': 'int',
        'log_size': 'int',
        'avg_daily_growth': 'int',
        'last_result_time': 'int'
    }

    attribute_map = {
        'total_size': 'total_size',
        'used_size': 'used_size',
        'data_size': 'data_size',
        'log_size': 'log_size',
        'avg_daily_growth': 'avg_daily_growth',
        'last_result_time': 'last_result_time'
    }

    def __init__(self, total_size=None, used_size=None, data_size=None, log_size=None, avg_daily_growth=None, last_result_time=None):
        r"""InstanceSpaceInfo

        The model defined in huaweicloud sdk

        :param total_size: 实例总空间，以字节为单位。GaussDB(for MySQL)不会返回总空间
        :type total_size: int
        :param used_size: 已使用空间，以字节为单位
        :type used_size: int
        :param data_size: 数据空间，以字节为单位
        :type data_size: int
        :param log_size: 日志空间，以字节为单位
        :type log_size: int
        :param avg_daily_growth: 近七日的数据平均日增长量，以字节为单位
        :type avg_daily_growth: int
        :param last_result_time: 最后一次分析的结果时间，毫秒单位时间戳
        :type last_result_time: int
        """
        
        

        self._total_size = None
        self._used_size = None
        self._data_size = None
        self._log_size = None
        self._avg_daily_growth = None
        self._last_result_time = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if used_size is not None:
            self.used_size = used_size
        if data_size is not None:
            self.data_size = data_size
        if log_size is not None:
            self.log_size = log_size
        if avg_daily_growth is not None:
            self.avg_daily_growth = avg_daily_growth
        if last_result_time is not None:
            self.last_result_time = last_result_time

    @property
    def total_size(self):
        r"""Gets the total_size of this InstanceSpaceInfo.

        实例总空间，以字节为单位。GaussDB(for MySQL)不会返回总空间

        :return: The total_size of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this InstanceSpaceInfo.

        实例总空间，以字节为单位。GaussDB(for MySQL)不会返回总空间

        :param total_size: The total_size of this InstanceSpaceInfo.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def used_size(self):
        r"""Gets the used_size of this InstanceSpaceInfo.

        已使用空间，以字节为单位

        :return: The used_size of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        r"""Sets the used_size of this InstanceSpaceInfo.

        已使用空间，以字节为单位

        :param used_size: The used_size of this InstanceSpaceInfo.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def data_size(self):
        r"""Gets the data_size of this InstanceSpaceInfo.

        数据空间，以字节为单位

        :return: The data_size of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        r"""Sets the data_size of this InstanceSpaceInfo.

        数据空间，以字节为单位

        :param data_size: The data_size of this InstanceSpaceInfo.
        :type data_size: int
        """
        self._data_size = data_size

    @property
    def log_size(self):
        r"""Gets the log_size of this InstanceSpaceInfo.

        日志空间，以字节为单位

        :return: The log_size of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._log_size

    @log_size.setter
    def log_size(self, log_size):
        r"""Sets the log_size of this InstanceSpaceInfo.

        日志空间，以字节为单位

        :param log_size: The log_size of this InstanceSpaceInfo.
        :type log_size: int
        """
        self._log_size = log_size

    @property
    def avg_daily_growth(self):
        r"""Gets the avg_daily_growth of this InstanceSpaceInfo.

        近七日的数据平均日增长量，以字节为单位

        :return: The avg_daily_growth of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._avg_daily_growth

    @avg_daily_growth.setter
    def avg_daily_growth(self, avg_daily_growth):
        r"""Sets the avg_daily_growth of this InstanceSpaceInfo.

        近七日的数据平均日增长量，以字节为单位

        :param avg_daily_growth: The avg_daily_growth of this InstanceSpaceInfo.
        :type avg_daily_growth: int
        """
        self._avg_daily_growth = avg_daily_growth

    @property
    def last_result_time(self):
        r"""Gets the last_result_time of this InstanceSpaceInfo.

        最后一次分析的结果时间，毫秒单位时间戳

        :return: The last_result_time of this InstanceSpaceInfo.
        :rtype: int
        """
        return self._last_result_time

    @last_result_time.setter
    def last_result_time(self, last_result_time):
        r"""Sets the last_result_time of this InstanceSpaceInfo.

        最后一次分析的结果时间，毫秒单位时间戳

        :param last_result_time: The last_result_time of this InstanceSpaceInfo.
        :type last_result_time: int
        """
        self._last_result_time = last_result_time

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
        if not isinstance(other, InstanceSpaceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
