# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowlogForLtsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_log_list': 'list[MysqlSlowLogDetailsItem]',
        'long_query_time': 'str'
    }

    attribute_map = {
        'slow_log_list': 'slow_log_list',
        'long_query_time': 'long_query_time'
    }

    def __init__(self, slow_log_list=None, long_query_time=None):
        """ListSlowlogForLtsResponse

        The model defined in huaweicloud sdk

        :param slow_log_list: 日志数据集合。
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogDetailsItem`]
        :param long_query_time: 当前慢日志阈值时间。
        :type long_query_time: str
        """
        
        super(ListSlowlogForLtsResponse, self).__init__()

        self._slow_log_list = None
        self._long_query_time = None
        self.discriminator = None

        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if long_query_time is not None:
            self.long_query_time = long_query_time

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListSlowlogForLtsResponse.

        日志数据集合。

        :return: The slow_log_list of this ListSlowlogForLtsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogDetailsItem`]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListSlowlogForLtsResponse.

        日志数据集合。

        :param slow_log_list: The slow_log_list of this ListSlowlogForLtsResponse.
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogDetailsItem`]
        """
        self._slow_log_list = slow_log_list

    @property
    def long_query_time(self):
        """Gets the long_query_time of this ListSlowlogForLtsResponse.

        当前慢日志阈值时间。

        :return: The long_query_time of this ListSlowlogForLtsResponse.
        :rtype: str
        """
        return self._long_query_time

    @long_query_time.setter
    def long_query_time(self, long_query_time):
        """Sets the long_query_time of this ListSlowlogForLtsResponse.

        当前慢日志阈值时间。

        :param long_query_time: The long_query_time of this ListSlowlogForLtsResponse.
        :type long_query_time: str
        """
        self._long_query_time = long_query_time

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
        if not isinstance(other, ListSlowlogForLtsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
