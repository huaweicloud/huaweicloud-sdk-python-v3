# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTopSlowLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_execute_slow_logs': 'list[TopInstanceSlowLogTopExecuteSlowLogs]',
        'top_avg_query_time_slow_logs': 'list[TopInstanceSlowLogTopExecuteSlowLogs]',
        'top_max_query_time_slow_logs': 'list[TopInstanceSlowLogTopExecuteSlowLogs]',
        'rows_examined_exceeding': 'list[TopInstanceSlowLogRowsExaminedExceeding]'
    }

    attribute_map = {
        'top_execute_slow_logs': 'top_execute_slow_logs',
        'top_avg_query_time_slow_logs': 'top_avg_query_time_slow_logs',
        'top_max_query_time_slow_logs': 'top_max_query_time_slow_logs',
        'rows_examined_exceeding': 'rows_examined_exceeding'
    }

    def __init__(self, top_execute_slow_logs=None, top_avg_query_time_slow_logs=None, top_max_query_time_slow_logs=None, rows_examined_exceeding=None):
        r"""ListInstanceTopSlowLogResponse

        The model defined in huaweicloud sdk

        :param top_execute_slow_logs: 执行次数列表
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        :param top_avg_query_time_slow_logs: 平均执行时间列表
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        :param top_max_query_time_slow_logs: 最大执行时间列表
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        :param rows_examined_exceeding: 扫描返回比列表
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogRowsExaminedExceeding`]
        """
        
        super(ListInstanceTopSlowLogResponse, self).__init__()

        self._top_execute_slow_logs = None
        self._top_avg_query_time_slow_logs = None
        self._top_max_query_time_slow_logs = None
        self._rows_examined_exceeding = None
        self.discriminator = None

        if top_execute_slow_logs is not None:
            self.top_execute_slow_logs = top_execute_slow_logs
        if top_avg_query_time_slow_logs is not None:
            self.top_avg_query_time_slow_logs = top_avg_query_time_slow_logs
        if top_max_query_time_slow_logs is not None:
            self.top_max_query_time_slow_logs = top_max_query_time_slow_logs
        if rows_examined_exceeding is not None:
            self.rows_examined_exceeding = rows_examined_exceeding

    @property
    def top_execute_slow_logs(self):
        r"""Gets the top_execute_slow_logs of this ListInstanceTopSlowLogResponse.

        执行次数列表

        :return: The top_execute_slow_logs of this ListInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        return self._top_execute_slow_logs

    @top_execute_slow_logs.setter
    def top_execute_slow_logs(self, top_execute_slow_logs):
        r"""Sets the top_execute_slow_logs of this ListInstanceTopSlowLogResponse.

        执行次数列表

        :param top_execute_slow_logs: The top_execute_slow_logs of this ListInstanceTopSlowLogResponse.
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        self._top_execute_slow_logs = top_execute_slow_logs

    @property
    def top_avg_query_time_slow_logs(self):
        r"""Gets the top_avg_query_time_slow_logs of this ListInstanceTopSlowLogResponse.

        平均执行时间列表

        :return: The top_avg_query_time_slow_logs of this ListInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        return self._top_avg_query_time_slow_logs

    @top_avg_query_time_slow_logs.setter
    def top_avg_query_time_slow_logs(self, top_avg_query_time_slow_logs):
        r"""Sets the top_avg_query_time_slow_logs of this ListInstanceTopSlowLogResponse.

        平均执行时间列表

        :param top_avg_query_time_slow_logs: The top_avg_query_time_slow_logs of this ListInstanceTopSlowLogResponse.
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        self._top_avg_query_time_slow_logs = top_avg_query_time_slow_logs

    @property
    def top_max_query_time_slow_logs(self):
        r"""Gets the top_max_query_time_slow_logs of this ListInstanceTopSlowLogResponse.

        最大执行时间列表

        :return: The top_max_query_time_slow_logs of this ListInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        return self._top_max_query_time_slow_logs

    @top_max_query_time_slow_logs.setter
    def top_max_query_time_slow_logs(self, top_max_query_time_slow_logs):
        r"""Sets the top_max_query_time_slow_logs of this ListInstanceTopSlowLogResponse.

        最大执行时间列表

        :param top_max_query_time_slow_logs: The top_max_query_time_slow_logs of this ListInstanceTopSlowLogResponse.
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogTopExecuteSlowLogs`]
        """
        self._top_max_query_time_slow_logs = top_max_query_time_slow_logs

    @property
    def rows_examined_exceeding(self):
        r"""Gets the rows_examined_exceeding of this ListInstanceTopSlowLogResponse.

        扫描返回比列表

        :return: The rows_examined_exceeding of this ListInstanceTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogRowsExaminedExceeding`]
        """
        return self._rows_examined_exceeding

    @rows_examined_exceeding.setter
    def rows_examined_exceeding(self, rows_examined_exceeding):
        r"""Sets the rows_examined_exceeding of this ListInstanceTopSlowLogResponse.

        扫描返回比列表

        :param rows_examined_exceeding: The rows_examined_exceeding of this ListInstanceTopSlowLogResponse.
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.TopInstanceSlowLogRowsExaminedExceeding`]
        """
        self._rows_examined_exceeding = rows_examined_exceeding

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
        if not isinstance(other, ListInstanceTopSlowLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
