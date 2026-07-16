# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeLabels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_node_cluster': 'str',
        'os_modelarts_node_elastic_quota': 'str',
        'os_modelarts_node_nodepool': 'str',
        'os_modelarts_node_batch_uid': 'str',
        'os_modelarts_node_batch_name': 'str',
        'os_modelarts_node_batch_type': 'str',
        'os_modelarts_node_batch_count': 'str',
        'os_modelarts_resource_id': 'str',
        'os_modelarts_tenant_domain_id': 'str',
        'os_modelarts_tenant_project_id': 'str',
        'os_modelarts_billing_status': 'str',
        'os_modelarts_node_volcano_scheduler_cabinet_exclusive': 'str',
        'cce_kubectl_kubernetes_io_cabinet': 'str',
        'os_modelarts_node_underlying_instance_id': 'str',
        'os_modelarts_node_ha_redundant_enabled': 'str',
        'os_modelarts_node_nodepoolname': 'str'
    }

    attribute_map = {
        'os_modelarts_node_cluster': 'os.modelarts.node/cluster',
        'os_modelarts_node_elastic_quota': 'os.modelarts.node/elastic.quota',
        'os_modelarts_node_nodepool': 'os.modelarts.node/nodepool',
        'os_modelarts_node_batch_uid': 'os.modelarts.node/batch.uid',
        'os_modelarts_node_batch_name': 'os.modelarts.node/batch.name',
        'os_modelarts_node_batch_type': 'os.modelarts.node/batch.type',
        'os_modelarts_node_batch_count': 'os.modelarts.node/batch.count',
        'os_modelarts_resource_id': 'os.modelarts/resource.id',
        'os_modelarts_tenant_domain_id': 'os.modelarts/tenant.domain.id',
        'os_modelarts_tenant_project_id': 'os.modelarts/tenant.project.id',
        'os_modelarts_billing_status': 'os.modelarts/billing.status',
        'os_modelarts_node_volcano_scheduler_cabinet_exclusive': 'os.modelarts.node/volcano.scheduler.cabinet-exclusive',
        'cce_kubectl_kubernetes_io_cabinet': 'cce.kubectl.kubernetes.io/cabinet',
        'os_modelarts_node_underlying_instance_id': 'os.modelarts.node/underlying.instance.id',
        'os_modelarts_node_ha_redundant_enabled': 'os.modelarts.node/ha.redundant.enabled',
        'os_modelarts_node_nodepoolname': 'os.modelarts.node/nodepoolname'
    }

    def __init__(self, os_modelarts_node_cluster=None, os_modelarts_node_elastic_quota=None, os_modelarts_node_nodepool=None, os_modelarts_node_batch_uid=None, os_modelarts_node_batch_name=None, os_modelarts_node_batch_type=None, os_modelarts_node_batch_count=None, os_modelarts_resource_id=None, os_modelarts_tenant_domain_id=None, os_modelarts_tenant_project_id=None, os_modelarts_billing_status=None, os_modelarts_node_volcano_scheduler_cabinet_exclusive=None, cce_kubectl_kubernetes_io_cabinet=None, os_modelarts_node_underlying_instance_id=None, os_modelarts_node_ha_redundant_enabled=None, os_modelarts_node_nodepoolname=None):
        r"""NodeLabels

        The model defined in huaweicloud sdk

        :param os_modelarts_node_cluster: **参数解释**：节点所在的集群名称。 **取值范围**：不涉及。
        :type os_modelarts_node_cluster: str
        :param os_modelarts_node_elastic_quota: **参数解释**：节点绑定的逻辑池。 **取值范围**：不涉及。
        :type os_modelarts_node_elastic_quota: str
        :param os_modelarts_node_nodepool: **参数解释**：节点所在的节点池id。 **取值范围**：不涉及。
        :type os_modelarts_node_nodepool: str
        :param os_modelarts_node_batch_uid: **参数解释**：批量创建批次标识。 **取值范围**：不涉及。
        :type os_modelarts_node_batch_uid: str
        :param os_modelarts_node_batch_name: **参数解释**：批量创建批次名称。 **取值范围**：不涉及。
        :type os_modelarts_node_batch_name: str
        :param os_modelarts_node_batch_type: **参数解释**：批量创建批次类型。 **取值范围**：可选值如下：   - hyperinstance：超节点。
        :type os_modelarts_node_batch_type: str
        :param os_modelarts_node_batch_count: **参数解释**：批量创建的节点个数。 **取值范围**：不涉及。
        :type os_modelarts_node_batch_count: str
        :param os_modelarts_resource_id: **参数解释**：节点的资源id。 **取值范围**：不涉及。
        :type os_modelarts_resource_id: str
        :param os_modelarts_tenant_domain_id: **参数解释**：节点的租户id，记录节点创建在哪个租户账号下。 **取值范围**：不涉及。
        :type os_modelarts_tenant_domain_id: str
        :param os_modelarts_tenant_project_id: **参数解释**：节点的项目id，记录节点创建在租户账号下哪个项目中。 **取值范围**：不涉及。
        :type os_modelarts_tenant_project_id: str
        :param os_modelarts_billing_status: **参数解释**：节点计费状态。 **取值范围**：可选值如下： - 0：正常状态。 - 1：冻结状态。 - 2：删除状态或者终止状态。
        :type os_modelarts_billing_status: str
        :param os_modelarts_node_volcano_scheduler_cabinet_exclusive: **参数解释**：标识该节点是否被整柜作业独占。当被某个整柜作业独占时，该标签存在，标签的值为独占的训练作业ID。 **取值范围**：不涉及。
        :type os_modelarts_node_volcano_scheduler_cabinet_exclusive: str
        :param cce_kubectl_kubernetes_io_cabinet: **参数解释**：节点所在tor交换机ip。多个tor交换机ip之间以中划线-分隔。 **取值范围**：不涉及。
        :type cce_kubectl_kubernetes_io_cabinet: str
        :param os_modelarts_node_underlying_instance_id: **参数解释**：节点底层资源的实例ID，如超节点的ECS实例ID。 **取值范围**：不涉及。
        :type os_modelarts_node_underlying_instance_id: str
        :param os_modelarts_node_ha_redundant_enabled: **参数解释**：节点是否启用高可用冗余。 **取值范围**：   - true：开启   - false：未开启
        :type os_modelarts_node_ha_redundant_enabled: str
        :param os_modelarts_node_nodepoolname: **参数解释**：节点所在的节点池名称,最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能 以-，-default结尾。 **取值范围**：不涉及。
        :type os_modelarts_node_nodepoolname: str
        """
        
        

        self._os_modelarts_node_cluster = None
        self._os_modelarts_node_elastic_quota = None
        self._os_modelarts_node_nodepool = None
        self._os_modelarts_node_batch_uid = None
        self._os_modelarts_node_batch_name = None
        self._os_modelarts_node_batch_type = None
        self._os_modelarts_node_batch_count = None
        self._os_modelarts_resource_id = None
        self._os_modelarts_tenant_domain_id = None
        self._os_modelarts_tenant_project_id = None
        self._os_modelarts_billing_status = None
        self._os_modelarts_node_volcano_scheduler_cabinet_exclusive = None
        self._cce_kubectl_kubernetes_io_cabinet = None
        self._os_modelarts_node_underlying_instance_id = None
        self._os_modelarts_node_ha_redundant_enabled = None
        self._os_modelarts_node_nodepoolname = None
        self.discriminator = None

        if os_modelarts_node_cluster is not None:
            self.os_modelarts_node_cluster = os_modelarts_node_cluster
        if os_modelarts_node_elastic_quota is not None:
            self.os_modelarts_node_elastic_quota = os_modelarts_node_elastic_quota
        if os_modelarts_node_nodepool is not None:
            self.os_modelarts_node_nodepool = os_modelarts_node_nodepool
        if os_modelarts_node_batch_uid is not None:
            self.os_modelarts_node_batch_uid = os_modelarts_node_batch_uid
        if os_modelarts_node_batch_name is not None:
            self.os_modelarts_node_batch_name = os_modelarts_node_batch_name
        if os_modelarts_node_batch_type is not None:
            self.os_modelarts_node_batch_type = os_modelarts_node_batch_type
        if os_modelarts_node_batch_count is not None:
            self.os_modelarts_node_batch_count = os_modelarts_node_batch_count
        if os_modelarts_resource_id is not None:
            self.os_modelarts_resource_id = os_modelarts_resource_id
        if os_modelarts_tenant_domain_id is not None:
            self.os_modelarts_tenant_domain_id = os_modelarts_tenant_domain_id
        if os_modelarts_tenant_project_id is not None:
            self.os_modelarts_tenant_project_id = os_modelarts_tenant_project_id
        if os_modelarts_billing_status is not None:
            self.os_modelarts_billing_status = os_modelarts_billing_status
        if os_modelarts_node_volcano_scheduler_cabinet_exclusive is not None:
            self.os_modelarts_node_volcano_scheduler_cabinet_exclusive = os_modelarts_node_volcano_scheduler_cabinet_exclusive
        if cce_kubectl_kubernetes_io_cabinet is not None:
            self.cce_kubectl_kubernetes_io_cabinet = cce_kubectl_kubernetes_io_cabinet
        if os_modelarts_node_underlying_instance_id is not None:
            self.os_modelarts_node_underlying_instance_id = os_modelarts_node_underlying_instance_id
        if os_modelarts_node_ha_redundant_enabled is not None:
            self.os_modelarts_node_ha_redundant_enabled = os_modelarts_node_ha_redundant_enabled
        if os_modelarts_node_nodepoolname is not None:
            self.os_modelarts_node_nodepoolname = os_modelarts_node_nodepoolname

    @property
    def os_modelarts_node_cluster(self):
        r"""Gets the os_modelarts_node_cluster of this NodeLabels.

        **参数解释**：节点所在的集群名称。 **取值范围**：不涉及。

        :return: The os_modelarts_node_cluster of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_cluster

    @os_modelarts_node_cluster.setter
    def os_modelarts_node_cluster(self, os_modelarts_node_cluster):
        r"""Sets the os_modelarts_node_cluster of this NodeLabels.

        **参数解释**：节点所在的集群名称。 **取值范围**：不涉及。

        :param os_modelarts_node_cluster: The os_modelarts_node_cluster of this NodeLabels.
        :type os_modelarts_node_cluster: str
        """
        self._os_modelarts_node_cluster = os_modelarts_node_cluster

    @property
    def os_modelarts_node_elastic_quota(self):
        r"""Gets the os_modelarts_node_elastic_quota of this NodeLabels.

        **参数解释**：节点绑定的逻辑池。 **取值范围**：不涉及。

        :return: The os_modelarts_node_elastic_quota of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_elastic_quota

    @os_modelarts_node_elastic_quota.setter
    def os_modelarts_node_elastic_quota(self, os_modelarts_node_elastic_quota):
        r"""Sets the os_modelarts_node_elastic_quota of this NodeLabels.

        **参数解释**：节点绑定的逻辑池。 **取值范围**：不涉及。

        :param os_modelarts_node_elastic_quota: The os_modelarts_node_elastic_quota of this NodeLabels.
        :type os_modelarts_node_elastic_quota: str
        """
        self._os_modelarts_node_elastic_quota = os_modelarts_node_elastic_quota

    @property
    def os_modelarts_node_nodepool(self):
        r"""Gets the os_modelarts_node_nodepool of this NodeLabels.

        **参数解释**：节点所在的节点池id。 **取值范围**：不涉及。

        :return: The os_modelarts_node_nodepool of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_nodepool

    @os_modelarts_node_nodepool.setter
    def os_modelarts_node_nodepool(self, os_modelarts_node_nodepool):
        r"""Sets the os_modelarts_node_nodepool of this NodeLabels.

        **参数解释**：节点所在的节点池id。 **取值范围**：不涉及。

        :param os_modelarts_node_nodepool: The os_modelarts_node_nodepool of this NodeLabels.
        :type os_modelarts_node_nodepool: str
        """
        self._os_modelarts_node_nodepool = os_modelarts_node_nodepool

    @property
    def os_modelarts_node_batch_uid(self):
        r"""Gets the os_modelarts_node_batch_uid of this NodeLabels.

        **参数解释**：批量创建批次标识。 **取值范围**：不涉及。

        :return: The os_modelarts_node_batch_uid of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_batch_uid

    @os_modelarts_node_batch_uid.setter
    def os_modelarts_node_batch_uid(self, os_modelarts_node_batch_uid):
        r"""Sets the os_modelarts_node_batch_uid of this NodeLabels.

        **参数解释**：批量创建批次标识。 **取值范围**：不涉及。

        :param os_modelarts_node_batch_uid: The os_modelarts_node_batch_uid of this NodeLabels.
        :type os_modelarts_node_batch_uid: str
        """
        self._os_modelarts_node_batch_uid = os_modelarts_node_batch_uid

    @property
    def os_modelarts_node_batch_name(self):
        r"""Gets the os_modelarts_node_batch_name of this NodeLabels.

        **参数解释**：批量创建批次名称。 **取值范围**：不涉及。

        :return: The os_modelarts_node_batch_name of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_batch_name

    @os_modelarts_node_batch_name.setter
    def os_modelarts_node_batch_name(self, os_modelarts_node_batch_name):
        r"""Sets the os_modelarts_node_batch_name of this NodeLabels.

        **参数解释**：批量创建批次名称。 **取值范围**：不涉及。

        :param os_modelarts_node_batch_name: The os_modelarts_node_batch_name of this NodeLabels.
        :type os_modelarts_node_batch_name: str
        """
        self._os_modelarts_node_batch_name = os_modelarts_node_batch_name

    @property
    def os_modelarts_node_batch_type(self):
        r"""Gets the os_modelarts_node_batch_type of this NodeLabels.

        **参数解释**：批量创建批次类型。 **取值范围**：可选值如下：   - hyperinstance：超节点。

        :return: The os_modelarts_node_batch_type of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_batch_type

    @os_modelarts_node_batch_type.setter
    def os_modelarts_node_batch_type(self, os_modelarts_node_batch_type):
        r"""Sets the os_modelarts_node_batch_type of this NodeLabels.

        **参数解释**：批量创建批次类型。 **取值范围**：可选值如下：   - hyperinstance：超节点。

        :param os_modelarts_node_batch_type: The os_modelarts_node_batch_type of this NodeLabels.
        :type os_modelarts_node_batch_type: str
        """
        self._os_modelarts_node_batch_type = os_modelarts_node_batch_type

    @property
    def os_modelarts_node_batch_count(self):
        r"""Gets the os_modelarts_node_batch_count of this NodeLabels.

        **参数解释**：批量创建的节点个数。 **取值范围**：不涉及。

        :return: The os_modelarts_node_batch_count of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_batch_count

    @os_modelarts_node_batch_count.setter
    def os_modelarts_node_batch_count(self, os_modelarts_node_batch_count):
        r"""Sets the os_modelarts_node_batch_count of this NodeLabels.

        **参数解释**：批量创建的节点个数。 **取值范围**：不涉及。

        :param os_modelarts_node_batch_count: The os_modelarts_node_batch_count of this NodeLabels.
        :type os_modelarts_node_batch_count: str
        """
        self._os_modelarts_node_batch_count = os_modelarts_node_batch_count

    @property
    def os_modelarts_resource_id(self):
        r"""Gets the os_modelarts_resource_id of this NodeLabels.

        **参数解释**：节点的资源id。 **取值范围**：不涉及。

        :return: The os_modelarts_resource_id of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_resource_id

    @os_modelarts_resource_id.setter
    def os_modelarts_resource_id(self, os_modelarts_resource_id):
        r"""Sets the os_modelarts_resource_id of this NodeLabels.

        **参数解释**：节点的资源id。 **取值范围**：不涉及。

        :param os_modelarts_resource_id: The os_modelarts_resource_id of this NodeLabels.
        :type os_modelarts_resource_id: str
        """
        self._os_modelarts_resource_id = os_modelarts_resource_id

    @property
    def os_modelarts_tenant_domain_id(self):
        r"""Gets the os_modelarts_tenant_domain_id of this NodeLabels.

        **参数解释**：节点的租户id，记录节点创建在哪个租户账号下。 **取值范围**：不涉及。

        :return: The os_modelarts_tenant_domain_id of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_tenant_domain_id

    @os_modelarts_tenant_domain_id.setter
    def os_modelarts_tenant_domain_id(self, os_modelarts_tenant_domain_id):
        r"""Sets the os_modelarts_tenant_domain_id of this NodeLabels.

        **参数解释**：节点的租户id，记录节点创建在哪个租户账号下。 **取值范围**：不涉及。

        :param os_modelarts_tenant_domain_id: The os_modelarts_tenant_domain_id of this NodeLabels.
        :type os_modelarts_tenant_domain_id: str
        """
        self._os_modelarts_tenant_domain_id = os_modelarts_tenant_domain_id

    @property
    def os_modelarts_tenant_project_id(self):
        r"""Gets the os_modelarts_tenant_project_id of this NodeLabels.

        **参数解释**：节点的项目id，记录节点创建在租户账号下哪个项目中。 **取值范围**：不涉及。

        :return: The os_modelarts_tenant_project_id of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_tenant_project_id

    @os_modelarts_tenant_project_id.setter
    def os_modelarts_tenant_project_id(self, os_modelarts_tenant_project_id):
        r"""Sets the os_modelarts_tenant_project_id of this NodeLabels.

        **参数解释**：节点的项目id，记录节点创建在租户账号下哪个项目中。 **取值范围**：不涉及。

        :param os_modelarts_tenant_project_id: The os_modelarts_tenant_project_id of this NodeLabels.
        :type os_modelarts_tenant_project_id: str
        """
        self._os_modelarts_tenant_project_id = os_modelarts_tenant_project_id

    @property
    def os_modelarts_billing_status(self):
        r"""Gets the os_modelarts_billing_status of this NodeLabels.

        **参数解释**：节点计费状态。 **取值范围**：可选值如下： - 0：正常状态。 - 1：冻结状态。 - 2：删除状态或者终止状态。

        :return: The os_modelarts_billing_status of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_billing_status

    @os_modelarts_billing_status.setter
    def os_modelarts_billing_status(self, os_modelarts_billing_status):
        r"""Sets the os_modelarts_billing_status of this NodeLabels.

        **参数解释**：节点计费状态。 **取值范围**：可选值如下： - 0：正常状态。 - 1：冻结状态。 - 2：删除状态或者终止状态。

        :param os_modelarts_billing_status: The os_modelarts_billing_status of this NodeLabels.
        :type os_modelarts_billing_status: str
        """
        self._os_modelarts_billing_status = os_modelarts_billing_status

    @property
    def os_modelarts_node_volcano_scheduler_cabinet_exclusive(self):
        r"""Gets the os_modelarts_node_volcano_scheduler_cabinet_exclusive of this NodeLabels.

        **参数解释**：标识该节点是否被整柜作业独占。当被某个整柜作业独占时，该标签存在，标签的值为独占的训练作业ID。 **取值范围**：不涉及。

        :return: The os_modelarts_node_volcano_scheduler_cabinet_exclusive of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_volcano_scheduler_cabinet_exclusive

    @os_modelarts_node_volcano_scheduler_cabinet_exclusive.setter
    def os_modelarts_node_volcano_scheduler_cabinet_exclusive(self, os_modelarts_node_volcano_scheduler_cabinet_exclusive):
        r"""Sets the os_modelarts_node_volcano_scheduler_cabinet_exclusive of this NodeLabels.

        **参数解释**：标识该节点是否被整柜作业独占。当被某个整柜作业独占时，该标签存在，标签的值为独占的训练作业ID。 **取值范围**：不涉及。

        :param os_modelarts_node_volcano_scheduler_cabinet_exclusive: The os_modelarts_node_volcano_scheduler_cabinet_exclusive of this NodeLabels.
        :type os_modelarts_node_volcano_scheduler_cabinet_exclusive: str
        """
        self._os_modelarts_node_volcano_scheduler_cabinet_exclusive = os_modelarts_node_volcano_scheduler_cabinet_exclusive

    @property
    def cce_kubectl_kubernetes_io_cabinet(self):
        r"""Gets the cce_kubectl_kubernetes_io_cabinet of this NodeLabels.

        **参数解释**：节点所在tor交换机ip。多个tor交换机ip之间以中划线-分隔。 **取值范围**：不涉及。

        :return: The cce_kubectl_kubernetes_io_cabinet of this NodeLabels.
        :rtype: str
        """
        return self._cce_kubectl_kubernetes_io_cabinet

    @cce_kubectl_kubernetes_io_cabinet.setter
    def cce_kubectl_kubernetes_io_cabinet(self, cce_kubectl_kubernetes_io_cabinet):
        r"""Sets the cce_kubectl_kubernetes_io_cabinet of this NodeLabels.

        **参数解释**：节点所在tor交换机ip。多个tor交换机ip之间以中划线-分隔。 **取值范围**：不涉及。

        :param cce_kubectl_kubernetes_io_cabinet: The cce_kubectl_kubernetes_io_cabinet of this NodeLabels.
        :type cce_kubectl_kubernetes_io_cabinet: str
        """
        self._cce_kubectl_kubernetes_io_cabinet = cce_kubectl_kubernetes_io_cabinet

    @property
    def os_modelarts_node_underlying_instance_id(self):
        r"""Gets the os_modelarts_node_underlying_instance_id of this NodeLabels.

        **参数解释**：节点底层资源的实例ID，如超节点的ECS实例ID。 **取值范围**：不涉及。

        :return: The os_modelarts_node_underlying_instance_id of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_underlying_instance_id

    @os_modelarts_node_underlying_instance_id.setter
    def os_modelarts_node_underlying_instance_id(self, os_modelarts_node_underlying_instance_id):
        r"""Sets the os_modelarts_node_underlying_instance_id of this NodeLabels.

        **参数解释**：节点底层资源的实例ID，如超节点的ECS实例ID。 **取值范围**：不涉及。

        :param os_modelarts_node_underlying_instance_id: The os_modelarts_node_underlying_instance_id of this NodeLabels.
        :type os_modelarts_node_underlying_instance_id: str
        """
        self._os_modelarts_node_underlying_instance_id = os_modelarts_node_underlying_instance_id

    @property
    def os_modelarts_node_ha_redundant_enabled(self):
        r"""Gets the os_modelarts_node_ha_redundant_enabled of this NodeLabels.

        **参数解释**：节点是否启用高可用冗余。 **取值范围**：   - true：开启   - false：未开启

        :return: The os_modelarts_node_ha_redundant_enabled of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_ha_redundant_enabled

    @os_modelarts_node_ha_redundant_enabled.setter
    def os_modelarts_node_ha_redundant_enabled(self, os_modelarts_node_ha_redundant_enabled):
        r"""Sets the os_modelarts_node_ha_redundant_enabled of this NodeLabels.

        **参数解释**：节点是否启用高可用冗余。 **取值范围**：   - true：开启   - false：未开启

        :param os_modelarts_node_ha_redundant_enabled: The os_modelarts_node_ha_redundant_enabled of this NodeLabels.
        :type os_modelarts_node_ha_redundant_enabled: str
        """
        self._os_modelarts_node_ha_redundant_enabled = os_modelarts_node_ha_redundant_enabled

    @property
    def os_modelarts_node_nodepoolname(self):
        r"""Gets the os_modelarts_node_nodepoolname of this NodeLabels.

        **参数解释**：节点所在的节点池名称,最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能 以-，-default结尾。 **取值范围**：不涉及。

        :return: The os_modelarts_node_nodepoolname of this NodeLabels.
        :rtype: str
        """
        return self._os_modelarts_node_nodepoolname

    @os_modelarts_node_nodepoolname.setter
    def os_modelarts_node_nodepoolname(self, os_modelarts_node_nodepoolname):
        r"""Sets the os_modelarts_node_nodepoolname of this NodeLabels.

        **参数解释**：节点所在的节点池名称,最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能 以-，-default结尾。 **取值范围**：不涉及。

        :param os_modelarts_node_nodepoolname: The os_modelarts_node_nodepoolname of this NodeLabels.
        :type os_modelarts_node_nodepoolname: str
        """
        self._os_modelarts_node_nodepoolname = os_modelarts_node_nodepoolname

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
        if not isinstance(other, NodeLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
