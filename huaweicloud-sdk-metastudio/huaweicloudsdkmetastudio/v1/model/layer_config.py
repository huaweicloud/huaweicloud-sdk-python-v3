# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'layer_type': 'str',
        'position': 'LayerPositionConfig',
        'size': 'LayerSizeConfig',
        'image_config': 'ImageLayerConfig',
        'video_config': 'VideoLayerConfig',
        'text_config': 'TextLayerConfig'
    }

    attribute_map = {
        'layer_type': 'layer_type',
        'position': 'position',
        'size': 'size',
        'image_config': 'image_config',
        'video_config': 'video_config',
        'text_config': 'text_config'
    }

    def __init__(self, layer_type=None, position=None, size=None, image_config=None, video_config=None, text_config=None):
        """LayerConfig

        The model defined in huaweicloud sdk

        :param layer_type: 图层类型。 - HUMAN:  人物图层 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层
        :type layer_type: str
        :param position: 
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        :param size: 
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        :param image_config: 
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextLayerConfig`
        """
        
        

        self._layer_type = None
        self._position = None
        self._size = None
        self._image_config = None
        self._video_config = None
        self._text_config = None
        self.discriminator = None

        self.layer_type = layer_type
        self.position = position
        if size is not None:
            self.size = size
        if image_config is not None:
            self.image_config = image_config
        if video_config is not None:
            self.video_config = video_config
        if text_config is not None:
            self.text_config = text_config

    @property
    def layer_type(self):
        """Gets the layer_type of this LayerConfig.

        图层类型。 - HUMAN:  人物图层 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层

        :return: The layer_type of this LayerConfig.
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        """Sets the layer_type of this LayerConfig.

        图层类型。 - HUMAN:  人物图层 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层

        :param layer_type: The layer_type of this LayerConfig.
        :type layer_type: str
        """
        self._layer_type = layer_type

    @property
    def position(self):
        """Gets the position of this LayerConfig.

        :return: The position of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this LayerConfig.

        :param position: The position of this LayerConfig.
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        self._position = position

    @property
    def size(self):
        """Gets the size of this LayerConfig.

        :return: The size of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LayerConfig.

        :param size: The size of this LayerConfig.
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        self._size = size

    @property
    def image_config(self):
        """Gets the image_config of this LayerConfig.

        :return: The image_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        """Sets the image_config of this LayerConfig.

        :param image_config: The image_config of this LayerConfig.
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        """
        self._image_config = image_config

    @property
    def video_config(self):
        """Gets the video_config of this LayerConfig.

        :return: The video_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this LayerConfig.

        :param video_config: The video_config of this LayerConfig.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        """
        self._video_config = video_config

    @property
    def text_config(self):
        """Gets the text_config of this LayerConfig.

        :return: The text_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextLayerConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        """Sets the text_config of this LayerConfig.

        :param text_config: The text_config of this LayerConfig.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextLayerConfig`
        """
        self._text_config = text_config

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
        if not isinstance(other, LayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
