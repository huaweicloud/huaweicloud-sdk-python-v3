# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogStatisticsForLtsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_log_list': 'list[MysqlSlowLogStatisticsItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'slow_log_list': 'slow_log_list',
        'total_count': 'total_count'
    }

    def __init__(self, slow_log_list=None, total_count=None):
        """ListSlowLogStatisticsForLtsResponse

        The model defined in huaweicloud sdk

        :param slow_log_list: 数据集合。
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogStatisticsItem`]
        :param total_count: 总条数。
        :type total_count: int
        """
        
        super(ListSlowLogStatisticsForLtsResponse, self).__init__()

        self._slow_log_list = None
        self._total_count = None
        self.discriminator = None

        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListSlowLogStatisticsForLtsResponse.

        数据集合。

        :return: The slow_log_list of this ListSlowLogStatisticsForLtsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogStatisticsItem`]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListSlowLogStatisticsForLtsResponse.

        数据集合。

        :param slow_log_list: The slow_log_list of this ListSlowLogStatisticsForLtsResponse.
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.MysqlSlowLogStatisticsItem`]
        """
        self._slow_log_list = slow_log_list

    @property
    def total_count(self):
        """Gets the total_count of this ListSlowLogStatisticsForLtsResponse.

        总条数。

        :return: The total_count of this ListSlowLogStatisticsForLtsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListSlowLogStatisticsForLtsResponse.

        总条数。

        :param total_count: The total_count of this ListSlowLogStatisticsForLtsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListSlowLogStatisticsForLtsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
