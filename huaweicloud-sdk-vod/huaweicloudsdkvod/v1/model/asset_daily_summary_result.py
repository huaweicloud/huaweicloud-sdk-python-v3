# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetDailySummaryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'link': 'str'
    }

    attribute_map = {
        'date': 'date',
        'link': 'link'
    }

    def __init__(self, date=None, link=None):
        r"""AssetDailySummaryResult

        The model defined in huaweicloud sdk

        :param date: 播放日期，格式为：yyyyMMdd000000。 
        :type date: str
        :param link: 日播放统计数据文件的下载地址，有效期为12个小时。  文件内容格式：[域名]\\t[媒资ID]\\t[日期]\\t[播放流量]\\t[播放次数]  播放次数统计说明： - HLS文件：访问M3U8文件时会统计播放次数，访问TS文件时不会统计播放次数。 - 其它文件：如MP4文件，当播放请求带有range且range的start参数不等于0时，不统计播放次数。其它情况下，会统计播放次数。
        :type link: str
        """
        
        

        self._date = None
        self._link = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if link is not None:
            self.link = link

    @property
    def date(self):
        r"""Gets the date of this AssetDailySummaryResult.

        播放日期，格式为：yyyyMMdd000000。 

        :return: The date of this AssetDailySummaryResult.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this AssetDailySummaryResult.

        播放日期，格式为：yyyyMMdd000000。 

        :param date: The date of this AssetDailySummaryResult.
        :type date: str
        """
        self._date = date

    @property
    def link(self):
        r"""Gets the link of this AssetDailySummaryResult.

        日播放统计数据文件的下载地址，有效期为12个小时。  文件内容格式：[域名]\\t[媒资ID]\\t[日期]\\t[播放流量]\\t[播放次数]  播放次数统计说明： - HLS文件：访问M3U8文件时会统计播放次数，访问TS文件时不会统计播放次数。 - 其它文件：如MP4文件，当播放请求带有range且range的start参数不等于0时，不统计播放次数。其它情况下，会统计播放次数。

        :return: The link of this AssetDailySummaryResult.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this AssetDailySummaryResult.

        日播放统计数据文件的下载地址，有效期为12个小时。  文件内容格式：[域名]\\t[媒资ID]\\t[日期]\\t[播放流量]\\t[播放次数]  播放次数统计说明： - HLS文件：访问M3U8文件时会统计播放次数，访问TS文件时不会统计播放次数。 - 其它文件：如MP4文件，当播放请求带有range且range的start参数不等于0时，不统计播放次数。其它情况下，会统计播放次数。

        :param link: The link of this AssetDailySummaryResult.
        :type link: str
        """
        self._link = link

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
        if not isinstance(other, AssetDailySummaryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
