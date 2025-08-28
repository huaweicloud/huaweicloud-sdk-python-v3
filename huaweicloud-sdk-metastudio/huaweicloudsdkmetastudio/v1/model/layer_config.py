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
        'asset_id': 'str',
        'group_id': 'str',
        'sequence_no': 'int',
        'position': 'LayerPositionConfig',
        'size': 'LayerSizeConfig',
        'rotation': 'LayerRotationConfig',
        'image_config': 'ImageLayerConfig',
        'video_config': 'VideoLayerConfig',
        'text_config': 'TextLayerConfig'
    }

    attribute_map = {
        'layer_type': 'layer_type',
        'asset_id': 'asset_id',
        'group_id': 'group_id',
        'sequence_no': 'sequence_no',
        'position': 'position',
        'size': 'size',
        'rotation': 'rotation',
        'image_config': 'image_config',
        'video_config': 'video_config',
        'text_config': 'text_config'
    }

    def __init__(self, layer_type=None, asset_id=None, group_id=None, sequence_no=None, position=None, size=None, rotation=None, image_config=None, video_config=None, text_config=None):
        r"""LayerConfig

        The model defined in huaweicloud sdk

        :param layer_type: **参数解释**： 图层类型。 **约束限制**： 不涉及。 **取值范围**： * HUMAN:  人物图层 * IMAGE： 素材图片图层 * VIDEO： 素材视频图层 * TEXT: 素材文字图层  **默认取值**： 不涉及
        :type layer_type: str
        :param asset_id: **参数解释**： 图层所需资产的资产id，外部资产信息无需填写。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及
        :type asset_id: str
        :param group_id: **参数解释**： 多场景素材编组。同一group_id的素材，在应用全局时共享位置信息。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及
        :type group_id: str
        :param sequence_no: **参数解释**： 播放到对应的段落，显示对应的图层。该字段向前兼容，可以不填，字段可选。 只支持直播业务。 **约束限制**： 段落sequence_no。 **默认取值**： 不涉及。
        :type sequence_no: int
        :param position: 
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        :param size: 
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        :param rotation: 
        :type rotation: :class:`huaweicloudsdkmetastudio.v1.LayerRotationConfig`
        :param image_config: 
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextLayerConfig`
        """
        
        

        self._layer_type = None
        self._asset_id = None
        self._group_id = None
        self._sequence_no = None
        self._position = None
        self._size = None
        self._rotation = None
        self._image_config = None
        self._video_config = None
        self._text_config = None
        self.discriminator = None

        self.layer_type = layer_type
        if asset_id is not None:
            self.asset_id = asset_id
        if group_id is not None:
            self.group_id = group_id
        if sequence_no is not None:
            self.sequence_no = sequence_no
        if position is not None:
            self.position = position
        if size is not None:
            self.size = size
        if rotation is not None:
            self.rotation = rotation
        if image_config is not None:
            self.image_config = image_config
        if video_config is not None:
            self.video_config = video_config
        if text_config is not None:
            self.text_config = text_config

    @property
    def layer_type(self):
        r"""Gets the layer_type of this LayerConfig.

        **参数解释**： 图层类型。 **约束限制**： 不涉及。 **取值范围**： * HUMAN:  人物图层 * IMAGE： 素材图片图层 * VIDEO： 素材视频图层 * TEXT: 素材文字图层  **默认取值**： 不涉及

        :return: The layer_type of this LayerConfig.
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        r"""Sets the layer_type of this LayerConfig.

        **参数解释**： 图层类型。 **约束限制**： 不涉及。 **取值范围**： * HUMAN:  人物图层 * IMAGE： 素材图片图层 * VIDEO： 素材视频图层 * TEXT: 素材文字图层  **默认取值**： 不涉及

        :param layer_type: The layer_type of this LayerConfig.
        :type layer_type: str
        """
        self._layer_type = layer_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this LayerConfig.

        **参数解释**： 图层所需资产的资产id，外部资产信息无需填写。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :return: The asset_id of this LayerConfig.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this LayerConfig.

        **参数解释**： 图层所需资产的资产id，外部资产信息无需填写。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :param asset_id: The asset_id of this LayerConfig.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def group_id(self):
        r"""Gets the group_id of this LayerConfig.

        **参数解释**： 多场景素材编组。同一group_id的素材，在应用全局时共享位置信息。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :return: The group_id of this LayerConfig.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this LayerConfig.

        **参数解释**： 多场景素材编组。同一group_id的素材，在应用全局时共享位置信息。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :param group_id: The group_id of this LayerConfig.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def sequence_no(self):
        r"""Gets the sequence_no of this LayerConfig.

        **参数解释**： 播放到对应的段落，显示对应的图层。该字段向前兼容，可以不填，字段可选。 只支持直播业务。 **约束限制**： 段落sequence_no。 **默认取值**： 不涉及。

        :return: The sequence_no of this LayerConfig.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        r"""Sets the sequence_no of this LayerConfig.

        **参数解释**： 播放到对应的段落，显示对应的图层。该字段向前兼容，可以不填，字段可选。 只支持直播业务。 **约束限制**： 段落sequence_no。 **默认取值**： 不涉及。

        :param sequence_no: The sequence_no of this LayerConfig.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def position(self):
        r"""Gets the position of this LayerConfig.

        :return: The position of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this LayerConfig.

        :param position: The position of this LayerConfig.
        :type position: :class:`huaweicloudsdkmetastudio.v1.LayerPositionConfig`
        """
        self._position = position

    @property
    def size(self):
        r"""Gets the size of this LayerConfig.

        :return: The size of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this LayerConfig.

        :param size: The size of this LayerConfig.
        :type size: :class:`huaweicloudsdkmetastudio.v1.LayerSizeConfig`
        """
        self._size = size

    @property
    def rotation(self):
        r"""Gets the rotation of this LayerConfig.

        :return: The rotation of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LayerRotationConfig`
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        r"""Sets the rotation of this LayerConfig.

        :param rotation: The rotation of this LayerConfig.
        :type rotation: :class:`huaweicloudsdkmetastudio.v1.LayerRotationConfig`
        """
        self._rotation = rotation

    @property
    def image_config(self):
        r"""Gets the image_config of this LayerConfig.

        :return: The image_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        r"""Sets the image_config of this LayerConfig.

        :param image_config: The image_config of this LayerConfig.
        :type image_config: :class:`huaweicloudsdkmetastudio.v1.ImageLayerConfig`
        """
        self._image_config = image_config

    @property
    def video_config(self):
        r"""Gets the video_config of this LayerConfig.

        :return: The video_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this LayerConfig.

        :param video_config: The video_config of this LayerConfig.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoLayerConfig`
        """
        self._video_config = video_config

    @property
    def text_config(self):
        r"""Gets the text_config of this LayerConfig.

        :return: The text_config of this LayerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextLayerConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        r"""Sets the text_config of this LayerConfig.

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
