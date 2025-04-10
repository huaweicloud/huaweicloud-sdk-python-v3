# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureResultUrlVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'captcha': 'str',
        'expires': 'int',
        'file_list': 'list[CaptureFile]',
        'request_header': 'HostHeaderInfo',
        'url': 'str'
    }

    attribute_map = {
        'captcha': 'captcha',
        'expires': 'expires',
        'file_list': 'file_list',
        'request_header': 'request_header',
        'url': 'url'
    }

    def __init__(self, captcha=None, expires=None, file_list=None, request_header=None, url=None):
        r"""CaptureResultUrlVO

        The model defined in huaweicloud sdk

        :param captcha: 下载链接提取码，用于打开下载链接时使用。
        :type captcha: str
        :param expires: 下载链接过期时间
        :type expires: int
        :param file_list: 抓包文件列表，当环境不支持obs文件夹分享时使用。当此字段存在时，无captch，expires，url返回值。
        :type file_list: list[:class:`huaweicloudsdkcfw.v1.CaptureFile`]
        :param request_header: 
        :type request_header: :class:`huaweicloudsdkcfw.v1.HostHeaderInfo`
        :param url: 下载链接
        :type url: str
        """
        
        

        self._captcha = None
        self._expires = None
        self._file_list = None
        self._request_header = None
        self._url = None
        self.discriminator = None

        if captcha is not None:
            self.captcha = captcha
        if expires is not None:
            self.expires = expires
        if file_list is not None:
            self.file_list = file_list
        if request_header is not None:
            self.request_header = request_header
        if url is not None:
            self.url = url

    @property
    def captcha(self):
        r"""Gets the captcha of this CaptureResultUrlVO.

        下载链接提取码，用于打开下载链接时使用。

        :return: The captcha of this CaptureResultUrlVO.
        :rtype: str
        """
        return self._captcha

    @captcha.setter
    def captcha(self, captcha):
        r"""Sets the captcha of this CaptureResultUrlVO.

        下载链接提取码，用于打开下载链接时使用。

        :param captcha: The captcha of this CaptureResultUrlVO.
        :type captcha: str
        """
        self._captcha = captcha

    @property
    def expires(self):
        r"""Gets the expires of this CaptureResultUrlVO.

        下载链接过期时间

        :return: The expires of this CaptureResultUrlVO.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        r"""Sets the expires of this CaptureResultUrlVO.

        下载链接过期时间

        :param expires: The expires of this CaptureResultUrlVO.
        :type expires: int
        """
        self._expires = expires

    @property
    def file_list(self):
        r"""Gets the file_list of this CaptureResultUrlVO.

        抓包文件列表，当环境不支持obs文件夹分享时使用。当此字段存在时，无captch，expires，url返回值。

        :return: The file_list of this CaptureResultUrlVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.CaptureFile`]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        r"""Sets the file_list of this CaptureResultUrlVO.

        抓包文件列表，当环境不支持obs文件夹分享时使用。当此字段存在时，无captch，expires，url返回值。

        :param file_list: The file_list of this CaptureResultUrlVO.
        :type file_list: list[:class:`huaweicloudsdkcfw.v1.CaptureFile`]
        """
        self._file_list = file_list

    @property
    def request_header(self):
        r"""Gets the request_header of this CaptureResultUrlVO.

        :return: The request_header of this CaptureResultUrlVO.
        :rtype: :class:`huaweicloudsdkcfw.v1.HostHeaderInfo`
        """
        return self._request_header

    @request_header.setter
    def request_header(self, request_header):
        r"""Sets the request_header of this CaptureResultUrlVO.

        :param request_header: The request_header of this CaptureResultUrlVO.
        :type request_header: :class:`huaweicloudsdkcfw.v1.HostHeaderInfo`
        """
        self._request_header = request_header

    @property
    def url(self):
        r"""Gets the url of this CaptureResultUrlVO.

        下载链接

        :return: The url of this CaptureResultUrlVO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CaptureResultUrlVO.

        下载链接

        :param url: The url of this CaptureResultUrlVO.
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
        if not isinstance(other, CaptureResultUrlVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
