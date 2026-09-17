# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexUsageTrendPoint:

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
        'max_fragmentation_percentage': 'float',
        'index_size_mb': 'float',
        'page_count': 'float'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'max_fragmentation_percentage': 'max_fragmentation_percentage',
        'index_size_mb': 'index_size_mb',
        'page_count': 'page_count'
    }

    def __init__(self, collect_time=None, max_fragmentation_percentage=None, index_size_mb=None, page_count=None):
        r"""IndexUsageTrendPoint

        The model defined in huaweicloud sdk

        :param collect_time: 采集时间
        :type collect_time: int
        :param max_fragmentation_percentage: TOP1碎片率
        :type max_fragmentation_percentage: float
        :param index_size_mb: 总空间大小(MB)
        :type index_size_mb: float
        :param page_count: 页数量
        :type page_count: float
        """
        
        

        self._collect_time = None
        self._max_fragmentation_percentage = None
        self._index_size_mb = None
        self._page_count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if max_fragmentation_percentage is not None:
            self.max_fragmentation_percentage = max_fragmentation_percentage
        if index_size_mb is not None:
            self.index_size_mb = index_size_mb
        if page_count is not None:
            self.page_count = page_count

    @property
    def collect_time(self):
        r"""Gets the collect_time of this IndexUsageTrendPoint.

        采集时间

        :return: The collect_time of this IndexUsageTrendPoint.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this IndexUsageTrendPoint.

        采集时间

        :param collect_time: The collect_time of this IndexUsageTrendPoint.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def max_fragmentation_percentage(self):
        r"""Gets the max_fragmentation_percentage of this IndexUsageTrendPoint.

        TOP1碎片率

        :return: The max_fragmentation_percentage of this IndexUsageTrendPoint.
        :rtype: float
        """
        return self._max_fragmentation_percentage

    @max_fragmentation_percentage.setter
    def max_fragmentation_percentage(self, max_fragmentation_percentage):
        r"""Sets the max_fragmentation_percentage of this IndexUsageTrendPoint.

        TOP1碎片率

        :param max_fragmentation_percentage: The max_fragmentation_percentage of this IndexUsageTrendPoint.
        :type max_fragmentation_percentage: float
        """
        self._max_fragmentation_percentage = max_fragmentation_percentage

    @property
    def index_size_mb(self):
        r"""Gets the index_size_mb of this IndexUsageTrendPoint.

        总空间大小(MB)

        :return: The index_size_mb of this IndexUsageTrendPoint.
        :rtype: float
        """
        return self._index_size_mb

    @index_size_mb.setter
    def index_size_mb(self, index_size_mb):
        r"""Sets the index_size_mb of this IndexUsageTrendPoint.

        总空间大小(MB)

        :param index_size_mb: The index_size_mb of this IndexUsageTrendPoint.
        :type index_size_mb: float
        """
        self._index_size_mb = index_size_mb

    @property
    def page_count(self):
        r"""Gets the page_count of this IndexUsageTrendPoint.

        页数量

        :return: The page_count of this IndexUsageTrendPoint.
        :rtype: float
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        r"""Sets the page_count of this IndexUsageTrendPoint.

        页数量

        :param page_count: The page_count of this IndexUsageTrendPoint.
        :type page_count: float
        """
        self._page_count = page_count

    def to_dict(self):
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
        if not isinstance(other, IndexUsageTrendPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
