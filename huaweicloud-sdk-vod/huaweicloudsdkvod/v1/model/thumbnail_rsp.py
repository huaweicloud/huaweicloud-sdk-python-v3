# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbnailRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'url': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'url': 'url'
    }

    def __init__(self, offset=None, url=None):
        """ThumbnailRsp

        The model defined in huaweicloud sdk

        :param offset: 截图在视频中的时间偏移，单位为秒。
        :type offset: int
        :param url: 截图访问URL
        :type url: str
        """
        
        

        self._offset = None
        self._url = None
        self.discriminator = None

        self.offset = offset
        self.url = url

    @property
    def offset(self):
        """Gets the offset of this ThumbnailRsp.

        截图在视频中的时间偏移，单位为秒。

        :return: The offset of this ThumbnailRsp.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ThumbnailRsp.

        截图在视频中的时间偏移，单位为秒。

        :param offset: The offset of this ThumbnailRsp.
        :type offset: int
        """
        self._offset = offset

    @property
    def url(self):
        """Gets the url of this ThumbnailRsp.

        截图访问URL

        :return: The url of this ThumbnailRsp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ThumbnailRsp.

        截图访问URL

        :param url: The url of this ThumbnailRsp.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ThumbnailRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
