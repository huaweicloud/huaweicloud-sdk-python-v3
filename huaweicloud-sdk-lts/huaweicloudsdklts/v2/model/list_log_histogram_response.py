# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogHistogramResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'histogram': 'str',
        'count': 'int',
        'is_query_complete': 'bool'
    }

    attribute_map = {
        'histogram': 'histogram',
        'count': 'count',
        'is_query_complete': 'isQueryComplete'
    }

    def __init__(self, histogram=None, count=None, is_query_complete=None):
        """ListLogHistogramResponse

        The model defined in huaweicloud sdk

        :param histogram: 直方图结果
        :type histogram: str
        :param count: 日志条数
        :type count: int
        :param is_query_complete: 是否查询完成。
        :type is_query_complete: bool
        """
        
        super(ListLogHistogramResponse, self).__init__()

        self._histogram = None
        self._count = None
        self._is_query_complete = None
        self.discriminator = None

        if histogram is not None:
            self.histogram = histogram
        if count is not None:
            self.count = count
        if is_query_complete is not None:
            self.is_query_complete = is_query_complete

    @property
    def histogram(self):
        """Gets the histogram of this ListLogHistogramResponse.

        直方图结果

        :return: The histogram of this ListLogHistogramResponse.
        :rtype: str
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this ListLogHistogramResponse.

        直方图结果

        :param histogram: The histogram of this ListLogHistogramResponse.
        :type histogram: str
        """
        self._histogram = histogram

    @property
    def count(self):
        """Gets the count of this ListLogHistogramResponse.

        日志条数

        :return: The count of this ListLogHistogramResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListLogHistogramResponse.

        日志条数

        :param count: The count of this ListLogHistogramResponse.
        :type count: int
        """
        self._count = count

    @property
    def is_query_complete(self):
        """Gets the is_query_complete of this ListLogHistogramResponse.

        是否查询完成。

        :return: The is_query_complete of this ListLogHistogramResponse.
        :rtype: bool
        """
        return self._is_query_complete

    @is_query_complete.setter
    def is_query_complete(self, is_query_complete):
        """Sets the is_query_complete of this ListLogHistogramResponse.

        是否查询完成。

        :param is_query_complete: The is_query_complete of this ListLogHistogramResponse.
        :type is_query_complete: bool
        """
        self._is_query_complete = is_query_complete

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
        if not isinstance(other, ListLogHistogramResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
