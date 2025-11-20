# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionReqBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_network': 'PartitionReqBodySpecHostNetwork',
        'container_network': 'list[PartitionReqBodySpecContainerNetwork]',
        'public_border_group': 'str',
        'category': 'str'
    }

    attribute_map = {
        'host_network': 'hostNetwork',
        'container_network': 'containerNetwork',
        'public_border_group': 'publicBorderGroup',
        'category': 'category'
    }

    def __init__(self, host_network=None, container_network=None, public_border_group=None, category=None):
        r"""PartitionReqBodySpec

        The model defined in huaweicloud sdk

        :param host_network: 
        :type host_network: :class:`huaweicloudsdkcce.v3.PartitionReqBodySpecHostNetwork`
        :param container_network: **参数解释**： 分区容器子网 **约束限制**： 列表长度不能大于20 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type container_network: list[:class:`huaweicloudsdkcce.v3.PartitionReqBodySpecContainerNetwork`]
        :param public_border_group: **参数解释**： 群组，IES边缘场景为可用区ID，中心区统一为“center”。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type public_border_group: str
        :param category: **参数解释**： 可用区分类 **约束限制**： 不涉及 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区 **默认取值**： 不涉及
        :type category: str
        """
        
        

        self._host_network = None
        self._container_network = None
        self._public_border_group = None
        self._category = None
        self.discriminator = None

        if host_network is not None:
            self.host_network = host_network
        if container_network is not None:
            self.container_network = container_network
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if category is not None:
            self.category = category

    @property
    def host_network(self):
        r"""Gets the host_network of this PartitionReqBodySpec.

        :return: The host_network of this PartitionReqBodySpec.
        :rtype: :class:`huaweicloudsdkcce.v3.PartitionReqBodySpecHostNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        r"""Sets the host_network of this PartitionReqBodySpec.

        :param host_network: The host_network of this PartitionReqBodySpec.
        :type host_network: :class:`huaweicloudsdkcce.v3.PartitionReqBodySpecHostNetwork`
        """
        self._host_network = host_network

    @property
    def container_network(self):
        r"""Gets the container_network of this PartitionReqBodySpec.

        **参数解释**： 分区容器子网 **约束限制**： 列表长度不能大于20 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The container_network of this PartitionReqBodySpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PartitionReqBodySpecContainerNetwork`]
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        r"""Sets the container_network of this PartitionReqBodySpec.

        **参数解释**： 分区容器子网 **约束限制**： 列表长度不能大于20 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param container_network: The container_network of this PartitionReqBodySpec.
        :type container_network: list[:class:`huaweicloudsdkcce.v3.PartitionReqBodySpecContainerNetwork`]
        """
        self._container_network = container_network

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this PartitionReqBodySpec.

        **参数解释**： 群组，IES边缘场景为可用区ID，中心区统一为“center”。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The public_border_group of this PartitionReqBodySpec.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this PartitionReqBodySpec.

        **参数解释**： 群组，IES边缘场景为可用区ID，中心区统一为“center”。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param public_border_group: The public_border_group of this PartitionReqBodySpec.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this PartitionReqBodySpec.

        **参数解释**： 可用区分类 **约束限制**： 不涉及 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区 **默认取值**： 不涉及

        :return: The category of this PartitionReqBodySpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this PartitionReqBodySpec.

        **参数解释**： 可用区分类 **约束限制**： 不涉及 **取值范围**： - Default: 中心云可用区 - IES: 专属云可用区 - HomeZone: 智能边缘云可用区 **默认取值**： 不涉及

        :param category: The category of this PartitionReqBodySpec.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, PartitionReqBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
