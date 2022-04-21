# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowQueryLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'slow_logs': 'list[SlowLog]',
        'next_marker': 'str'
    }

    attribute_map = {
        'slow_logs': 'slow_logs',
        'next_marker': 'next_marker'
    }

    def __init__(self, slow_logs=None, next_marker=None):
        """ExportSlowQueryLogsResponse

        The model defined in huaweicloud sdk

        :param slow_logs: 慢SQL集合。当集合为空时，说明慢SQL已全部导出。
        :type slow_logs: list[:class:`huaweicloudsdkdas.v3.SlowLog`]
        :param next_marker: 获取下一页所需的标识符。marker仅在3分钟内有效。
        :type next_marker: str
        """
        
        super(ExportSlowQueryLogsResponse, self).__init__()

        self._slow_logs = None
        self._next_marker = None
        self.discriminator = None

        if slow_logs is not None:
            self.slow_logs = slow_logs
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def slow_logs(self):
        """Gets the slow_logs of this ExportSlowQueryLogsResponse.

        慢SQL集合。当集合为空时，说明慢SQL已全部导出。

        :return: The slow_logs of this ExportSlowQueryLogsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLog`]
        """
        return self._slow_logs

    @slow_logs.setter
    def slow_logs(self, slow_logs):
        """Sets the slow_logs of this ExportSlowQueryLogsResponse.

        慢SQL集合。当集合为空时，说明慢SQL已全部导出。

        :param slow_logs: The slow_logs of this ExportSlowQueryLogsResponse.
        :type slow_logs: list[:class:`huaweicloudsdkdas.v3.SlowLog`]
        """
        self._slow_logs = slow_logs

    @property
    def next_marker(self):
        """Gets the next_marker of this ExportSlowQueryLogsResponse.

        获取下一页所需的标识符。marker仅在3分钟内有效。

        :return: The next_marker of this ExportSlowQueryLogsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ExportSlowQueryLogsResponse.

        获取下一页所需的标识符。marker仅在3分钟内有效。

        :param next_marker: The next_marker of this ExportSlowQueryLogsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ExportSlowQueryLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
