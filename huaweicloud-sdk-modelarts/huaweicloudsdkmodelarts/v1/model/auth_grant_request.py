# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthGrantRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_reset': 'bool'
    }

    attribute_map = {
        'is_reset': 'is_reset'
    }

    def __init__(self, is_reset=None):
        r"""AuthGrantRequest

        The model defined in huaweicloud sdk

        :param is_reset: **参数解释**：是否重置授权。 **约束限制**：不涉及。 **取值范围**： - true：重置已有委托（先删除再创建）。 - false：普通授权。 **默认取值**：false。
        :type is_reset: bool
        """
        
        

        self._is_reset = None
        self.discriminator = None

        if is_reset is not None:
            self.is_reset = is_reset

    @property
    def is_reset(self):
        r"""Gets the is_reset of this AuthGrantRequest.

        **参数解释**：是否重置授权。 **约束限制**：不涉及。 **取值范围**： - true：重置已有委托（先删除再创建）。 - false：普通授权。 **默认取值**：false。

        :return: The is_reset of this AuthGrantRequest.
        :rtype: bool
        """
        return self._is_reset

    @is_reset.setter
    def is_reset(self, is_reset):
        r"""Sets the is_reset of this AuthGrantRequest.

        **参数解释**：是否重置授权。 **约束限制**：不涉及。 **取值范围**： - true：重置已有委托（先删除再创建）。 - false：普通授权。 **默认取值**：false。

        :param is_reset: The is_reset of this AuthGrantRequest.
        :type is_reset: bool
        """
        self._is_reset = is_reset

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
        if not isinstance(other, AuthGrantRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
