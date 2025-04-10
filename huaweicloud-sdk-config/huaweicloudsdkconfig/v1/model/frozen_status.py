# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrozenStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_frozen': 'bool',
        'frozen_scene': 'list[str]'
    }

    attribute_map = {
        'is_frozen': 'is_frozen',
        'frozen_scene': 'frozen_scene'
    }

    def __init__(self, is_frozen=None, frozen_scene=None):
        r"""FrozenStatus

        The model defined in huaweicloud sdk

        :param is_frozen: 是否冻结
        :type is_frozen: bool
        :param frozen_scene: 冻结场景
        :type frozen_scene: list[str]
        """
        
        

        self._is_frozen = None
        self._frozen_scene = None
        self.discriminator = None

        if is_frozen is not None:
            self.is_frozen = is_frozen
        if frozen_scene is not None:
            self.frozen_scene = frozen_scene

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this FrozenStatus.

        是否冻结

        :return: The is_frozen of this FrozenStatus.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this FrozenStatus.

        是否冻结

        :param is_frozen: The is_frozen of this FrozenStatus.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def frozen_scene(self):
        r"""Gets the frozen_scene of this FrozenStatus.

        冻结场景

        :return: The frozen_scene of this FrozenStatus.
        :rtype: list[str]
        """
        return self._frozen_scene

    @frozen_scene.setter
    def frozen_scene(self, frozen_scene):
        r"""Sets the frozen_scene of this FrozenStatus.

        冻结场景

        :param frozen_scene: The frozen_scene of this FrozenStatus.
        :type frozen_scene: list[str]
        """
        self._frozen_scene = frozen_scene

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
        if not isinstance(other, FrozenStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
