# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignCombineBodyBackgroundattrs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backgroundtype': 'str',
        'color': 'str',
        'image': 'str',
        'url': 'str'
    }

    attribute_map = {
        'backgroundtype': 'backgroundtype',
        'color': 'color',
        'image': 'image',
        'url': 'url'
    }

    def __init__(self, backgroundtype=None, color=None, image=None, url=None):
        """ImageWisedesignCombineBodyBackgroundattrs

        The model defined in huaweicloud sdk

        :param backgroundtype: 背景类型：color-颜色，image-背景图，transparent-透明，默认为transparent-透明
        :type backgroundtype: str
        :param color: RGB值 如#FFFFFF为白色
        :type color: str
        :param image: 背景内容，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  &gt; - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 &gt; - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 &gt; - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。
        :type url: str
        """
        
        

        self._backgroundtype = None
        self._color = None
        self._image = None
        self._url = None
        self.discriminator = None

        if backgroundtype is not None:
            self.backgroundtype = backgroundtype
        if color is not None:
            self.color = color
        if image is not None:
            self.image = image
        if url is not None:
            self.url = url

    @property
    def backgroundtype(self):
        """Gets the backgroundtype of this ImageWisedesignCombineBodyBackgroundattrs.

        背景类型：color-颜色，image-背景图，transparent-透明，默认为transparent-透明

        :return: The backgroundtype of this ImageWisedesignCombineBodyBackgroundattrs.
        :rtype: str
        """
        return self._backgroundtype

    @backgroundtype.setter
    def backgroundtype(self, backgroundtype):
        """Sets the backgroundtype of this ImageWisedesignCombineBodyBackgroundattrs.

        背景类型：color-颜色，image-背景图，transparent-透明，默认为transparent-透明

        :param backgroundtype: The backgroundtype of this ImageWisedesignCombineBodyBackgroundattrs.
        :type backgroundtype: str
        """
        self._backgroundtype = backgroundtype

    @property
    def color(self):
        """Gets the color of this ImageWisedesignCombineBodyBackgroundattrs.

        RGB值 如#FFFFFF为白色

        :return: The color of this ImageWisedesignCombineBodyBackgroundattrs.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ImageWisedesignCombineBodyBackgroundattrs.

        RGB值 如#FFFFFF为白色

        :param color: The color of this ImageWisedesignCombineBodyBackgroundattrs.
        :type color: str
        """
        self._color = color

    @property
    def image(self):
        """Gets the image of this ImageWisedesignCombineBodyBackgroundattrs.

        背景内容，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式

        :return: The image of this ImageWisedesignCombineBodyBackgroundattrs.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageWisedesignCombineBodyBackgroundattrs.

        背景内容，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式

        :param image: The image of this ImageWisedesignCombineBodyBackgroundattrs.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this ImageWisedesignCombineBodyBackgroundattrs.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。

        :return: The url of this ImageWisedesignCombineBodyBackgroundattrs.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageWisedesignCombineBodyBackgroundattrs.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。

        :param url: The url of this ImageWisedesignCombineBodyBackgroundattrs.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ImageWisedesignCombineBodyBackgroundattrs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
