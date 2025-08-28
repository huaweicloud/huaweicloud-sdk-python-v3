# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountPreoccupyIpNumRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7_flavor_id': 'str',
        'ip_target_enable': 'bool',
        'ip_version': 'int',
        'loadbalancer_id': 'str',
        'availability_zone_id': 'list[str]',
        'scene': 'str',
        'nat64_enable': 'bool'
    }

    attribute_map = {
        'l7_flavor_id': 'l7_flavor_id',
        'ip_target_enable': 'ip_target_enable',
        'ip_version': 'ip_version',
        'loadbalancer_id': 'loadbalancer_id',
        'availability_zone_id': 'availability_zone_id',
        'scene': 'scene',
        'nat64_enable': 'nat64_enable'
    }

    def __init__(self, l7_flavor_id=None, ip_target_enable=None, ip_version=None, loadbalancer_id=None, availability_zone_id=None, scene=None, nat64_enable=None):
        r"""CountPreoccupyIpNumRequest

        The model defined in huaweicloud sdk

        :param l7_flavor_id: **参数解释**：负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB的预占IP数量，或变更LB的原七层规格到该规格所需要的新增预占IP数量。  **约束限制**：仅支持创建LB、变更LB规格场景。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持传入l7_flavor_id。](tag:hcso,hk_vdf,srg,fcs)
        :type l7_flavor_id: str
        :param ip_target_enable: **参数解释**：IP类型后端转发开关。  **约束限制**：仅支持创建LB、LB开启IP类型后端转发场景。  **取值范围**： - 取值true表示计算创建开启IP类型后端转发的LB的预占IP数量，或开启IP类型后端转发所需要的新增预占IP数量。 - 取值false表示计算创建不开启IP类型后端转发的LB的预占IP。 - 不传等价false。  **默认取值**：false [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type ip_target_enable: bool
        :param ip_version: **参数解释**：负载均衡器IP地址类型，取值4、6 。  **约束限制**：仅支持创建LB场景。  **取值范围**： - 取值4表示计算创建支持IPv4地址的LB的预占IP。 - 取值6表示计算创建支持IPv6地址的LB的预占IP。  **默认取值**：不涉及  [不支持IPv6，请勿设置为6。](tag:dt)
        :type ip_version: int
        :param loadbalancer_id: **参数解释**：负载均衡器ID。计算LB变更或创建LB中的第一个七层监听器的新增预占IP。  **约束限制**：仅支持变更LB规格、开启IP类型后端转发、开启/不开启地址转换功能、创建LB中的第一个七层监听器场景。  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: str
        :param availability_zone_id: **参数解释**：计算创建AZ列表为availability_zone_id的负载均衡器实例的预占IP。  **约束限制**： - 仅支持创建LB场景。 - 传入loadbalancer_id时，该参数无效。  **取值范围**：不涉及  **默认取值**：不涉及
        :type availability_zone_id: list[str]
        :param scene: **参数解释**：计算共享型升级为独享型ELB负载均衡器实例的所需预占IP。  **约束限制**： - 仅支持共享型升级为独享型ELB场景。 - 必须同时传入loadbalancer_id。  **取值范围**：UPGRADE - 共享型升级为独享型ELB场景。  **默认取值**：不涉及
        :type scene: str
        :param nat64_enable: **参数解释**：开启地址转换。传入该字段表示计算创建LB及该LB下开启/不开启地址转换特性的监听器所需要的预占IP，或者指定LB创建开启/不开启地址转换特性的监听器所需要的新增预占IP。  **约束限制**： - 仅支持计算ELB实例开启NAT64特性场景。  **取值范围**： - true：开启地址转换特性。 - false：不开启地址转换特性。  **默认取值**：false
        :type nat64_enable: bool
        """
        
        

        self._l7_flavor_id = None
        self._ip_target_enable = None
        self._ip_version = None
        self._loadbalancer_id = None
        self._availability_zone_id = None
        self._scene = None
        self._nat64_enable = None
        self.discriminator = None

        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if ip_version is not None:
            self.ip_version = ip_version
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if scene is not None:
            self.scene = scene
        if nat64_enable is not None:
            self.nat64_enable = nat64_enable

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB的预占IP数量，或变更LB的原七层规格到该规格所需要的新增预占IP数量。  **约束限制**：仅支持创建LB、变更LB规格场景。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持传入l7_flavor_id。](tag:hcso,hk_vdf,srg,fcs)

        :return: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器七层规格的ID。传入该字段表示计算创建该规格的LB的预占IP数量，或变更LB的原七层规格到该规格所需要的新增预占IP数量。  **约束限制**：仅支持创建LB、变更LB规格场景。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持传入l7_flavor_id。](tag:hcso,hk_vdf,srg,fcs)

        :param l7_flavor_id: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ip_target_enable(self):
        r"""Gets the ip_target_enable of this CountPreoccupyIpNumRequest.

        **参数解释**：IP类型后端转发开关。  **约束限制**：仅支持创建LB、LB开启IP类型后端转发场景。  **取值范围**： - 取值true表示计算创建开启IP类型后端转发的LB的预占IP数量，或开启IP类型后端转发所需要的新增预占IP数量。 - 取值false表示计算创建不开启IP类型后端转发的LB的预占IP。 - 不传等价false。  **默认取值**：false [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        r"""Sets the ip_target_enable of this CountPreoccupyIpNumRequest.

        **参数解释**：IP类型后端转发开关。  **约束限制**：仅支持创建LB、LB开启IP类型后端转发场景。  **取值范围**： - 取值true表示计算创建开启IP类型后端转发的LB的预占IP数量，或开启IP类型后端转发所需要的新增预占IP数量。 - 取值false表示计算创建不开启IP类型后端转发的LB的预占IP。 - 不传等价false。  **默认取值**：false [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param ip_target_enable: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器IP地址类型，取值4、6 。  **约束限制**：仅支持创建LB场景。  **取值范围**： - 取值4表示计算创建支持IPv4地址的LB的预占IP。 - 取值6表示计算创建支持IPv6地址的LB的预占IP。  **默认取值**：不涉及  [不支持IPv6，请勿设置为6。](tag:dt)

        :return: The ip_version of this CountPreoccupyIpNumRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器IP地址类型，取值4、6 。  **约束限制**：仅支持创建LB场景。  **取值范围**： - 取值4表示计算创建支持IPv4地址的LB的预占IP。 - 取值6表示计算创建支持IPv6地址的LB的预占IP。  **默认取值**：不涉及  [不支持IPv6，请勿设置为6。](tag:dt)

        :param ip_version: The ip_version of this CountPreoccupyIpNumRequest.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器ID。计算LB变更或创建LB中的第一个七层监听器的新增预占IP。  **约束限制**：仅支持变更LB规格、开启IP类型后端转发、开启/不开启地址转换功能、创建LB中的第一个七层监听器场景。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CountPreoccupyIpNumRequest.

        **参数解释**：负载均衡器ID。计算LB变更或创建LB中的第一个七层监听器的新增预占IP。  **约束限制**：仅支持变更LB规格、开启IP类型后端转发、开启/不开启地址转换功能、创建LB中的第一个七层监听器场景。  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this CountPreoccupyIpNumRequest.

        **参数解释**：计算创建AZ列表为availability_zone_id的负载均衡器实例的预占IP。  **约束限制**： - 仅支持创建LB场景。 - 传入loadbalancer_id时，该参数无效。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :rtype: list[str]
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this CountPreoccupyIpNumRequest.

        **参数解释**：计算创建AZ列表为availability_zone_id的负载均衡器实例的预占IP。  **约束限制**： - 仅支持创建LB场景。 - 传入loadbalancer_id时，该参数无效。  **取值范围**：不涉及  **默认取值**：不涉及

        :param availability_zone_id: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :type availability_zone_id: list[str]
        """
        self._availability_zone_id = availability_zone_id

    @property
    def scene(self):
        r"""Gets the scene of this CountPreoccupyIpNumRequest.

        **参数解释**：计算共享型升级为独享型ELB负载均衡器实例的所需预占IP。  **约束限制**： - 仅支持共享型升级为独享型ELB场景。 - 必须同时传入loadbalancer_id。  **取值范围**：UPGRADE - 共享型升级为独享型ELB场景。  **默认取值**：不涉及

        :return: The scene of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this CountPreoccupyIpNumRequest.

        **参数解释**：计算共享型升级为独享型ELB负载均衡器实例的所需预占IP。  **约束限制**： - 仅支持共享型升级为独享型ELB场景。 - 必须同时传入loadbalancer_id。  **取值范围**：UPGRADE - 共享型升级为独享型ELB场景。  **默认取值**：不涉及

        :param scene: The scene of this CountPreoccupyIpNumRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def nat64_enable(self):
        r"""Gets the nat64_enable of this CountPreoccupyIpNumRequest.

        **参数解释**：开启地址转换。传入该字段表示计算创建LB及该LB下开启/不开启地址转换特性的监听器所需要的预占IP，或者指定LB创建开启/不开启地址转换特性的监听器所需要的新增预占IP。  **约束限制**： - 仅支持计算ELB实例开启NAT64特性场景。  **取值范围**： - true：开启地址转换特性。 - false：不开启地址转换特性。  **默认取值**：false

        :return: The nat64_enable of this CountPreoccupyIpNumRequest.
        :rtype: bool
        """
        return self._nat64_enable

    @nat64_enable.setter
    def nat64_enable(self, nat64_enable):
        r"""Sets the nat64_enable of this CountPreoccupyIpNumRequest.

        **参数解释**：开启地址转换。传入该字段表示计算创建LB及该LB下开启/不开启地址转换特性的监听器所需要的预占IP，或者指定LB创建开启/不开启地址转换特性的监听器所需要的新增预占IP。  **约束限制**： - 仅支持计算ELB实例开启NAT64特性场景。  **取值范围**： - true：开启地址转换特性。 - false：不开启地址转换特性。  **默认取值**：false

        :param nat64_enable: The nat64_enable of this CountPreoccupyIpNumRequest.
        :type nat64_enable: bool
        """
        self._nat64_enable = nat64_enable

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
        if not isinstance(other, CountPreoccupyIpNumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
