# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackgroundConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'background_type': 'str',
        'background_title': 'str',
        'human_position_2d': 'HumanPosition2D',
        'human_size_2d': 'HumanSize2D',
        'background_cover_url': 'str',
        'background_config': 'str',
        'background_asset_id': 'str'
    }

    attribute_map = {
        'background_type': 'background_type',
        'background_title': 'background_title',
        'human_position_2d': 'human_position_2d',
        'human_size_2d': 'human_size_2d',
        'background_cover_url': 'background_cover_url',
        'background_config': 'background_config',
        'background_asset_id': 'background_asset_id'
    }

    def __init__(self, background_type=None, background_title=None, human_position_2d=None, human_size_2d=None, background_cover_url=None, background_config=None, background_asset_id=None):
        """BackgroundConfigInfo

        The model defined in huaweicloud sdk

        :param background_type: 背景类型。 - IMAGE：图片，用于3D数字人演示素材讲解模式的图片或分身数字背景图片 - IMAGE_2D：图片，用于3D数字人主播播报模式的2D场景背景图片 - VIDEO：视频 - AUDIO：音频 &gt; * 分身数字人视频制作仅支持IMAGE
        :type background_type: str
        :param background_title: 背景标题。
        :type background_title: str
        :param human_position_2d: 
        :type human_position_2d: :class:`huaweicloudsdkmetastudio.v1.HumanPosition2D`
        :param human_size_2d: 
        :type human_size_2d: :class:`huaweicloudsdkmetastudio.v1.HumanSize2D`
        :param background_cover_url: 视频文件封面图片的下载URL。  演示素材为视频时有效。
        :type background_cover_url: str
        :param background_config: 背景文件的URL。
        :type background_config: str
        :param background_asset_id: 背景资产ID。 &gt; * 背景是背景图片时，填图片资产ID。
        :type background_asset_id: str
        """
        
        

        self._background_type = None
        self._background_title = None
        self._human_position_2d = None
        self._human_size_2d = None
        self._background_cover_url = None
        self._background_config = None
        self._background_asset_id = None
        self.discriminator = None

        self.background_type = background_type
        if background_title is not None:
            self.background_title = background_title
        if human_position_2d is not None:
            self.human_position_2d = human_position_2d
        if human_size_2d is not None:
            self.human_size_2d = human_size_2d
        if background_cover_url is not None:
            self.background_cover_url = background_cover_url
        self.background_config = background_config
        if background_asset_id is not None:
            self.background_asset_id = background_asset_id

    @property
    def background_type(self):
        """Gets the background_type of this BackgroundConfigInfo.

        背景类型。 - IMAGE：图片，用于3D数字人演示素材讲解模式的图片或分身数字背景图片 - IMAGE_2D：图片，用于3D数字人主播播报模式的2D场景背景图片 - VIDEO：视频 - AUDIO：音频 > * 分身数字人视频制作仅支持IMAGE

        :return: The background_type of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_type

    @background_type.setter
    def background_type(self, background_type):
        """Sets the background_type of this BackgroundConfigInfo.

        背景类型。 - IMAGE：图片，用于3D数字人演示素材讲解模式的图片或分身数字背景图片 - IMAGE_2D：图片，用于3D数字人主播播报模式的2D场景背景图片 - VIDEO：视频 - AUDIO：音频 > * 分身数字人视频制作仅支持IMAGE

        :param background_type: The background_type of this BackgroundConfigInfo.
        :type background_type: str
        """
        self._background_type = background_type

    @property
    def background_title(self):
        """Gets the background_title of this BackgroundConfigInfo.

        背景标题。

        :return: The background_title of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_title

    @background_title.setter
    def background_title(self, background_title):
        """Sets the background_title of this BackgroundConfigInfo.

        背景标题。

        :param background_title: The background_title of this BackgroundConfigInfo.
        :type background_title: str
        """
        self._background_title = background_title

    @property
    def human_position_2d(self):
        """Gets the human_position_2d of this BackgroundConfigInfo.

        :return: The human_position_2d of this BackgroundConfigInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanPosition2D`
        """
        return self._human_position_2d

    @human_position_2d.setter
    def human_position_2d(self, human_position_2d):
        """Sets the human_position_2d of this BackgroundConfigInfo.

        :param human_position_2d: The human_position_2d of this BackgroundConfigInfo.
        :type human_position_2d: :class:`huaweicloudsdkmetastudio.v1.HumanPosition2D`
        """
        self._human_position_2d = human_position_2d

    @property
    def human_size_2d(self):
        """Gets the human_size_2d of this BackgroundConfigInfo.

        :return: The human_size_2d of this BackgroundConfigInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanSize2D`
        """
        return self._human_size_2d

    @human_size_2d.setter
    def human_size_2d(self, human_size_2d):
        """Sets the human_size_2d of this BackgroundConfigInfo.

        :param human_size_2d: The human_size_2d of this BackgroundConfigInfo.
        :type human_size_2d: :class:`huaweicloudsdkmetastudio.v1.HumanSize2D`
        """
        self._human_size_2d = human_size_2d

    @property
    def background_cover_url(self):
        """Gets the background_cover_url of this BackgroundConfigInfo.

        视频文件封面图片的下载URL。  演示素材为视频时有效。

        :return: The background_cover_url of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_cover_url

    @background_cover_url.setter
    def background_cover_url(self, background_cover_url):
        """Sets the background_cover_url of this BackgroundConfigInfo.

        视频文件封面图片的下载URL。  演示素材为视频时有效。

        :param background_cover_url: The background_cover_url of this BackgroundConfigInfo.
        :type background_cover_url: str
        """
        self._background_cover_url = background_cover_url

    @property
    def background_config(self):
        """Gets the background_config of this BackgroundConfigInfo.

        背景文件的URL。

        :return: The background_config of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        """Sets the background_config of this BackgroundConfigInfo.

        背景文件的URL。

        :param background_config: The background_config of this BackgroundConfigInfo.
        :type background_config: str
        """
        self._background_config = background_config

    @property
    def background_asset_id(self):
        """Gets the background_asset_id of this BackgroundConfigInfo.

        背景资产ID。 > * 背景是背景图片时，填图片资产ID。

        :return: The background_asset_id of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_asset_id

    @background_asset_id.setter
    def background_asset_id(self, background_asset_id):
        """Sets the background_asset_id of this BackgroundConfigInfo.

        背景资产ID。 > * 背景是背景图片时，填图片资产ID。

        :param background_asset_id: The background_asset_id of this BackgroundConfigInfo.
        :type background_asset_id: str
        """
        self._background_asset_id = background_asset_id

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
        if not isinstance(other, BackgroundConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
