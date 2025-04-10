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
        'background_config': 'str',
        'background_color_config': 'str',
        'background_asset_id': 'str',
        'background_image_config': 'BackgroundImageConfig'
    }

    attribute_map = {
        'background_type': 'background_type',
        'background_config': 'background_config',
        'background_color_config': 'background_color_config',
        'background_asset_id': 'background_asset_id',
        'background_image_config': 'background_image_config'
    }

    def __init__(self, background_type=None, background_config=None, background_color_config=None, background_asset_id=None, background_image_config=None):
        r"""BackgroundConfigInfo

        The model defined in huaweicloud sdk

        :param background_type: **参数解释**： 背景类型。 **约束限制**： 不涉及。 **取值范围**： * IMAGE：图片背景，指定图片用作分身数字人背景。 * COLOR：纯色背景，指定颜色RGB值作为分身数字人背景。  **默认取值**： 不涉及
        :type background_type: str
        :param background_config: **参数解释**： 背景文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 * background_type&#x3D;IMAGE时需要填写。  **取值范围**： 字符长度1-2048位 **默认取值**： 不涉及。
        :type background_config: str
        :param background_color_config: **参数解释**： 纯色背景的RGB颜色值。 **约束限制**： background_type&#x3D;COLOR时需要填写。 **取值范围**： 字符长度0-16位
        :type background_color_config: str
        :param background_asset_id: **参数解释**： 背景资产ID。 &gt; 背景是背景图片时，填图片资产ID。  **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及
        :type background_asset_id: str
        :param background_image_config: 
        :type background_image_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundImageConfig`
        """
        
        

        self._background_type = None
        self._background_config = None
        self._background_color_config = None
        self._background_asset_id = None
        self._background_image_config = None
        self.discriminator = None

        self.background_type = background_type
        if background_config is not None:
            self.background_config = background_config
        if background_color_config is not None:
            self.background_color_config = background_color_config
        if background_asset_id is not None:
            self.background_asset_id = background_asset_id
        if background_image_config is not None:
            self.background_image_config = background_image_config

    @property
    def background_type(self):
        r"""Gets the background_type of this BackgroundConfigInfo.

        **参数解释**： 背景类型。 **约束限制**： 不涉及。 **取值范围**： * IMAGE：图片背景，指定图片用作分身数字人背景。 * COLOR：纯色背景，指定颜色RGB值作为分身数字人背景。  **默认取值**： 不涉及

        :return: The background_type of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_type

    @background_type.setter
    def background_type(self, background_type):
        r"""Sets the background_type of this BackgroundConfigInfo.

        **参数解释**： 背景类型。 **约束限制**： 不涉及。 **取值范围**： * IMAGE：图片背景，指定图片用作分身数字人背景。 * COLOR：纯色背景，指定颜色RGB值作为分身数字人背景。  **默认取值**： 不涉及

        :param background_type: The background_type of this BackgroundConfigInfo.
        :type background_type: str
        """
        self._background_type = background_type

    @property
    def background_config(self):
        r"""Gets the background_config of this BackgroundConfigInfo.

        **参数解释**： 背景文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 * background_type=IMAGE时需要填写。  **取值范围**： 字符长度1-2048位 **默认取值**： 不涉及。

        :return: The background_config of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        r"""Sets the background_config of this BackgroundConfigInfo.

        **参数解释**： 背景文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 * background_type=IMAGE时需要填写。  **取值范围**： 字符长度1-2048位 **默认取值**： 不涉及。

        :param background_config: The background_config of this BackgroundConfigInfo.
        :type background_config: str
        """
        self._background_config = background_config

    @property
    def background_color_config(self):
        r"""Gets the background_color_config of this BackgroundConfigInfo.

        **参数解释**： 纯色背景的RGB颜色值。 **约束限制**： background_type=COLOR时需要填写。 **取值范围**： 字符长度0-16位

        :return: The background_color_config of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_color_config

    @background_color_config.setter
    def background_color_config(self, background_color_config):
        r"""Sets the background_color_config of this BackgroundConfigInfo.

        **参数解释**： 纯色背景的RGB颜色值。 **约束限制**： background_type=COLOR时需要填写。 **取值范围**： 字符长度0-16位

        :param background_color_config: The background_color_config of this BackgroundConfigInfo.
        :type background_color_config: str
        """
        self._background_color_config = background_color_config

    @property
    def background_asset_id(self):
        r"""Gets the background_asset_id of this BackgroundConfigInfo.

        **参数解释**： 背景资产ID。 > 背景是背景图片时，填图片资产ID。  **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :return: The background_asset_id of this BackgroundConfigInfo.
        :rtype: str
        """
        return self._background_asset_id

    @background_asset_id.setter
    def background_asset_id(self, background_asset_id):
        r"""Sets the background_asset_id of this BackgroundConfigInfo.

        **参数解释**： 背景资产ID。 > 背景是背景图片时，填图片资产ID。  **约束限制**： 不涉及 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :param background_asset_id: The background_asset_id of this BackgroundConfigInfo.
        :type background_asset_id: str
        """
        self._background_asset_id = background_asset_id

    @property
    def background_image_config(self):
        r"""Gets the background_image_config of this BackgroundConfigInfo.

        :return: The background_image_config of this BackgroundConfigInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundImageConfig`
        """
        return self._background_image_config

    @background_image_config.setter
    def background_image_config(self, background_image_config):
        r"""Sets the background_image_config of this BackgroundConfigInfo.

        :param background_image_config: The background_image_config of this BackgroundConfigInfo.
        :type background_image_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundImageConfig`
        """
        self._background_image_config = background_image_config

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
