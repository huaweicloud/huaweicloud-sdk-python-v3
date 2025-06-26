# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicMessageStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'total': 'SumCountDetail',
        'statistics': 'list[StatisticsDetail]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'total': 'total',
        'statistics': 'statistics'
    }

    def __init__(self, request_id=None, total=None, statistics=None):
        r"""ListTopicMessageStatisticsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param total: 
        :type total: :class:`huaweicloudsdksmn.v2.SumCountDetail`
        :param statistics: 周期内的发送详情列表
        :type statistics: list[:class:`huaweicloudsdksmn.v2.StatisticsDetail`]
        """
        
        super(ListTopicMessageStatisticsResponse, self).__init__()

        self._request_id = None
        self._total = None
        self._statistics = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if total is not None:
            self.total = total
        if statistics is not None:
            self.statistics = statistics

    @property
    def request_id(self):
        r"""Gets the request_id of this ListTopicMessageStatisticsResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListTopicMessageStatisticsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListTopicMessageStatisticsResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListTopicMessageStatisticsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total(self):
        r"""Gets the total of this ListTopicMessageStatisticsResponse.

        :return: The total of this ListTopicMessageStatisticsResponse.
        :rtype: :class:`huaweicloudsdksmn.v2.SumCountDetail`
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTopicMessageStatisticsResponse.

        :param total: The total of this ListTopicMessageStatisticsResponse.
        :type total: :class:`huaweicloudsdksmn.v2.SumCountDetail`
        """
        self._total = total

    @property
    def statistics(self):
        r"""Gets the statistics of this ListTopicMessageStatisticsResponse.

        周期内的发送详情列表

        :return: The statistics of this ListTopicMessageStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.StatisticsDetail`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ListTopicMessageStatisticsResponse.

        周期内的发送详情列表

        :param statistics: The statistics of this ListTopicMessageStatisticsResponse.
        :type statistics: list[:class:`huaweicloudsdksmn.v2.StatisticsDetail`]
        """
        self._statistics = statistics

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
        if not isinstance(other, ListTopicMessageStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
