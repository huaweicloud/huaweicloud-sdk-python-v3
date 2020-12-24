# coding: utf-8

import pprint
import re

import six





class RecognizePassportRequestBody:


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
        'image': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'url': 'url',
        'image': 'image',
        'country_code': 'country_code'
    }

    def __init__(self, url=None, image=None, country_code=None):
        """RecognizePassportRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._image = None
        self._country_code = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if image is not None:
            self.image = image
        if country_code is not None:
            self.country_code = country_code

    @property
    def url(self):
        """Gets the url of this RecognizePassportRequestBody.

        图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The url of this RecognizePassportRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecognizePassportRequestBody.

        图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param url: The url of this RecognizePassportRequestBody.
        :type: str
        """
        self._url = url

    @property
    def image(self):
        """Gets the image of this RecognizePassportRequestBody.

        图片文件Base64编码字符串。要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过4096像素。  支持JPEG/JPG/PNG/BMP/TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。 

        :return: The image of this RecognizePassportRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this RecognizePassportRequestBody.

        图片文件Base64编码字符串。要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过4096像素。  支持JPEG/JPG/PNG/BMP/TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。 

        :param image: The image of this RecognizePassportRequestBody.
        :type: str
        """
        self._image = image

    @property
    def country_code(self):
        """Gets the country_code of this RecognizePassportRequestBody.

        输入值为护照颁发国的国家码，根据国家码选择对应的护照识别服务。  - 若输入中未选此字段，服务会根据自己识别判断的护照类型匹配相应的护照识别服务。  - 若选择值为GENERAL，则选择护照机器码识别。  - 若选择值为CHN，则选择中国护照全字段识别。 

        :return: The country_code of this RecognizePassportRequestBody.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RecognizePassportRequestBody.

        输入值为护照颁发国的国家码，根据国家码选择对应的护照识别服务。  - 若输入中未选此字段，服务会根据自己识别判断的护照类型匹配相应的护照识别服务。  - 若选择值为GENERAL，则选择护照机器码识别。  - 若选择值为CHN，则选择中国护照全字段识别。 

        :param country_code: The country_code of this RecognizePassportRequestBody.
        :type: str
        """
        self._country_code = country_code

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizePassportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
