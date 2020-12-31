# coding: utf-8

import pprint
import re

import six





class RecognizeDriverLicenseRequestBody:


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
        'side': 'str',
        'return_issuing_authority': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'image': 'image',
        'side': 'side',
        'return_issuing_authority': 'return_issuing_authority'
    }

    def __init__(self, url=None, image=None, side=None, return_issuing_authority=None):
        """RecognizeDriverLicenseRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._image = None
        self._side = None
        self._return_issuing_authority = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if image is not None:
            self.image = image
        if side is not None:
            self.side = side
        if return_issuing_authority is not None:
            self.return_issuing_authority = return_issuing_authority

    @property
    def url(self):
        """Gets the url of this RecognizeDriverLicenseRequestBody.

        图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The url of this RecognizeDriverLicenseRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecognizeDriverLicenseRequestBody.

        图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见配置OBS访问权限。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param url: The url of this RecognizeDriverLicenseRequestBody.
        :type: str
        """
        self._url = url

    @property
    def image(self):
        """Gets the image of this RecognizeDriverLicenseRequestBody.

        图像数据, Base64编码字符串。要求base64编码后大小不超过10M。  图片最小边不小于100像素，最长边不超过8000像素。  支持JPEG/JPG/PNG/BMP/TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this RecognizeDriverLicenseRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this RecognizeDriverLicenseRequestBody.

        图像数据, Base64编码字符串。要求base64编码后大小不超过10M。  图片最小边不小于100像素，最长边不超过8000像素。  支持JPEG/JPG/PNG/BMP/TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this RecognizeDriverLicenseRequestBody.
        :type: str
        """
        self._image = image

    @property
    def side(self):
        """Gets the side of this RecognizeDriverLicenseRequestBody.

        检测场景:  - front：驾驶证主页。  - back：驾驶证副页。  > 说明：如果参数值为空或无该参数，系统默认识别主页，建议填写，准确率更高。 

        :return: The side of this RecognizeDriverLicenseRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this RecognizeDriverLicenseRequestBody.

        检测场景:  - front：驾驶证主页。  - back：驾驶证副页。  > 说明：如果参数值为空或无该参数，系统默认识别主页，建议填写，准确率更高。 

        :param side: The side of this RecognizeDriverLicenseRequestBody.
        :type: str
        """
        self._side = side

    @property
    def return_issuing_authority(self):
        """Gets the return_issuing_authority of this RecognizeDriverLicenseRequestBody.

        是否返回发证机关的开关，可选值包括：  true：返回发证机关  false：不返回发证机关  如果无该参数，系统默认不返回发证机关。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_issuing_authority of this RecognizeDriverLicenseRequestBody.
        :rtype: bool
        """
        return self._return_issuing_authority

    @return_issuing_authority.setter
    def return_issuing_authority(self, return_issuing_authority):
        """Sets the return_issuing_authority of this RecognizeDriverLicenseRequestBody.

        是否返回发证机关的开关，可选值包括：  true：返回发证机关  false：不返回发证机关  如果无该参数，系统默认不返回发证机关。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_issuing_authority: The return_issuing_authority of this RecognizeDriverLicenseRequestBody.
        :type: bool
        """
        self._return_issuing_authority = return_issuing_authority

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
        if not isinstance(other, RecognizeDriverLicenseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
