# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceRsp:

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
        'enable_snapshot': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'bitrate': 'bitrate',
        'width': 'width',
        'height': 'height',
        'enable_snapshot': 'enable_snapshot'
    }

    def __init__(self, url=None, bitrate=None, width=None, height=None, enable_snapshot=None):
        r"""SourceRsp

        The model defined in huaweicloud sdk

        :param url: RTMP推流地址
        :type url: str
        :param bitrate: 码率。  单位：bps。取值范围：(0,104,857,600]（100Mbps）
        :type bitrate: int
        :param width: 分辨率对应宽的值。取值范围：0 - 4096（4K）
        :type width: int
        :param height: 分辨率对应高的值。取值范围：0 - 2160（4K）
        :type height: int
        :param enable_snapshot: 描述是否使用该流做截图
        :type enable_snapshot: bool
        """
        
        

        self._url = None
        self._bitrate = None
        self._width = None
        self._height = None
        self._enable_snapshot = None
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

    @property
    def url(self):
        r"""Gets the url of this SourceRsp.

        RTMP推流地址

        :return: The url of this SourceRsp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SourceRsp.

        RTMP推流地址

        :param url: The url of this SourceRsp.
        :type url: str
        """
        self._url = url

    @property
    def bitrate(self):
        r"""Gets the bitrate of this SourceRsp.

        码率。  单位：bps。取值范围：(0,104,857,600]（100Mbps）

        :return: The bitrate of this SourceRsp.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this SourceRsp.

        码率。  单位：bps。取值范围：(0,104,857,600]（100Mbps）

        :param bitrate: The bitrate of this SourceRsp.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def width(self):
        r"""Gets the width of this SourceRsp.

        分辨率对应宽的值。取值范围：0 - 4096（4K）

        :return: The width of this SourceRsp.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this SourceRsp.

        分辨率对应宽的值。取值范围：0 - 4096（4K）

        :param width: The width of this SourceRsp.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this SourceRsp.

        分辨率对应高的值。取值范围：0 - 2160（4K）

        :return: The height of this SourceRsp.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this SourceRsp.

        分辨率对应高的值。取值范围：0 - 2160（4K）

        :param height: The height of this SourceRsp.
        :type height: int
        """
        self._height = height

    @property
    def enable_snapshot(self):
        r"""Gets the enable_snapshot of this SourceRsp.

        描述是否使用该流做截图

        :return: The enable_snapshot of this SourceRsp.
        :rtype: bool
        """
        return self._enable_snapshot

    @enable_snapshot.setter
    def enable_snapshot(self, enable_snapshot):
        r"""Sets the enable_snapshot of this SourceRsp.

        描述是否使用该流做截图

        :param enable_snapshot: The enable_snapshot of this SourceRsp.
        :type enable_snapshot: bool
        """
        self._enable_snapshot = enable_snapshot

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
        if not isinstance(other, SourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
