# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerScaleEvaluation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_sold_out': 'bool',
        'flavor': 'str',
        'resource_flavor': 'str'
    }

    attribute_map = {
        'is_sold_out': 'is_sold_out',
        'flavor': 'flavor',
        'resource_flavor': 'resource_flavor'
    }

    def __init__(self, is_sold_out=None, flavor=None, resource_flavor=None):
        r"""ServerScaleEvaluation

        The model defined in huaweicloud sdk

        :param is_sold_out: **参数解释**：是否售罄。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type is_sold_out: bool
        :param flavor: **参数解释**：规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param resource_flavor: **参数解释**：资源规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type resource_flavor: str
        """
        
        

        self._is_sold_out = None
        self._flavor = None
        self._resource_flavor = None
        self.discriminator = None

        if is_sold_out is not None:
            self.is_sold_out = is_sold_out
        if flavor is not None:
            self.flavor = flavor
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor

    @property
    def is_sold_out(self):
        r"""Gets the is_sold_out of this ServerScaleEvaluation.

        **参数解释**：是否售罄。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The is_sold_out of this ServerScaleEvaluation.
        :rtype: bool
        """
        return self._is_sold_out

    @is_sold_out.setter
    def is_sold_out(self, is_sold_out):
        r"""Sets the is_sold_out of this ServerScaleEvaluation.

        **参数解释**：是否售罄。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param is_sold_out: The is_sold_out of this ServerScaleEvaluation.
        :type is_sold_out: bool
        """
        self._is_sold_out = is_sold_out

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerScaleEvaluation.

        **参数解释**：规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this ServerScaleEvaluation.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerScaleEvaluation.

        **参数解释**：规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this ServerScaleEvaluation.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this ServerScaleEvaluation.

        **参数解释**：资源规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The resource_flavor of this ServerScaleEvaluation.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this ServerScaleEvaluation.

        **参数解释**：资源规格信息。 **约束限制**：不涉及 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this ServerScaleEvaluation.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

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
        if not isinstance(other, ServerScaleEvaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
