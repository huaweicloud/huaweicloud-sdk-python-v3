# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'resource_name': 'str',
        'provider': 'str',
        'resource_type': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'resource_detail': 'dict(str, object)',
        'state': 'str',
        'resource_level': 'ResourceLevelBase',
        'is_level_manual': 'bool',
        'snapshot_backup_flag': 'bool',
        'local_backup_flag': 'bool',
        'remote_backup_flag': 'bool',
        'compliance_rule': 'ComplianceRule',
        'inventory_result': 'str',
        'local_vaults': 'list[str]',
        'remote_vaults': 'list[str]',
        'compliance_result': 'str',
        'compliance_detail': 'str',
        'tags': 'list[TagItem]',
        'domain_id': 'str',
        'resource_created': 'int',
        'resource_updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'resource_name': 'resource_name',
        'provider': 'provider',
        'resource_type': 'resource_type',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'resource_detail': 'resource_detail',
        'state': 'state',
        'resource_level': 'resource_level',
        'is_level_manual': 'is_level_manual',
        'snapshot_backup_flag': 'snapshot_backup_flag',
        'local_backup_flag': 'local_backup_flag',
        'remote_backup_flag': 'remote_backup_flag',
        'compliance_rule': 'compliance_rule',
        'inventory_result': 'inventory_result',
        'local_vaults': 'local_vaults',
        'remote_vaults': 'remote_vaults',
        'compliance_result': 'compliance_result',
        'compliance_detail': 'compliance_detail',
        'tags': 'tags',
        'domain_id': 'domain_id',
        'resource_created': 'resource_created',
        'resource_updated': 'resource_updated'
    }

    def __init__(self, id=None, resource_name=None, provider=None, resource_type=None, region_id=None, project_id=None, project_name=None, ep_id=None, ep_name=None, resource_detail=None, state=None, resource_level=None, is_level_manual=None, snapshot_backup_flag=None, local_backup_flag=None, remote_backup_flag=None, compliance_rule=None, inventory_result=None, local_vaults=None, remote_vaults=None, compliance_result=None, compliance_detail=None, tags=None, domain_id=None, resource_created=None, resource_updated=None):
        r"""ShowResourceDetailResponse

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param provider: 云服务名称
        :type provider: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param region_id: 区域ID
        :type region_id: str
        :param project_id: Openstack中的项目ID
        :type project_id: str
        :param project_name: Openstack中的项目名称
        :type project_name: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param ep_name: 企业项目名称
        :type ep_name: str
        :param resource_detail: 资源详细属性
        :type resource_detail: dict(str, object)
        :param state: 资源状态
        :type state: str
        :param resource_level: 
        :type resource_level: :class:`huaweicloudsdkbcc.v1.ResourceLevelBase`
        :param is_level_manual: 等级是否手动指定
        :type is_level_manual: bool
        :param snapshot_backup_flag: 快照备份是否开启
        :type snapshot_backup_flag: bool
        :param local_backup_flag: 本地备份是否开启
        :type local_backup_flag: bool
        :param remote_backup_flag: 异地备份是否开启
        :type remote_backup_flag: bool
        :param compliance_rule: 
        :type compliance_rule: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        :param inventory_result: 资源保护状态
        :type inventory_result: str
        :param local_vaults: 本地备份存储库
        :type local_vaults: list[str]
        :param remote_vaults: 异地备份存储库
        :type remote_vaults: list[str]
        :param compliance_result: 资产合规盘点结果
        :type compliance_result: str
        :param compliance_detail: 资产合规盘点明细，合规校验针对local_backup_enabled,local_backup_frequency, local_worm_enabled, local_backup_retention 等每一项都给出规则要求值，资源实际值，是否满足匹配。结合多项给出最终的匹配结果。
        :type compliance_detail: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkbcc.v1.TagItem`]
        :param domain_id: 账户ID
        :type domain_id: str
        :param resource_created: 资源创建时间
        :type resource_created: int
        :param resource_updated: 资源更新时间
        :type resource_updated: int
        """
        
        super(ShowResourceDetailResponse, self).__init__()

        self._id = None
        self._resource_name = None
        self._provider = None
        self._resource_type = None
        self._region_id = None
        self._project_id = None
        self._project_name = None
        self._ep_id = None
        self._ep_name = None
        self._resource_detail = None
        self._state = None
        self._resource_level = None
        self._is_level_manual = None
        self._snapshot_backup_flag = None
        self._local_backup_flag = None
        self._remote_backup_flag = None
        self._compliance_rule = None
        self._inventory_result = None
        self._local_vaults = None
        self._remote_vaults = None
        self._compliance_result = None
        self._compliance_detail = None
        self._tags = None
        self._domain_id = None
        self._resource_created = None
        self._resource_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_name is not None:
            self.resource_name = resource_name
        if provider is not None:
            self.provider = provider
        if resource_type is not None:
            self.resource_type = resource_type
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if resource_detail is not None:
            self.resource_detail = resource_detail
        if state is not None:
            self.state = state
        if resource_level is not None:
            self.resource_level = resource_level
        if is_level_manual is not None:
            self.is_level_manual = is_level_manual
        if snapshot_backup_flag is not None:
            self.snapshot_backup_flag = snapshot_backup_flag
        if local_backup_flag is not None:
            self.local_backup_flag = local_backup_flag
        if remote_backup_flag is not None:
            self.remote_backup_flag = remote_backup_flag
        if compliance_rule is not None:
            self.compliance_rule = compliance_rule
        if inventory_result is not None:
            self.inventory_result = inventory_result
        if local_vaults is not None:
            self.local_vaults = local_vaults
        if remote_vaults is not None:
            self.remote_vaults = remote_vaults
        if compliance_result is not None:
            self.compliance_result = compliance_result
        if compliance_detail is not None:
            self.compliance_detail = compliance_detail
        if tags is not None:
            self.tags = tags
        if domain_id is not None:
            self.domain_id = domain_id
        if resource_created is not None:
            self.resource_created = resource_created
        if resource_updated is not None:
            self.resource_updated = resource_updated

    @property
    def id(self):
        r"""Gets the id of this ShowResourceDetailResponse.

        资源ID

        :return: The id of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowResourceDetailResponse.

        资源ID

        :param id: The id of this ShowResourceDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ShowResourceDetailResponse.

        资源名称

        :return: The resource_name of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ShowResourceDetailResponse.

        资源名称

        :param resource_name: The resource_name of this ShowResourceDetailResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def provider(self):
        r"""Gets the provider of this ShowResourceDetailResponse.

        云服务名称

        :return: The provider of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ShowResourceDetailResponse.

        云服务名称

        :param provider: The provider of this ShowResourceDetailResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowResourceDetailResponse.

        资源类型

        :return: The resource_type of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowResourceDetailResponse.

        资源类型

        :param resource_type: The resource_type of this ShowResourceDetailResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowResourceDetailResponse.

        区域ID

        :return: The region_id of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowResourceDetailResponse.

        区域ID

        :param region_id: The region_id of this ShowResourceDetailResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowResourceDetailResponse.

        Openstack中的项目ID

        :return: The project_id of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowResourceDetailResponse.

        Openstack中的项目ID

        :param project_id: The project_id of this ShowResourceDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowResourceDetailResponse.

        Openstack中的项目名称

        :return: The project_name of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowResourceDetailResponse.

        Openstack中的项目名称

        :param project_name: The project_name of this ShowResourceDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ShowResourceDetailResponse.

        企业项目ID

        :return: The ep_id of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ShowResourceDetailResponse.

        企业项目ID

        :param ep_id: The ep_id of this ShowResourceDetailResponse.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ShowResourceDetailResponse.

        企业项目名称

        :return: The ep_name of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ShowResourceDetailResponse.

        企业项目名称

        :param ep_name: The ep_name of this ShowResourceDetailResponse.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this ShowResourceDetailResponse.

        资源详细属性

        :return: The resource_detail of this ShowResourceDetailResponse.
        :rtype: dict(str, object)
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this ShowResourceDetailResponse.

        资源详细属性

        :param resource_detail: The resource_detail of this ShowResourceDetailResponse.
        :type resource_detail: dict(str, object)
        """
        self._resource_detail = resource_detail

    @property
    def state(self):
        r"""Gets the state of this ShowResourceDetailResponse.

        资源状态

        :return: The state of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowResourceDetailResponse.

        资源状态

        :param state: The state of this ShowResourceDetailResponse.
        :type state: str
        """
        self._state = state

    @property
    def resource_level(self):
        r"""Gets the resource_level of this ShowResourceDetailResponse.

        :return: The resource_level of this ShowResourceDetailResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ResourceLevelBase`
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this ShowResourceDetailResponse.

        :param resource_level: The resource_level of this ShowResourceDetailResponse.
        :type resource_level: :class:`huaweicloudsdkbcc.v1.ResourceLevelBase`
        """
        self._resource_level = resource_level

    @property
    def is_level_manual(self):
        r"""Gets the is_level_manual of this ShowResourceDetailResponse.

        等级是否手动指定

        :return: The is_level_manual of this ShowResourceDetailResponse.
        :rtype: bool
        """
        return self._is_level_manual

    @is_level_manual.setter
    def is_level_manual(self, is_level_manual):
        r"""Sets the is_level_manual of this ShowResourceDetailResponse.

        等级是否手动指定

        :param is_level_manual: The is_level_manual of this ShowResourceDetailResponse.
        :type is_level_manual: bool
        """
        self._is_level_manual = is_level_manual

    @property
    def snapshot_backup_flag(self):
        r"""Gets the snapshot_backup_flag of this ShowResourceDetailResponse.

        快照备份是否开启

        :return: The snapshot_backup_flag of this ShowResourceDetailResponse.
        :rtype: bool
        """
        return self._snapshot_backup_flag

    @snapshot_backup_flag.setter
    def snapshot_backup_flag(self, snapshot_backup_flag):
        r"""Sets the snapshot_backup_flag of this ShowResourceDetailResponse.

        快照备份是否开启

        :param snapshot_backup_flag: The snapshot_backup_flag of this ShowResourceDetailResponse.
        :type snapshot_backup_flag: bool
        """
        self._snapshot_backup_flag = snapshot_backup_flag

    @property
    def local_backup_flag(self):
        r"""Gets the local_backup_flag of this ShowResourceDetailResponse.

        本地备份是否开启

        :return: The local_backup_flag of this ShowResourceDetailResponse.
        :rtype: bool
        """
        return self._local_backup_flag

    @local_backup_flag.setter
    def local_backup_flag(self, local_backup_flag):
        r"""Sets the local_backup_flag of this ShowResourceDetailResponse.

        本地备份是否开启

        :param local_backup_flag: The local_backup_flag of this ShowResourceDetailResponse.
        :type local_backup_flag: bool
        """
        self._local_backup_flag = local_backup_flag

    @property
    def remote_backup_flag(self):
        r"""Gets the remote_backup_flag of this ShowResourceDetailResponse.

        异地备份是否开启

        :return: The remote_backup_flag of this ShowResourceDetailResponse.
        :rtype: bool
        """
        return self._remote_backup_flag

    @remote_backup_flag.setter
    def remote_backup_flag(self, remote_backup_flag):
        r"""Sets the remote_backup_flag of this ShowResourceDetailResponse.

        异地备份是否开启

        :param remote_backup_flag: The remote_backup_flag of this ShowResourceDetailResponse.
        :type remote_backup_flag: bool
        """
        self._remote_backup_flag = remote_backup_flag

    @property
    def compliance_rule(self):
        r"""Gets the compliance_rule of this ShowResourceDetailResponse.

        :return: The compliance_rule of this ShowResourceDetailResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        """
        return self._compliance_rule

    @compliance_rule.setter
    def compliance_rule(self, compliance_rule):
        r"""Sets the compliance_rule of this ShowResourceDetailResponse.

        :param compliance_rule: The compliance_rule of this ShowResourceDetailResponse.
        :type compliance_rule: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        """
        self._compliance_rule = compliance_rule

    @property
    def inventory_result(self):
        r"""Gets the inventory_result of this ShowResourceDetailResponse.

        资源保护状态

        :return: The inventory_result of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._inventory_result

    @inventory_result.setter
    def inventory_result(self, inventory_result):
        r"""Sets the inventory_result of this ShowResourceDetailResponse.

        资源保护状态

        :param inventory_result: The inventory_result of this ShowResourceDetailResponse.
        :type inventory_result: str
        """
        self._inventory_result = inventory_result

    @property
    def local_vaults(self):
        r"""Gets the local_vaults of this ShowResourceDetailResponse.

        本地备份存储库

        :return: The local_vaults of this ShowResourceDetailResponse.
        :rtype: list[str]
        """
        return self._local_vaults

    @local_vaults.setter
    def local_vaults(self, local_vaults):
        r"""Sets the local_vaults of this ShowResourceDetailResponse.

        本地备份存储库

        :param local_vaults: The local_vaults of this ShowResourceDetailResponse.
        :type local_vaults: list[str]
        """
        self._local_vaults = local_vaults

    @property
    def remote_vaults(self):
        r"""Gets the remote_vaults of this ShowResourceDetailResponse.

        异地备份存储库

        :return: The remote_vaults of this ShowResourceDetailResponse.
        :rtype: list[str]
        """
        return self._remote_vaults

    @remote_vaults.setter
    def remote_vaults(self, remote_vaults):
        r"""Sets the remote_vaults of this ShowResourceDetailResponse.

        异地备份存储库

        :param remote_vaults: The remote_vaults of this ShowResourceDetailResponse.
        :type remote_vaults: list[str]
        """
        self._remote_vaults = remote_vaults

    @property
    def compliance_result(self):
        r"""Gets the compliance_result of this ShowResourceDetailResponse.

        资产合规盘点结果

        :return: The compliance_result of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._compliance_result

    @compliance_result.setter
    def compliance_result(self, compliance_result):
        r"""Sets the compliance_result of this ShowResourceDetailResponse.

        资产合规盘点结果

        :param compliance_result: The compliance_result of this ShowResourceDetailResponse.
        :type compliance_result: str
        """
        self._compliance_result = compliance_result

    @property
    def compliance_detail(self):
        r"""Gets the compliance_detail of this ShowResourceDetailResponse.

        资产合规盘点明细，合规校验针对local_backup_enabled,local_backup_frequency, local_worm_enabled, local_backup_retention 等每一项都给出规则要求值，资源实际值，是否满足匹配。结合多项给出最终的匹配结果。

        :return: The compliance_detail of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._compliance_detail

    @compliance_detail.setter
    def compliance_detail(self, compliance_detail):
        r"""Sets the compliance_detail of this ShowResourceDetailResponse.

        资产合规盘点明细，合规校验针对local_backup_enabled,local_backup_frequency, local_worm_enabled, local_backup_retention 等每一项都给出规则要求值，资源实际值，是否满足匹配。结合多项给出最终的匹配结果。

        :param compliance_detail: The compliance_detail of this ShowResourceDetailResponse.
        :type compliance_detail: str
        """
        self._compliance_detail = compliance_detail

    @property
    def tags(self):
        r"""Gets the tags of this ShowResourceDetailResponse.

        标签

        :return: The tags of this ShowResourceDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.TagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowResourceDetailResponse.

        标签

        :param tags: The tags of this ShowResourceDetailResponse.
        :type tags: list[:class:`huaweicloudsdkbcc.v1.TagItem`]
        """
        self._tags = tags

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowResourceDetailResponse.

        账户ID

        :return: The domain_id of this ShowResourceDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowResourceDetailResponse.

        账户ID

        :param domain_id: The domain_id of this ShowResourceDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resource_created(self):
        r"""Gets the resource_created of this ShowResourceDetailResponse.

        资源创建时间

        :return: The resource_created of this ShowResourceDetailResponse.
        :rtype: int
        """
        return self._resource_created

    @resource_created.setter
    def resource_created(self, resource_created):
        r"""Sets the resource_created of this ShowResourceDetailResponse.

        资源创建时间

        :param resource_created: The resource_created of this ShowResourceDetailResponse.
        :type resource_created: int
        """
        self._resource_created = resource_created

    @property
    def resource_updated(self):
        r"""Gets the resource_updated of this ShowResourceDetailResponse.

        资源更新时间

        :return: The resource_updated of this ShowResourceDetailResponse.
        :rtype: int
        """
        return self._resource_updated

    @resource_updated.setter
    def resource_updated(self, resource_updated):
        r"""Sets the resource_updated of this ShowResourceDetailResponse.

        资源更新时间

        :param resource_updated: The resource_updated of this ShowResourceDetailResponse.
        :type resource_updated: int
        """
        self._resource_updated = resource_updated

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
        if not isinstance(other, ShowResourceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
