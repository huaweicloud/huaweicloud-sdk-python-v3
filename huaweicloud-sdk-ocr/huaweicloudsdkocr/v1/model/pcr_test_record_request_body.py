# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PcrTestRecordRequestBody:

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
        'detect_direction': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'detect_direction': 'detect_direction'
    }

    def __init__(self, image=None, url=None, detect_direction=None):
        """PcrTestRecordRequestBody

        The model defined in huaweicloud sdk

        :param image: 图像数据，base64编码，图片尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF格式。
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。 
        :type url: str
        :param detect_direction: 校正图片的倾斜角度开关，可选值如下所示：  - true：校正图片的倾斜角度  - false：不校正图片的倾斜角度  支持任意角度的校正，未传入该参数时默认为“false”。 
        :type detect_direction: bool
        """
        
        

        self._image = None
        self._url = None
        self._detect_direction = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if detect_direction is not None:
            self.detect_direction = detect_direction

    @property
    def image(self):
        """Gets the image of this PcrTestRecordRequestBody.

        图像数据，base64编码，图片尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF格式。

        :return: The image of this PcrTestRecordRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PcrTestRecordRequestBody.

        图像数据，base64编码，图片尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF格式。

        :param image: The image of this PcrTestRecordRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this PcrTestRecordRequestBody.

        与image二选一  图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。 

        :return: The url of this PcrTestRecordRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PcrTestRecordRequestBody.

        与image二选一  图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。 

        :param url: The url of this PcrTestRecordRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def detect_direction(self):
        """Gets the detect_direction of this PcrTestRecordRequestBody.

        校正图片的倾斜角度开关，可选值如下所示：  - true：校正图片的倾斜角度  - false：不校正图片的倾斜角度  支持任意角度的校正，未传入该参数时默认为“false”。 

        :return: The detect_direction of this PcrTestRecordRequestBody.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        """Sets the detect_direction of this PcrTestRecordRequestBody.

        校正图片的倾斜角度开关，可选值如下所示：  - true：校正图片的倾斜角度  - false：不校正图片的倾斜角度  支持任意角度的校正，未传入该参数时默认为“false”。 

        :param detect_direction: The detect_direction of this PcrTestRecordRequestBody.
        :type detect_direction: bool
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
        if not isinstance(other, PcrTestRecordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
