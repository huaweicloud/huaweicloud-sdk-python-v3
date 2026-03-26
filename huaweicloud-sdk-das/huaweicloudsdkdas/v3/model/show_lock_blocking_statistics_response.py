# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLockBlockingStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_day_count': 'int',
        'last_week_count': 'int',
        'last_two_week_count': 'int',
        'last_month_count': 'int'
    }

    attribute_map = {
        'last_day_count': 'last_day_count',
        'last_week_count': 'last_week_count',
        'last_two_week_count': 'last_two_week_count',
        'last_month_count': 'last_month_count'
    }

    def __init__(self, last_day_count=None, last_week_count=None, last_two_week_count=None, last_month_count=None):
        r"""ShowLockBlockingStatisticsResponse

        The model defined in huaweicloud sdk

        :param last_day_count: 近1天锁阻塞总数
        :type last_day_count: int
        :param last_week_count: 近1周锁阻塞总数
        :type last_week_count: int
        :param last_two_week_count: 近2周锁阻塞总数
        :type last_two_week_count: int
        :param last_month_count: 近1月锁阻塞总数
        :type last_month_count: int
        """
        
        super().__init__()

        self._last_day_count = None
        self._last_week_count = None
        self._last_two_week_count = None
        self._last_month_count = None
        self.discriminator = None

        if last_day_count is not None:
            self.last_day_count = last_day_count
        if last_week_count is not None:
            self.last_week_count = last_week_count
        if last_two_week_count is not None:
            self.last_two_week_count = last_two_week_count
        if last_month_count is not None:
            self.last_month_count = last_month_count

    @property
    def last_day_count(self):
        r"""Gets the last_day_count of this ShowLockBlockingStatisticsResponse.

        近1天锁阻塞总数

        :return: The last_day_count of this ShowLockBlockingStatisticsResponse.
        :rtype: int
        """
        return self._last_day_count

    @last_day_count.setter
    def last_day_count(self, last_day_count):
        r"""Sets the last_day_count of this ShowLockBlockingStatisticsResponse.

        近1天锁阻塞总数

        :param last_day_count: The last_day_count of this ShowLockBlockingStatisticsResponse.
        :type last_day_count: int
        """
        self._last_day_count = last_day_count

    @property
    def last_week_count(self):
        r"""Gets the last_week_count of this ShowLockBlockingStatisticsResponse.

        近1周锁阻塞总数

        :return: The last_week_count of this ShowLockBlockingStatisticsResponse.
        :rtype: int
        """
        return self._last_week_count

    @last_week_count.setter
    def last_week_count(self, last_week_count):
        r"""Sets the last_week_count of this ShowLockBlockingStatisticsResponse.

        近1周锁阻塞总数

        :param last_week_count: The last_week_count of this ShowLockBlockingStatisticsResponse.
        :type last_week_count: int
        """
        self._last_week_count = last_week_count

    @property
    def last_two_week_count(self):
        r"""Gets the last_two_week_count of this ShowLockBlockingStatisticsResponse.

        近2周锁阻塞总数

        :return: The last_two_week_count of this ShowLockBlockingStatisticsResponse.
        :rtype: int
        """
        return self._last_two_week_count

    @last_two_week_count.setter
    def last_two_week_count(self, last_two_week_count):
        r"""Sets the last_two_week_count of this ShowLockBlockingStatisticsResponse.

        近2周锁阻塞总数

        :param last_two_week_count: The last_two_week_count of this ShowLockBlockingStatisticsResponse.
        :type last_two_week_count: int
        """
        self._last_two_week_count = last_two_week_count

    @property
    def last_month_count(self):
        r"""Gets the last_month_count of this ShowLockBlockingStatisticsResponse.

        近1月锁阻塞总数

        :return: The last_month_count of this ShowLockBlockingStatisticsResponse.
        :rtype: int
        """
        return self._last_month_count

    @last_month_count.setter
    def last_month_count(self, last_month_count):
        r"""Sets the last_month_count of this ShowLockBlockingStatisticsResponse.

        近1月锁阻塞总数

        :param last_month_count: The last_month_count of this ShowLockBlockingStatisticsResponse.
        :type last_month_count: int
        """
        self._last_month_count = last_month_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowLockBlockingStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLockBlockingStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
