# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMetaLabels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_name': 'str',
        'os_modelarts_workspace_id': 'str',
        'os_modelarts_node_prefix': 'str',
        'os_modelarts_resource_id': 'str',
        'os_modelarts_tenant_domain_id': 'str',
        'os_modelarts_tenant_project_id': 'str',
        'os_modelarts_enterprise_project_id': 'str',
        'os_modelarts_pool_biz': 'str',
        'os_modelarts_create_from': 'str',
        'os_modelarts_nobilling': 'str',
        'os_modelarts_order_name': 'str',
        'os_modelarts_region': 'str'
    }

    attribute_map = {
        'os_modelarts_name': 'os.modelarts/name',
        'os_modelarts_workspace_id': 'os.modelarts/workspace.id',
        'os_modelarts_node_prefix': 'os.modelarts/node.prefix',
        'os_modelarts_resource_id': 'os.modelarts/resource.id',
        'os_modelarts_tenant_domain_id': 'os.modelarts/tenant.domain.id',
        'os_modelarts_tenant_project_id': 'os.modelarts/tenant.project.id',
        'os_modelarts_enterprise_project_id': 'os.modelarts/enterprise.project.id',
        'os_modelarts_pool_biz': 'os.modelarts.pool/biz',
        'os_modelarts_create_from': 'os.modelarts/create-from',
        'os_modelarts_nobilling': 'os.modelarts/nobilling',
        'os_modelarts_order_name': 'os.modelarts/order.name',
        'os_modelarts_region': 'os.modelarts/region'
    }

    def __init__(self, os_modelarts_name=None, os_modelarts_workspace_id=None, os_modelarts_node_prefix=None, os_modelarts_resource_id=None, os_modelarts_tenant_domain_id=None, os_modelarts_tenant_project_id=None, os_modelarts_enterprise_project_id=None, os_modelarts_pool_biz=None, os_modelarts_create_from=None, os_modelarts_nobilling=None, os_modelarts_order_name=None, os_modelarts_region=None):
        r"""PoolMetaLabels

        The model defined in huaweicloud sdk

        :param os_modelarts_name: **参数解释**：资源池的显示名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_name: str
        :param os_modelarts_workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。
        :type os_modelarts_workspace_id: str
        :param os_modelarts_node_prefix: **参数解释**：自定义节点前缀，可选值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_node_prefix: str
        :param os_modelarts_resource_id: **参数解释**：资源池计费使用的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_resource_id: str
        :param os_modelarts_tenant_domain_id: **参数解释**：资源池所属的租户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_tenant_domain_id: str
        :param os_modelarts_tenant_project_id: **参数解释**：资源池所属的租户项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_tenant_project_id: str
        :param os_modelarts_enterprise_project_id: **参数解释**：资源池所属的企业项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_enterprise_project_id: str
        :param os_modelarts_pool_biz: **参数解释**：资源池商业类型，public是公共池，private个人专属池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_pool_biz: str
        :param os_modelarts_create_from: **参数解释**：资源池创建来源，比如admin-console，标记来自admin创建，console标记来自ma console。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_create_from: str
        :param os_modelarts_nobilling: **参数解释**：资源池是否计费。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_nobilling: str
        :param os_modelarts_order_name: **参数解释**：资源池关联的上一次订单作业记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_order_name: str
        :param os_modelarts_region: **参数解释**：资源池所属区域。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_region: str
        """
        
        

        self._os_modelarts_name = None
        self._os_modelarts_workspace_id = None
        self._os_modelarts_node_prefix = None
        self._os_modelarts_resource_id = None
        self._os_modelarts_tenant_domain_id = None
        self._os_modelarts_tenant_project_id = None
        self._os_modelarts_enterprise_project_id = None
        self._os_modelarts_pool_biz = None
        self._os_modelarts_create_from = None
        self._os_modelarts_nobilling = None
        self._os_modelarts_order_name = None
        self._os_modelarts_region = None
        self.discriminator = None

        if os_modelarts_name is not None:
            self.os_modelarts_name = os_modelarts_name
        if os_modelarts_workspace_id is not None:
            self.os_modelarts_workspace_id = os_modelarts_workspace_id
        if os_modelarts_node_prefix is not None:
            self.os_modelarts_node_prefix = os_modelarts_node_prefix
        if os_modelarts_resource_id is not None:
            self.os_modelarts_resource_id = os_modelarts_resource_id
        if os_modelarts_tenant_domain_id is not None:
            self.os_modelarts_tenant_domain_id = os_modelarts_tenant_domain_id
        if os_modelarts_tenant_project_id is not None:
            self.os_modelarts_tenant_project_id = os_modelarts_tenant_project_id
        if os_modelarts_enterprise_project_id is not None:
            self.os_modelarts_enterprise_project_id = os_modelarts_enterprise_project_id
        if os_modelarts_pool_biz is not None:
            self.os_modelarts_pool_biz = os_modelarts_pool_biz
        if os_modelarts_create_from is not None:
            self.os_modelarts_create_from = os_modelarts_create_from
        if os_modelarts_nobilling is not None:
            self.os_modelarts_nobilling = os_modelarts_nobilling
        if os_modelarts_order_name is not None:
            self.os_modelarts_order_name = os_modelarts_order_name
        if os_modelarts_region is not None:
            self.os_modelarts_region = os_modelarts_region

    @property
    def os_modelarts_name(self):
        r"""Gets the os_modelarts_name of this PoolMetaLabels.

        **参数解释**：资源池的显示名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_name of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_name

    @os_modelarts_name.setter
    def os_modelarts_name(self, os_modelarts_name):
        r"""Sets the os_modelarts_name of this PoolMetaLabels.

        **参数解释**：资源池的显示名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_name: The os_modelarts_name of this PoolMetaLabels.
        :type os_modelarts_name: str
        """
        self._os_modelarts_name = os_modelarts_name

    @property
    def os_modelarts_workspace_id(self):
        r"""Gets the os_modelarts_workspace_id of this PoolMetaLabels.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The os_modelarts_workspace_id of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_workspace_id

    @os_modelarts_workspace_id.setter
    def os_modelarts_workspace_id(self, os_modelarts_workspace_id):
        r"""Sets the os_modelarts_workspace_id of this PoolMetaLabels.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :param os_modelarts_workspace_id: The os_modelarts_workspace_id of this PoolMetaLabels.
        :type os_modelarts_workspace_id: str
        """
        self._os_modelarts_workspace_id = os_modelarts_workspace_id

    @property
    def os_modelarts_node_prefix(self):
        r"""Gets the os_modelarts_node_prefix of this PoolMetaLabels.

        **参数解释**：自定义节点前缀，可选值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_node_prefix of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_node_prefix

    @os_modelarts_node_prefix.setter
    def os_modelarts_node_prefix(self, os_modelarts_node_prefix):
        r"""Sets the os_modelarts_node_prefix of this PoolMetaLabels.

        **参数解释**：自定义节点前缀，可选值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_node_prefix: The os_modelarts_node_prefix of this PoolMetaLabels.
        :type os_modelarts_node_prefix: str
        """
        self._os_modelarts_node_prefix = os_modelarts_node_prefix

    @property
    def os_modelarts_resource_id(self):
        r"""Gets the os_modelarts_resource_id of this PoolMetaLabels.

        **参数解释**：资源池计费使用的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_resource_id of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_resource_id

    @os_modelarts_resource_id.setter
    def os_modelarts_resource_id(self, os_modelarts_resource_id):
        r"""Sets the os_modelarts_resource_id of this PoolMetaLabels.

        **参数解释**：资源池计费使用的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_resource_id: The os_modelarts_resource_id of this PoolMetaLabels.
        :type os_modelarts_resource_id: str
        """
        self._os_modelarts_resource_id = os_modelarts_resource_id

    @property
    def os_modelarts_tenant_domain_id(self):
        r"""Gets the os_modelarts_tenant_domain_id of this PoolMetaLabels.

        **参数解释**：资源池所属的租户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_tenant_domain_id of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_tenant_domain_id

    @os_modelarts_tenant_domain_id.setter
    def os_modelarts_tenant_domain_id(self, os_modelarts_tenant_domain_id):
        r"""Sets the os_modelarts_tenant_domain_id of this PoolMetaLabels.

        **参数解释**：资源池所属的租户ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_tenant_domain_id: The os_modelarts_tenant_domain_id of this PoolMetaLabels.
        :type os_modelarts_tenant_domain_id: str
        """
        self._os_modelarts_tenant_domain_id = os_modelarts_tenant_domain_id

    @property
    def os_modelarts_tenant_project_id(self):
        r"""Gets the os_modelarts_tenant_project_id of this PoolMetaLabels.

        **参数解释**：资源池所属的租户项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_tenant_project_id of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_tenant_project_id

    @os_modelarts_tenant_project_id.setter
    def os_modelarts_tenant_project_id(self, os_modelarts_tenant_project_id):
        r"""Sets the os_modelarts_tenant_project_id of this PoolMetaLabels.

        **参数解释**：资源池所属的租户项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_tenant_project_id: The os_modelarts_tenant_project_id of this PoolMetaLabels.
        :type os_modelarts_tenant_project_id: str
        """
        self._os_modelarts_tenant_project_id = os_modelarts_tenant_project_id

    @property
    def os_modelarts_enterprise_project_id(self):
        r"""Gets the os_modelarts_enterprise_project_id of this PoolMetaLabels.

        **参数解释**：资源池所属的企业项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_enterprise_project_id of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_enterprise_project_id

    @os_modelarts_enterprise_project_id.setter
    def os_modelarts_enterprise_project_id(self, os_modelarts_enterprise_project_id):
        r"""Sets the os_modelarts_enterprise_project_id of this PoolMetaLabels.

        **参数解释**：资源池所属的企业项目ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_enterprise_project_id: The os_modelarts_enterprise_project_id of this PoolMetaLabels.
        :type os_modelarts_enterprise_project_id: str
        """
        self._os_modelarts_enterprise_project_id = os_modelarts_enterprise_project_id

    @property
    def os_modelarts_pool_biz(self):
        r"""Gets the os_modelarts_pool_biz of this PoolMetaLabels.

        **参数解释**：资源池商业类型，public是公共池，private个人专属池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_pool_biz of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_pool_biz

    @os_modelarts_pool_biz.setter
    def os_modelarts_pool_biz(self, os_modelarts_pool_biz):
        r"""Sets the os_modelarts_pool_biz of this PoolMetaLabels.

        **参数解释**：资源池商业类型，public是公共池，private个人专属池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_pool_biz: The os_modelarts_pool_biz of this PoolMetaLabels.
        :type os_modelarts_pool_biz: str
        """
        self._os_modelarts_pool_biz = os_modelarts_pool_biz

    @property
    def os_modelarts_create_from(self):
        r"""Gets the os_modelarts_create_from of this PoolMetaLabels.

        **参数解释**：资源池创建来源，比如admin-console，标记来自admin创建，console标记来自ma console。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_create_from of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_create_from

    @os_modelarts_create_from.setter
    def os_modelarts_create_from(self, os_modelarts_create_from):
        r"""Sets the os_modelarts_create_from of this PoolMetaLabels.

        **参数解释**：资源池创建来源，比如admin-console，标记来自admin创建，console标记来自ma console。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_create_from: The os_modelarts_create_from of this PoolMetaLabels.
        :type os_modelarts_create_from: str
        """
        self._os_modelarts_create_from = os_modelarts_create_from

    @property
    def os_modelarts_nobilling(self):
        r"""Gets the os_modelarts_nobilling of this PoolMetaLabels.

        **参数解释**：资源池是否计费。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_nobilling of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_nobilling

    @os_modelarts_nobilling.setter
    def os_modelarts_nobilling(self, os_modelarts_nobilling):
        r"""Sets the os_modelarts_nobilling of this PoolMetaLabels.

        **参数解释**：资源池是否计费。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_nobilling: The os_modelarts_nobilling of this PoolMetaLabels.
        :type os_modelarts_nobilling: str
        """
        self._os_modelarts_nobilling = os_modelarts_nobilling

    @property
    def os_modelarts_order_name(self):
        r"""Gets the os_modelarts_order_name of this PoolMetaLabels.

        **参数解释**：资源池关联的上一次订单作业记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_order_name of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_order_name

    @os_modelarts_order_name.setter
    def os_modelarts_order_name(self, os_modelarts_order_name):
        r"""Sets the os_modelarts_order_name of this PoolMetaLabels.

        **参数解释**：资源池关联的上一次订单作业记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_order_name: The os_modelarts_order_name of this PoolMetaLabels.
        :type os_modelarts_order_name: str
        """
        self._os_modelarts_order_name = os_modelarts_order_name

    @property
    def os_modelarts_region(self):
        r"""Gets the os_modelarts_region of this PoolMetaLabels.

        **参数解释**：资源池所属区域。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_region of this PoolMetaLabels.
        :rtype: str
        """
        return self._os_modelarts_region

    @os_modelarts_region.setter
    def os_modelarts_region(self, os_modelarts_region):
        r"""Sets the os_modelarts_region of this PoolMetaLabels.

        **参数解释**：资源池所属区域。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_region: The os_modelarts_region of this PoolMetaLabels.
        :type os_modelarts_region: str
        """
        self._os_modelarts_region = os_modelarts_region

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
        if not isinstance(other, PoolMetaLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
