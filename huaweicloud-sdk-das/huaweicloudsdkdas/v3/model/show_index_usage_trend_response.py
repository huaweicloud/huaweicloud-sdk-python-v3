# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIndexUsageTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trend_list': 'list[IndexUsageTrendPoint]',
        'fragmentation_trend': 'IndexUsagePercent',
        'usage_trend': 'IndexUsagePercent'
    }

    attribute_map = {
        'trend_list': 'trend_list',
        'fragmentation_trend': 'fragmentation_trend',
        'usage_trend': 'usage_trend'
    }

    def __init__(self, trend_list=None, fragmentation_trend=None, usage_trend=None):
        r"""ShowIndexUsageTrendResponse

        The model defined in huaweicloud sdk

        :param trend_list: 趋势数量列表
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.IndexUsageTrendPoint`]
        :param fragmentation_trend: 
        :type fragmentation_trend: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        :param usage_trend: 
        :type usage_trend: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        """
        
        super().__init__()

        self._trend_list = None
        self._fragmentation_trend = None
        self._usage_trend = None
        self.discriminator = None

        if trend_list is not None:
            self.trend_list = trend_list
        if fragmentation_trend is not None:
            self.fragmentation_trend = fragmentation_trend
        if usage_trend is not None:
            self.usage_trend = usage_trend

    @property
    def trend_list(self):
        r"""Gets the trend_list of this ShowIndexUsageTrendResponse.

        趋势数量列表

        :return: The trend_list of this ShowIndexUsageTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.IndexUsageTrendPoint`]
        """
        return self._trend_list

    @trend_list.setter
    def trend_list(self, trend_list):
        r"""Sets the trend_list of this ShowIndexUsageTrendResponse.

        趋势数量列表

        :param trend_list: The trend_list of this ShowIndexUsageTrendResponse.
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.IndexUsageTrendPoint`]
        """
        self._trend_list = trend_list

    @property
    def fragmentation_trend(self):
        r"""Gets the fragmentation_trend of this ShowIndexUsageTrendResponse.

        :return: The fragmentation_trend of this ShowIndexUsageTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        """
        return self._fragmentation_trend

    @fragmentation_trend.setter
    def fragmentation_trend(self, fragmentation_trend):
        r"""Sets the fragmentation_trend of this ShowIndexUsageTrendResponse.

        :param fragmentation_trend: The fragmentation_trend of this ShowIndexUsageTrendResponse.
        :type fragmentation_trend: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        """
        self._fragmentation_trend = fragmentation_trend

    @property
    def usage_trend(self):
        r"""Gets the usage_trend of this ShowIndexUsageTrendResponse.

        :return: The usage_trend of this ShowIndexUsageTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        """
        return self._usage_trend

    @usage_trend.setter
    def usage_trend(self, usage_trend):
        r"""Sets the usage_trend of this ShowIndexUsageTrendResponse.

        :param usage_trend: The usage_trend of this ShowIndexUsageTrendResponse.
        :type usage_trend: :class:`huaweicloudsdkdas.v3.IndexUsagePercent`
        """
        self._usage_trend = usage_trend

    def to_dict(self):
        import warnings
        warnings.warn("ShowIndexUsageTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowIndexUsageTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
