# coding: utf-8

import pprint
import re

import six





class WebImageReq:


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
        'detect_direction': 'bool',
        'extract_type': 'list[str]'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'detect_direction': 'detect_direction',
        'extract_type': 'extract_type'
    }

    def __init__(self, image=None, url=None, detect_direction=None, extract_type=None):
        """WebImageReq - a model defined in huaweicloud sdk"""
        
        

        self._image = None
        self._url = None
        self._detect_direction = None
        self._extract_type = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if detect_direction is not None:
            self.detect_direction = detect_direction
        if extract_type is not None:
            self.extract_type = extract_type

    @property
    def image(self):
        """Gets the image of this WebImageReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。 

        :return: The image of this WebImageReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this WebImageReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M。  图片最小边不小于15像素，最长边不超过8192像素。  支持JPEG/JPG/PNG/BMP/TIFF/GIF/WEBP格式  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。 

        :param image: The image of this WebImageReq.
        :type: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this WebImageReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。 

        :return: The url of this WebImageReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebImageReq.

        与image二选一  图片的URL路径，目前仅支持华为云OBS提供的匿名公开授权访问的URL以及公网URL。 

        :param url: The url of this WebImageReq.
        :type: str
        """
        self._url = url

    @property
    def detect_direction(self):
        """Gets the detect_direction of this WebImageReq.

        图片朝向检测开关，可选值包括：  - true：检测图片朝向;  - false：不检测图片朝向。  > 说明：  - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :return: The detect_direction of this WebImageReq.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        """Sets the detect_direction of this WebImageReq.

        图片朝向检测开关，可选值包括：  - true：检测图片朝向;  - false：不检测图片朝向。  > 说明：  - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :param detect_direction: The detect_direction of this WebImageReq.
        :type: bool
        """
        self._detect_direction = detect_direction

    @property
    def extract_type(self):
        """Gets the extract_type of this WebImageReq.

        结构化数据提取参数列表，目前只支持联系人信息、图像宽高，其入参值分别为\"contact_info\"，\"image_size\"，若该字段为空列表或缺失该字段，默认不提取。 

        :return: The extract_type of this WebImageReq.
        :rtype: list[str]
        """
        return self._extract_type

    @extract_type.setter
    def extract_type(self, extract_type):
        """Sets the extract_type of this WebImageReq.

        结构化数据提取参数列表，目前只支持联系人信息、图像宽高，其入参值分别为\"contact_info\"，\"image_size\"，若该字段为空列表或缺失该字段，默认不提取。 

        :param extract_type: The extract_type of this WebImageReq.
        :type: list[str]
        """
        self._extract_type = extract_type

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
        if not isinstance(other, WebImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
