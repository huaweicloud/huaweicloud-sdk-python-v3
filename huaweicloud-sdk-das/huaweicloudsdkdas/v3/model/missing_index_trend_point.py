# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MissingIndexTrendPoint:

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
        'total_missing_index_count': 'int'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'total_missing_index_count': 'total_missing_index_count'
    }

    def __init__(self, collect_time=None, total_missing_index_count=None):
        r"""MissingIndexTrendPoint

        The model defined in huaweicloud sdk

        :param collect_time: 采集时间
        :type collect_time: int
        :param total_missing_index_count: 索引缺失总数
        :type total_missing_index_count: int
        """
        
        

        self._collect_time = None
        self._total_missing_index_count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if total_missing_index_count is not None:
            self.total_missing_index_count = total_missing_index_count

    @property
    def collect_time(self):
        r"""Gets the collect_time of this MissingIndexTrendPoint.

        采集时间

        :return: The collect_time of this MissingIndexTrendPoint.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this MissingIndexTrendPoint.

        采集时间

        :param collect_time: The collect_time of this MissingIndexTrendPoint.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def total_missing_index_count(self):
        r"""Gets the total_missing_index_count of this MissingIndexTrendPoint.

        索引缺失总数

        :return: The total_missing_index_count of this MissingIndexTrendPoint.
        :rtype: int
        """
        return self._total_missing_index_count

    @total_missing_index_count.setter
    def total_missing_index_count(self, total_missing_index_count):
        r"""Sets the total_missing_index_count of this MissingIndexTrendPoint.

        索引缺失总数

        :param total_missing_index_count: The total_missing_index_count of this MissingIndexTrendPoint.
        :type total_missing_index_count: int
        """
        self._total_missing_index_count = total_missing_index_count

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
        if not isinstance(other, MissingIndexTrendPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
