# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLockBlockingTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval_millis': 'int',
        'trend_list': 'list[ShowLockBlockingTrendRespTrendList]'
    }

    attribute_map = {
        'interval_millis': 'interval_millis',
        'trend_list': 'trend_list'
    }

    def __init__(self, interval_millis=None, trend_list=None):
        r"""ShowLockBlockingTrendResponse

        The model defined in huaweicloud sdk

        :param interval_millis: 时间间隔（ms）
        :type interval_millis: int
        :param trend_list: 锁阻塞趋势列表
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.ShowLockBlockingTrendRespTrendList`]
        """
        
        super().__init__()

        self._interval_millis = None
        self._trend_list = None
        self.discriminator = None

        if interval_millis is not None:
            self.interval_millis = interval_millis
        if trend_list is not None:
            self.trend_list = trend_list

    @property
    def interval_millis(self):
        r"""Gets the interval_millis of this ShowLockBlockingTrendResponse.

        时间间隔（ms）

        :return: The interval_millis of this ShowLockBlockingTrendResponse.
        :rtype: int
        """
        return self._interval_millis

    @interval_millis.setter
    def interval_millis(self, interval_millis):
        r"""Sets the interval_millis of this ShowLockBlockingTrendResponse.

        时间间隔（ms）

        :param interval_millis: The interval_millis of this ShowLockBlockingTrendResponse.
        :type interval_millis: int
        """
        self._interval_millis = interval_millis

    @property
    def trend_list(self):
        r"""Gets the trend_list of this ShowLockBlockingTrendResponse.

        锁阻塞趋势列表

        :return: The trend_list of this ShowLockBlockingTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowLockBlockingTrendRespTrendList`]
        """
        return self._trend_list

    @trend_list.setter
    def trend_list(self, trend_list):
        r"""Sets the trend_list of this ShowLockBlockingTrendResponse.

        锁阻塞趋势列表

        :param trend_list: The trend_list of this ShowLockBlockingTrendResponse.
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.ShowLockBlockingTrendRespTrendList`]
        """
        self._trend_list = trend_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowLockBlockingTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLockBlockingTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
