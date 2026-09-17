# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMissingIndexTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trend_list': 'list[MissingIndexTrendPoint]',
        'user_cost_trend': 'UserTrendPercent',
        'user_impact_trend': 'UserTrendPercent',
        'user_seek_trend': 'UserSeekTrend'
    }

    attribute_map = {
        'trend_list': 'trend_list',
        'user_cost_trend': 'user_cost_trend',
        'user_impact_trend': 'user_impact_trend',
        'user_seek_trend': 'user_seek_trend'
    }

    def __init__(self, trend_list=None, user_cost_trend=None, user_impact_trend=None, user_seek_trend=None):
        r"""ShowMissingIndexTrendResponse

        The model defined in huaweicloud sdk

        :param trend_list: 趋势数量列表
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.MissingIndexTrendPoint`]
        :param user_cost_trend: 
        :type user_cost_trend: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        :param user_impact_trend: 
        :type user_impact_trend: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        :param user_seek_trend: 
        :type user_seek_trend: :class:`huaweicloudsdkdas.v3.UserSeekTrend`
        """
        
        super().__init__()

        self._trend_list = None
        self._user_cost_trend = None
        self._user_impact_trend = None
        self._user_seek_trend = None
        self.discriminator = None

        if trend_list is not None:
            self.trend_list = trend_list
        if user_cost_trend is not None:
            self.user_cost_trend = user_cost_trend
        if user_impact_trend is not None:
            self.user_impact_trend = user_impact_trend
        if user_seek_trend is not None:
            self.user_seek_trend = user_seek_trend

    @property
    def trend_list(self):
        r"""Gets the trend_list of this ShowMissingIndexTrendResponse.

        趋势数量列表

        :return: The trend_list of this ShowMissingIndexTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.MissingIndexTrendPoint`]
        """
        return self._trend_list

    @trend_list.setter
    def trend_list(self, trend_list):
        r"""Sets the trend_list of this ShowMissingIndexTrendResponse.

        趋势数量列表

        :param trend_list: The trend_list of this ShowMissingIndexTrendResponse.
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.MissingIndexTrendPoint`]
        """
        self._trend_list = trend_list

    @property
    def user_cost_trend(self):
        r"""Gets the user_cost_trend of this ShowMissingIndexTrendResponse.

        :return: The user_cost_trend of this ShowMissingIndexTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        """
        return self._user_cost_trend

    @user_cost_trend.setter
    def user_cost_trend(self, user_cost_trend):
        r"""Sets the user_cost_trend of this ShowMissingIndexTrendResponse.

        :param user_cost_trend: The user_cost_trend of this ShowMissingIndexTrendResponse.
        :type user_cost_trend: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        """
        self._user_cost_trend = user_cost_trend

    @property
    def user_impact_trend(self):
        r"""Gets the user_impact_trend of this ShowMissingIndexTrendResponse.

        :return: The user_impact_trend of this ShowMissingIndexTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        """
        return self._user_impact_trend

    @user_impact_trend.setter
    def user_impact_trend(self, user_impact_trend):
        r"""Sets the user_impact_trend of this ShowMissingIndexTrendResponse.

        :param user_impact_trend: The user_impact_trend of this ShowMissingIndexTrendResponse.
        :type user_impact_trend: :class:`huaweicloudsdkdas.v3.UserTrendPercent`
        """
        self._user_impact_trend = user_impact_trend

    @property
    def user_seek_trend(self):
        r"""Gets the user_seek_trend of this ShowMissingIndexTrendResponse.

        :return: The user_seek_trend of this ShowMissingIndexTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.UserSeekTrend`
        """
        return self._user_seek_trend

    @user_seek_trend.setter
    def user_seek_trend(self, user_seek_trend):
        r"""Sets the user_seek_trend of this ShowMissingIndexTrendResponse.

        :param user_seek_trend: The user_seek_trend of this ShowMissingIndexTrendResponse.
        :type user_seek_trend: :class:`huaweicloudsdkdas.v3.UserSeekTrend`
        """
        self._user_seek_trend = user_seek_trend

    def to_dict(self):
        import warnings
        warnings.warn("ShowMissingIndexTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMissingIndexTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
