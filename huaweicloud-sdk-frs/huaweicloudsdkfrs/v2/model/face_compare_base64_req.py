# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceCompareBase64Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image2_base64': 'str',
        'image1_base64': 'str'
    }

    attribute_map = {
        'image2_base64': 'image2_base64',
        'image1_base64': 'image1_base64'
    }

    def __init__(self, image2_base64=None, image1_base64=None):
        """FaceCompareBase64Req

        The model defined in huaweicloud sdk

        :param image2_base64: 图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。
        :type image2_base64: str
        :param image1_base64: 图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。
        :type image1_base64: str
        """
        
        

        self._image2_base64 = None
        self._image1_base64 = None
        self.discriminator = None

        self.image2_base64 = image2_base64
        self.image1_base64 = image1_base64

    @property
    def image2_base64(self):
        """Gets the image2_base64 of this FaceCompareBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :return: The image2_base64 of this FaceCompareBase64Req.
        :rtype: str
        """
        return self._image2_base64

    @image2_base64.setter
    def image2_base64(self, image2_base64):
        """Sets the image2_base64 of this FaceCompareBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :param image2_base64: The image2_base64 of this FaceCompareBase64Req.
        :type image2_base64: str
        """
        self._image2_base64 = image2_base64

    @property
    def image1_base64(self):
        """Gets the image1_base64 of this FaceCompareBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :return: The image1_base64 of this FaceCompareBase64Req.
        :rtype: str
        """
        return self._image1_base64

    @image1_base64.setter
    def image1_base64(self, image1_base64):
        """Sets the image1_base64 of this FaceCompareBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :param image1_base64: The image1_base64 of this FaceCompareBase64Req.
        :type image1_base64: str
        """
        self._image1_base64 = image1_base64

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
        if not isinstance(other, FaceCompareBase64Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
