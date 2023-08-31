# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectFaceByFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_file': 'file',
        'attributes': 'str'
    }

    attribute_map = {
        'image_file': 'image_file',
        'attributes': 'attributes'
    }

    def __init__(self, image_file=None, attributes=None):
        """DetectFaceByFileRequestBody

        The model defined in huaweicloud sdk

        :param image_file: 本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param attributes: 是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有： • 1：性别 • 2：年龄 • 4：装束（帽子、眼镜） • 6：口罩 • 7：发型 • 8：胡须 • 11：图片类型 • 12：质量 • 13：表情 • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转
        :type attributes: str
        """
        
        

        self._image_file = None
        self._attributes = None
        self.discriminator = None

        self.image_file = image_file
        if attributes is not None:
            self.attributes = attributes

    @property
    def image_file(self):
        """Gets the image_file of this DetectFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :return: The image_file of this DetectFaceByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this DetectFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :param image_file: The image_file of this DetectFaceByFileRequestBody.
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._image_file = image_file

    @property
    def attributes(self):
        """Gets the attributes of this DetectFaceByFileRequestBody.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有： • 1：性别 • 2：年龄 • 4：装束（帽子、眼镜） • 6：口罩 • 7：发型 • 8：胡须 • 11：图片类型 • 12：质量 • 13：表情 • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :return: The attributes of this DetectFaceByFileRequestBody.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DetectFaceByFileRequestBody.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有： • 1：性别 • 2：年龄 • 4：装束（帽子、眼镜） • 6：口罩 • 7：发型 • 8：胡须 • 11：图片类型 • 12：质量 • 13：表情 • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :param attributes: The attributes of this DetectFaceByFileRequestBody.
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
        if not isinstance(other, DetectFaceByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
