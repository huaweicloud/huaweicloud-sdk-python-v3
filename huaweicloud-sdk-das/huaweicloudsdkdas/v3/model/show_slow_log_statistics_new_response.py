# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogStatisticsNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistics_list': 'list[SlowLogStatistics]'
    }

    attribute_map = {
        'statistics_list': 'statistics_list'
    }

    def __init__(self, statistics_list=None):
        r"""ShowSlowLogStatisticsNewResponse

        The model defined in huaweicloud sdk

        :param statistics_list: 慢日志统计列表
        :type statistics_list: list[:class:`huaweicloudsdkdas.v3.SlowLogStatistics`]
        """
        
        super().__init__()

        self._statistics_list = None
        self.discriminator = None

        if statistics_list is not None:
            self.statistics_list = statistics_list

    @property
    def statistics_list(self):
        r"""Gets the statistics_list of this ShowSlowLogStatisticsNewResponse.

        慢日志统计列表

        :return: The statistics_list of this ShowSlowLogStatisticsNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogStatistics`]
        """
        return self._statistics_list

    @statistics_list.setter
    def statistics_list(self, statistics_list):
        r"""Sets the statistics_list of this ShowSlowLogStatisticsNewResponse.

        慢日志统计列表

        :param statistics_list: The statistics_list of this ShowSlowLogStatisticsNewResponse.
        :type statistics_list: list[:class:`huaweicloudsdkdas.v3.SlowLogStatistics`]
        """
        self._statistics_list = statistics_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowSlowLogStatisticsNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSlowLogStatisticsNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
