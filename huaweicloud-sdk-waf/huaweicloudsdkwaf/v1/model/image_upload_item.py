# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageUploadItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_size': 'int',
        'upload_content_type': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_size': 'image_size',
        'upload_content_type': 'upload_content_type'
    }

    def __init__(self, image_name=None, image_size=None, upload_content_type=None):
        r"""ImageUploadItem

        The model defined in huaweicloud sdk

        :param image_name: 图片名称（后缀必须为jpg/jpeg/png/bmp）
        :type image_name: str
        :param image_size: 图片大小（字节，不超过max_image_size默认5MB）
        :type image_size: int
        :param upload_content_type: 上传内容类型（作为Content-Type请求头纳入OBS预签名，客户端PUT上传时须用相同值）
        :type upload_content_type: str
        """
        
        

        self._image_name = None
        self._image_size = None
        self._upload_content_type = None
        self.discriminator = None

        self.image_name = image_name
        self.image_size = image_size
        self.upload_content_type = upload_content_type

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageUploadItem.

        图片名称（后缀必须为jpg/jpeg/png/bmp）

        :return: The image_name of this ImageUploadItem.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageUploadItem.

        图片名称（后缀必须为jpg/jpeg/png/bmp）

        :param image_name: The image_name of this ImageUploadItem.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_size(self):
        r"""Gets the image_size of this ImageUploadItem.

        图片大小（字节，不超过max_image_size默认5MB）

        :return: The image_size of this ImageUploadItem.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ImageUploadItem.

        图片大小（字节，不超过max_image_size默认5MB）

        :param image_size: The image_size of this ImageUploadItem.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def upload_content_type(self):
        r"""Gets the upload_content_type of this ImageUploadItem.

        上传内容类型（作为Content-Type请求头纳入OBS预签名，客户端PUT上传时须用相同值）

        :return: The upload_content_type of this ImageUploadItem.
        :rtype: str
        """
        return self._upload_content_type

    @upload_content_type.setter
    def upload_content_type(self, upload_content_type):
        r"""Sets the upload_content_type of this ImageUploadItem.

        上传内容类型（作为Content-Type请求头纳入OBS预签名，客户端PUT上传时须用相同值）

        :param upload_content_type: The upload_content_type of this ImageUploadItem.
        :type upload_content_type: str
        """
        self._upload_content_type = upload_content_type

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
        if not isinstance(other, ImageUploadItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
