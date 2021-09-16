# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchStatisticUserInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'data': 'list[StatisticUserDataItem]'
    }

    attribute_map = {
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'data': 'data'
    }

    def __init__(self, count=None, limit=None, offset=None, data=None):
        """SearchStatisticUserInfoResponse - a model defined in huaweicloud sdk"""
        
        super(SearchStatisticUserInfoResponse, self).__init__()

        self._count = None
        self._limit = None
        self._offset = None
        self._data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if data is not None:
            self.data = data

    @property
    def count(self):
        """Gets the count of this SearchStatisticUserInfoResponse.

        总记录数。

        :return: The count of this SearchStatisticUserInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SearchStatisticUserInfoResponse.

        总记录数。

        :param count: The count of this SearchStatisticUserInfoResponse.
        :type: int
        """
        self._count = count

    @property
    def limit(self):
        """Gets the limit of this SearchStatisticUserInfoResponse.

        查询条目数量。

        :return: The limit of this SearchStatisticUserInfoResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchStatisticUserInfoResponse.

        查询条目数量。

        :param limit: The limit of this SearchStatisticUserInfoResponse.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchStatisticUserInfoResponse.

        查询偏移量。

        :return: The offset of this SearchStatisticUserInfoResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchStatisticUserInfoResponse.

        查询偏移量。

        :param offset: The offset of this SearchStatisticUserInfoResponse.
        :type: int
        """
        self._offset = offset

    @property
    def data(self):
        """Gets the data of this SearchStatisticUserInfoResponse.

        会议用户数据按时间点统计的查询结果数组。

        :return: The data of this SearchStatisticUserInfoResponse.
        :rtype: list[StatisticUserDataItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SearchStatisticUserInfoResponse.

        会议用户数据按时间点统计的查询结果数组。

        :param data: The data of this SearchStatisticUserInfoResponse.
        :type: list[StatisticUserDataItem]
        """
        self._data = data

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
        if not isinstance(other, SearchStatisticUserInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other