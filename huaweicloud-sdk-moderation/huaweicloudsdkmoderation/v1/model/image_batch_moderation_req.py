# coding: utf-8

import pprint
import re

import six





class ImageBatchModerationReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'urls': 'list[str]',
        'categories': 'list[str]',
        'threshold': 'float'
    }

    attribute_map = {
        'urls': 'urls',
        'categories': 'categories',
        'threshold': 'threshold'
    }

    def __init__(self, urls=None, categories=None, threshold=None):
        """ImageBatchModerationReq - a model defined in huaweicloud sdk"""
        
        

        self._urls = None
        self._categories = None
        self._threshold = None
        self.discriminator = None

        self.urls = urls
        if categories is not None:
            self.categories = categories
        if threshold is not None:
            self.threshold = threshold

    @property
    def urls(self):
        """Gets the urls of this ImageBatchModerationReq.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。 > 说明：图片的URL路径列表最多支持10个URL地址。接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The urls of this ImageBatchModerationReq.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ImageBatchModerationReq.

        图片的URL路径，目前支持： - 公网HTTP/HTTPS URL - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。 > 说明：图片的URL路径列表最多支持10个URL地址。接口响应时间依赖图片的下载时间，如果图片下载时间过长，会返回接口调用失败。请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param urls: The urls of this ImageBatchModerationReq.
        :type: list[str]
        """
        self._urls = urls

    @property
    def categories(self):
        """Gets the categories of this ImageBatchModerationReq.

        请参见[表1](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table2693546819540)中categories参数说明。

        :return: The categories of this ImageBatchModerationReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ImageBatchModerationReq.

        请参见[表1](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table2693546819540)中categories参数说明。

        :param categories: The categories of this ImageBatchModerationReq.
        :type: list[str]
        """
        self._categories = categories

    @property
    def threshold(self):
        """Gets the threshold of this ImageBatchModerationReq.

        请参见[表1](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table2693546819540)中threshold参数说明。

        :return: The threshold of this ImageBatchModerationReq.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ImageBatchModerationReq.

        请参见[表1](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table2693546819540)中threshold参数说明。

        :param threshold: The threshold of this ImageBatchModerationReq.
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
        if not isinstance(other, ImageBatchModerationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
