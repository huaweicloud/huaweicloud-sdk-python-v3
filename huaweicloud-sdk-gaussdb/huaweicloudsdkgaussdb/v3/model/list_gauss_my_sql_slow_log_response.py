# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGaussMySqlSlowLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'slow_log_list': 'list[MysqlSlowLogList]',
        'long_query_time': 'str',
        'total_record': 'int'
    }

    attribute_map = {
        'slow_log_list': 'slow_log_list',
        'long_query_time': 'long_query_time',
        'total_record': 'total_record'
    }

    def __init__(self, slow_log_list=None, long_query_time=None, total_record=None):
        """ListGaussMySqlSlowLogResponse

        The model defined in huaweicloud sdk

        :param slow_log_list: 错误日志具体信息。
        :type slow_log_list: list[:class:`huaweicloudsdkgaussdb.v3.MysqlSlowLogList`]
        :param long_query_time: 慢日志阈值。
        :type long_query_time: str
        :param total_record: 总记录数。
        :type total_record: int
        """
        
        super(ListGaussMySqlSlowLogResponse, self).__init__()

        self._slow_log_list = None
        self._long_query_time = None
        self._total_record = None
        self.discriminator = None

        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if long_query_time is not None:
            self.long_query_time = long_query_time
        if total_record is not None:
            self.total_record = total_record

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListGaussMySqlSlowLogResponse.

        错误日志具体信息。

        :return: The slow_log_list of this ListGaussMySqlSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlSlowLogList`]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListGaussMySqlSlowLogResponse.

        错误日志具体信息。

        :param slow_log_list: The slow_log_list of this ListGaussMySqlSlowLogResponse.
        :type slow_log_list: list[:class:`huaweicloudsdkgaussdb.v3.MysqlSlowLogList`]
        """
        self._slow_log_list = slow_log_list

    @property
    def long_query_time(self):
        """Gets the long_query_time of this ListGaussMySqlSlowLogResponse.

        慢日志阈值。

        :return: The long_query_time of this ListGaussMySqlSlowLogResponse.
        :rtype: str
        """
        return self._long_query_time

    @long_query_time.setter
    def long_query_time(self, long_query_time):
        """Sets the long_query_time of this ListGaussMySqlSlowLogResponse.

        慢日志阈值。

        :param long_query_time: The long_query_time of this ListGaussMySqlSlowLogResponse.
        :type long_query_time: str
        """
        self._long_query_time = long_query_time

    @property
    def total_record(self):
        """Gets the total_record of this ListGaussMySqlSlowLogResponse.

        总记录数。

        :return: The total_record of this ListGaussMySqlSlowLogResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListGaussMySqlSlowLogResponse.

        总记录数。

        :param total_record: The total_record of this ListGaussMySqlSlowLogResponse.
        :type total_record: int
        """
        self._total_record = total_record

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
        if not isinstance(other, ListGaussMySqlSlowLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
