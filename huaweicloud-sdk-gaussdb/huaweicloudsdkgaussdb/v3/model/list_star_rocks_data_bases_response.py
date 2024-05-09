# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDataBasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[str]',
        'total_count': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'databases': 'databases',
        'total_count': 'total_count',
        'timestamp': 'timestamp'
    }

    def __init__(self, databases=None, total_count=None, timestamp=None):
        """ListStarRocksDataBasesResponse

        The model defined in huaweicloud sdk

        :param databases: 数据库名称。
        :type databases: list[str]
        :param total_count: 数据库数量。
        :type total_count: int
        :param timestamp: 查询时间戳。
        :type timestamp: int
        """
        
        super(ListStarRocksDataBasesResponse, self).__init__()

        self._databases = None
        self._total_count = None
        self._timestamp = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if total_count is not None:
            self.total_count = total_count
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def databases(self):
        """Gets the databases of this ListStarRocksDataBasesResponse.

        数据库名称。

        :return: The databases of this ListStarRocksDataBasesResponse.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ListStarRocksDataBasesResponse.

        数据库名称。

        :param databases: The databases of this ListStarRocksDataBasesResponse.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def total_count(self):
        """Gets the total_count of this ListStarRocksDataBasesResponse.

        数据库数量。

        :return: The total_count of this ListStarRocksDataBasesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListStarRocksDataBasesResponse.

        数据库数量。

        :param total_count: The total_count of this ListStarRocksDataBasesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def timestamp(self):
        """Gets the timestamp of this ListStarRocksDataBasesResponse.

        查询时间戳。

        :return: The timestamp of this ListStarRocksDataBasesResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ListStarRocksDataBasesResponse.

        查询时间戳。

        :param timestamp: The timestamp of this ListStarRocksDataBasesResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListStarRocksDataBasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
