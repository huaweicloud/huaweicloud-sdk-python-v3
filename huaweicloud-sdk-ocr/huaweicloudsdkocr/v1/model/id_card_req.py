# coding: utf-8

import pprint
import re

import six





class IDCardReq:


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
        'side': 'str'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side'
    }

    def __init__(self, image=None, url=None, side=None):
        """IDCardReq - a model defined in huaweicloud sdk"""
        
        

        self._image = None
        self._url = None
        self._side = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if side is not None:
            self.side = side

    @property
    def image(self):
        """Gets the image of this IDCardReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this IDCardReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IDCardReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this IDCardReq.
        :type: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this IDCardReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。    

        :return: The url of this IDCardReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IDCardReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。    

        :param url: The url of this IDCardReq.
        :type: str
        """
        self._url = url

    @property
    def side(self):
        """Gets the side of this IDCardReq.

         - front：身份证正面。  - back：身份证背面。  > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :return: The side of this IDCardReq.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this IDCardReq.

         - front：身份证正面。  - back：身份证背面。  > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :param side: The side of this IDCardReq.
        :type: str
        """
        self._side = side

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
        if not isinstance(other, IDCardReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
