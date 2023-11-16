# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeruIdCardRequestBody:

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
        'return_portrait_image': 'bool',
        'return_portrait_location': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_portrait_image': 'return_portrait_image',
        'return_portrait_location': 'return_portrait_location'
    }

    def __init__(self, image=None, url=None, return_portrait_image=None, return_portrait_location=None):
        """PeruIdCardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式，支持识别多页PDF数据。
        :type image: str
        :param url: 与image二选一。 图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。
        :type url: str
        :param return_portrait_image: 是否返回头像内容开关，可选值如下所示：  - true: 返回身份证头像照片的 base64 编码。 - false:  返回为空值。 未传入该参数时默认为“false”，即返回为空值。 
        :type return_portrait_image: bool
        :param return_portrait_location: 是否返回头像坐标的开关，可选值如下所示：  - true: 返回身份证头像的位置坐标。 - false: 返回为空值 未传入该参数时默认为“false”，即返回为空。 
        :type return_portrait_location: bool
        """
        
        

        self._image = None
        self._url = None
        self._return_portrait_image = None
        self._return_portrait_location = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image
        if return_portrait_location is not None:
            self.return_portrait_location = return_portrait_location

    @property
    def image(self):
        """Gets the image of this PeruIdCardRequestBody.

        与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式，支持识别多页PDF数据。

        :return: The image of this PeruIdCardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PeruIdCardRequestBody.

        与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式，支持识别多页PDF数据。

        :param image: The image of this PeruIdCardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this PeruIdCardRequestBody.

        与image二选一。 图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。

        :return: The url of this PeruIdCardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PeruIdCardRequestBody.

        与image二选一。 图片的URL路径，目前仅支持华为云上OBS提供的匿名公开授权访问的URL以及公网URL。

        :param url: The url of this PeruIdCardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_portrait_image(self):
        """Gets the return_portrait_image of this PeruIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示：  - true: 返回身份证头像照片的 base64 编码。 - false:  返回为空值。 未传入该参数时默认为“false”，即返回为空值。 

        :return: The return_portrait_image of this PeruIdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        """Sets the return_portrait_image of this PeruIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示：  - true: 返回身份证头像照片的 base64 编码。 - false:  返回为空值。 未传入该参数时默认为“false”，即返回为空值。 

        :param return_portrait_image: The return_portrait_image of this PeruIdCardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

    @property
    def return_portrait_location(self):
        """Gets the return_portrait_location of this PeruIdCardRequestBody.

        是否返回头像坐标的开关，可选值如下所示：  - true: 返回身份证头像的位置坐标。 - false: 返回为空值 未传入该参数时默认为“false”，即返回为空。 

        :return: The return_portrait_location of this PeruIdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_location

    @return_portrait_location.setter
    def return_portrait_location(self, return_portrait_location):
        """Sets the return_portrait_location of this PeruIdCardRequestBody.

        是否返回头像坐标的开关，可选值如下所示：  - true: 返回身份证头像的位置坐标。 - false: 返回为空值 未传入该参数时默认为“false”，即返回为空。 

        :param return_portrait_location: The return_portrait_location of this PeruIdCardRequestBody.
        :type return_portrait_location: bool
        """
        self._return_portrait_location = return_portrait_location

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
        if not isinstance(other, PeruIdCardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
