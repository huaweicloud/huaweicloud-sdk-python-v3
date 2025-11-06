# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'region_id': 'str',
        'provider': 'str',
        'id': 'str',
        'name': 'str',
        'tags': 'str',
        'vault_id': 'str',
        'vault_name': 'str',
        'resource_level_id': 'str',
        'resource_level_name': 'str',
        'compliance_result': 'str',
        'inventory_result': 'str',
        'compliance_rule_type': 'str',
        'compliance_rule_matched': 'bool',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'provider': 'provider',
        'id': 'id',
        'name': 'name',
        'tags': 'tags',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'resource_level_id': 'resource_level_id',
        'resource_level_name': 'resource_level_name',
        'compliance_result': 'compliance_result',
        'inventory_result': 'inventory_result',
        'compliance_rule_type': 'compliance_rule_type',
        'compliance_rule_matched': 'compliance_rule_matched',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, domain_id=None, region_id=None, provider=None, id=None, name=None, tags=None, vault_id=None, vault_name=None, resource_level_id=None, resource_level_name=None, compliance_result=None, inventory_result=None, compliance_rule_type=None, compliance_rule_matched=None, limit=None, marker=None):
        r"""ListResourcesRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param provider: 云服务类型，如ecs,evs,sfsturbo,workspace,rds,gaussdb
        :type provider: str
        :param id: 资源ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param tags: 标签列表, 标签值的格式为key或key&#x3D;value,用英文逗号分隔，最多支持5对标签的查询，超过5对的只生效前5对
        :type tags: str
        :param vault_id: CBR存储库ID
        :type vault_id: str
        :param vault_name: CBR存储库名称
        :type vault_name: str
        :param resource_level_id: 资源等级定义ID
        :type resource_level_id: str
        :param resource_level_name: 资源等级名称
        :type resource_level_name: str
        :param compliance_result: 资源合规结果,complete_match,partial_match,no_match
        :type compliance_result: str
        :param inventory_result: 资源保护状态,unprotected,protected
        :type inventory_result: str
        :param compliance_rule_type: 合规规则类型,local_backup_enabled,local_backup_retention,local_backup_frequency,remote_backup_enabled,remote_backup_retention,local_worm_enabledd,remote_worm_enabled,is_cross_account_backup_forced
        :type compliance_rule_type: str
        :param compliance_rule_matched: 合规规则是否符合，必须搭配compliance_rule_type使用
        :type compliance_rule_matched: bool
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._provider = None
        self._id = None
        self._name = None
        self._tags = None
        self._vault_id = None
        self._vault_name = None
        self._resource_level_id = None
        self._resource_level_name = None
        self._compliance_result = None
        self._inventory_result = None
        self._compliance_rule_type = None
        self._compliance_rule_matched = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if provider is not None:
            self.provider = provider
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if resource_level_id is not None:
            self.resource_level_id = resource_level_id
        if resource_level_name is not None:
            self.resource_level_name = resource_level_name
        if compliance_result is not None:
            self.compliance_result = compliance_result
        if inventory_result is not None:
            self.inventory_result = inventory_result
        if compliance_rule_type is not None:
            self.compliance_rule_type = compliance_rule_type
        if compliance_rule_matched is not None:
            self.compliance_rule_matched = compliance_rule_matched
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListResourcesRequest.

        账号ID

        :return: The domain_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListResourcesRequest.

        账号ID

        :param domain_id: The domain_id of this ListResourcesRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListResourcesRequest.

        区域ID

        :return: The region_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListResourcesRequest.

        区域ID

        :param region_id: The region_id of this ListResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def provider(self):
        r"""Gets the provider of this ListResourcesRequest.

        云服务类型，如ecs,evs,sfsturbo,workspace,rds,gaussdb

        :return: The provider of this ListResourcesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ListResourcesRequest.

        云服务类型，如ecs,evs,sfsturbo,workspace,rds,gaussdb

        :param provider: The provider of this ListResourcesRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def id(self):
        r"""Gets the id of this ListResourcesRequest.

        资源ID

        :return: The id of this ListResourcesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListResourcesRequest.

        资源ID

        :param id: The id of this ListResourcesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListResourcesRequest.

        资源名称

        :return: The name of this ListResourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListResourcesRequest.

        资源名称

        :param name: The name of this ListResourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this ListResourcesRequest.

        标签列表, 标签值的格式为key或key=value,用英文逗号分隔，最多支持5对标签的查询，超过5对的只生效前5对

        :return: The tags of this ListResourcesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListResourcesRequest.

        标签列表, 标签值的格式为key或key=value,用英文逗号分隔，最多支持5对标签的查询，超过5对的只生效前5对

        :param tags: The tags of this ListResourcesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ListResourcesRequest.

        CBR存储库ID

        :return: The vault_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ListResourcesRequest.

        CBR存储库ID

        :param vault_id: The vault_id of this ListResourcesRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this ListResourcesRequest.

        CBR存储库名称

        :return: The vault_name of this ListResourcesRequest.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this ListResourcesRequest.

        CBR存储库名称

        :param vault_name: The vault_name of this ListResourcesRequest.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def resource_level_id(self):
        r"""Gets the resource_level_id of this ListResourcesRequest.

        资源等级定义ID

        :return: The resource_level_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._resource_level_id

    @resource_level_id.setter
    def resource_level_id(self, resource_level_id):
        r"""Sets the resource_level_id of this ListResourcesRequest.

        资源等级定义ID

        :param resource_level_id: The resource_level_id of this ListResourcesRequest.
        :type resource_level_id: str
        """
        self._resource_level_id = resource_level_id

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this ListResourcesRequest.

        资源等级名称

        :return: The resource_level_name of this ListResourcesRequest.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this ListResourcesRequest.

        资源等级名称

        :param resource_level_name: The resource_level_name of this ListResourcesRequest.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def compliance_result(self):
        r"""Gets the compliance_result of this ListResourcesRequest.

        资源合规结果,complete_match,partial_match,no_match

        :return: The compliance_result of this ListResourcesRequest.
        :rtype: str
        """
        return self._compliance_result

    @compliance_result.setter
    def compliance_result(self, compliance_result):
        r"""Sets the compliance_result of this ListResourcesRequest.

        资源合规结果,complete_match,partial_match,no_match

        :param compliance_result: The compliance_result of this ListResourcesRequest.
        :type compliance_result: str
        """
        self._compliance_result = compliance_result

    @property
    def inventory_result(self):
        r"""Gets the inventory_result of this ListResourcesRequest.

        资源保护状态,unprotected,protected

        :return: The inventory_result of this ListResourcesRequest.
        :rtype: str
        """
        return self._inventory_result

    @inventory_result.setter
    def inventory_result(self, inventory_result):
        r"""Sets the inventory_result of this ListResourcesRequest.

        资源保护状态,unprotected,protected

        :param inventory_result: The inventory_result of this ListResourcesRequest.
        :type inventory_result: str
        """
        self._inventory_result = inventory_result

    @property
    def compliance_rule_type(self):
        r"""Gets the compliance_rule_type of this ListResourcesRequest.

        合规规则类型,local_backup_enabled,local_backup_retention,local_backup_frequency,remote_backup_enabled,remote_backup_retention,local_worm_enabledd,remote_worm_enabled,is_cross_account_backup_forced

        :return: The compliance_rule_type of this ListResourcesRequest.
        :rtype: str
        """
        return self._compliance_rule_type

    @compliance_rule_type.setter
    def compliance_rule_type(self, compliance_rule_type):
        r"""Sets the compliance_rule_type of this ListResourcesRequest.

        合规规则类型,local_backup_enabled,local_backup_retention,local_backup_frequency,remote_backup_enabled,remote_backup_retention,local_worm_enabledd,remote_worm_enabled,is_cross_account_backup_forced

        :param compliance_rule_type: The compliance_rule_type of this ListResourcesRequest.
        :type compliance_rule_type: str
        """
        self._compliance_rule_type = compliance_rule_type

    @property
    def compliance_rule_matched(self):
        r"""Gets the compliance_rule_matched of this ListResourcesRequest.

        合规规则是否符合，必须搭配compliance_rule_type使用

        :return: The compliance_rule_matched of this ListResourcesRequest.
        :rtype: bool
        """
        return self._compliance_rule_matched

    @compliance_rule_matched.setter
    def compliance_rule_matched(self, compliance_rule_matched):
        r"""Sets the compliance_rule_matched of this ListResourcesRequest.

        合规规则是否符合，必须搭配compliance_rule_type使用

        :param compliance_rule_matched: The compliance_rule_matched of this ListResourcesRequest.
        :type compliance_rule_matched: bool
        """
        self._compliance_rule_matched = compliance_rule_matched

    @property
    def limit(self):
        r"""Gets the limit of this ListResourcesRequest.

        最大的返回数量

        :return: The limit of this ListResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourcesRequest.

        最大的返回数量

        :param limit: The limit of this ListResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListResourcesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListResourcesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
