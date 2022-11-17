# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceDetectBase64Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_base64': 'str',
        'attributes': 'str'
    }

    attribute_map = {
        'image_base64': 'image_base64',
        'attributes': 'attributes'
    }

    def __init__(self, image_base64=None, attributes=None):
        """FaceDetectBase64Req

        The model defined in huaweicloud sdk

        :param image_base64: 图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。
        :type image_base64: str
        :param attributes: 是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转
        :type attributes: str
        """
        
        

        self._image_base64 = None
        self._attributes = None
        self.discriminator = None

        self.image_base64 = image_base64
        if attributes is not None:
            self.attributes = attributes

    @property
    def image_base64(self):
        """Gets the image_base64 of this FaceDetectBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :return: The image_base64 of this FaceDetectBase64Req.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this FaceDetectBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于1MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :param image_base64: The image_base64 of this FaceDetectBase64Req.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def attributes(self):
        """Gets the attributes of this FaceDetectBase64Req.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :return: The attributes of this FaceDetectBase64Req.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FaceDetectBase64Req.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :param attributes: The attributes of this FaceDetectBase64Req.
        :type attributes: str
        """
        self._attributes = attributes

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
        if not isinstance(other, FaceDetectBase64Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
