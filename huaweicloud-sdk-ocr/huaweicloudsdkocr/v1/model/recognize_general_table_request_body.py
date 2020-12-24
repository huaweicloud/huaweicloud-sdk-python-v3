# coding: utf-8

import pprint
import re

import six





class RecognizeGeneralTableRequestBody:


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
        'return_confidence': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'image': 'image',
        'return_confidence': 'return_confidence'
    }

    def __init__(self, url=None, image=None, return_confidence=None):
        """RecognizeGeneralTableRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._image = None
        self._return_confidence = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if image is not None:
            self.image = image
        if return_confidence is not None:
            self.return_confidence = return_confidence

    @property
    def url(self):
        """Gets the url of this RecognizeGeneralTableRequestBody.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。 > 说明： - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The url of this RecognizeGeneralTableRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecognizeGeneralTableRequestBody.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。 > 说明： - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param url: The url of this RecognizeGeneralTableRequestBody.
        :type: str
        """
        self._url = url

    @property
    def image(self):
        """Gets the image of this RecognizeGeneralTableRequestBody.

        图片文件Base64编码字符串。要求base64编码后大小不超过10M。 图片最小边不小于15像素，最长边不超过4096像素。 支持JPEG/JPG/PNG/BMP/TIFF格式。 图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式 

        :return: The image of this RecognizeGeneralTableRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this RecognizeGeneralTableRequestBody.

        图片文件Base64编码字符串。要求base64编码后大小不超过10M。 图片最小边不小于15像素，最长边不超过4096像素。 支持JPEG/JPG/PNG/BMP/TIFF格式。 图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式 

        :param image: The image of this RecognizeGeneralTableRequestBody.
        :type: str
        """
        self._image = image

    @property
    def return_confidence(self):
        """Gets the return_confidence of this RecognizeGeneralTableRequestBody.

        是否返回置信度的开关，可选值包括： - true：返回置信度; - false：不返回置信度。 > 说明： - 如果无该参数，系统默认不返回置信度。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_confidence of this RecognizeGeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_confidence

    @return_confidence.setter
    def return_confidence(self, return_confidence):
        """Sets the return_confidence of this RecognizeGeneralTableRequestBody.

        是否返回置信度的开关，可选值包括： - true：返回置信度; - false：不返回置信度。 > 说明： - 如果无该参数，系统默认不返回置信度。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_confidence: The return_confidence of this RecognizeGeneralTableRequestBody.
        :type: bool
        """
        self._return_confidence = return_confidence

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
        if not isinstance(other, RecognizeGeneralTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
