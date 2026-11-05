# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PresignUploadUrlBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'images': 'list[ImageUploadItem]'
    }

    attribute_map = {
        'images': 'images'
    }

    def __init__(self, images=None):
        r"""PresignUploadUrlBody

        The model defined in huaweicloud sdk

        :param images: 待获取预签名上传地址的图片列表
        :type images: list[:class:`huaweicloudsdkwaf.v1.ImageUploadItem`]
        """
        
        

        self._images = None
        self.discriminator = None

        self.images = images

    @property
    def images(self):
        r"""Gets the images of this PresignUploadUrlBody.

        待获取预签名上传地址的图片列表

        :return: The images of this PresignUploadUrlBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ImageUploadItem`]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this PresignUploadUrlBody.

        待获取预签名上传地址的图片列表

        :param images: The images of this PresignUploadUrlBody.
        :type images: list[:class:`huaweicloudsdkwaf.v1.ImageUploadItem`]
        """
        self._images = images

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PresignUploadUrlBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
