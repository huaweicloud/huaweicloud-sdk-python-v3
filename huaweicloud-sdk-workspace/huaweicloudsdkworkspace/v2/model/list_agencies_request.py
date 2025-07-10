# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgenciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene': 'str'
    }

    attribute_map = {
        'scene': 'scene'
    }

    def __init__(self, scene=None):
        r"""ListAgenciesRequest

        The model defined in huaweicloud sdk

        :param scene: 委托场景。 - WORKSPACE：云桌面。 - CLOUD_GAME：云游戏。 - CLOUD_STORAGE 云存储。 - SCREEN_RECORD：录屏审计。
        :type scene: str
        """
        
        

        self._scene = None
        self.discriminator = None

        if scene is not None:
            self.scene = scene

    @property
    def scene(self):
        r"""Gets the scene of this ListAgenciesRequest.

        委托场景。 - WORKSPACE：云桌面。 - CLOUD_GAME：云游戏。 - CLOUD_STORAGE 云存储。 - SCREEN_RECORD：录屏审计。

        :return: The scene of this ListAgenciesRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListAgenciesRequest.

        委托场景。 - WORKSPACE：云桌面。 - CLOUD_GAME：云游戏。 - CLOUD_STORAGE 云存储。 - SCREEN_RECORD：录屏审计。

        :param scene: The scene of this ListAgenciesRequest.
        :type scene: str
        """
        self._scene = scene

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
        if not isinstance(other, ListAgenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
