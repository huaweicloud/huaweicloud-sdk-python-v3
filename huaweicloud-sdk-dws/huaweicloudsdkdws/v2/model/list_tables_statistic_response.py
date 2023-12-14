# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesStatisticResponse(SdkResponse):

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
        'data': 'list[ListTablesStatisticDto]',
        'count': 'int'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'data': 'data',
        'count': 'count'
    }

    def __init__(self, collect_time=None, data=None, count=None):
        """ListTablesStatisticResponse

        The model defined in huaweicloud sdk

        :param collect_time: 数据采集时间毫秒级时间戳。
        :type collect_time: int
        :param data: 表倾斜率或脏页率列表。
        :type data: list[:class:`huaweicloudsdkdws.v2.ListTablesStatisticDto`]
        :param count: 总列表大小。
        :type count: int
        """
        
        super(ListTablesStatisticResponse, self).__init__()

        self._collect_time = None
        self._data = None
        self._count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if data is not None:
            self.data = data
        if count is not None:
            self.count = count

    @property
    def collect_time(self):
        """Gets the collect_time of this ListTablesStatisticResponse.

        数据采集时间毫秒级时间戳。

        :return: The collect_time of this ListTablesStatisticResponse.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this ListTablesStatisticResponse.

        数据采集时间毫秒级时间戳。

        :param collect_time: The collect_time of this ListTablesStatisticResponse.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def data(self):
        """Gets the data of this ListTablesStatisticResponse.

        表倾斜率或脏页率列表。

        :return: The data of this ListTablesStatisticResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ListTablesStatisticDto`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListTablesStatisticResponse.

        表倾斜率或脏页率列表。

        :param data: The data of this ListTablesStatisticResponse.
        :type data: list[:class:`huaweicloudsdkdws.v2.ListTablesStatisticDto`]
        """
        self._data = data

    @property
    def count(self):
        """Gets the count of this ListTablesStatisticResponse.

        总列表大小。

        :return: The count of this ListTablesStatisticResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTablesStatisticResponse.

        总列表大小。

        :param count: The count of this ListTablesStatisticResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListTablesStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
