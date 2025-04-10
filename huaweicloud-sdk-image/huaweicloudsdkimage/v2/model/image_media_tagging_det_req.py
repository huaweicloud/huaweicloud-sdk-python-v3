# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageMediaTaggingDetReq:

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
        'language': 'str',
        'threshold': 'float',
        'limit': 'int'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'language': 'language',
        'threshold': 'threshold',
        'limit': 'limit'
    }

    def __init__(self, image=None, url=None, language=None, threshold=None, limit=None):
        r"""ImageMediaTaggingDetReq

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M，最短边至少1px，最长边最大10000px，支持JPG、PNG、BMP、WEBP格式。 
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  &gt; - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 &gt; - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 &gt; - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 
        :type url: str
        :param language: zh：返回标签的语言类型为中文。  en：返回标签的语言类型为英文。  默认值为zh。
        :type language: str
        :param threshold: 置信度的阈值（0~100），低于此置信数的标签，将不会返回。  默认值：20。  最小值：0。  最大值：100。
        :type threshold: float
        :param limit: 最多返回的tag数（取值范围：1~50），默认值： 10
        :type limit: int
        """
        
        

        self._image = None
        self._url = None
        self._language = None
        self._threshold = None
        self._limit = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if language is not None:
            self.language = language
        if threshold is not None:
            self.threshold = threshold
        if limit is not None:
            self.limit = limit

    @property
    def image(self):
        r"""Gets the image of this ImageMediaTaggingDetReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M，最短边至少1px，最长边最大10000px，支持JPG、PNG、BMP、WEBP格式。 

        :return: The image of this ImageMediaTaggingDetReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ImageMediaTaggingDetReq.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10M，最短边至少1px，最长边最大10000px，支持JPG、PNG、BMP、WEBP格式。 

        :param image: The image of this ImageMediaTaggingDetReq.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this ImageMediaTaggingDetReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 

        :return: The url of this ImageMediaTaggingDetReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageMediaTaggingDetReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。 

        :param url: The url of this ImageMediaTaggingDetReq.
        :type url: str
        """
        self._url = url

    @property
    def language(self):
        r"""Gets the language of this ImageMediaTaggingDetReq.

        zh：返回标签的语言类型为中文。  en：返回标签的语言类型为英文。  默认值为zh。

        :return: The language of this ImageMediaTaggingDetReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ImageMediaTaggingDetReq.

        zh：返回标签的语言类型为中文。  en：返回标签的语言类型为英文。  默认值为zh。

        :param language: The language of this ImageMediaTaggingDetReq.
        :type language: str
        """
        self._language = language

    @property
    def threshold(self):
        r"""Gets the threshold of this ImageMediaTaggingDetReq.

        置信度的阈值（0~100），低于此置信数的标签，将不会返回。  默认值：20。  最小值：0。  最大值：100。

        :return: The threshold of this ImageMediaTaggingDetReq.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ImageMediaTaggingDetReq.

        置信度的阈值（0~100），低于此置信数的标签，将不会返回。  默认值：20。  最小值：0。  最大值：100。

        :param threshold: The threshold of this ImageMediaTaggingDetReq.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def limit(self):
        r"""Gets the limit of this ImageMediaTaggingDetReq.

        最多返回的tag数（取值范围：1~50），默认值： 10

        :return: The limit of this ImageMediaTaggingDetReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ImageMediaTaggingDetReq.

        最多返回的tag数（取值范围：1~50），默认值： 10

        :param limit: The limit of this ImageMediaTaggingDetReq.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ImageMediaTaggingDetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
