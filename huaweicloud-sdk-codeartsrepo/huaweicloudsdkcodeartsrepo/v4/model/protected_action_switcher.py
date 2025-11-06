# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedActionSwitcher:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable'
    }

    def __init__(self, name=None, enable=None):
        r"""ProtectedActionSwitcher

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 开关名。 **约束限制：** 不涉及。 **取值范围：** - allowed_force_push，允许强制推送（默认不允许强推）。 **默认取值：** 不涉及。
        :type name: str
        :param enable: **参数解释：** 是否开启。 **约束限制：** 不涉及。 **取值范围：** - true，开启 - false，关闭 **默认取值：** 不涉及。
        :type enable: bool
        """
        
        

        self._name = None
        self._enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable

    @property
    def name(self):
        r"""Gets the name of this ProtectedActionSwitcher.

        **参数解释：** 开关名。 **约束限制：** 不涉及。 **取值范围：** - allowed_force_push，允许强制推送（默认不允许强推）。 **默认取值：** 不涉及。

        :return: The name of this ProtectedActionSwitcher.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProtectedActionSwitcher.

        **参数解释：** 开关名。 **约束限制：** 不涉及。 **取值范围：** - allowed_force_push，允许强制推送（默认不允许强推）。 **默认取值：** 不涉及。

        :param name: The name of this ProtectedActionSwitcher.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this ProtectedActionSwitcher.

        **参数解释：** 是否开启。 **约束限制：** 不涉及。 **取值范围：** - true，开启 - false，关闭 **默认取值：** 不涉及。

        :return: The enable of this ProtectedActionSwitcher.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ProtectedActionSwitcher.

        **参数解释：** 是否开启。 **约束限制：** 不涉及。 **取值范围：** - true，开启 - false，关闭 **默认取值：** 不涉及。

        :param enable: The enable of this ProtectedActionSwitcher.
        :type enable: bool
        """
        self._enable = enable

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtectedActionSwitcher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
