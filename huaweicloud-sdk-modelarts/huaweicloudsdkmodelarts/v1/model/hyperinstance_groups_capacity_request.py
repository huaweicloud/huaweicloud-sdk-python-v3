# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperinstanceGroupsCapacityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hyperinstance_group_ids': 'list[str]',
        'availability_zone': 'str',
        'resource_flavor': 'str'
    }

    attribute_map = {
        'hyperinstance_group_ids': 'hyperinstance_group_ids',
        'availability_zone': 'availability_zone',
        'resource_flavor': 'resource_flavor'
    }

    def __init__(self, hyperinstance_group_ids=None, availability_zone=None, resource_flavor=None):
        r"""HyperinstanceGroupsCapacityRequest

        The model defined in huaweicloud sdk

        :param hyperinstance_group_ids: **参数解释**：hyperinstance-group ID列表。 **默认取值**：不涉及。 **取值范围**：1-5
        :type hyperinstance_group_ids: list[str]
        :param availability_zone: **参数解释**：可用区。 **默认取值**：不涉及。
        :type availability_zone: str
        :param resource_flavor: **参数解释**：规格名称。 **默认取值**：不涉及。
        :type resource_flavor: str
        """
        
        

        self._hyperinstance_group_ids = None
        self._availability_zone = None
        self._resource_flavor = None
        self.discriminator = None

        self.hyperinstance_group_ids = hyperinstance_group_ids
        self.availability_zone = availability_zone
        self.resource_flavor = resource_flavor

    @property
    def hyperinstance_group_ids(self):
        r"""Gets the hyperinstance_group_ids of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：hyperinstance-group ID列表。 **默认取值**：不涉及。 **取值范围**：1-5

        :return: The hyperinstance_group_ids of this HyperinstanceGroupsCapacityRequest.
        :rtype: list[str]
        """
        return self._hyperinstance_group_ids

    @hyperinstance_group_ids.setter
    def hyperinstance_group_ids(self, hyperinstance_group_ids):
        r"""Sets the hyperinstance_group_ids of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：hyperinstance-group ID列表。 **默认取值**：不涉及。 **取值范围**：1-5

        :param hyperinstance_group_ids: The hyperinstance_group_ids of this HyperinstanceGroupsCapacityRequest.
        :type hyperinstance_group_ids: list[str]
        """
        self._hyperinstance_group_ids = hyperinstance_group_ids

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：可用区。 **默认取值**：不涉及。

        :return: The availability_zone of this HyperinstanceGroupsCapacityRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：可用区。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this HyperinstanceGroupsCapacityRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：规格名称。 **默认取值**：不涉及。

        :return: The resource_flavor of this HyperinstanceGroupsCapacityRequest.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this HyperinstanceGroupsCapacityRequest.

        **参数解释**：规格名称。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this HyperinstanceGroupsCapacityRequest.
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
        if not isinstance(other, HyperinstanceGroupsCapacityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
