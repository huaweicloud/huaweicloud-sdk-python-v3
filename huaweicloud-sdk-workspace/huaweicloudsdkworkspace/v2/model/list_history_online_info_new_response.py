# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOnlineInfoNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_counts': 'list[str]'
    }

    attribute_map = {
        'time_counts': 'time_counts'
    }

    def __init__(self, time_counts=None):
        r"""ListHistoryOnlineInfoNewResponse

        The model defined in huaweicloud sdk

        :param time_counts: 返回前端历史登录信息。查询的时间和计数之间用冒号分隔。查询的时间，按Day查询或时间段在同一天时，按小时计数，其他场景为按天计数。
        :type time_counts: list[str]
        """
        
        super(ListHistoryOnlineInfoNewResponse, self).__init__()

        self._time_counts = None
        self.discriminator = None

        if time_counts is not None:
            self.time_counts = time_counts

    @property
    def time_counts(self):
        r"""Gets the time_counts of this ListHistoryOnlineInfoNewResponse.

        返回前端历史登录信息。查询的时间和计数之间用冒号分隔。查询的时间，按Day查询或时间段在同一天时，按小时计数，其他场景为按天计数。

        :return: The time_counts of this ListHistoryOnlineInfoNewResponse.
        :rtype: list[str]
        """
        return self._time_counts

    @time_counts.setter
    def time_counts(self, time_counts):
        r"""Sets the time_counts of this ListHistoryOnlineInfoNewResponse.

        返回前端历史登录信息。查询的时间和计数之间用冒号分隔。查询的时间，按Day查询或时间段在同一天时，按小时计数，其他场景为按天计数。

        :param time_counts: The time_counts of this ListHistoryOnlineInfoNewResponse.
        :type time_counts: list[str]
        """
        self._time_counts = time_counts

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
        if not isinstance(other, ListHistoryOnlineInfoNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
