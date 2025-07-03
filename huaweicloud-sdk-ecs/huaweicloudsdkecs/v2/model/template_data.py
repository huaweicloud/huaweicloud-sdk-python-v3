# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'name': 'str',
        'description': 'str',
        'availability_zone_id': 'str',
        'enterprise_project_id': 'str',
        'auto_recovery': 'bool',
        'os_profile': 'TemplateOsProfile',
        'security_group_ids': 'list[str]',
        'network_interfaces': 'list[TemplateNetworkInterfaceOption]',
        'block_device_mappings': 'list[TemplateBlockDeviceMappingOption]',
        'market_options': 'TemplateMarketOptions',
        'internet_access': 'TemplateInternetAccessOption',
        'metadata': 'dict(str, str)',
        'tag_options': 'list[TemplateTagOptions]'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'name': 'name',
        'description': 'description',
        'availability_zone_id': 'availability_zone_id',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_recovery': 'auto_recovery',
        'os_profile': 'os_profile',
        'security_group_ids': 'security_group_ids',
        'network_interfaces': 'network_interfaces',
        'block_device_mappings': 'block_device_mappings',
        'market_options': 'market_options',
        'internet_access': 'internet_access',
        'metadata': 'metadata',
        'tag_options': 'tag_options'
    }

    def __init__(self, flavor_id=None, name=None, description=None, availability_zone_id=None, enterprise_project_id=None, auto_recovery=None, os_profile=None, security_group_ids=None, network_interfaces=None, block_device_mappings=None, market_options=None, internet_access=None, metadata=None, tag_options=None):
        r"""TemplateData

        The model defined in huaweicloud sdk

        :param flavor_id: 规格ID
        :type flavor_id: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param availability_zone_id: AZ
        :type availability_zone_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param auto_recovery: 开启自动恢复
        :type auto_recovery: bool
        :param os_profile: 
        :type os_profile: :class:`huaweicloudsdkecs.v2.TemplateOsProfile`
        :param security_group_ids: 安全组ID列表。全网卡生效。
        :type security_group_ids: list[str]
        :param network_interfaces: 
        :type network_interfaces: list[:class:`huaweicloudsdkecs.v2.TemplateNetworkInterfaceOption`]
        :param block_device_mappings: BDM挂载信息。按flavor限制为准。 1. 整机镜像，不修改卷属性，按原镜像配置创建。 2. 整机镜像，修改卷属性，要用户解开填写BDM。 3. 提供解镜像为BDM接口。
        :type block_device_mappings: list[:class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingOption`]
        :param market_options: 
        :type market_options: :class:`huaweicloudsdkecs.v2.TemplateMarketOptions`
        :param internet_access: 
        :type internet_access: :class:`huaweicloudsdkecs.v2.TemplateInternetAccessOption`
        :param metadata: 
        :type metadata: dict(str, str)
        :param tag_options: 创建虚拟机标签，目前仅支持给虚拟机打标签，后续会支持同时给相关资源如卷等打标签
        :type tag_options: list[:class:`huaweicloudsdkecs.v2.TemplateTagOptions`]
        """
        
        

        self._flavor_id = None
        self._name = None
        self._description = None
        self._availability_zone_id = None
        self._enterprise_project_id = None
        self._auto_recovery = None
        self._os_profile = None
        self._security_group_ids = None
        self._network_interfaces = None
        self._block_device_mappings = None
        self._market_options = None
        self._internet_access = None
        self._metadata = None
        self._tag_options = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_recovery is not None:
            self.auto_recovery = auto_recovery
        if os_profile is not None:
            self.os_profile = os_profile
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if block_device_mappings is not None:
            self.block_device_mappings = block_device_mappings
        if market_options is not None:
            self.market_options = market_options
        if internet_access is not None:
            self.internet_access = internet_access
        if metadata is not None:
            self.metadata = metadata
        if tag_options is not None:
            self.tag_options = tag_options

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this TemplateData.

        规格ID

        :return: The flavor_id of this TemplateData.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this TemplateData.

        规格ID

        :param flavor_id: The flavor_id of this TemplateData.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def name(self):
        r"""Gets the name of this TemplateData.

        名称

        :return: The name of this TemplateData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateData.

        名称

        :param name: The name of this TemplateData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TemplateData.

        描述

        :return: The description of this TemplateData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateData.

        描述

        :param description: The description of this TemplateData.
        :type description: str
        """
        self._description = description

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this TemplateData.

        AZ

        :return: The availability_zone_id of this TemplateData.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this TemplateData.

        AZ

        :param availability_zone_id: The availability_zone_id of this TemplateData.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this TemplateData.

        企业项目ID

        :return: The enterprise_project_id of this TemplateData.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this TemplateData.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this TemplateData.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_recovery(self):
        r"""Gets the auto_recovery of this TemplateData.

        开启自动恢复

        :return: The auto_recovery of this TemplateData.
        :rtype: bool
        """
        return self._auto_recovery

    @auto_recovery.setter
    def auto_recovery(self, auto_recovery):
        r"""Sets the auto_recovery of this TemplateData.

        开启自动恢复

        :param auto_recovery: The auto_recovery of this TemplateData.
        :type auto_recovery: bool
        """
        self._auto_recovery = auto_recovery

    @property
    def os_profile(self):
        r"""Gets the os_profile of this TemplateData.

        :return: The os_profile of this TemplateData.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateOsProfile`
        """
        return self._os_profile

    @os_profile.setter
    def os_profile(self, os_profile):
        r"""Sets the os_profile of this TemplateData.

        :param os_profile: The os_profile of this TemplateData.
        :type os_profile: :class:`huaweicloudsdkecs.v2.TemplateOsProfile`
        """
        self._os_profile = os_profile

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this TemplateData.

        安全组ID列表。全网卡生效。

        :return: The security_group_ids of this TemplateData.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this TemplateData.

        安全组ID列表。全网卡生效。

        :param security_group_ids: The security_group_ids of this TemplateData.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

    @property
    def network_interfaces(self):
        r"""Gets the network_interfaces of this TemplateData.

        :return: The network_interfaces of this TemplateData.
        :rtype: list[:class:`huaweicloudsdkecs.v2.TemplateNetworkInterfaceOption`]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        r"""Sets the network_interfaces of this TemplateData.

        :param network_interfaces: The network_interfaces of this TemplateData.
        :type network_interfaces: list[:class:`huaweicloudsdkecs.v2.TemplateNetworkInterfaceOption`]
        """
        self._network_interfaces = network_interfaces

    @property
    def block_device_mappings(self):
        r"""Gets the block_device_mappings of this TemplateData.

        BDM挂载信息。按flavor限制为准。 1. 整机镜像，不修改卷属性，按原镜像配置创建。 2. 整机镜像，修改卷属性，要用户解开填写BDM。 3. 提供解镜像为BDM接口。

        :return: The block_device_mappings of this TemplateData.
        :rtype: list[:class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingOption`]
        """
        return self._block_device_mappings

    @block_device_mappings.setter
    def block_device_mappings(self, block_device_mappings):
        r"""Sets the block_device_mappings of this TemplateData.

        BDM挂载信息。按flavor限制为准。 1. 整机镜像，不修改卷属性，按原镜像配置创建。 2. 整机镜像，修改卷属性，要用户解开填写BDM。 3. 提供解镜像为BDM接口。

        :param block_device_mappings: The block_device_mappings of this TemplateData.
        :type block_device_mappings: list[:class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingOption`]
        """
        self._block_device_mappings = block_device_mappings

    @property
    def market_options(self):
        r"""Gets the market_options of this TemplateData.

        :return: The market_options of this TemplateData.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateMarketOptions`
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        r"""Sets the market_options of this TemplateData.

        :param market_options: The market_options of this TemplateData.
        :type market_options: :class:`huaweicloudsdkecs.v2.TemplateMarketOptions`
        """
        self._market_options = market_options

    @property
    def internet_access(self):
        r"""Gets the internet_access of this TemplateData.

        :return: The internet_access of this TemplateData.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateInternetAccessOption`
        """
        return self._internet_access

    @internet_access.setter
    def internet_access(self, internet_access):
        r"""Sets the internet_access of this TemplateData.

        :param internet_access: The internet_access of this TemplateData.
        :type internet_access: :class:`huaweicloudsdkecs.v2.TemplateInternetAccessOption`
        """
        self._internet_access = internet_access

    @property
    def metadata(self):
        r"""Gets the metadata of this TemplateData.

        :return: The metadata of this TemplateData.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this TemplateData.

        :param metadata: The metadata of this TemplateData.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def tag_options(self):
        r"""Gets the tag_options of this TemplateData.

        创建虚拟机标签，目前仅支持给虚拟机打标签，后续会支持同时给相关资源如卷等打标签

        :return: The tag_options of this TemplateData.
        :rtype: list[:class:`huaweicloudsdkecs.v2.TemplateTagOptions`]
        """
        return self._tag_options

    @tag_options.setter
    def tag_options(self, tag_options):
        r"""Sets the tag_options of this TemplateData.

        创建虚拟机标签，目前仅支持给虚拟机打标签，后续会支持同时给相关资源如卷等打标签

        :param tag_options: The tag_options of this TemplateData.
        :type tag_options: list[:class:`huaweicloudsdkecs.v2.TemplateTagOptions`]
        """
        self._tag_options = tag_options

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
        if not isinstance(other, TemplateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
