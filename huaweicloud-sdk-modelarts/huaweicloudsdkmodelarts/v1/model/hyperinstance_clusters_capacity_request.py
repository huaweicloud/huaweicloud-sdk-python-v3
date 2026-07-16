# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperinstanceClustersCapacityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hyperinstance_cluster_ids': 'list[str]',
        'flavor': 'str',
        'availability_zone': 'str',
        'resource_flavor': 'str'
    }

    attribute_map = {
        'hyperinstance_cluster_ids': 'hyperinstance_cluster_ids',
        'flavor': 'flavor',
        'availability_zone': 'availability_zone',
        'resource_flavor': 'resource_flavor'
    }

    def __init__(self, hyperinstance_cluster_ids=None, flavor=None, availability_zone=None, resource_flavor=None):
        r"""HyperinstanceClustersCapacityRequest

        The model defined in huaweicloud sdk

        :param hyperinstance_cluster_ids: **参数解释**：超节点集群ID列表。 **约束限制**：数组长度0-5，每个元素长度1-128字符。 **默认取值**：不涉及。
        :type hyperinstance_cluster_ids: list[str]
        :param flavor: **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type flavor: str
        :param availability_zone: **参数解释**：可用区。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type availability_zone: str
        :param resource_flavor: **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type resource_flavor: str
        """
        
        

        self._hyperinstance_cluster_ids = None
        self._flavor = None
        self._availability_zone = None
        self._resource_flavor = None
        self.discriminator = None

        if hyperinstance_cluster_ids is not None:
            self.hyperinstance_cluster_ids = hyperinstance_cluster_ids
        if flavor is not None:
            self.flavor = flavor
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor

    @property
    def hyperinstance_cluster_ids(self):
        r"""Gets the hyperinstance_cluster_ids of this HyperinstanceClustersCapacityRequest.

        **参数解释**：超节点集群ID列表。 **约束限制**：数组长度0-5，每个元素长度1-128字符。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_ids of this HyperinstanceClustersCapacityRequest.
        :rtype: list[str]
        """
        return self._hyperinstance_cluster_ids

    @hyperinstance_cluster_ids.setter
    def hyperinstance_cluster_ids(self, hyperinstance_cluster_ids):
        r"""Sets the hyperinstance_cluster_ids of this HyperinstanceClustersCapacityRequest.

        **参数解释**：超节点集群ID列表。 **约束限制**：数组长度0-5，每个元素长度1-128字符。 **默认取值**：不涉及。

        :param hyperinstance_cluster_ids: The hyperinstance_cluster_ids of this HyperinstanceClustersCapacityRequest.
        :type hyperinstance_cluster_ids: list[str]
        """
        self._hyperinstance_cluster_ids = hyperinstance_cluster_ids

    @property
    def flavor(self):
        r"""Gets the flavor of this HyperinstanceClustersCapacityRequest.

        **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The flavor of this HyperinstanceClustersCapacityRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this HyperinstanceClustersCapacityRequest.

        **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param flavor: The flavor of this HyperinstanceClustersCapacityRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this HyperinstanceClustersCapacityRequest.

        **参数解释**：可用区。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The availability_zone of this HyperinstanceClustersCapacityRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this HyperinstanceClustersCapacityRequest.

        **参数解释**：可用区。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this HyperinstanceClustersCapacityRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this HyperinstanceClustersCapacityRequest.

        **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The resource_flavor of this HyperinstanceClustersCapacityRequest.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this HyperinstanceClustersCapacityRequest.

        **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this HyperinstanceClustersCapacityRequest.
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
        if not isinstance(other, HyperinstanceClustersCapacityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
