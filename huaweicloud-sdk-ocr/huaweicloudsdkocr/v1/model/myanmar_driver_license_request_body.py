# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarDriverLicenseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'convert_unicode': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'convert_unicode': 'convert_unicode'
    }

    def __init__(self, image=None, url=None, convert_unicode=None):
        """MyanmarDriverLicenseRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param convert_unicode: - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 
        :type convert_unicode: bool
        """
        
        

        self._image = None
        self._url = None
        self._convert_unicode = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if convert_unicode is not None:
            self.convert_unicode = convert_unicode

    @property
    def image(self):
        """Gets the image of this MyanmarDriverLicenseRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :return: The image of this MyanmarDriverLicenseRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MyanmarDriverLicenseRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :param image: The image of this MyanmarDriverLicenseRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this MyanmarDriverLicenseRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this MyanmarDriverLicenseRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MyanmarDriverLicenseRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this MyanmarDriverLicenseRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def convert_unicode(self):
        """Gets the convert_unicode of this MyanmarDriverLicenseRequestBody.

        - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 

        :return: The convert_unicode of this MyanmarDriverLicenseRequestBody.
        :rtype: bool
        """
        return self._convert_unicode

    @convert_unicode.setter
    def convert_unicode(self, convert_unicode):
        """Sets the convert_unicode of this MyanmarDriverLicenseRequestBody.

        - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 

        :param convert_unicode: The convert_unicode of this MyanmarDriverLicenseRequestBody.
        :type convert_unicode: bool
        """
        self._convert_unicode = convert_unicode

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
        if not isinstance(other, MyanmarDriverLicenseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
