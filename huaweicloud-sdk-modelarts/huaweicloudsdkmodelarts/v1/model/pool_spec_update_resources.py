# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecUpdateResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'count': 'int',
        'azs': 'list[PoolNodeAz]'
    }

    attribute_map = {
        'flavor': 'flavor',
        'count': 'count',
        'azs': 'azs'
    }

    def __init__(self, flavor=None, count=None, azs=None):
        r"""PoolSpecUpdateResources

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param count: **参数解释**：相应规格的资源数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type count: int
        :param azs: **参数解释**：更新的AZ列表。
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        
        

        self._flavor = None
        self._count = None
        self._azs = None
        self.discriminator = None

        self.flavor = flavor
        self.count = count
        if azs is not None:
            self.azs = azs

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolSpecUpdateResources.

        **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this PoolSpecUpdateResources.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolSpecUpdateResources.

        **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this PoolSpecUpdateResources.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def count(self):
        r"""Gets the count of this PoolSpecUpdateResources.

        **参数解释**：相应规格的资源数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The count of this PoolSpecUpdateResources.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolSpecUpdateResources.

        **参数解释**：相应规格的资源数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param count: The count of this PoolSpecUpdateResources.
        :type count: int
        """
        self._count = count

    @property
    def azs(self):
        r"""Gets the azs of this PoolSpecUpdateResources.

        **参数解释**：更新的AZ列表。

        :return: The azs of this PoolSpecUpdateResources.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this PoolSpecUpdateResources.

        **参数解释**：更新的AZ列表。

        :param azs: The azs of this PoolSpecUpdateResources.
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        self._azs = azs

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
        if not isinstance(other, PoolSpecUpdateResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
