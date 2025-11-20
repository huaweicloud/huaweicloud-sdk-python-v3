# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInformationSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'description': 'str',
        'custom_san': 'list[str]',
        'container_network': 'ContainerNetworkUpdate',
        'eni_network': 'EniNetworkUpdate',
        'host_network': 'ClusterInformationSpecHostNetwork',
        'deletion_protection': 'bool'
    }

    attribute_map = {
        'agency_name': 'agencyName',
        'description': 'description',
        'custom_san': 'customSan',
        'container_network': 'containerNetwork',
        'eni_network': 'eniNetwork',
        'host_network': 'hostNetwork',
        'deletion_protection': 'deletionProtection'
    }

    def __init__(self, agency_name=None, description=None, custom_san=None, container_network=None, eni_network=None, host_network=None, deletion_protection=None):
        r"""ClusterInformationSpec

        The model defined in huaweicloud sdk

        :param agency_name: **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。当不传或为空时，集群将自动选择使用CCE的系统委托cce_admin_trust或cce_cluster_agency。  [ &gt; 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ &gt; 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅1.27及以上版本集群支持该参数  **取值范围：** 不涉及 **默认取值：** 空 
        :type agency_name: str
        :param description: **参数解释：** 集群的描述信息。 **约束限制：** 仅运行和扩容状态（Available、ScalingUp、ScalingDown）的集群允许修改。 **取值范围：** 字符取值范围[0,200]。不包含~$%^&amp;*&lt;&gt;[]{}()&#39;\&quot;#\\等特殊字符。 **默认取值：** 无
        :type description: str
        :param custom_san: 集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: &#x60;&#x60;&#x60; SAN 1: DNS Name&#x3D;example.com SAN 2: DNS Name&#x3D;www.example.com SAN 3: DNS Name&#x3D;example.net SAN 4: IP Address&#x3D;93.184.216.34 &#x60;&#x60;&#x60;
        :type custom_san: list[str]
        :param container_network: 
        :type container_network: :class:`huaweicloudsdkcce.v3.ContainerNetworkUpdate`
        :param eni_network: 
        :type eni_network: :class:`huaweicloudsdkcce.v3.EniNetworkUpdate`
        :param host_network: 
        :type host_network: :class:`huaweicloudsdkcce.v3.ClusterInformationSpecHostNetwork`
        :param deletion_protection: **参数解释：** 集群删除保护，如果开启后用户将无法删除该集群。 **约束限制：** 不涉及 **取值范围：** - true: 开启集群删除保护 - false: 关闭集群删除保护  **默认取值：** 默认false
        :type deletion_protection: bool
        """
        
        

        self._agency_name = None
        self._description = None
        self._custom_san = None
        self._container_network = None
        self._eni_network = None
        self._host_network = None
        self._deletion_protection = None
        self.discriminator = None

        if agency_name is not None:
            self.agency_name = agency_name
        if description is not None:
            self.description = description
        if custom_san is not None:
            self.custom_san = custom_san
        if container_network is not None:
            self.container_network = container_network
        if eni_network is not None:
            self.eni_network = eni_network
        if host_network is not None:
            self.host_network = host_network
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ClusterInformationSpec.

        **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。当不传或为空时，集群将自动选择使用CCE的系统委托cce_admin_trust或cce_cluster_agency。  [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅1.27及以上版本集群支持该参数  **取值范围：** 不涉及 **默认取值：** 空 

        :return: The agency_name of this ClusterInformationSpec.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ClusterInformationSpec.

        **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。当不传或为空时，集群将自动选择使用CCE的系统委托cce_admin_trust或cce_cluster_agency。  [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅1.27及以上版本集群支持该参数  **取值范围：** 不涉及 **默认取值：** 空 

        :param agency_name: The agency_name of this ClusterInformationSpec.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def description(self):
        r"""Gets the description of this ClusterInformationSpec.

        **参数解释：** 集群的描述信息。 **约束限制：** 仅运行和扩容状态（Available、ScalingUp、ScalingDown）的集群允许修改。 **取值范围：** 字符取值范围[0,200]。不包含~$%^&*<>[]{}()'\"#\\等特殊字符。 **默认取值：** 无

        :return: The description of this ClusterInformationSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterInformationSpec.

        **参数解释：** 集群的描述信息。 **约束限制：** 仅运行和扩容状态（Available、ScalingUp、ScalingDown）的集群允许修改。 **取值范围：** 字符取值范围[0,200]。不包含~$%^&*<>[]{}()'\"#\\等特殊字符。 **默认取值：** 无

        :param description: The description of this ClusterInformationSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        r"""Gets the custom_san of this ClusterInformationSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :return: The custom_san of this ClusterInformationSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        r"""Sets the custom_san of this ClusterInformationSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :param custom_san: The custom_san of this ClusterInformationSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def container_network(self):
        r"""Gets the container_network of this ClusterInformationSpec.

        :return: The container_network of this ClusterInformationSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ContainerNetworkUpdate`
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        r"""Sets the container_network of this ClusterInformationSpec.

        :param container_network: The container_network of this ClusterInformationSpec.
        :type container_network: :class:`huaweicloudsdkcce.v3.ContainerNetworkUpdate`
        """
        self._container_network = container_network

    @property
    def eni_network(self):
        r"""Gets the eni_network of this ClusterInformationSpec.

        :return: The eni_network of this ClusterInformationSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.EniNetworkUpdate`
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        r"""Sets the eni_network of this ClusterInformationSpec.

        :param eni_network: The eni_network of this ClusterInformationSpec.
        :type eni_network: :class:`huaweicloudsdkcce.v3.EniNetworkUpdate`
        """
        self._eni_network = eni_network

    @property
    def host_network(self):
        r"""Gets the host_network of this ClusterInformationSpec.

        :return: The host_network of this ClusterInformationSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterInformationSpecHostNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        r"""Sets the host_network of this ClusterInformationSpec.

        :param host_network: The host_network of this ClusterInformationSpec.
        :type host_network: :class:`huaweicloudsdkcce.v3.ClusterInformationSpecHostNetwork`
        """
        self._host_network = host_network

    @property
    def deletion_protection(self):
        r"""Gets the deletion_protection of this ClusterInformationSpec.

        **参数解释：** 集群删除保护，如果开启后用户将无法删除该集群。 **约束限制：** 不涉及 **取值范围：** - true: 开启集群删除保护 - false: 关闭集群删除保护  **默认取值：** 默认false

        :return: The deletion_protection of this ClusterInformationSpec.
        :rtype: bool
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        r"""Sets the deletion_protection of this ClusterInformationSpec.

        **参数解释：** 集群删除保护，如果开启后用户将无法删除该集群。 **约束限制：** 不涉及 **取值范围：** - true: 开启集群删除保护 - false: 关闭集群删除保护  **默认取值：** 默认false

        :param deletion_protection: The deletion_protection of this ClusterInformationSpec.
        :type deletion_protection: bool
        """
        self._deletion_protection = deletion_protection

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
        if not isinstance(other, ClusterInformationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
