# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElbIpGroupOpsReq:

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
        'type': 'str',
        'enable_ip_group': 'bool',
        'group_id': 'str',
        'ip_list': 'list[IpGroupItem]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'enable_ip_group': 'enable_ip_group',
        'group_id': 'group_id',
        'ip_list': 'ip_list'
    }

    def __init__(self, name=None, type=None, enable_ip_group=None, group_id=None, ip_list=None):
        r"""ElbIpGroupOpsReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  弹性负载均衡ip组名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type name: str
        :param type: **参数解释**：  弹性负载均衡ip组类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type type: str
        :param enable_ip_group: **参数解释**：  是否开启弹性负载均衡ip组。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type enable_ip_group: bool
        :param group_id: **参数解释**：  弹性负载均衡ip组id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type group_id: str
        :param ip_list: **参数解释**：  ip列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type ip_list: list[:class:`huaweicloudsdkddm.v1.IpGroupItem`]
        """
        
        

        self._name = None
        self._type = None
        self._enable_ip_group = None
        self._group_id = None
        self._ip_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if enable_ip_group is not None:
            self.enable_ip_group = enable_ip_group
        if group_id is not None:
            self.group_id = group_id
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def name(self):
        r"""Gets the name of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The name of this ElbIpGroupOpsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param name: The name of this ElbIpGroupOpsReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The type of this ElbIpGroupOpsReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param type: The type of this ElbIpGroupOpsReq.
        :type type: str
        """
        self._type = type

    @property
    def enable_ip_group(self):
        r"""Gets the enable_ip_group of this ElbIpGroupOpsReq.

        **参数解释**：  是否开启弹性负载均衡ip组。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The enable_ip_group of this ElbIpGroupOpsReq.
        :rtype: bool
        """
        return self._enable_ip_group

    @enable_ip_group.setter
    def enable_ip_group(self, enable_ip_group):
        r"""Sets the enable_ip_group of this ElbIpGroupOpsReq.

        **参数解释**：  是否开启弹性负载均衡ip组。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param enable_ip_group: The enable_ip_group of this ElbIpGroupOpsReq.
        :type enable_ip_group: bool
        """
        self._enable_ip_group = enable_ip_group

    @property
    def group_id(self):
        r"""Gets the group_id of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The group_id of this ElbIpGroupOpsReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ElbIpGroupOpsReq.

        **参数解释**：  弹性负载均衡ip组id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param group_id: The group_id of this ElbIpGroupOpsReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def ip_list(self):
        r"""Gets the ip_list of this ElbIpGroupOpsReq.

        **参数解释**：  ip列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The ip_list of this ElbIpGroupOpsReq.
        :rtype: list[:class:`huaweicloudsdkddm.v1.IpGroupItem`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this ElbIpGroupOpsReq.

        **参数解释**：  ip列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param ip_list: The ip_list of this ElbIpGroupOpsReq.
        :type ip_list: list[:class:`huaweicloudsdkddm.v1.IpGroupItem`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, ElbIpGroupOpsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
