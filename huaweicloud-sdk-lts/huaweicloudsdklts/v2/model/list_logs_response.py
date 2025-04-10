# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'logs': 'list[LogContents]',
        'is_query_complete': 'bool',
        'analysis_logs': 'list[object]'
    }

    attribute_map = {
        'count': 'count',
        'logs': 'logs',
        'is_query_complete': 'isQueryComplete',
        'analysis_logs': 'analysisLogs'
    }

    def __init__(self, count=None, logs=None, is_query_complete=None, analysis_logs=None):
        r"""ListLogsResponse

        The model defined in huaweicloud sdk

        :param count: 日志条数。
        :type count: int
        :param logs: 日志信息。
        :type logs: list[:class:`huaweicloudsdklts.v2.LogContents`]
        :param is_query_complete: 是否查询完成。
        :type is_query_complete: bool
        :param analysis_logs: 分析日志返回响应体
        :type analysis_logs: list[object]
        """
        
        super(ListLogsResponse, self).__init__()

        self._count = None
        self._logs = None
        self._is_query_complete = None
        self._analysis_logs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if logs is not None:
            self.logs = logs
        if is_query_complete is not None:
            self.is_query_complete = is_query_complete
        if analysis_logs is not None:
            self.analysis_logs = analysis_logs

    @property
    def count(self):
        r"""Gets the count of this ListLogsResponse.

        日志条数。

        :return: The count of this ListLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListLogsResponse.

        日志条数。

        :param count: The count of this ListLogsResponse.
        :type count: int
        """
        self._count = count

    @property
    def logs(self):
        r"""Gets the logs of this ListLogsResponse.

        日志信息。

        :return: The logs of this ListLogsResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.LogContents`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ListLogsResponse.

        日志信息。

        :param logs: The logs of this ListLogsResponse.
        :type logs: list[:class:`huaweicloudsdklts.v2.LogContents`]
        """
        self._logs = logs

    @property
    def is_query_complete(self):
        r"""Gets the is_query_complete of this ListLogsResponse.

        是否查询完成。

        :return: The is_query_complete of this ListLogsResponse.
        :rtype: bool
        """
        return self._is_query_complete

    @is_query_complete.setter
    def is_query_complete(self, is_query_complete):
        r"""Sets the is_query_complete of this ListLogsResponse.

        是否查询完成。

        :param is_query_complete: The is_query_complete of this ListLogsResponse.
        :type is_query_complete: bool
        """
        self._is_query_complete = is_query_complete

    @property
    def analysis_logs(self):
        r"""Gets the analysis_logs of this ListLogsResponse.

        分析日志返回响应体

        :return: The analysis_logs of this ListLogsResponse.
        :rtype: list[object]
        """
        return self._analysis_logs

    @analysis_logs.setter
    def analysis_logs(self, analysis_logs):
        r"""Sets the analysis_logs of this ListLogsResponse.

        分析日志返回响应体

        :param analysis_logs: The analysis_logs of this ListLogsResponse.
        :type analysis_logs: list[object]
        """
        self._analysis_logs = analysis_logs

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
        if not isinstance(other, ListLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
