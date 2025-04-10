# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStreamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'stream_names': 'list[str]',
        'has_more_streams': 'bool',
        'stream_info_list': 'list[StreamInfo]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'stream_names': 'stream_names',
        'has_more_streams': 'has_more_streams',
        'stream_info_list': 'stream_info_list'
    }

    def __init__(self, total_number=None, stream_names=None, has_more_streams=None, stream_info_list=None):
        r"""ListStreamsResponse

        The model defined in huaweicloud sdk

        :param total_number: 当前租户所有通道数量。
        :type total_number: int
        :param stream_names: 满足当前请求条件的通道名称的列表。
        :type stream_names: list[str]
        :param has_more_streams: 是否还有更多满足条件的通道。  - true：是 - false：否
        :type has_more_streams: bool
        :param stream_info_list: 通道列表详情。
        :type stream_info_list: list[:class:`huaweicloudsdkdis.v2.StreamInfo`]
        """
        
        super(ListStreamsResponse, self).__init__()

        self._total_number = None
        self._stream_names = None
        self._has_more_streams = None
        self._stream_info_list = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if stream_names is not None:
            self.stream_names = stream_names
        if has_more_streams is not None:
            self.has_more_streams = has_more_streams
        if stream_info_list is not None:
            self.stream_info_list = stream_info_list

    @property
    def total_number(self):
        r"""Gets the total_number of this ListStreamsResponse.

        当前租户所有通道数量。

        :return: The total_number of this ListStreamsResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this ListStreamsResponse.

        当前租户所有通道数量。

        :param total_number: The total_number of this ListStreamsResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def stream_names(self):
        r"""Gets the stream_names of this ListStreamsResponse.

        满足当前请求条件的通道名称的列表。

        :return: The stream_names of this ListStreamsResponse.
        :rtype: list[str]
        """
        return self._stream_names

    @stream_names.setter
    def stream_names(self, stream_names):
        r"""Sets the stream_names of this ListStreamsResponse.

        满足当前请求条件的通道名称的列表。

        :param stream_names: The stream_names of this ListStreamsResponse.
        :type stream_names: list[str]
        """
        self._stream_names = stream_names

    @property
    def has_more_streams(self):
        r"""Gets the has_more_streams of this ListStreamsResponse.

        是否还有更多满足条件的通道。  - true：是 - false：否

        :return: The has_more_streams of this ListStreamsResponse.
        :rtype: bool
        """
        return self._has_more_streams

    @has_more_streams.setter
    def has_more_streams(self, has_more_streams):
        r"""Sets the has_more_streams of this ListStreamsResponse.

        是否还有更多满足条件的通道。  - true：是 - false：否

        :param has_more_streams: The has_more_streams of this ListStreamsResponse.
        :type has_more_streams: bool
        """
        self._has_more_streams = has_more_streams

    @property
    def stream_info_list(self):
        r"""Gets the stream_info_list of this ListStreamsResponse.

        通道列表详情。

        :return: The stream_info_list of this ListStreamsResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.StreamInfo`]
        """
        return self._stream_info_list

    @stream_info_list.setter
    def stream_info_list(self, stream_info_list):
        r"""Sets the stream_info_list of this ListStreamsResponse.

        通道列表详情。

        :param stream_info_list: The stream_info_list of this ListStreamsResponse.
        :type stream_info_list: list[:class:`huaweicloudsdkdis.v2.StreamInfo`]
        """
        self._stream_info_list = stream_info_list

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
        if not isinstance(other, ListStreamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
