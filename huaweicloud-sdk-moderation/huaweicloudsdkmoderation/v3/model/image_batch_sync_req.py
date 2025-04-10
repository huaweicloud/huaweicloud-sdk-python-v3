# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBatchSyncReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'categories': 'list[str]',
        'image_text_config': 'ImageBatchSyncReqImageTextConfig',
        'urls': 'list[ImageBatchSyncReqUrls]',
        'language': 'str',
        'biz_type': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'categories': 'categories',
        'image_text_config': 'image_text_config',
        'urls': 'urls',
        'language': 'language',
        'biz_type': 'biz_type'
    }

    def __init__(self, event_type=None, categories=None, image_text_config=None, urls=None, language=None, biz_type=None):
        r"""ImageBatchSyncReq

        The model defined in huaweicloud sdk

        :param event_type: 事件类型。可选值如下： - head_image：头像 - album：相册 - dynamic：动态 - article：帖子 - comment：评论 - room_cover：房间封面 - group_message：群聊图片 - message：私聊图片 - product：商品图片
        :type event_type: str
        :param categories: 检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 可通过配置上述场景，来完对应场景元素的检测。每个检测场景的检测次数会分类统计。
        :type categories: list[str]
        :param image_text_config: 
        :type image_text_config: :class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqImageTextConfig`
        :param urls: 图片url列表。
        :type urls: list[:class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqUrls`]
        :param language: 指定图片中文字语种类型。 - zh: 中文 - en: 英文 默认值为zh，中国站仅支持zh。
        :type language: str
        :param biz_type: 用户在控制台界面创建的自定义审核策略名称。 - 如果请求参数中包含biz_type则优先使用biztype。 - 如果未传biz_type则event_type和categories为必传参数。
        :type biz_type: str
        """
        
        

        self._event_type = None
        self._categories = None
        self._image_text_config = None
        self._urls = None
        self._language = None
        self._biz_type = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if categories is not None:
            self.categories = categories
        if image_text_config is not None:
            self.image_text_config = image_text_config
        self.urls = urls
        if language is not None:
            self.language = language
        if biz_type is not None:
            self.biz_type = biz_type

    @property
    def event_type(self):
        r"""Gets the event_type of this ImageBatchSyncReq.

        事件类型。可选值如下： - head_image：头像 - album：相册 - dynamic：动态 - article：帖子 - comment：评论 - room_cover：房间封面 - group_message：群聊图片 - message：私聊图片 - product：商品图片

        :return: The event_type of this ImageBatchSyncReq.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ImageBatchSyncReq.

        事件类型。可选值如下： - head_image：头像 - album：相册 - dynamic：动态 - article：帖子 - comment：评论 - room_cover：房间封面 - group_message：群聊图片 - message：私聊图片 - product：商品图片

        :param event_type: The event_type of this ImageBatchSyncReq.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def categories(self):
        r"""Gets the categories of this ImageBatchSyncReq.

        检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 可通过配置上述场景，来完对应场景元素的检测。每个检测场景的检测次数会分类统计。

        :return: The categories of this ImageBatchSyncReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ImageBatchSyncReq.

        检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 可通过配置上述场景，来完对应场景元素的检测。每个检测场景的检测次数会分类统计。

        :param categories: The categories of this ImageBatchSyncReq.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def image_text_config(self):
        r"""Gets the image_text_config of this ImageBatchSyncReq.

        :return: The image_text_config of this ImageBatchSyncReq.
        :rtype: :class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqImageTextConfig`
        """
        return self._image_text_config

    @image_text_config.setter
    def image_text_config(self, image_text_config):
        r"""Sets the image_text_config of this ImageBatchSyncReq.

        :param image_text_config: The image_text_config of this ImageBatchSyncReq.
        :type image_text_config: :class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqImageTextConfig`
        """
        self._image_text_config = image_text_config

    @property
    def urls(self):
        r"""Gets the urls of this ImageBatchSyncReq.

        图片url列表。

        :return: The urls of this ImageBatchSyncReq.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqUrls`]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this ImageBatchSyncReq.

        图片url列表。

        :param urls: The urls of this ImageBatchSyncReq.
        :type urls: list[:class:`huaweicloudsdkmoderation.v3.ImageBatchSyncReqUrls`]
        """
        self._urls = urls

    @property
    def language(self):
        r"""Gets the language of this ImageBatchSyncReq.

        指定图片中文字语种类型。 - zh: 中文 - en: 英文 默认值为zh，中国站仅支持zh。

        :return: The language of this ImageBatchSyncReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ImageBatchSyncReq.

        指定图片中文字语种类型。 - zh: 中文 - en: 英文 默认值为zh，中国站仅支持zh。

        :param language: The language of this ImageBatchSyncReq.
        :type language: str
        """
        self._language = language

    @property
    def biz_type(self):
        r"""Gets the biz_type of this ImageBatchSyncReq.

        用户在控制台界面创建的自定义审核策略名称。 - 如果请求参数中包含biz_type则优先使用biztype。 - 如果未传biz_type则event_type和categories为必传参数。

        :return: The biz_type of this ImageBatchSyncReq.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this ImageBatchSyncReq.

        用户在控制台界面创建的自定义审核策略名称。 - 如果请求参数中包含biz_type则优先使用biztype。 - 如果未传biz_type则event_type和categories为必传参数。

        :param biz_type: The biz_type of this ImageBatchSyncReq.
        :type biz_type: str
        """
        self._biz_type = biz_type

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
        if not isinstance(other, ImageBatchSyncReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
