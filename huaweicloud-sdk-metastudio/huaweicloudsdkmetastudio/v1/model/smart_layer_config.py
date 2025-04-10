# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartLayerConfig:

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
        'asset_id': 'str',
        'position': 'LayerPositionConfig',
        'size': 'LayerSizeConfig',
        'image_config': 'SmartImageLayerConfig',
        'video_config': 'SmartVideoLayerConfig',
        'text_config': 'SmartTextLayerConfig'
    }

    attribute_map = {
        'layer_type': 'layer_type',
        'asset_id': 'asset_id',
        'position': 'position',
        'size': 'size',
        'image_config': 'image_config',
        'video_config': 'video_config',
        'text_config': 'text_config'
    }

    def __init__(self, layer_type=None, asset_id=None, position=None, size=None, image_config=None, video_config=None, text_config=None):
        r"""SmartLayerConfig

        The model defined in huaweicloud sdk

        :param layer_type: 图层类型。 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层 - TEXT: 文本图层
        :type layer_type: str
        :param asset_id: 图层所需资产的资产id，外部资产信息无需填写
        :type asset_id: str
        :param position: 
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        :param size: 
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        :param image_config: 
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.SmartImageLayerConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartVideoLayerConfig`
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.SmartTextLayerConfig`
        """
        
        

        self._layer_type = None
        self._asset_id = None
        self._position = None
        self._size = None
        self._image_config = None
        self._video_config = None
        self._text_config = None
        self.discriminator = None

        self.layer_type = layer_type
        if asset_id is not None:
            self.asset_id = asset_id
        if position is not None:
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
        r"""Gets the layer_type of this SmartLayerConfig.

        图层类型。 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层 - TEXT: 文本图层

        :return: The layer_type of this SmartLayerConfig.
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        r"""Sets the layer_type of this SmartLayerConfig.

        图层类型。 - IMAGE： 素材图片图层 - VIDEO： 素材视频图层 - TEXT: 文本图层

        :param layer_type: The layer_type of this SmartLayerConfig.
        :type layer_type: str
        """
        self._layer_type = layer_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this SmartLayerConfig.

        图层所需资产的资产id，外部资产信息无需填写

        :return: The asset_id of this SmartLayerConfig.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this SmartLayerConfig.

        图层所需资产的资产id，外部资产信息无需填写

        :param asset_id: The asset_id of this SmartLayerConfig.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def position(self):
        r"""Gets the position of this SmartLayerConfig.

        :return: The position of this SmartLayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this SmartLayerConfig.

        :param position: The position of this SmartLayerConfig.
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        self._position = position

    @property
    def size(self):
        r"""Gets the size of this SmartLayerConfig.

        :return: The size of this SmartLayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SmartLayerConfig.

        :param size: The size of this SmartLayerConfig.
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        self._size = size

    @property
    def image_config(self):
        r"""Gets the image_config of this SmartLayerConfig.

        :return: The image_config of this SmartLayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartImageLayerConfig`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        r"""Sets the image_config of this SmartLayerConfig.

        :param image_config: The image_config of this SmartLayerConfig.
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.SmartImageLayerConfig`
        """
        self._image_config = image_config

    @property
    def video_config(self):
        r"""Gets the video_config of this SmartLayerConfig.

        :return: The video_config of this SmartLayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartVideoLayerConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this SmartLayerConfig.

        :param video_config: The video_config of this SmartLayerConfig.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartVideoLayerConfig`
        """
        self._video_config = video_config

    @property
    def text_config(self):
        r"""Gets the text_config of this SmartLayerConfig.

        :return: The text_config of this SmartLayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartTextLayerConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        r"""Sets the text_config of this SmartLayerConfig.

        :param text_config: The text_config of this SmartLayerConfig.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.SmartTextLayerConfig`
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
        if not isinstance(other, SmartLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
