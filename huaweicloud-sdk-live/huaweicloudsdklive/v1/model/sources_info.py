# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourcesInfo:

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
        'bitrate': 'int',
        'width': 'int',
        'height': 'int',
        'enable_snapshot': 'bool',
        'bitrate_for3u8': 'bool',
        'passphrase': 'str',
        'pbkeylen': 'int',
        'backup_urls': 'list[str]',
        'stream_id': 'str',
        'latency': 'int'
    }

    attribute_map = {
        'url': 'url',
        'bitrate': 'bitrate',
        'width': 'width',
        'height': 'height',
        'enable_snapshot': 'enable_snapshot',
        'bitrate_for3u8': 'bitrate_for3u8',
        'passphrase': 'passphrase',
        'pbkeylen': 'pbkeylen',
        'backup_urls': 'backup_urls',
        'stream_id': 'stream_id',
        'latency': 'latency'
    }

    def __init__(self, url=None, bitrate=None, width=None, height=None, enable_snapshot=None, bitrate_for3u8=None, passphrase=None, pbkeylen=None, backup_urls=None, stream_id=None, latency=None):
        r"""SourcesInfo

        The model defined in huaweicloud sdk

        :param url: 频道源流URL，用于外部拉流
        :type url: str
        :param bitrate: 码率。无需直播转码时，此参数为必填项  单位：bps。取值范围：(0,104,857,600]（100Mbps）
        :type bitrate: int
        :param width: 分辨率对应宽的值，非必填项  取值范围：0 - 4096（4K）
        :type width: int
        :param height: 分辨率对应高的值，非必填项  取值范围：0 - 2160（4K）
        :type height: int
        :param enable_snapshot: 描述是否使用该流做截图
        :type enable_snapshot: bool
        :param bitrate_for3u8: 是否使用bitrate来固定码率。默认值：false
        :type bitrate_for3u8: bool
        :param passphrase: 协议为SRT_PUSH时的加密信息
        :type passphrase: str
        :param pbkeylen: srt加密算法
        :type pbkeylen: int
        :param backup_urls: 备入流地址列表
        :type backup_urls: list[str]
        :param stream_id: 频道为SRT_PULL类型时，拉流地址的Stream ID。
        :type stream_id: str
        :param latency: 频道为SRT_PULL类型时的拉流时延。
        :type latency: int
        """
        
        

        self._url = None
        self._bitrate = None
        self._width = None
        self._height = None
        self._enable_snapshot = None
        self._bitrate_for3u8 = None
        self._passphrase = None
        self._pbkeylen = None
        self._backup_urls = None
        self._stream_id = None
        self._latency = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if bitrate is not None:
            self.bitrate = bitrate
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if enable_snapshot is not None:
            self.enable_snapshot = enable_snapshot
        if bitrate_for3u8 is not None:
            self.bitrate_for3u8 = bitrate_for3u8
        if passphrase is not None:
            self.passphrase = passphrase
        if pbkeylen is not None:
            self.pbkeylen = pbkeylen
        if backup_urls is not None:
            self.backup_urls = backup_urls
        if stream_id is not None:
            self.stream_id = stream_id
        if latency is not None:
            self.latency = latency

    @property
    def url(self):
        r"""Gets the url of this SourcesInfo.

        频道源流URL，用于外部拉流

        :return: The url of this SourcesInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SourcesInfo.

        频道源流URL，用于外部拉流

        :param url: The url of this SourcesInfo.
        :type url: str
        """
        self._url = url

    @property
    def bitrate(self):
        r"""Gets the bitrate of this SourcesInfo.

        码率。无需直播转码时，此参数为必填项  单位：bps。取值范围：(0,104,857,600]（100Mbps）

        :return: The bitrate of this SourcesInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this SourcesInfo.

        码率。无需直播转码时，此参数为必填项  单位：bps。取值范围：(0,104,857,600]（100Mbps）

        :param bitrate: The bitrate of this SourcesInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def width(self):
        r"""Gets the width of this SourcesInfo.

        分辨率对应宽的值，非必填项  取值范围：0 - 4096（4K）

        :return: The width of this SourcesInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this SourcesInfo.

        分辨率对应宽的值，非必填项  取值范围：0 - 4096（4K）

        :param width: The width of this SourcesInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this SourcesInfo.

        分辨率对应高的值，非必填项  取值范围：0 - 2160（4K）

        :return: The height of this SourcesInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this SourcesInfo.

        分辨率对应高的值，非必填项  取值范围：0 - 2160（4K）

        :param height: The height of this SourcesInfo.
        :type height: int
        """
        self._height = height

    @property
    def enable_snapshot(self):
        r"""Gets the enable_snapshot of this SourcesInfo.

        描述是否使用该流做截图

        :return: The enable_snapshot of this SourcesInfo.
        :rtype: bool
        """
        return self._enable_snapshot

    @enable_snapshot.setter
    def enable_snapshot(self, enable_snapshot):
        r"""Sets the enable_snapshot of this SourcesInfo.

        描述是否使用该流做截图

        :param enable_snapshot: The enable_snapshot of this SourcesInfo.
        :type enable_snapshot: bool
        """
        self._enable_snapshot = enable_snapshot

    @property
    def bitrate_for3u8(self):
        r"""Gets the bitrate_for3u8 of this SourcesInfo.

        是否使用bitrate来固定码率。默认值：false

        :return: The bitrate_for3u8 of this SourcesInfo.
        :rtype: bool
        """
        return self._bitrate_for3u8

    @bitrate_for3u8.setter
    def bitrate_for3u8(self, bitrate_for3u8):
        r"""Sets the bitrate_for3u8 of this SourcesInfo.

        是否使用bitrate来固定码率。默认值：false

        :param bitrate_for3u8: The bitrate_for3u8 of this SourcesInfo.
        :type bitrate_for3u8: bool
        """
        self._bitrate_for3u8 = bitrate_for3u8

    @property
    def passphrase(self):
        r"""Gets the passphrase of this SourcesInfo.

        协议为SRT_PUSH时的加密信息

        :return: The passphrase of this SourcesInfo.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        r"""Sets the passphrase of this SourcesInfo.

        协议为SRT_PUSH时的加密信息

        :param passphrase: The passphrase of this SourcesInfo.
        :type passphrase: str
        """
        self._passphrase = passphrase

    @property
    def pbkeylen(self):
        r"""Gets the pbkeylen of this SourcesInfo.

        srt加密算法

        :return: The pbkeylen of this SourcesInfo.
        :rtype: int
        """
        return self._pbkeylen

    @pbkeylen.setter
    def pbkeylen(self, pbkeylen):
        r"""Sets the pbkeylen of this SourcesInfo.

        srt加密算法

        :param pbkeylen: The pbkeylen of this SourcesInfo.
        :type pbkeylen: int
        """
        self._pbkeylen = pbkeylen

    @property
    def backup_urls(self):
        r"""Gets the backup_urls of this SourcesInfo.

        备入流地址列表

        :return: The backup_urls of this SourcesInfo.
        :rtype: list[str]
        """
        return self._backup_urls

    @backup_urls.setter
    def backup_urls(self, backup_urls):
        r"""Sets the backup_urls of this SourcesInfo.

        备入流地址列表

        :param backup_urls: The backup_urls of this SourcesInfo.
        :type backup_urls: list[str]
        """
        self._backup_urls = backup_urls

    @property
    def stream_id(self):
        r"""Gets the stream_id of this SourcesInfo.

        频道为SRT_PULL类型时，拉流地址的Stream ID。

        :return: The stream_id of this SourcesInfo.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this SourcesInfo.

        频道为SRT_PULL类型时，拉流地址的Stream ID。

        :param stream_id: The stream_id of this SourcesInfo.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def latency(self):
        r"""Gets the latency of this SourcesInfo.

        频道为SRT_PULL类型时的拉流时延。

        :return: The latency of this SourcesInfo.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this SourcesInfo.

        频道为SRT_PULL类型时的拉流时延。

        :param latency: The latency of this SourcesInfo.
        :type latency: int
        """
        self._latency = latency

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
        if not isinstance(other, SourcesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
