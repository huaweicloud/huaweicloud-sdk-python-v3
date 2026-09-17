# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogTrendNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trend_data': 'list[SlowLogTrendPoint]',
        'interval': 'int'
    }

    attribute_map = {
        'trend_data': 'trend_data',
        'interval': 'interval'
    }

    def __init__(self, trend_data=None, interval=None):
        r"""ShowSlowLogTrendNewResponse

        The model defined in huaweicloud sdk

        :param trend_data: 趋势数量列表
        :type trend_data: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        :param interval: 时间间隔
        :type interval: int
        """
        
        super().__init__()

        self._trend_data = None
        self._interval = None
        self.discriminator = None

        if trend_data is not None:
            self.trend_data = trend_data
        if interval is not None:
            self.interval = interval

    @property
    def trend_data(self):
        r"""Gets the trend_data of this ShowSlowLogTrendNewResponse.

        趋势数量列表

        :return: The trend_data of this ShowSlowLogTrendNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        """
        return self._trend_data

    @trend_data.setter
    def trend_data(self, trend_data):
        r"""Sets the trend_data of this ShowSlowLogTrendNewResponse.

        趋势数量列表

        :param trend_data: The trend_data of this ShowSlowLogTrendNewResponse.
        :type trend_data: list[:class:`huaweicloudsdkdas.v3.SlowLogTrendPoint`]
        """
        self._trend_data = trend_data

    @property
    def interval(self):
        r"""Gets the interval of this ShowSlowLogTrendNewResponse.

        时间间隔

        :return: The interval of this ShowSlowLogTrendNewResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowSlowLogTrendNewResponse.

        时间间隔

        :param interval: The interval of this ShowSlowLogTrendNewResponse.
        :type interval: int
        """
        self._interval = interval

    def to_dict(self):
        import warnings
        warnings.warn("ShowSlowLogTrendNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSlowLogTrendNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
