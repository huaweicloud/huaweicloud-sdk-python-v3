# coding: utf-8

import pprint
import re

import six





class HandwritingReq:


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
        'quick_mode': 'bool',
        'char_set': 'str',
        'detect_direction': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'quick_mode': 'quick_mode',
        'char_set': 'char_set',
        'detect_direction': 'detect_direction'
    }

    def __init__(self, image=None, url=None, quick_mode=None, char_set=None, detect_direction=None):
        """HandwritingReq - a model defined in huaweicloud sdk"""
        
        

        self._image = None
        self._url = None
        self._quick_mode = None
        self._char_set = None
        self._detect_direction = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if quick_mode is not None:
            self.quick_mode = quick_mode
        if char_set is not None:
            self.char_set = char_set
        if detect_direction is not None:
            self.detect_direction = detect_direction

    @property
    def image(self):
        """Gets the image of this HandwritingReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this HandwritingReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this HandwritingReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this HandwritingReq.
        :type: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this HandwritingReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。           

        :return: The url of this HandwritingReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HandwritingReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。           

        :param url: The url of this HandwritingReq.
        :type: str
        """
        self._url = url

    @property
    def quick_mode(self):
        """Gets the quick_mode of this HandwritingReq.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别内容。可选值包括：  - true：打开快速模式；  - false：关闭快速模式。  > 说明：  - 未传入该参数时默认为false，即关闭快速模式 

        :return: The quick_mode of this HandwritingReq.
        :rtype: bool
        """
        return self._quick_mode

    @quick_mode.setter
    def quick_mode(self, quick_mode):
        """Sets the quick_mode of this HandwritingReq.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别内容。可选值包括：  - true：打开快速模式；  - false：关闭快速模式。  > 说明：  - 未传入该参数时默认为false，即关闭快速模式 

        :param quick_mode: The quick_mode of this HandwritingReq.
        :type: bool
        """
        self._quick_mode = quick_mode

    @property
    def char_set(self):
        """Gets the char_set of this HandwritingReq.

        字符集设置，用户可以根据实际需要限定输出字符集范围。可选值如下所示。  - \"digit\": 数字模式；  - \"letter\": 大小写字母模式；  - \"digit_letter\": 数字+字母模式；  - \"general\": 数字+字母+中文模式；  > 说明：  - 未传入该参数时，默认为“general”模式。 

        :return: The char_set of this HandwritingReq.
        :rtype: str
        """
        return self._char_set

    @char_set.setter
    def char_set(self, char_set):
        """Sets the char_set of this HandwritingReq.

        字符集设置，用户可以根据实际需要限定输出字符集范围。可选值如下所示。  - \"digit\": 数字模式；  - \"letter\": 大小写字母模式；  - \"digit_letter\": 数字+字母模式；  - \"general\": 数字+字母+中文模式；  > 说明：  - 未传入该参数时，默认为“general”模式。 

        :param char_set: The char_set of this HandwritingReq.
        :type: str
        """
        self._char_set = char_set

    @property
    def detect_direction(self):
        """Gets the detect_direction of this HandwritingReq.

        校正图片的倾斜角度开关，可选值如下所示。  - true：校正图片的倾斜角度；  - false：不校正图片的倾斜角度。  > 说明：  - 支持任意角度的校正，未传入该参数时默认为“false”。 

        :return: The detect_direction of this HandwritingReq.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        """Sets the detect_direction of this HandwritingReq.

        校正图片的倾斜角度开关，可选值如下所示。  - true：校正图片的倾斜角度；  - false：不校正图片的倾斜角度。  > 说明：  - 支持任意角度的校正，未传入该参数时默认为“false”。 

        :param detect_direction: The detect_direction of this HandwritingReq.
        :type: bool
        """
        self._detect_direction = detect_direction

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
        if not isinstance(other, HandwritingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
