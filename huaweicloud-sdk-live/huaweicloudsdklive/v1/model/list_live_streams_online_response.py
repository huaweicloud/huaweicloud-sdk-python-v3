# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLiveStreamsOnlineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_page': 'int',
        'total_num': 'int',
        'offset': 'int',
        'limit': 'int',
        'request_id': 'str',
        'streams': 'list[OnlineInfo]'
    }

    attribute_map = {
        'total_page': 'total_page',
        'total_num': 'total_num',
        'offset': 'offset',
        'limit': 'limit',
        'request_id': 'request_id',
        'streams': 'streams'
    }

    def __init__(self, total_page=None, total_num=None, offset=None, limit=None, request_id=None, streams=None):
        r"""ListLiveStreamsOnlineResponse

        The model defined in huaweicloud sdk

        :param total_page: 总条页数
        :type total_page: int
        :param total_num: 总条目数
        :type total_num: int
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页条目数
        :type limit: int
        :param request_id: 请求唯一标识
        :type request_id: str
        :param streams: 推流统计
        :type streams: list[:class:`huaweicloudsdklive.v1.OnlineInfo`]
        """
        
        super(ListLiveStreamsOnlineResponse, self).__init__()

        self._total_page = None
        self._total_num = None
        self._offset = None
        self._limit = None
        self._request_id = None
        self._streams = None
        self.discriminator = None

        if total_page is not None:
            self.total_page = total_page
        if total_num is not None:
            self.total_num = total_num
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if request_id is not None:
            self.request_id = request_id
        if streams is not None:
            self.streams = streams

    @property
    def total_page(self):
        r"""Gets the total_page of this ListLiveStreamsOnlineResponse.

        总条页数

        :return: The total_page of this ListLiveStreamsOnlineResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        r"""Sets the total_page of this ListLiveStreamsOnlineResponse.

        总条页数

        :param total_page: The total_page of this ListLiveStreamsOnlineResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_num(self):
        r"""Gets the total_num of this ListLiveStreamsOnlineResponse.

        总条目数

        :return: The total_num of this ListLiveStreamsOnlineResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListLiveStreamsOnlineResponse.

        总条目数

        :param total_num: The total_num of this ListLiveStreamsOnlineResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def offset(self):
        r"""Gets the offset of this ListLiveStreamsOnlineResponse.

        偏移量

        :return: The offset of this ListLiveStreamsOnlineResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLiveStreamsOnlineResponse.

        偏移量

        :param offset: The offset of this ListLiveStreamsOnlineResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLiveStreamsOnlineResponse.

        每页条目数

        :return: The limit of this ListLiveStreamsOnlineResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLiveStreamsOnlineResponse.

        每页条目数

        :param limit: The limit of this ListLiveStreamsOnlineResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def request_id(self):
        r"""Gets the request_id of this ListLiveStreamsOnlineResponse.

        请求唯一标识

        :return: The request_id of this ListLiveStreamsOnlineResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListLiveStreamsOnlineResponse.

        请求唯一标识

        :param request_id: The request_id of this ListLiveStreamsOnlineResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def streams(self):
        r"""Gets the streams of this ListLiveStreamsOnlineResponse.

        推流统计

        :return: The streams of this ListLiveStreamsOnlineResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.OnlineInfo`]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        r"""Sets the streams of this ListLiveStreamsOnlineResponse.

        推流统计

        :param streams: The streams of this ListLiveStreamsOnlineResponse.
        :type streams: list[:class:`huaweicloudsdklive.v1.OnlineInfo`]
        """
        self._streams = streams

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
        if not isinstance(other, ListLiveStreamsOnlineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
