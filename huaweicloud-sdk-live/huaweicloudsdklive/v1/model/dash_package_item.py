# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashPackageItem:

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
        'ads': 'object',
        'ext_args': 'object',
        'request_args': 'PackageRequestArgs',
        'ad_marker': 'str'
    }

    attribute_map = {
        'url': 'url',
        'stream_selection': 'stream_selection',
        'segment_duration_seconds': 'segment_duration_seconds',
        'playlist_window_seconds': 'playlist_window_seconds',
        'encryption': 'encryption',
        'ads': 'ads',
        'ext_args': 'ext_args',
        'request_args': 'request_args',
        'ad_marker': 'ad_marker'
    }

    def __init__(self, url=None, stream_selection=None, segment_duration_seconds=None, playlist_window_seconds=None, encryption=None, ads=None, ext_args=None, request_args=None, ad_marker=None):
        """DashPackageItem

        The model defined in huaweicloud sdk

        :param url: 客户自定义的拉流地址，包括方法、域名、路径
        :type url: str
        :param stream_selection: 从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        :param segment_duration_seconds: 频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 &gt; 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！
        :type segment_duration_seconds: int
        :param playlist_window_seconds: 频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）
        :type playlist_window_seconds: int
        :param encryption: 
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        :param ads: 广告配置
        :type ads: object
        :param ext_args: 其他额外参数
        :type ext_args: object
        :param request_args: 
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        :param ad_marker: 广告标识。  DASH取值：\&quot;xml+bin\&quot;。 
        :type ad_marker: str
        """
        
        

        self._url = None
        self._stream_selection = None
        self._segment_duration_seconds = None
        self._playlist_window_seconds = None
        self._encryption = None
        self._ads = None
        self._ext_args = None
        self._request_args = None
        self._ad_marker = None
        self.discriminator = None

        self.url = url
        if stream_selection is not None:
            self.stream_selection = stream_selection
        self.segment_duration_seconds = segment_duration_seconds
        if playlist_window_seconds is not None:
            self.playlist_window_seconds = playlist_window_seconds
        if encryption is not None:
            self.encryption = encryption
        if ads is not None:
            self.ads = ads
        if ext_args is not None:
            self.ext_args = ext_args
        if request_args is not None:
            self.request_args = request_args
        if ad_marker is not None:
            self.ad_marker = ad_marker

    @property
    def url(self):
        """Gets the url of this DashPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :return: The url of this DashPackageItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DashPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :param url: The url of this DashPackageItem.
        :type url: str
        """
        self._url = url

    @property
    def stream_selection(self):
        """Gets the stream_selection of this DashPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :return: The stream_selection of this DashPackageItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        return self._stream_selection

    @stream_selection.setter
    def stream_selection(self, stream_selection):
        """Sets the stream_selection of this DashPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :param stream_selection: The stream_selection of this DashPackageItem.
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        self._stream_selection = stream_selection

    @property
    def segment_duration_seconds(self):
        """Gets the segment_duration_seconds of this DashPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 > 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！

        :return: The segment_duration_seconds of this DashPackageItem.
        :rtype: int
        """
        return self._segment_duration_seconds

    @segment_duration_seconds.setter
    def segment_duration_seconds(self, segment_duration_seconds):
        """Sets the segment_duration_seconds of this DashPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 > 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！

        :param segment_duration_seconds: The segment_duration_seconds of this DashPackageItem.
        :type segment_duration_seconds: int
        """
        self._segment_duration_seconds = segment_duration_seconds

    @property
    def playlist_window_seconds(self):
        """Gets the playlist_window_seconds of this DashPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :return: The playlist_window_seconds of this DashPackageItem.
        :rtype: int
        """
        return self._playlist_window_seconds

    @playlist_window_seconds.setter
    def playlist_window_seconds(self, playlist_window_seconds):
        """Sets the playlist_window_seconds of this DashPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :param playlist_window_seconds: The playlist_window_seconds of this DashPackageItem.
        :type playlist_window_seconds: int
        """
        self._playlist_window_seconds = playlist_window_seconds

    @property
    def encryption(self):
        """Gets the encryption of this DashPackageItem.

        :return: The encryption of this DashPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.Encryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this DashPackageItem.

        :param encryption: The encryption of this DashPackageItem.
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        """
        self._encryption = encryption

    @property
    def ads(self):
        """Gets the ads of this DashPackageItem.

        广告配置

        :return: The ads of this DashPackageItem.
        :rtype: object
        """
        return self._ads

    @ads.setter
    def ads(self, ads):
        """Sets the ads of this DashPackageItem.

        广告配置

        :param ads: The ads of this DashPackageItem.
        :type ads: object
        """
        self._ads = ads

    @property
    def ext_args(self):
        """Gets the ext_args of this DashPackageItem.

        其他额外参数

        :return: The ext_args of this DashPackageItem.
        :rtype: object
        """
        return self._ext_args

    @ext_args.setter
    def ext_args(self, ext_args):
        """Sets the ext_args of this DashPackageItem.

        其他额外参数

        :param ext_args: The ext_args of this DashPackageItem.
        :type ext_args: object
        """
        self._ext_args = ext_args

    @property
    def request_args(self):
        """Gets the request_args of this DashPackageItem.

        :return: The request_args of this DashPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        return self._request_args

    @request_args.setter
    def request_args(self, request_args):
        """Sets the request_args of this DashPackageItem.

        :param request_args: The request_args of this DashPackageItem.
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        self._request_args = request_args

    @property
    def ad_marker(self):
        """Gets the ad_marker of this DashPackageItem.

        广告标识。  DASH取值：\"xml+bin\"。 

        :return: The ad_marker of this DashPackageItem.
        :rtype: str
        """
        return self._ad_marker

    @ad_marker.setter
    def ad_marker(self, ad_marker):
        """Sets the ad_marker of this DashPackageItem.

        广告标识。  DASH取值：\"xml+bin\"。 

        :param ad_marker: The ad_marker of this DashPackageItem.
        :type ad_marker: str
        """
        self._ad_marker = ad_marker

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
        if not isinstance(other, DashPackageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
