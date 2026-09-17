# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdsSlowLogTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'points': 'list[SlowLogPoint]',
        'interval': 'int'
    }

    attribute_map = {
        'points': 'points',
        'interval': 'interval'
    }

    def __init__(self, points=None, interval=None):
        r"""ShowDdsSlowLogTrendResponse

        The model defined in huaweicloud sdk

        :param points: 慢日志趋势数量列表
        :type points: list[:class:`huaweicloudsdkdas.v3.SlowLogPoint`]
        :param interval: 时间间隔
        :type interval: int
        """
        
        super().__init__()

        self._points = None
        self._interval = None
        self.discriminator = None

        if points is not None:
            self.points = points
        if interval is not None:
            self.interval = interval

    @property
    def points(self):
        r"""Gets the points of this ShowDdsSlowLogTrendResponse.

        慢日志趋势数量列表

        :return: The points of this ShowDdsSlowLogTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogPoint`]
        """
        return self._points

    @points.setter
    def points(self, points):
        r"""Sets the points of this ShowDdsSlowLogTrendResponse.

        慢日志趋势数量列表

        :param points: The points of this ShowDdsSlowLogTrendResponse.
        :type points: list[:class:`huaweicloudsdkdas.v3.SlowLogPoint`]
        """
        self._points = points

    @property
    def interval(self):
        r"""Gets the interval of this ShowDdsSlowLogTrendResponse.

        时间间隔

        :return: The interval of this ShowDdsSlowLogTrendResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDdsSlowLogTrendResponse.

        时间间隔

        :param interval: The interval of this ShowDdsSlowLogTrendResponse.
        :type interval: int
        """
        self._interval = interval

    def to_dict(self):
        import warnings
        warnings.warn("ShowDdsSlowLogTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDdsSlowLogTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
