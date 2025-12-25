# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc': 'str',
        'subnet': 'str',
        'security_group': 'str',
        'control_plane_security_group': 'str',
        'auto_generate_security_group_hardening_config': 'AutoGenerateSecurityGroupHardeningConfigSpec'
    }

    attribute_map = {
        'vpc': 'vpc',
        'subnet': 'subnet',
        'security_group': 'SecurityGroup',
        'control_plane_security_group': 'controlPlaneSecurityGroup',
        'auto_generate_security_group_hardening_config': 'autoGenerateSecurityGroupHardeningConfig'
    }

    def __init__(self, vpc=None, subnet=None, security_group=None, control_plane_security_group=None, auto_generate_security_group_hardening_config=None):
        r"""HostNetwork

        The model defined in huaweicloud sdk

        :param vpc: **参数解释：** 用于创建节点的VPC的ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询。   [链接请参见[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。](tag:hws)   [链接请参见[查询VPC列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_api01_0003.html)。](tag:hws_hk)  
        :type vpc: str
        :param subnet: **参数解释：** 用于创建节点的子网的网络ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的查询子网列表接口查询，获取响应中neutron_network_id字段的值。   [链接请参见[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。](tag:hws)   [链接请参见[查询子网列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)。](tag:hws_hk)  
        :type subnet: str
        :param security_group: 集群默认的Node节点安全组ID，不指定该字段系统将自动为用户创建默认Node节点安全组，指定该字段时集群将绑定指定的安全组。Node节点安全组需要放通部分端口来保证正常通信。[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 
        :type security_group: str
        :param control_plane_security_group: **参数解释：** 集群控制面节点安全组ID。 **约束限制：** 创建成功后自动生成，填写无效。 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type control_plane_security_group: str
        :param auto_generate_security_group_hardening_config: 
        :type auto_generate_security_group_hardening_config: :class:`huaweicloudsdkcce.v3.AutoGenerateSecurityGroupHardeningConfigSpec`
        """
        
        

        self._vpc = None
        self._subnet = None
        self._security_group = None
        self._control_plane_security_group = None
        self._auto_generate_security_group_hardening_config = None
        self.discriminator = None

        self.vpc = vpc
        self.subnet = subnet
        if security_group is not None:
            self.security_group = security_group
        if control_plane_security_group is not None:
            self.control_plane_security_group = control_plane_security_group
        if auto_generate_security_group_hardening_config is not None:
            self.auto_generate_security_group_hardening_config = auto_generate_security_group_hardening_config

    @property
    def vpc(self):
        r"""Gets the vpc of this HostNetwork.

        **参数解释：** 用于创建节点的VPC的ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询。   [链接请参见[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。](tag:hws)   [链接请参见[查询VPC列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_api01_0003.html)。](tag:hws_hk)  

        :return: The vpc of this HostNetwork.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this HostNetwork.

        **参数解释：** 用于创建节点的VPC的ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询。   [链接请参见[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。](tag:hws)   [链接请参见[查询VPC列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_api01_0003.html)。](tag:hws_hk)  

        :param vpc: The vpc of this HostNetwork.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def subnet(self):
        r"""Gets the subnet of this HostNetwork.

        **参数解释：** 用于创建节点的子网的网络ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的查询子网列表接口查询，获取响应中neutron_network_id字段的值。   [链接请参见[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。](tag:hws)   [链接请参见[查询子网列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)。](tag:hws_hk)  

        :return: The subnet of this HostNetwork.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        r"""Sets the subnet of this HostNetwork.

        **参数解释：** 用于创建节点的子网的网络ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的查询子网列表接口查询，获取响应中neutron_network_id字段的值。   [链接请参见[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。](tag:hws)   [链接请参见[查询子网列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)。](tag:hws_hk)  

        :param subnet: The subnet of this HostNetwork.
        :type subnet: str
        """
        self._subnet = subnet

    @property
    def security_group(self):
        r"""Gets the security_group of this HostNetwork.

        集群默认的Node节点安全组ID，不指定该字段系统将自动为用户创建默认Node节点安全组，指定该字段时集群将绑定指定的安全组。Node节点安全组需要放通部分端口来保证正常通信。[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 

        :return: The security_group of this HostNetwork.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this HostNetwork.

        集群默认的Node节点安全组ID，不指定该字段系统将自动为用户创建默认Node节点安全组，指定该字段时集群将绑定指定的安全组。Node节点安全组需要放通部分端口来保证正常通信。[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 

        :param security_group: The security_group of this HostNetwork.
        :type security_group: str
        """
        self._security_group = security_group

    @property
    def control_plane_security_group(self):
        r"""Gets the control_plane_security_group of this HostNetwork.

        **参数解释：** 集群控制面节点安全组ID。 **约束限制：** 创建成功后自动生成，填写无效。 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The control_plane_security_group of this HostNetwork.
        :rtype: str
        """
        return self._control_plane_security_group

    @control_plane_security_group.setter
    def control_plane_security_group(self, control_plane_security_group):
        r"""Sets the control_plane_security_group of this HostNetwork.

        **参数解释：** 集群控制面节点安全组ID。 **约束限制：** 创建成功后自动生成，填写无效。 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param control_plane_security_group: The control_plane_security_group of this HostNetwork.
        :type control_plane_security_group: str
        """
        self._control_plane_security_group = control_plane_security_group

    @property
    def auto_generate_security_group_hardening_config(self):
        r"""Gets the auto_generate_security_group_hardening_config of this HostNetwork.

        :return: The auto_generate_security_group_hardening_config of this HostNetwork.
        :rtype: :class:`huaweicloudsdkcce.v3.AutoGenerateSecurityGroupHardeningConfigSpec`
        """
        return self._auto_generate_security_group_hardening_config

    @auto_generate_security_group_hardening_config.setter
    def auto_generate_security_group_hardening_config(self, auto_generate_security_group_hardening_config):
        r"""Sets the auto_generate_security_group_hardening_config of this HostNetwork.

        :param auto_generate_security_group_hardening_config: The auto_generate_security_group_hardening_config of this HostNetwork.
        :type auto_generate_security_group_hardening_config: :class:`huaweicloudsdkcce.v3.AutoGenerateSecurityGroupHardeningConfigSpec`
        """
        self._auto_generate_security_group_hardening_config = auto_generate_security_group_hardening_config

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
        if not isinstance(other, HostNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
