# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMissingIndexStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_time': 'int',
        'total_missing_index_count': 'int',
        'user_impact_gt80_count': 'int',
        'last_day_accessed_count': 'int',
        'last_week_accessed_count': 'int',
        'last_two_week_accessed_count': 'int',
        'last_month_accessed_count': 'int'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'total_missing_index_count': 'total_missing_index_count',
        'user_impact_gt80_count': 'user_impact_gt80_count',
        'last_day_accessed_count': 'last_day_accessed_count',
        'last_week_accessed_count': 'last_week_accessed_count',
        'last_two_week_accessed_count': 'last_two_week_accessed_count',
        'last_month_accessed_count': 'last_month_accessed_count'
    }

    def __init__(self, collect_time=None, total_missing_index_count=None, user_impact_gt80_count=None, last_day_accessed_count=None, last_week_accessed_count=None, last_two_week_accessed_count=None, last_month_accessed_count=None):
        r"""ShowMissingIndexStatisticsResponse

        The model defined in huaweicloud sdk

        :param collect_time: 采集时间（ms）
        :type collect_time: int
        :param total_missing_index_count: 索引缺失总数
        :type total_missing_index_count: int
        :param user_impact_gt80_count: 性能提示大于80%的数量
        :type user_impact_gt80_count: int
        :param last_day_accessed_count: 近1天用户访问条数
        :type last_day_accessed_count: int
        :param last_week_accessed_count: 近1周用户访问条数
        :type last_week_accessed_count: int
        :param last_two_week_accessed_count: 近2周用户访问条数
        :type last_two_week_accessed_count: int
        :param last_month_accessed_count: 近1月用户访问条数
        :type last_month_accessed_count: int
        """
        
        super().__init__()

        self._collect_time = None
        self._total_missing_index_count = None
        self._user_impact_gt80_count = None
        self._last_day_accessed_count = None
        self._last_week_accessed_count = None
        self._last_two_week_accessed_count = None
        self._last_month_accessed_count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if total_missing_index_count is not None:
            self.total_missing_index_count = total_missing_index_count
        if user_impact_gt80_count is not None:
            self.user_impact_gt80_count = user_impact_gt80_count
        if last_day_accessed_count is not None:
            self.last_day_accessed_count = last_day_accessed_count
        if last_week_accessed_count is not None:
            self.last_week_accessed_count = last_week_accessed_count
        if last_two_week_accessed_count is not None:
            self.last_two_week_accessed_count = last_two_week_accessed_count
        if last_month_accessed_count is not None:
            self.last_month_accessed_count = last_month_accessed_count

    @property
    def collect_time(self):
        r"""Gets the collect_time of this ShowMissingIndexStatisticsResponse.

        采集时间（ms）

        :return: The collect_time of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this ShowMissingIndexStatisticsResponse.

        采集时间（ms）

        :param collect_time: The collect_time of this ShowMissingIndexStatisticsResponse.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def total_missing_index_count(self):
        r"""Gets the total_missing_index_count of this ShowMissingIndexStatisticsResponse.

        索引缺失总数

        :return: The total_missing_index_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._total_missing_index_count

    @total_missing_index_count.setter
    def total_missing_index_count(self, total_missing_index_count):
        r"""Sets the total_missing_index_count of this ShowMissingIndexStatisticsResponse.

        索引缺失总数

        :param total_missing_index_count: The total_missing_index_count of this ShowMissingIndexStatisticsResponse.
        :type total_missing_index_count: int
        """
        self._total_missing_index_count = total_missing_index_count

    @property
    def user_impact_gt80_count(self):
        r"""Gets the user_impact_gt80_count of this ShowMissingIndexStatisticsResponse.

        性能提示大于80%的数量

        :return: The user_impact_gt80_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._user_impact_gt80_count

    @user_impact_gt80_count.setter
    def user_impact_gt80_count(self, user_impact_gt80_count):
        r"""Sets the user_impact_gt80_count of this ShowMissingIndexStatisticsResponse.

        性能提示大于80%的数量

        :param user_impact_gt80_count: The user_impact_gt80_count of this ShowMissingIndexStatisticsResponse.
        :type user_impact_gt80_count: int
        """
        self._user_impact_gt80_count = user_impact_gt80_count

    @property
    def last_day_accessed_count(self):
        r"""Gets the last_day_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1天用户访问条数

        :return: The last_day_accessed_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._last_day_accessed_count

    @last_day_accessed_count.setter
    def last_day_accessed_count(self, last_day_accessed_count):
        r"""Sets the last_day_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1天用户访问条数

        :param last_day_accessed_count: The last_day_accessed_count of this ShowMissingIndexStatisticsResponse.
        :type last_day_accessed_count: int
        """
        self._last_day_accessed_count = last_day_accessed_count

    @property
    def last_week_accessed_count(self):
        r"""Gets the last_week_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1周用户访问条数

        :return: The last_week_accessed_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._last_week_accessed_count

    @last_week_accessed_count.setter
    def last_week_accessed_count(self, last_week_accessed_count):
        r"""Sets the last_week_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1周用户访问条数

        :param last_week_accessed_count: The last_week_accessed_count of this ShowMissingIndexStatisticsResponse.
        :type last_week_accessed_count: int
        """
        self._last_week_accessed_count = last_week_accessed_count

    @property
    def last_two_week_accessed_count(self):
        r"""Gets the last_two_week_accessed_count of this ShowMissingIndexStatisticsResponse.

        近2周用户访问条数

        :return: The last_two_week_accessed_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._last_two_week_accessed_count

    @last_two_week_accessed_count.setter
    def last_two_week_accessed_count(self, last_two_week_accessed_count):
        r"""Sets the last_two_week_accessed_count of this ShowMissingIndexStatisticsResponse.

        近2周用户访问条数

        :param last_two_week_accessed_count: The last_two_week_accessed_count of this ShowMissingIndexStatisticsResponse.
        :type last_two_week_accessed_count: int
        """
        self._last_two_week_accessed_count = last_two_week_accessed_count

    @property
    def last_month_accessed_count(self):
        r"""Gets the last_month_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1月用户访问条数

        :return: The last_month_accessed_count of this ShowMissingIndexStatisticsResponse.
        :rtype: int
        """
        return self._last_month_accessed_count

    @last_month_accessed_count.setter
    def last_month_accessed_count(self, last_month_accessed_count):
        r"""Sets the last_month_accessed_count of this ShowMissingIndexStatisticsResponse.

        近1月用户访问条数

        :param last_month_accessed_count: The last_month_accessed_count of this ShowMissingIndexStatisticsResponse.
        :type last_month_accessed_count: int
        """
        self._last_month_accessed_count = last_month_accessed_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowMissingIndexStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMissingIndexStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
