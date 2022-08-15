# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MacaoIdCardRequestBody:

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
        'side': 'str',
        'return_portrait_image': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side',
        'return_portrait_image': 'return_portrait_image'
    }

    def __init__(self, image=None, url=None, side=None, return_portrait_image=None):
        """MacaoIdCardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素。支持JPG/PNG/BMP/TIFF格式。 图片Base64编码示例 如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。
        :type image: str
        :param url: 与image二选一。  图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/en-us/api-ocr/ocr_03_0132.html)&gt;。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param side: front：身份证正面 back：身份证背面  如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 
        :type side: str
        :param return_portrait_image: 是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 
        :type return_portrait_image: bool
        """
        
        

        self._image = None
        self._url = None
        self._side = None
        self._return_portrait_image = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if side is not None:
            self.side = side
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image

    @property
    def image(self):
        """Gets the image of this MacaoIdCardRequestBody.

        与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素。支持JPG/PNG/BMP/TIFF格式。 图片Base64编码示例 如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。

        :return: The image of this MacaoIdCardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MacaoIdCardRequestBody.

        与url二选一。 图像数据，base64编码，要求base64编码后大小不超过10M。图片最小边不小于15像素，最长边不超过8192像素。支持JPG/PNG/BMP/TIFF格式。 图片Base64编码示例 如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。

        :param image: The image of this MacaoIdCardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this MacaoIdCardRequestBody.

        与image二选一。  图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/en-us/api-ocr/ocr_03_0132.html)>。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this MacaoIdCardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MacaoIdCardRequestBody.

        与image二选一。  图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/en-us/api-ocr/ocr_03_0132.html)>。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this MacaoIdCardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def side(self):
        """Gets the side of this MacaoIdCardRequestBody.

        front：身份证正面 back：身份证背面  如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :return: The side of this MacaoIdCardRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this MacaoIdCardRequestBody.

        front：身份证正面 back：身份证背面  如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :param side: The side of this MacaoIdCardRequestBody.
        :type side: str
        """
        self._side = side

    @property
    def return_portrait_image(self):
        """Gets the return_portrait_image of this MacaoIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 

        :return: The return_portrait_image of this MacaoIdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        """Sets the return_portrait_image of this MacaoIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 

        :param return_portrait_image: The return_portrait_image of this MacaoIdCardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

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
        if not isinstance(other, MacaoIdCardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
