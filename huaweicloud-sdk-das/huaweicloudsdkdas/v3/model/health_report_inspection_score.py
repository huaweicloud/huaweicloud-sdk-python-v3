# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportInspectionScore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'critical': 'int',
        'medium': 'int',
        'light': 'int',
        'cpu_usage': 'float',
        'mem_usage': 'float',
        'space_usage': 'float',
        'connection_rate': 'float',
        'iops_usage': 'float',
        'thread_running': 'float',
        'slow_sql_total': 'int',
        'lost_points_detail_list': 'list[HealthReportLostPointsDetail]'
    }

    attribute_map = {
        'score': 'score',
        'critical': 'critical',
        'medium': 'medium',
        'light': 'light',
        'cpu_usage': 'cpu_usage',
        'mem_usage': 'mem_usage',
        'space_usage': 'space_usage',
        'connection_rate': 'connection_rate',
        'iops_usage': 'iops_usage',
        'thread_running': 'thread_running',
        'slow_sql_total': 'slow_sql_total',
        'lost_points_detail_list': 'lost_points_detail_list'
    }

    def __init__(self, score=None, critical=None, medium=None, light=None, cpu_usage=None, mem_usage=None, space_usage=None, connection_rate=None, iops_usage=None, thread_running=None, slow_sql_total=None, lost_points_detail_list=None):
        r"""HealthReportInspectionScore

        The model defined in huaweicloud sdk

        :param score: 得分。
        :type score: float
        :param critical: 严重事件。
        :type critical: int
        :param medium: 警告事件。
        :type medium: int
        :param light: 优化事件。
        :type light: int
        :param cpu_usage: CPU使用率。
        :type cpu_usage: float
        :param mem_usage: 内存使用率。
        :type mem_usage: float
        :param space_usage: 空间使用率。
        :type space_usage: float
        :param connection_rate: 连接使用率。
        :type connection_rate: float
        :param iops_usage: IOPS使用率。
        :type iops_usage: float
        :param thread_running: 活跃会话。
        :type thread_running: float
        :param slow_sql_total: 慢SQL数量。
        :type slow_sql_total: int
        :param lost_points_detail_list: 扣分详情。
        :type lost_points_detail_list: list[:class:`huaweicloudsdkdas.v3.HealthReportLostPointsDetail`]
        """
        
        

        self._score = None
        self._critical = None
        self._medium = None
        self._light = None
        self._cpu_usage = None
        self._mem_usage = None
        self._space_usage = None
        self._connection_rate = None
        self._iops_usage = None
        self._thread_running = None
        self._slow_sql_total = None
        self._lost_points_detail_list = None
        self.discriminator = None

        self.score = score
        self.critical = critical
        self.medium = medium
        self.light = light
        self.cpu_usage = cpu_usage
        self.mem_usage = mem_usage
        self.space_usage = space_usage
        self.connection_rate = connection_rate
        self.iops_usage = iops_usage
        self.thread_running = thread_running
        self.slow_sql_total = slow_sql_total
        self.lost_points_detail_list = lost_points_detail_list

    @property
    def score(self):
        r"""Gets the score of this HealthReportInspectionScore.

        得分。

        :return: The score of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this HealthReportInspectionScore.

        得分。

        :param score: The score of this HealthReportInspectionScore.
        :type score: float
        """
        self._score = score

    @property
    def critical(self):
        r"""Gets the critical of this HealthReportInspectionScore.

        严重事件。

        :return: The critical of this HealthReportInspectionScore.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        r"""Sets the critical of this HealthReportInspectionScore.

        严重事件。

        :param critical: The critical of this HealthReportInspectionScore.
        :type critical: int
        """
        self._critical = critical

    @property
    def medium(self):
        r"""Gets the medium of this HealthReportInspectionScore.

        警告事件。

        :return: The medium of this HealthReportInspectionScore.
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        r"""Sets the medium of this HealthReportInspectionScore.

        警告事件。

        :param medium: The medium of this HealthReportInspectionScore.
        :type medium: int
        """
        self._medium = medium

    @property
    def light(self):
        r"""Gets the light of this HealthReportInspectionScore.

        优化事件。

        :return: The light of this HealthReportInspectionScore.
        :rtype: int
        """
        return self._light

    @light.setter
    def light(self, light):
        r"""Sets the light of this HealthReportInspectionScore.

        优化事件。

        :param light: The light of this HealthReportInspectionScore.
        :type light: int
        """
        self._light = light

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this HealthReportInspectionScore.

        CPU使用率。

        :return: The cpu_usage of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this HealthReportInspectionScore.

        CPU使用率。

        :param cpu_usage: The cpu_usage of this HealthReportInspectionScore.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def mem_usage(self):
        r"""Gets the mem_usage of this HealthReportInspectionScore.

        内存使用率。

        :return: The mem_usage of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._mem_usage

    @mem_usage.setter
    def mem_usage(self, mem_usage):
        r"""Sets the mem_usage of this HealthReportInspectionScore.

        内存使用率。

        :param mem_usage: The mem_usage of this HealthReportInspectionScore.
        :type mem_usage: float
        """
        self._mem_usage = mem_usage

    @property
    def space_usage(self):
        r"""Gets the space_usage of this HealthReportInspectionScore.

        空间使用率。

        :return: The space_usage of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._space_usage

    @space_usage.setter
    def space_usage(self, space_usage):
        r"""Sets the space_usage of this HealthReportInspectionScore.

        空间使用率。

        :param space_usage: The space_usage of this HealthReportInspectionScore.
        :type space_usage: float
        """
        self._space_usage = space_usage

    @property
    def connection_rate(self):
        r"""Gets the connection_rate of this HealthReportInspectionScore.

        连接使用率。

        :return: The connection_rate of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._connection_rate

    @connection_rate.setter
    def connection_rate(self, connection_rate):
        r"""Sets the connection_rate of this HealthReportInspectionScore.

        连接使用率。

        :param connection_rate: The connection_rate of this HealthReportInspectionScore.
        :type connection_rate: float
        """
        self._connection_rate = connection_rate

    @property
    def iops_usage(self):
        r"""Gets the iops_usage of this HealthReportInspectionScore.

        IOPS使用率。

        :return: The iops_usage of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._iops_usage

    @iops_usage.setter
    def iops_usage(self, iops_usage):
        r"""Sets the iops_usage of this HealthReportInspectionScore.

        IOPS使用率。

        :param iops_usage: The iops_usage of this HealthReportInspectionScore.
        :type iops_usage: float
        """
        self._iops_usage = iops_usage

    @property
    def thread_running(self):
        r"""Gets the thread_running of this HealthReportInspectionScore.

        活跃会话。

        :return: The thread_running of this HealthReportInspectionScore.
        :rtype: float
        """
        return self._thread_running

    @thread_running.setter
    def thread_running(self, thread_running):
        r"""Sets the thread_running of this HealthReportInspectionScore.

        活跃会话。

        :param thread_running: The thread_running of this HealthReportInspectionScore.
        :type thread_running: float
        """
        self._thread_running = thread_running

    @property
    def slow_sql_total(self):
        r"""Gets the slow_sql_total of this HealthReportInspectionScore.

        慢SQL数量。

        :return: The slow_sql_total of this HealthReportInspectionScore.
        :rtype: int
        """
        return self._slow_sql_total

    @slow_sql_total.setter
    def slow_sql_total(self, slow_sql_total):
        r"""Sets the slow_sql_total of this HealthReportInspectionScore.

        慢SQL数量。

        :param slow_sql_total: The slow_sql_total of this HealthReportInspectionScore.
        :type slow_sql_total: int
        """
        self._slow_sql_total = slow_sql_total

    @property
    def lost_points_detail_list(self):
        r"""Gets the lost_points_detail_list of this HealthReportInspectionScore.

        扣分详情。

        :return: The lost_points_detail_list of this HealthReportInspectionScore.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportLostPointsDetail`]
        """
        return self._lost_points_detail_list

    @lost_points_detail_list.setter
    def lost_points_detail_list(self, lost_points_detail_list):
        r"""Sets the lost_points_detail_list of this HealthReportInspectionScore.

        扣分详情。

        :param lost_points_detail_list: The lost_points_detail_list of this HealthReportInspectionScore.
        :type lost_points_detail_list: list[:class:`huaweicloudsdkdas.v3.HealthReportLostPointsDetail`]
        """
        self._lost_points_detail_list = lost_points_detail_list

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
        if not isinstance(other, HealthReportInspectionScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
