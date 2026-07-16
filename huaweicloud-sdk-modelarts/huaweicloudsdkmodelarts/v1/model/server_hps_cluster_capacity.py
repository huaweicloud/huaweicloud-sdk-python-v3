# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerHpsClusterCapacity:

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
        'availability_zone': 'str',
        'hyperinstance_cluster_id': 'str',
        'hyperinstance_cluster_name': 'str',
        'resource_flavor': 'str',
        'is_sold_out': 'bool'
    }

    attribute_map = {
        'flavor': 'flavor',
        'availability_zone': 'availability_zone',
        'hyperinstance_cluster_id': 'hyperinstance_cluster_id',
        'hyperinstance_cluster_name': 'hyperinstance_cluster_name',
        'resource_flavor': 'resource_flavor',
        'is_sold_out': 'is_sold_out'
    }

    def __init__(self, flavor=None, availability_zone=None, hyperinstance_cluster_id=None, hyperinstance_cluster_name=None, resource_flavor=None, is_sold_out=None):
        r"""ServerHpsClusterCapacity

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type flavor: str
        :param availability_zone: **参数解释**：可用区ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type availability_zone: str
        :param hyperinstance_cluster_id: **参数解释**：超节点集群ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type hyperinstance_cluster_id: str
        :param hyperinstance_cluster_name: **参数解释**：超节点集群名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type hyperinstance_cluster_name: str
        :param resource_flavor: **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。
        :type resource_flavor: str
        :param is_sold_out: **参数解释**：售罄状态。 **约束限制**：布尔值（true/false）。 **默认取值**：不涉及。
        :type is_sold_out: bool
        """
        
        

        self._flavor = None
        self._availability_zone = None
        self._hyperinstance_cluster_id = None
        self._hyperinstance_cluster_name = None
        self._resource_flavor = None
        self._is_sold_out = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if hyperinstance_cluster_id is not None:
            self.hyperinstance_cluster_id = hyperinstance_cluster_id
        if hyperinstance_cluster_name is not None:
            self.hyperinstance_cluster_name = hyperinstance_cluster_name
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor
        if is_sold_out is not None:
            self.is_sold_out = is_sold_out

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerHpsClusterCapacity.

        **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The flavor of this ServerHpsClusterCapacity.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerHpsClusterCapacity.

        **参数解释**：规格名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param flavor: The flavor of this ServerHpsClusterCapacity.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ServerHpsClusterCapacity.

        **参数解释**：可用区ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The availability_zone of this ServerHpsClusterCapacity.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ServerHpsClusterCapacity.

        **参数解释**：可用区ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this ServerHpsClusterCapacity.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def hyperinstance_cluster_id(self):
        r"""Gets the hyperinstance_cluster_id of this ServerHpsClusterCapacity.

        **参数解释**：超节点集群ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_id of this ServerHpsClusterCapacity.
        :rtype: str
        """
        return self._hyperinstance_cluster_id

    @hyperinstance_cluster_id.setter
    def hyperinstance_cluster_id(self, hyperinstance_cluster_id):
        r"""Sets the hyperinstance_cluster_id of this ServerHpsClusterCapacity.

        **参数解释**：超节点集群ID。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param hyperinstance_cluster_id: The hyperinstance_cluster_id of this ServerHpsClusterCapacity.
        :type hyperinstance_cluster_id: str
        """
        self._hyperinstance_cluster_id = hyperinstance_cluster_id

    @property
    def hyperinstance_cluster_name(self):
        r"""Gets the hyperinstance_cluster_name of this ServerHpsClusterCapacity.

        **参数解释**：超节点集群名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The hyperinstance_cluster_name of this ServerHpsClusterCapacity.
        :rtype: str
        """
        return self._hyperinstance_cluster_name

    @hyperinstance_cluster_name.setter
    def hyperinstance_cluster_name(self, hyperinstance_cluster_name):
        r"""Sets the hyperinstance_cluster_name of this ServerHpsClusterCapacity.

        **参数解释**：超节点集群名称。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param hyperinstance_cluster_name: The hyperinstance_cluster_name of this ServerHpsClusterCapacity.
        :type hyperinstance_cluster_name: str
        """
        self._hyperinstance_cluster_name = hyperinstance_cluster_name

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this ServerHpsClusterCapacity.

        **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :return: The resource_flavor of this ServerHpsClusterCapacity.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this ServerHpsClusterCapacity.

        **参数解释**：资源规格。 **约束限制**：长度1-65536个字符。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this ServerHpsClusterCapacity.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

    @property
    def is_sold_out(self):
        r"""Gets the is_sold_out of this ServerHpsClusterCapacity.

        **参数解释**：售罄状态。 **约束限制**：布尔值（true/false）。 **默认取值**：不涉及。

        :return: The is_sold_out of this ServerHpsClusterCapacity.
        :rtype: bool
        """
        return self._is_sold_out

    @is_sold_out.setter
    def is_sold_out(self, is_sold_out):
        r"""Sets the is_sold_out of this ServerHpsClusterCapacity.

        **参数解释**：售罄状态。 **约束限制**：布尔值（true/false）。 **默认取值**：不涉及。

        :param is_sold_out: The is_sold_out of this ServerHpsClusterCapacity.
        :type is_sold_out: bool
        """
        self._is_sold_out = is_sold_out

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
        if not isinstance(other, ServerHpsClusterCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
