# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceDetectUrlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_url': 'str',
        'attributes': 'str'
    }

    attribute_map = {
        'image_url': 'image_url',
        'attributes': 'attributes'
    }

    def __init__(self, image_url=None, attributes=None):
        """FaceDetectUrlReq

        The model defined in huaweicloud sdk

        :param image_url: [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。](tag:hk)
        :type image_url: str
        :param attributes: 是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转
        :type attributes: str
        """
        
        

        self._image_url = None
        self._attributes = None
        self.discriminator = None

        self.image_url = image_url
        if attributes is not None:
            self.attributes = attributes

    @property
    def image_url(self):
        """Gets the image_url of this FaceDetectUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。](tag:hk)

        :return: The image_url of this FaceDetectUrlReq.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this FaceDetectUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。](tag:hk)

        :param image_url: The image_url of this FaceDetectUrlReq.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def attributes(self):
        """Gets the attributes of this FaceDetectUrlReq.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :return: The attributes of this FaceDetectUrlReq.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FaceDetectUrlReq.

        是否返回人脸属性，希望获取的属性列表，多个属性间使用逗号（,）隔开。目前支持的属性有：   • 2：年龄   • 4：装束（帽子、眼镜）   • 6：口罩   • 7：发型   • 8：胡须   • 11：图片类型   • 12：质量   • 13：表情   • 21：人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转

        :param attributes: The attributes of this FaceDetectUrlReq.
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
        if not isinstance(other, FaceDetectUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
