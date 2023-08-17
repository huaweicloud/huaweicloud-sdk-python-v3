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
        """SystemProperty

        The model defined in huaweicloud sdk

        :param action: 操作。 - ADD：增加 - DELETE：删除
        :type action: str
        :param key: 系统属性。 * STYLE_ID：风格Id。 * DH_ID：数字人ID(尚未启用)。 * PLATFORM_AVAILABLE：是否平台可用(尚未启用)。 * RENDER_ENGINE：引擎类型。value可选UE或MetaEngine。 * BACKGROUND_IMG：视频制作的2D背景图片。value设置成Yes。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * CREATED_BY_PLATFORM：是否平台生成
        :type key: str
        :param value: 属性值。
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
        """Gets the action of this SystemProperty.

        操作。 - ADD：增加 - DELETE：删除

        :return: The action of this SystemProperty.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SystemProperty.

        操作。 - ADD：增加 - DELETE：删除

        :param action: The action of this SystemProperty.
        :type action: str
        """
        self._action = action

    @property
    def key(self):
        """Gets the key of this SystemProperty.

        系统属性。 * STYLE_ID：风格Id。 * DH_ID：数字人ID(尚未启用)。 * PLATFORM_AVAILABLE：是否平台可用(尚未启用)。 * RENDER_ENGINE：引擎类型。value可选UE或MetaEngine。 * BACKGROUND_IMG：视频制作的2D背景图片。value设置成Yes。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * CREATED_BY_PLATFORM：是否平台生成

        :return: The key of this SystemProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SystemProperty.

        系统属性。 * STYLE_ID：风格Id。 * DH_ID：数字人ID(尚未启用)。 * PLATFORM_AVAILABLE：是否平台可用(尚未启用)。 * RENDER_ENGINE：引擎类型。value可选UE或MetaEngine。 * BACKGROUND_IMG：视频制作的2D背景图片。value设置成Yes。 * BACKGROUND_SCENE：视频制作的2D背景场景。value可选Horizontal（横屏）或者Vertical（竖屏）。 * CREATED_BY_PLATFORM：是否平台生成

        :param key: The key of this SystemProperty.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this SystemProperty.

        属性值。

        :return: The value of this SystemProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SystemProperty.

        属性值。

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
