# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpaceTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'series': 'list[SpaceTrend]'
    }

    attribute_map = {
        'series': 'series'
    }

    def __init__(self, series=None):
        r"""ShowSpaceTrendResponse

        The model defined in huaweicloud sdk

        :param series: 空间趋势指标列表
        :type series: list[:class:`huaweicloudsdkdas.v3.SpaceTrend`]
        """
        
        super().__init__()

        self._series = None
        self.discriminator = None

        if series is not None:
            self.series = series

    @property
    def series(self):
        r"""Gets the series of this ShowSpaceTrendResponse.

        空间趋势指标列表

        :return: The series of this ShowSpaceTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SpaceTrend`]
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this ShowSpaceTrendResponse.

        空间趋势指标列表

        :param series: The series of this ShowSpaceTrendResponse.
        :type series: list[:class:`huaweicloudsdkdas.v3.SpaceTrend`]
        """
        self._series = series

    def to_dict(self):
        import warnings
        warnings.warn("ShowSpaceTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSpaceTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
