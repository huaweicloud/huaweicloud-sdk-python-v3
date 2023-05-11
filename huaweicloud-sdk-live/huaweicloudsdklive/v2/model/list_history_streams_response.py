# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryStreamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'history_stream_list': 'list[HistoryStreamInfo]',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'history_stream_list': 'history_stream_list',
        'total': 'total',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, history_stream_list=None, total=None, x_request_id=None):
        """ListHistoryStreamsResponse

        The model defined in huaweicloud sdk

        :param history_stream_list: 历史流信息列表。
        :type history_stream_list: list[:class:`huaweicloudsdklive.v2.HistoryStreamInfo`]
        :param total: 总记录数。
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListHistoryStreamsResponse, self).__init__()

        self._history_stream_list = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if history_stream_list is not None:
            self.history_stream_list = history_stream_list
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def history_stream_list(self):
        """Gets the history_stream_list of this ListHistoryStreamsResponse.

        历史流信息列表。

        :return: The history_stream_list of this ListHistoryStreamsResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.HistoryStreamInfo`]
        """
        return self._history_stream_list

    @history_stream_list.setter
    def history_stream_list(self, history_stream_list):
        """Sets the history_stream_list of this ListHistoryStreamsResponse.

        历史流信息列表。

        :param history_stream_list: The history_stream_list of this ListHistoryStreamsResponse.
        :type history_stream_list: list[:class:`huaweicloudsdklive.v2.HistoryStreamInfo`]
        """
        self._history_stream_list = history_stream_list

    @property
    def total(self):
        """Gets the total of this ListHistoryStreamsResponse.

        总记录数。

        :return: The total of this ListHistoryStreamsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListHistoryStreamsResponse.

        总记录数。

        :param total: The total of this ListHistoryStreamsResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListHistoryStreamsResponse.

        :return: The x_request_id of this ListHistoryStreamsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListHistoryStreamsResponse.

        :param x_request_id: The x_request_id of this ListHistoryStreamsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListHistoryStreamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
