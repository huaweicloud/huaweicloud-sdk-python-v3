# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MssPackageItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'stream_selection': 'list[StreamSelectionItem]',
        'segment_duration_seconds': 'int',
        'playlist_window_seconds': 'int',
        'encryption': 'Encryption',
        'ext_args': 'object',
        'delay_segment': 'int',
        'request_args': 'PackageRequestArgs'
    }

    attribute_map = {
        'url': 'url',
        'stream_selection': 'stream_selection',
        'segment_duration_seconds': 'segment_duration_seconds',
        'playlist_window_seconds': 'playlist_window_seconds',
        'encryption': 'encryption',
        'ext_args': 'ext_args',
        'delay_segment': 'delay_segment',
        'request_args': 'request_args'
    }

    def __init__(self, url=None, stream_selection=None, segment_duration_seconds=None, playlist_window_seconds=None, encryption=None, ext_args=None, delay_segment=None, request_args=None):
        """MssPackageItem

        The model defined in huaweicloud sdk

        :param url: 客户自定义的拉流地址，包括方法、域名、路径和参数
        :type url: str
        :param stream_selection: 从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        :param segment_duration_seconds: 频道输出分片的时长，为必选项  单位：秒。取值范围：1-10
        :type segment_duration_seconds: int
        :param playlist_window_seconds: 频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）
        :type playlist_window_seconds: int
        :param encryption: 
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        :param ext_args: 其他额外参数
        :type ext_args: object
        :param delay_segment: 延播时长，单位秒
        :type delay_segment: int
        :param request_args: 
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        
        

        self._url = None
        self._stream_selection = None
        self._segment_duration_seconds = None
        self._playlist_window_seconds = None
        self._encryption = None
        self._ext_args = None
        self._delay_segment = None
        self._request_args = None
        self.discriminator = None

        self.url = url
        if stream_selection is not None:
            self.stream_selection = stream_selection
        if segment_duration_seconds is not None:
            self.segment_duration_seconds = segment_duration_seconds
        if playlist_window_seconds is not None:
            self.playlist_window_seconds = playlist_window_seconds
        if encryption is not None:
            self.encryption = encryption
        if ext_args is not None:
            self.ext_args = ext_args
        if delay_segment is not None:
            self.delay_segment = delay_segment
        if request_args is not None:
            self.request_args = request_args

    @property
    def url(self):
        """Gets the url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径和参数

        :return: The url of this MssPackageItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径和参数

        :param url: The url of this MssPackageItem.
        :type url: str
        """
        self._url = url

    @property
    def stream_selection(self):
        """Gets the stream_selection of this MssPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :return: The stream_selection of this MssPackageItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        return self._stream_selection

    @stream_selection.setter
    def stream_selection(self, stream_selection):
        """Sets the stream_selection of this MssPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :param stream_selection: The stream_selection of this MssPackageItem.
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        self._stream_selection = stream_selection

    @property
    def segment_duration_seconds(self):
        """Gets the segment_duration_seconds of this MssPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10

        :return: The segment_duration_seconds of this MssPackageItem.
        :rtype: int
        """
        return self._segment_duration_seconds

    @segment_duration_seconds.setter
    def segment_duration_seconds(self, segment_duration_seconds):
        """Sets the segment_duration_seconds of this MssPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10

        :param segment_duration_seconds: The segment_duration_seconds of this MssPackageItem.
        :type segment_duration_seconds: int
        """
        self._segment_duration_seconds = segment_duration_seconds

    @property
    def playlist_window_seconds(self):
        """Gets the playlist_window_seconds of this MssPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :return: The playlist_window_seconds of this MssPackageItem.
        :rtype: int
        """
        return self._playlist_window_seconds

    @playlist_window_seconds.setter
    def playlist_window_seconds(self, playlist_window_seconds):
        """Sets the playlist_window_seconds of this MssPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :param playlist_window_seconds: The playlist_window_seconds of this MssPackageItem.
        :type playlist_window_seconds: int
        """
        self._playlist_window_seconds = playlist_window_seconds

    @property
    def encryption(self):
        """Gets the encryption of this MssPackageItem.

        :return: The encryption of this MssPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.Encryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this MssPackageItem.

        :param encryption: The encryption of this MssPackageItem.
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        """
        self._encryption = encryption

    @property
    def ext_args(self):
        """Gets the ext_args of this MssPackageItem.

        其他额外参数

        :return: The ext_args of this MssPackageItem.
        :rtype: object
        """
        return self._ext_args

    @ext_args.setter
    def ext_args(self, ext_args):
        """Sets the ext_args of this MssPackageItem.

        其他额外参数

        :param ext_args: The ext_args of this MssPackageItem.
        :type ext_args: object
        """
        self._ext_args = ext_args

    @property
    def delay_segment(self):
        """Gets the delay_segment of this MssPackageItem.

        延播时长，单位秒

        :return: The delay_segment of this MssPackageItem.
        :rtype: int
        """
        return self._delay_segment

    @delay_segment.setter
    def delay_segment(self, delay_segment):
        """Sets the delay_segment of this MssPackageItem.

        延播时长，单位秒

        :param delay_segment: The delay_segment of this MssPackageItem.
        :type delay_segment: int
        """
        self._delay_segment = delay_segment

    @property
    def request_args(self):
        """Gets the request_args of this MssPackageItem.

        :return: The request_args of this MssPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        return self._request_args

    @request_args.setter
    def request_args(self, request_args):
        """Sets the request_args of this MssPackageItem.

        :param request_args: The request_args of this MssPackageItem.
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        self._request_args = request_args

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
        if not isinstance(other, MssPackageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
