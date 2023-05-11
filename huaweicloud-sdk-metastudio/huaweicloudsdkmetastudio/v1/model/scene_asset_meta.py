# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SceneAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'components': 'list[SceneComponentInfo]',
        'default_configs': 'dict(str, SceneComponentInfo)'
    }

    attribute_map = {
        'components': 'components',
        'default_configs': 'default_configs'
    }

    def __init__(self, components=None, default_configs=None):
        """SceneAssetMeta

        The model defined in huaweicloud sdk

        :param components: 可操作组件列表（如屏幕，灯光，摄像机）。
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.SceneComponentInfo`]
        :param default_configs: 默认场景设置（机位，初始人位置）。
        :type default_configs: dict(str, SceneComponentInfo)
        """
        
        

        self._components = None
        self._default_configs = None
        self.discriminator = None

        if components is not None:
            self.components = components
        if default_configs is not None:
            self.default_configs = default_configs

    @property
    def components(self):
        """Gets the components of this SceneAssetMeta.

        可操作组件列表（如屏幕，灯光，摄像机）。

        :return: The components of this SceneAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SceneComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this SceneAssetMeta.

        可操作组件列表（如屏幕，灯光，摄像机）。

        :param components: The components of this SceneAssetMeta.
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.SceneComponentInfo`]
        """
        self._components = components

    @property
    def default_configs(self):
        """Gets the default_configs of this SceneAssetMeta.

        默认场景设置（机位，初始人位置）。

        :return: The default_configs of this SceneAssetMeta.
        :rtype: dict(str, SceneComponentInfo)
        """
        return self._default_configs

    @default_configs.setter
    def default_configs(self, default_configs):
        """Sets the default_configs of this SceneAssetMeta.

        默认场景设置（机位，初始人位置）。

        :param default_configs: The default_configs of this SceneAssetMeta.
        :type default_configs: dict(str, SceneComponentInfo)
        """
        self._default_configs = default_configs

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
        if not isinstance(other, SceneAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
