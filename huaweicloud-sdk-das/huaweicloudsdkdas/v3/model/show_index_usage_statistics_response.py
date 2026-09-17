# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIndexUsageStatisticsResponse(SdkResponse):

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
        'total_index_usage_count': 'int',
        'index_size_mb': 'float',
        'fragmentation_gl30_count': 'int',
        'key_lookup_lt100_count': 'int'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'total_index_usage_count': 'total_index_usage_count',
        'index_size_mb': 'index_size_mb',
        'fragmentation_gl30_count': 'fragmentation_gl30_count',
        'key_lookup_lt100_count': 'key_lookup_lt100_count'
    }

    def __init__(self, collect_time=None, total_index_usage_count=None, index_size_mb=None, fragmentation_gl30_count=None, key_lookup_lt100_count=None):
        r"""ShowIndexUsageStatisticsResponse

        The model defined in huaweicloud sdk

        :param collect_time: 采集时间(ms)
        :type collect_time: int
        :param total_index_usage_count: 索引使用总数
        :type total_index_usage_count: int
        :param index_size_mb: 索引总空间(MB)
        :type index_size_mb: float
        :param fragmentation_gl30_count: 碎片率大于30%的数量
        :type fragmentation_gl30_count: int
        :param key_lookup_lt100_count: 查找次数小于100的数量
        :type key_lookup_lt100_count: int
        """
        
        super().__init__()

        self._collect_time = None
        self._total_index_usage_count = None
        self._index_size_mb = None
        self._fragmentation_gl30_count = None
        self._key_lookup_lt100_count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if total_index_usage_count is not None:
            self.total_index_usage_count = total_index_usage_count
        if index_size_mb is not None:
            self.index_size_mb = index_size_mb
        if fragmentation_gl30_count is not None:
            self.fragmentation_gl30_count = fragmentation_gl30_count
        if key_lookup_lt100_count is not None:
            self.key_lookup_lt100_count = key_lookup_lt100_count

    @property
    def collect_time(self):
        r"""Gets the collect_time of this ShowIndexUsageStatisticsResponse.

        采集时间(ms)

        :return: The collect_time of this ShowIndexUsageStatisticsResponse.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this ShowIndexUsageStatisticsResponse.

        采集时间(ms)

        :param collect_time: The collect_time of this ShowIndexUsageStatisticsResponse.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def total_index_usage_count(self):
        r"""Gets the total_index_usage_count of this ShowIndexUsageStatisticsResponse.

        索引使用总数

        :return: The total_index_usage_count of this ShowIndexUsageStatisticsResponse.
        :rtype: int
        """
        return self._total_index_usage_count

    @total_index_usage_count.setter
    def total_index_usage_count(self, total_index_usage_count):
        r"""Sets the total_index_usage_count of this ShowIndexUsageStatisticsResponse.

        索引使用总数

        :param total_index_usage_count: The total_index_usage_count of this ShowIndexUsageStatisticsResponse.
        :type total_index_usage_count: int
        """
        self._total_index_usage_count = total_index_usage_count

    @property
    def index_size_mb(self):
        r"""Gets the index_size_mb of this ShowIndexUsageStatisticsResponse.

        索引总空间(MB)

        :return: The index_size_mb of this ShowIndexUsageStatisticsResponse.
        :rtype: float
        """
        return self._index_size_mb

    @index_size_mb.setter
    def index_size_mb(self, index_size_mb):
        r"""Sets the index_size_mb of this ShowIndexUsageStatisticsResponse.

        索引总空间(MB)

        :param index_size_mb: The index_size_mb of this ShowIndexUsageStatisticsResponse.
        :type index_size_mb: float
        """
        self._index_size_mb = index_size_mb

    @property
    def fragmentation_gl30_count(self):
        r"""Gets the fragmentation_gl30_count of this ShowIndexUsageStatisticsResponse.

        碎片率大于30%的数量

        :return: The fragmentation_gl30_count of this ShowIndexUsageStatisticsResponse.
        :rtype: int
        """
        return self._fragmentation_gl30_count

    @fragmentation_gl30_count.setter
    def fragmentation_gl30_count(self, fragmentation_gl30_count):
        r"""Sets the fragmentation_gl30_count of this ShowIndexUsageStatisticsResponse.

        碎片率大于30%的数量

        :param fragmentation_gl30_count: The fragmentation_gl30_count of this ShowIndexUsageStatisticsResponse.
        :type fragmentation_gl30_count: int
        """
        self._fragmentation_gl30_count = fragmentation_gl30_count

    @property
    def key_lookup_lt100_count(self):
        r"""Gets the key_lookup_lt100_count of this ShowIndexUsageStatisticsResponse.

        查找次数小于100的数量

        :return: The key_lookup_lt100_count of this ShowIndexUsageStatisticsResponse.
        :rtype: int
        """
        return self._key_lookup_lt100_count

    @key_lookup_lt100_count.setter
    def key_lookup_lt100_count(self, key_lookup_lt100_count):
        r"""Sets the key_lookup_lt100_count of this ShowIndexUsageStatisticsResponse.

        查找次数小于100的数量

        :param key_lookup_lt100_count: The key_lookup_lt100_count of this ShowIndexUsageStatisticsResponse.
        :type key_lookup_lt100_count: int
        """
        self._key_lookup_lt100_count = key_lookup_lt100_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowIndexUsageStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowIndexUsageStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
