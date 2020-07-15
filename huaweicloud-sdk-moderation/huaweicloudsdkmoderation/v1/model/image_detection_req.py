# coding: utf-8

import pprint
import re

import six





class ImageDetectionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'image': 'str',
        'categories': 'list[str]',
        'threshold': 'float'
    }

    attribute_map = {
        'url': 'url',
        'image': 'image',
        'categories': 'categories',
        'threshold': 'threshold'
    }

    def __init__(self, url=None, image=None, categories=None, threshold=None):
        """ImageDetectionReq - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._image = None
        self._categories = None
        self._threshold = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if image is not None:
            self.image = image
        if categories is not None:
            self.categories = categories
        if threshold is not None:
            self.threshold = threshold

    @property
    def url(self):
        """Gets the url of this ImageDetectionReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The url of this ImageDetectionReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageDetectionReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。  > 说明：  - 接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param url: The url of this ImageDetectionReq.
        :type: str
        """
        self._url = url

    @property
    def image(self):
        """Gets the image of this ImageDetectionReq.

        与url二选一  图片文件Base64编码字符串。要求base64编码后大小不超过10M。  政治人物检测人脸部分不小于50*50像素。  支持JPG/PNG/BMP格式。 

        :return: The image of this ImageDetectionReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageDetectionReq.

        与url二选一  图片文件Base64编码字符串。要求base64编码后大小不超过10M。  政治人物检测人脸部分不小于50*50像素。  支持JPG/PNG/BMP格式。 

        :param image: The image of this ImageDetectionReq.
        :type: str
        """
        self._image = image

    @property
    def categories(self):
        """Gets the categories of this ImageDetectionReq.

        检测场景:  - politics：是否涉及政治人物的检测。  - terrorism：是否包含涉政暴恐元素的检测。  - porn：是否包含涉黄内容元素的检测。  - ad：是否包含广告的检测（公测特性）。  - all：包含politics、terrorism和porn三种场景的检测。  可通过配置上述场景，来完对应场景元素的检测。  为空或无此参数表示politics和terrorism都检测，但不包含porn场景。  > 说明： 每个检测场景的检测次数会分类统计。 

        :return: The categories of this ImageDetectionReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ImageDetectionReq.

        检测场景:  - politics：是否涉及政治人物的检测。  - terrorism：是否包含涉政暴恐元素的检测。  - porn：是否包含涉黄内容元素的检测。  - ad：是否包含广告的检测（公测特性）。  - all：包含politics、terrorism和porn三种场景的检测。  可通过配置上述场景，来完对应场景元素的检测。  为空或无此参数表示politics和terrorism都检测，但不包含porn场景。  > 说明： 每个检测场景的检测次数会分类统计。 

        :param categories: The categories of this ImageDetectionReq.
        :type: list[str]
        """
        self._categories = categories

    @property
    def threshold(self):
        """Gets the threshold of this ImageDetectionReq.

        结果过滤门限，只有置信度不低于此门限的结果才会呈现在detail的列表中，取值范围 0-1，当未设置此值时各个检测场景会使用各自的默认值。  politics检测场景的默认值为0.95。  terrorism检测场景的默认值为0。  ad检测场景的默认值为0。  无特殊需求直接不传此参数或像示例中一样值设为空字符串即可。  > 说明：  - 如果检测场景中的最高置信度也未达到threshold，则结果列表为空；反之threshold过小，则会使结果列表中内容过多。  - threshold参数不支持porn场景筛选。  - threshold参数不会影响响应中的suggestion。 

        :return: The threshold of this ImageDetectionReq.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ImageDetectionReq.

        结果过滤门限，只有置信度不低于此门限的结果才会呈现在detail的列表中，取值范围 0-1，当未设置此值时各个检测场景会使用各自的默认值。  politics检测场景的默认值为0.95。  terrorism检测场景的默认值为0。  ad检测场景的默认值为0。  无特殊需求直接不传此参数或像示例中一样值设为空字符串即可。  > 说明：  - 如果检测场景中的最高置信度也未达到threshold，则结果列表为空；反之threshold过小，则会使结果列表中内容过多。  - threshold参数不支持porn场景筛选。  - threshold参数不会影响响应中的suggestion。 

        :param threshold: The threshold of this ImageDetectionReq.
        :type: float
        """
        self._threshold = threshold

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageDetectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
