# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceTopSlowLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_slow_log': 'bool',
        'top_execute_slow_logs': 'list[InsTopSlowLogInfo]',
        'top_avg_query_time_slow_logs': 'list[InsTopSlowLogInfo]',
        'top_max_query_time_slow_logs': 'list[InsTopSlowLogInfo]',
        'rows_examined_exceeding': 'list[InsTopSlowLogInfo]'
    }

    attribute_map = {
        'collect_slow_log': 'collect_slow_log',
        'top_execute_slow_logs': 'top_execute_slow_logs',
        'top_avg_query_time_slow_logs': 'top_avg_query_time_slow_logs',
        'top_max_query_time_slow_logs': 'top_max_query_time_slow_logs',
        'rows_examined_exceeding': 'rows_examined_exceeding'
    }

    def __init__(self, collect_slow_log=None, top_execute_slow_logs=None, top_avg_query_time_slow_logs=None, top_max_query_time_slow_logs=None, rows_examined_exceeding=None):
        r"""ShowInstanceTopSlowLogResponse

        The model defined in huaweicloud sdk

        :param collect_slow_log: 采集慢SQL开关
        :type collect_slow_log: bool
        :param top_execute_slow_logs: 按执行次数排序的慢SQL列表
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        :param top_avg_query_time_slow_logs: 按平均执行时间排序的慢SQL列表
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        :param top_max_query_time_slow_logs: 按最大执行时间排序的慢SQL列表
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        :param rows_examined_exceeding: 按扫描返回比排序的慢SQL列表
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        
        super().__init__()

        self._collect_slow_log = None
        self._top_execute_slow_logs = None
        self._top_avg_query_time_slow_logs = None
        self._top_max_query_time_slow_logs = None
        self._rows_examined_exceeding = None
        self.discriminator = None

        if collect_slow_log is not None:
            self.collect_slow_log = collect_slow_log
        if top_execute_slow_logs is not None:
            self.top_execute_slow_logs = top_execute_slow_logs
        if top_avg_query_time_slow_logs is not None:
            self.top_avg_query_time_slow_logs = top_avg_query_time_slow_logs
        if top_max_query_time_slow_logs is not None:
            self.top_max_query_time_slow_logs = top_max_query_time_slow_logs
        if rows_examined_exceeding is not None:
            self.rows_examined_exceeding = rows_examined_exceeding

    @property
    def collect_slow_log(self):
        r"""Gets the collect_slow_log of this ShowInstanceTopSlowLogResponse.

        采集慢SQL开关

        :return: The collect_slow_log of this ShowInstanceTopSlowLogResponse.
        :rtype: bool
        """
        return self._collect_slow_log

    @collect_slow_log.setter
    def collect_slow_log(self, collect_slow_log):
        r"""Sets the collect_slow_log of this ShowInstanceTopSlowLogResponse.

        采集慢SQL开关

        :param collect_slow_log: The collect_slow_log of this ShowInstanceTopSlowLogResponse.
        :type collect_slow_log: bool
        """
        self._collect_slow_log = collect_slow_log

    @property
    def top_execute_slow_logs(self):
        r"""Gets the top_execute_slow_logs of this ShowInstanceTopSlowLogResponse.

        按执行次数排序的慢SQL列表

        :return: The top_execute_slow_logs of this ShowInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        return self._top_execute_slow_logs

    @top_execute_slow_logs.setter
    def top_execute_slow_logs(self, top_execute_slow_logs):
        r"""Sets the top_execute_slow_logs of this ShowInstanceTopSlowLogResponse.

        按执行次数排序的慢SQL列表

        :param top_execute_slow_logs: The top_execute_slow_logs of this ShowInstanceTopSlowLogResponse.
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        self._top_execute_slow_logs = top_execute_slow_logs

    @property
    def top_avg_query_time_slow_logs(self):
        r"""Gets the top_avg_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.

        按平均执行时间排序的慢SQL列表

        :return: The top_avg_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        return self._top_avg_query_time_slow_logs

    @top_avg_query_time_slow_logs.setter
    def top_avg_query_time_slow_logs(self, top_avg_query_time_slow_logs):
        r"""Sets the top_avg_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.

        按平均执行时间排序的慢SQL列表

        :param top_avg_query_time_slow_logs: The top_avg_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        self._top_avg_query_time_slow_logs = top_avg_query_time_slow_logs

    @property
    def top_max_query_time_slow_logs(self):
        r"""Gets the top_max_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.

        按最大执行时间排序的慢SQL列表

        :return: The top_max_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        return self._top_max_query_time_slow_logs

    @top_max_query_time_slow_logs.setter
    def top_max_query_time_slow_logs(self, top_max_query_time_slow_logs):
        r"""Sets the top_max_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.

        按最大执行时间排序的慢SQL列表

        :param top_max_query_time_slow_logs: The top_max_query_time_slow_logs of this ShowInstanceTopSlowLogResponse.
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        self._top_max_query_time_slow_logs = top_max_query_time_slow_logs

    @property
    def rows_examined_exceeding(self):
        r"""Gets the rows_examined_exceeding of this ShowInstanceTopSlowLogResponse.

        按扫描返回比排序的慢SQL列表

        :return: The rows_examined_exceeding of this ShowInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        return self._rows_examined_exceeding

    @rows_examined_exceeding.setter
    def rows_examined_exceeding(self, rows_examined_exceeding):
        r"""Sets the rows_examined_exceeding of this ShowInstanceTopSlowLogResponse.

        按扫描返回比排序的慢SQL列表

        :param rows_examined_exceeding: The rows_examined_exceeding of this ShowInstanceTopSlowLogResponse.
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.InsTopSlowLogInfo`]
        """
        self._rows_examined_exceeding = rows_examined_exceeding

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceTopSlowLogResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowInstanceTopSlowLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
