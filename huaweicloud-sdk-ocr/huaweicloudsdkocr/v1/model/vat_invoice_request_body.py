# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VatInvoiceRequestBody:

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
        'advanced_mode': 'bool',
        'return_text_location': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'advanced_mode': 'advanced_mode',
        'return_text_location': 'return_text_location'
    }

    def __init__(self, image=None, url=None, advanced_mode=None, return_text_location=None):
        """VatInvoiceRequestBody

        The model defined in huaweicloud sdk

        :param image: 该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式，多页PDF仅识别第一页。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  &gt; 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param advanced_mode: 默认为false，如果传参为true，则返回更多字段 
        :type advanced_mode: bool
        :param return_text_location: 识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_text_location: bool
        """
        
        

        self._image = None
        self._url = None
        self._advanced_mode = None
        self._return_text_location = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if advanced_mode is not None:
            self.advanced_mode = advanced_mode
        if return_text_location is not None:
            self.return_text_location = return_text_location

    @property
    def image(self):
        """Gets the image of this VatInvoiceRequestBody.

        该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式，多页PDF仅识别第一页。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this VatInvoiceRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VatInvoiceRequestBody.

        该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式，多页PDF仅识别第一页。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this VatInvoiceRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this VatInvoiceRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this VatInvoiceRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VatInvoiceRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this VatInvoiceRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def advanced_mode(self):
        """Gets the advanced_mode of this VatInvoiceRequestBody.

        默认为false，如果传参为true，则返回更多字段 

        :return: The advanced_mode of this VatInvoiceRequestBody.
        :rtype: bool
        """
        return self._advanced_mode

    @advanced_mode.setter
    def advanced_mode(self, advanced_mode):
        """Sets the advanced_mode of this VatInvoiceRequestBody.

        默认为false，如果传参为true，则返回更多字段 

        :param advanced_mode: The advanced_mode of this VatInvoiceRequestBody.
        :type advanced_mode: bool
        """
        self._advanced_mode = advanced_mode

    @property
    def return_text_location(self):
        """Gets the return_text_location of this VatInvoiceRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_text_location of this VatInvoiceRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this VatInvoiceRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_text_location: The return_text_location of this VatInvoiceRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

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
        if not isinstance(other, VatInvoiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
