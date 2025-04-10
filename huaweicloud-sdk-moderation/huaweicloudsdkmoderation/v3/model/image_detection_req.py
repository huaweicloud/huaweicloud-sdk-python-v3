# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'event_type': 'str',
        'categories': 'list[str]',
        'image_text_config': 'ImgTextConfig',
        'url': 'str',
        'image': 'str',
        'biz_type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'categories': 'categories',
        'image_text_config': 'image_text_config',
        'url': 'url',
        'image': 'image',
        'biz_type': 'biz_type',
        'language': 'language'
    }

    def __init__(self, event_type=None, categories=None, image_text_config=None, url=None, image=None, biz_type=None, language=None):
        r"""ImageDetectionReq

        The model defined in huaweicloud sdk

        :param event_type: 事件类型。 可选值如下： head_image：头像 album：相册 dynamic：动态 article：帖子 comment：评论 room_cover：房间封面 group_message：群聊图片 message：私聊图片 product：商品图片
        :type event_type: str
        :param categories: 检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 - 可通过配置上述场景，来完对应场景元素的检测。 &gt; 每个检测场景的检测次数会分类统计。
        :type categories: list[str]
        :param image_text_config: 
        :type image_text_config: :class:`huaweicloudsdkmoderation.v3.ImgTextConfig`
        :param url: 图片url, 与image二选一，目前支持： - 公网HTTP/HTTPS URL
        :type url: str
        :param image: 与url二选一，图片文件Base64编码字符串，要求base64编码后大小不超过10M，支持JPG/PNG/JPEG/WEBP/GIF/TIFF/TIF/HEIF等格式。
        :type image: str
        :param biz_type: 自定义审核策略名称，可在控制台配置;如果请求参数中传了biz_type则优先使用biz_type,如果用户没传biz_type则event_type和categories必须传。
        :type biz_type: str
        :param language: 可指定图片中文字语种类型
        :type language: str
        """
        
        

        self._event_type = None
        self._categories = None
        self._image_text_config = None
        self._url = None
        self._image = None
        self._biz_type = None
        self._language = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if categories is not None:
            self.categories = categories
        if image_text_config is not None:
            self.image_text_config = image_text_config
        if url is not None:
            self.url = url
        if image is not None:
            self.image = image
        if biz_type is not None:
            self.biz_type = biz_type
        if language is not None:
            self.language = language

    @property
    def event_type(self):
        r"""Gets the event_type of this ImageDetectionReq.

        事件类型。 可选值如下： head_image：头像 album：相册 dynamic：动态 article：帖子 comment：评论 room_cover：房间封面 group_message：群聊图片 message：私聊图片 product：商品图片

        :return: The event_type of this ImageDetectionReq.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ImageDetectionReq.

        事件类型。 可选值如下： head_image：头像 album：相册 dynamic：动态 article：帖子 comment：评论 room_cover：房间封面 group_message：群聊图片 message：私聊图片 product：商品图片

        :param event_type: The event_type of this ImageDetectionReq.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def categories(self):
        r"""Gets the categories of this ImageDetectionReq.

        检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 - 可通过配置上述场景，来完对应场景元素的检测。 > 每个检测场景的检测次数会分类统计。

        :return: The categories of this ImageDetectionReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ImageDetectionReq.

        检测场景。可添加的检测场景如下： - terrorism：暴恐元素的检测。 - porn：涉黄元素的检测。 - image_text：广告图文的检测。 - 可通过配置上述场景，来完对应场景元素的检测。 > 每个检测场景的检测次数会分类统计。

        :param categories: The categories of this ImageDetectionReq.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def image_text_config(self):
        r"""Gets the image_text_config of this ImageDetectionReq.

        :return: The image_text_config of this ImageDetectionReq.
        :rtype: :class:`huaweicloudsdkmoderation.v3.ImgTextConfig`
        """
        return self._image_text_config

    @image_text_config.setter
    def image_text_config(self, image_text_config):
        r"""Sets the image_text_config of this ImageDetectionReq.

        :param image_text_config: The image_text_config of this ImageDetectionReq.
        :type image_text_config: :class:`huaweicloudsdkmoderation.v3.ImgTextConfig`
        """
        self._image_text_config = image_text_config

    @property
    def url(self):
        r"""Gets the url of this ImageDetectionReq.

        图片url, 与image二选一，目前支持： - 公网HTTP/HTTPS URL

        :return: The url of this ImageDetectionReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageDetectionReq.

        图片url, 与image二选一，目前支持： - 公网HTTP/HTTPS URL

        :param url: The url of this ImageDetectionReq.
        :type url: str
        """
        self._url = url

    @property
    def image(self):
        r"""Gets the image of this ImageDetectionReq.

        与url二选一，图片文件Base64编码字符串，要求base64编码后大小不超过10M，支持JPG/PNG/JPEG/WEBP/GIF/TIFF/TIF/HEIF等格式。

        :return: The image of this ImageDetectionReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ImageDetectionReq.

        与url二选一，图片文件Base64编码字符串，要求base64编码后大小不超过10M，支持JPG/PNG/JPEG/WEBP/GIF/TIFF/TIF/HEIF等格式。

        :param image: The image of this ImageDetectionReq.
        :type image: str
        """
        self._image = image

    @property
    def biz_type(self):
        r"""Gets the biz_type of this ImageDetectionReq.

        自定义审核策略名称，可在控制台配置;如果请求参数中传了biz_type则优先使用biz_type,如果用户没传biz_type则event_type和categories必须传。

        :return: The biz_type of this ImageDetectionReq.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this ImageDetectionReq.

        自定义审核策略名称，可在控制台配置;如果请求参数中传了biz_type则优先使用biz_type,如果用户没传biz_type则event_type和categories必须传。

        :param biz_type: The biz_type of this ImageDetectionReq.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def language(self):
        r"""Gets the language of this ImageDetectionReq.

        可指定图片中文字语种类型

        :return: The language of this ImageDetectionReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ImageDetectionReq.

        可指定图片中文字语种类型

        :param language: The language of this ImageDetectionReq.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ImageDetectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
