# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadBalancerPublicIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_version': 'int',
        'network_type': 'str',
        'billing_info': 'str',
        'description': 'str',
        'bandwidth': 'CreateLoadBalancerBandwidthOption'
    }

    attribute_map = {
        'ip_version': 'ip_version',
        'network_type': 'network_type',
        'billing_info': 'billing_info',
        'description': 'description',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, ip_version=None, network_type=None, billing_info=None, description=None, bandwidth=None):
        r"""CreateLoadBalancerPublicIpOption

        The model defined in huaweicloud sdk

        :param ip_version: **参数解释**：IP版本。  **约束限制**：不涉及  **取值范围**：  - 4：表示IPv4。  - 6：表示IPv6。  **默认取值**：4  [不支持IPv6，请勿设置为6。](tag:dt)
        :type ip_version: int
        :param network_type: **参数解释**：弹性公网IP的网络类型，默认5_bgp，更多请参考弹性公网ip创建。  [**约束限制**：华南-深圳局点该参数取值只能为5_gray。](tag:hws) [**约束限制**：只支持设置为5_gray。](tag:dt)  **取值范围**：5_bgp  **默认取值**：5_bgp
        :type network_type: str
        :param billing_info: **参数解释**：计费订单信息。  **约束限制**： - 空：按需计费。 [- 非空：包周期计费。格式：order_id:product_id:region_id:project_id](tag:hws)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)
        :type billing_info: str
        :param description: **参数解释**：弹性公网IP的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerBandwidthOption`
        """
        
        

        self._ip_version = None
        self._network_type = None
        self._billing_info = None
        self._description = None
        self._bandwidth = None
        self.discriminator = None

        if ip_version is not None:
            self.ip_version = ip_version
        self.network_type = network_type
        if billing_info is not None:
            self.billing_info = billing_info
        if description is not None:
            self.description = description
        self.bandwidth = bandwidth

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CreateLoadBalancerPublicIpOption.

        **参数解释**：IP版本。  **约束限制**：不涉及  **取值范围**：  - 4：表示IPv4。  - 6：表示IPv6。  **默认取值**：4  [不支持IPv6，请勿设置为6。](tag:dt)

        :return: The ip_version of this CreateLoadBalancerPublicIpOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CreateLoadBalancerPublicIpOption.

        **参数解释**：IP版本。  **约束限制**：不涉及  **取值范围**：  - 4：表示IPv4。  - 6：表示IPv6。  **默认取值**：4  [不支持IPv6，请勿设置为6。](tag:dt)

        :param ip_version: The ip_version of this CreateLoadBalancerPublicIpOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def network_type(self):
        r"""Gets the network_type of this CreateLoadBalancerPublicIpOption.

        **参数解释**：弹性公网IP的网络类型，默认5_bgp，更多请参考弹性公网ip创建。  [**约束限制**：华南-深圳局点该参数取值只能为5_gray。](tag:hws) [**约束限制**：只支持设置为5_gray。](tag:dt)  **取值范围**：5_bgp  **默认取值**：5_bgp

        :return: The network_type of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this CreateLoadBalancerPublicIpOption.

        **参数解释**：弹性公网IP的网络类型，默认5_bgp，更多请参考弹性公网ip创建。  [**约束限制**：华南-深圳局点该参数取值只能为5_gray。](tag:hws) [**约束限制**：只支持设置为5_gray。](tag:dt)  **取值范围**：5_bgp  **默认取值**：5_bgp

        :param network_type: The network_type of this CreateLoadBalancerPublicIpOption.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def billing_info(self):
        r"""Gets the billing_info of this CreateLoadBalancerPublicIpOption.

        **参数解释**：计费订单信息。  **约束限制**： - 空：按需计费。 [- 非空：包周期计费。格式：order_id:product_id:region_id:project_id](tag:hws)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :return: The billing_info of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this CreateLoadBalancerPublicIpOption.

        **参数解释**：计费订单信息。  **约束限制**： - 空：按需计费。 [- 非空：包周期计费。格式：order_id:product_id:region_id:project_id](tag:hws)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,ct)

        :param billing_info: The billing_info of this CreateLoadBalancerPublicIpOption.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def description(self):
        r"""Gets the description of this CreateLoadBalancerPublicIpOption.

        **参数解释**：弹性公网IP的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateLoadBalancerPublicIpOption.

        **参数解释**：弹性公网IP的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this CreateLoadBalancerPublicIpOption.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CreateLoadBalancerPublicIpOption.

        :return: The bandwidth of this CreateLoadBalancerPublicIpOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CreateLoadBalancerPublicIpOption.

        :param bandwidth: The bandwidth of this CreateLoadBalancerPublicIpOption.
        :type bandwidth: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerBandwidthOption`
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, CreateLoadBalancerPublicIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
