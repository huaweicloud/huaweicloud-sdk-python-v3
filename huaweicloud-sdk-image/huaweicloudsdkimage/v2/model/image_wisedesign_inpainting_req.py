# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignInpaintingReq:

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
        'image_url': 'str',
        'polygon_coord': 'list[list[list[int]]]'
    }

    attribute_map = {
        'image_base64': 'image_base64',
        'image_url': 'image_url',
        'polygon_coord': 'polygon_coord'
    }

    def __init__(self, image_base64=None, image_url=None, polygon_coord=None):
        """ImageWisedesignInpaintingReq

        The model defined in huaweicloud sdk

        :param image_base64: 图像数据，base64编码，要求base64编码最长边最大4000px，支持JPG/PNG/BMP/JPEG格式
        :type image_base64: str
        :param image_url: 与image_base64二选一  图片的URL路径，目前支持：   - &gt;-   公网HTTP/HTTPS URL   - &gt;-   华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。   &gt; - &gt;-   接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  &gt; - &gt;-   请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。  &gt; - &gt;-   lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 
        :type image_url: str
        :param polygon_coord: 指定的多个待修复区域信息，每个待修复区域的类型为list[list[list[int,int]]]，待修复区域至少由3个顺时针的坐标构成。若该参数为空，则会自动识别图像中的文字部分进行修复。默认为空
        :type polygon_coord: list[list[list[int]]]
        """
        
        

        self._image_base64 = None
        self._image_url = None
        self._polygon_coord = None
        self.discriminator = None

        if image_base64 is not None:
            self.image_base64 = image_base64
        if image_url is not None:
            self.image_url = image_url
        if polygon_coord is not None:
            self.polygon_coord = polygon_coord

    @property
    def image_base64(self):
        """Gets the image_base64 of this ImageWisedesignInpaintingReq.

        图像数据，base64编码，要求base64编码最长边最大4000px，支持JPG/PNG/BMP/JPEG格式

        :return: The image_base64 of this ImageWisedesignInpaintingReq.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this ImageWisedesignInpaintingReq.

        图像数据，base64编码，要求base64编码最长边最大4000px，支持JPG/PNG/BMP/JPEG格式

        :param image_base64: The image_base64 of this ImageWisedesignInpaintingReq.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def image_url(self):
        """Gets the image_url of this ImageWisedesignInpaintingReq.

        与image_base64二选一  图片的URL路径，目前支持：   - >-   公网HTTP/HTTPS URL   - >-   华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。   > - >-   接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  > - >-   请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。  > - >-   lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 

        :return: The image_url of this ImageWisedesignInpaintingReq.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ImageWisedesignInpaintingReq.

        与image_base64二选一  图片的URL路径，目前支持：   - >-   公网HTTP/HTTPS URL   - >-   华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。   > - >-   接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  > - >-   请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。  > - >-   lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 

        :param image_url: The image_url of this ImageWisedesignInpaintingReq.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def polygon_coord(self):
        """Gets the polygon_coord of this ImageWisedesignInpaintingReq.

        指定的多个待修复区域信息，每个待修复区域的类型为list[list[list[int,int]]]，待修复区域至少由3个顺时针的坐标构成。若该参数为空，则会自动识别图像中的文字部分进行修复。默认为空

        :return: The polygon_coord of this ImageWisedesignInpaintingReq.
        :rtype: list[list[list[int]]]
        """
        return self._polygon_coord

    @polygon_coord.setter
    def polygon_coord(self, polygon_coord):
        """Sets the polygon_coord of this ImageWisedesignInpaintingReq.

        指定的多个待修复区域信息，每个待修复区域的类型为list[list[list[int,int]]]，待修复区域至少由3个顺时针的坐标构成。若该参数为空，则会自动识别图像中的文字部分进行修复。默认为空

        :param polygon_coord: The polygon_coord of this ImageWisedesignInpaintingReq.
        :type polygon_coord: list[list[list[int]]]
        """
        self._polygon_coord = polygon_coord

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
        if not isinstance(other, ImageWisedesignInpaintingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
