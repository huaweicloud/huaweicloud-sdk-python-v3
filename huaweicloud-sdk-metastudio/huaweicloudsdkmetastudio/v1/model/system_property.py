# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'action': 'action',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, action=None, key=None, value=None):
        r"""SystemProperty

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 操作。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： * ADD：增加 * DELETE：删除  **默认取值**： 不涉及
        :type action: str
        :param key: **参数解释**： 系统属性条目。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 公共资产属性： * BACKGROUND_IMG：视频制作的背景图片。value设置成Yes * CREATED_BY_PLATFORM: 是否平台生成。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * MEITUAN_MATERIAL_APPROVED: 美团平台已审核标识，value设置成YES。 * IS_CONTROLLED: 是否管控。当前仅用于形象/声音资产。可取值YES。 * LIVE_IS_AUTHORIZED：直播业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * VIDEO_IS_AUTHORIZED：视频制作业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * CHAT_IS_AUTHORIZED：智能交互业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作图片图层。value设置成Yes，否则控制台视频制作、直播等界面的贴图区域，将无法看到此图片。 * MATERIAL_VIDEO：素材视频，用作视频图层。value设置成Yes，否则控制台视频制作、直播等界面的视频区域，将无法看到此视频。 * DIGITAL_HUMAN_2D_VIDEO：分身数字人视频。 * BUSINESS_CARD_VIDEO：名片视频。 * BUSSINESS_CARD_VIDEO：名片视频(过期) * PHOTO_VIDEO：照片数字人视频。  **默认取值**： 不涉及
        :type key: str
        :param value: **参数解释**： 系统属性属性值。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 字符长度1-1024位 **默认取值** 不涉及
        :type value: str
        """
        
        

        self._action = None
        self._key = None
        self._value = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def action(self):
        r"""Gets the action of this SystemProperty.

        **参数解释**： 操作。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： * ADD：增加 * DELETE：删除  **默认取值**： 不涉及

        :return: The action of this SystemProperty.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SystemProperty.

        **参数解释**： 操作。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： * ADD：增加 * DELETE：删除  **默认取值**： 不涉及

        :param action: The action of this SystemProperty.
        :type action: str
        """
        self._action = action

    @property
    def key(self):
        r"""Gets the key of this SystemProperty.

        **参数解释**： 系统属性条目。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 公共资产属性： * BACKGROUND_IMG：视频制作的背景图片。value设置成Yes * CREATED_BY_PLATFORM: 是否平台生成。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * MEITUAN_MATERIAL_APPROVED: 美团平台已审核标识，value设置成YES。 * IS_CONTROLLED: 是否管控。当前仅用于形象/声音资产。可取值YES。 * LIVE_IS_AUTHORIZED：直播业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * VIDEO_IS_AUTHORIZED：视频制作业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * CHAT_IS_AUTHORIZED：智能交互业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作图片图层。value设置成Yes，否则控制台视频制作、直播等界面的贴图区域，将无法看到此图片。 * MATERIAL_VIDEO：素材视频，用作视频图层。value设置成Yes，否则控制台视频制作、直播等界面的视频区域，将无法看到此视频。 * DIGITAL_HUMAN_2D_VIDEO：分身数字人视频。 * BUSINESS_CARD_VIDEO：名片视频。 * BUSSINESS_CARD_VIDEO：名片视频(过期) * PHOTO_VIDEO：照片数字人视频。  **默认取值**： 不涉及

        :return: The key of this SystemProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SystemProperty.

        **参数解释**： 系统属性条目。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 公共资产属性： * BACKGROUND_IMG：视频制作的背景图片。value设置成Yes * CREATED_BY_PLATFORM: 是否平台生成。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * MEITUAN_MATERIAL_APPROVED: 美团平台已审核标识，value设置成YES。 * IS_CONTROLLED: 是否管控。当前仅用于形象/声音资产。可取值YES。 * LIVE_IS_AUTHORIZED：直播业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * VIDEO_IS_AUTHORIZED：视频制作业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。 * CHAT_IS_AUTHORIZED：智能交互业务是否已授权。当前仅用于形象/声音资产，业务授权。 可取值YES。  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作图片图层。value设置成Yes，否则控制台视频制作、直播等界面的贴图区域，将无法看到此图片。 * MATERIAL_VIDEO：素材视频，用作视频图层。value设置成Yes，否则控制台视频制作、直播等界面的视频区域，将无法看到此视频。 * DIGITAL_HUMAN_2D_VIDEO：分身数字人视频。 * BUSINESS_CARD_VIDEO：名片视频。 * BUSSINESS_CARD_VIDEO：名片视频(过期) * PHOTO_VIDEO：照片数字人视频。  **默认取值**： 不涉及

        :param key: The key of this SystemProperty.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this SystemProperty.

        **参数解释**： 系统属性属性值。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 字符长度1-1024位 **默认取值** 不涉及

        :return: The value of this SystemProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SystemProperty.

        **参数解释**： 系统属性属性值。 **约束限制**： 系统属性仅为系统设置，普通用户无法修改。 **取值范围**： 字符长度1-1024位 **默认取值** 不涉及

        :param value: The value of this SystemProperty.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, SystemProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
