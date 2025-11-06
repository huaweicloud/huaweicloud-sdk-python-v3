# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_version': 'bool',
        'agent_version': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'namespace': 'str',
        'cluster_type': 'str',
        'node_num': 'int',
        'ds_info': 'ClusterInfoResponseDsInfo',
        'cluster_status': 'str',
        'installed_status': 'str',
        'access_status': 'str',
        'combined_status': 'str',
        'failed_message': 'str',
        'cluster_log_status': 'str',
        'invoked_service': 'str',
        'registry_info': 'ClusterInfoResponseRegistryInfo'
    }

    attribute_map = {
        'latest_version': 'latest_version',
        'agent_version': 'agent_version',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'namespace': 'namespace',
        'cluster_type': 'cluster_type',
        'node_num': 'node_num',
        'ds_info': 'ds_info',
        'cluster_status': 'cluster_status',
        'installed_status': 'installed_status',
        'access_status': 'access_status',
        'combined_status': 'combined_status',
        'failed_message': 'failed_message',
        'cluster_log_status': 'cluster_log_status',
        'invoked_service': 'invoked_service',
        'registry_info': 'registry_info'
    }

    def __init__(self, latest_version=None, agent_version=None, cluster_name=None, cluster_id=None, namespace=None, cluster_type=None, node_num=None, ds_info=None, cluster_status=None, installed_status=None, access_status=None, combined_status=None, failed_message=None, cluster_log_status=None, invoked_service=None, registry_info=None):
        r"""ClusterInfoResponse

        The model defined in huaweicloud sdk

        :param latest_version: **参数解释** 是否最新版本 **取值范围** - true：是。 - false：否。
        :type latest_version: bool
        :param agent_version: **参数解释** 集群agent版本 **取值范围** 字符长度0-32位
        :type agent_version: str
        :param cluster_name: **参数解释** 集群名称 **取值范围** 字符长度0-256位
        :type cluster_name: str
        :param cluster_id: **参数解释** 集群id **取值范围** 字符长度1-256位
        :type cluster_id: str
        :param namespace: **参数解释** 命名空间 **取值范围** 字符长度1-32位
        :type namespace: str
        :param cluster_type: **参数解释** 集群类型 **取值范围** 字符长度1-32位
        :type cluster_type: str
        :param node_num: **参数解释** 节点总数 **取值范围** 取值0-65535
        :type node_num: int
        :param ds_info: 
        :type ds_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        :param cluster_status: **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。 - Empty：集群无任何资源。  **默认取值**: 不涉及 
        :type cluster_status: str
        :param installed_status: **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。 - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 
        :type installed_status: str
        :param access_status: **参数解释**： 集群anp接入状态 **约束限制**： 不涉及 **取值范围**： - not_connect：未连接。 - connect_success：连接成功。 - connect_fail：连接失败。 - connect_disruption：连接中断。  **默认取值**： 不涉及 
        :type access_status: str
        :param combined_status: **参数解释**： 集群anp与ds的组合状态 **约束限制**： 不涉及 **取值范围**： - accessing：接入中。 - access_error：接入异常。 - running：运行中。 - run_error：运行异常。 - upgrading：升级中。 - upgrade_error：升级失败。  **默认取值**： 不涉及 
        :type combined_status: str
        :param failed_message: **参数解释** 集群插件接入失败的原因 **取值范围** 字符长度1-256位
        :type failed_message: str
        :param cluster_log_status: **参数解释**： 集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功。 - partial_success：部分接入。  **默认取值**： 不涉及 
        :type cluster_log_status: str
        :param invoked_service: **参数解释**： 调用服务，标识cce免费体检报告 **约束限制**： 不涉及 **取值范围**： - hss：hss服务。 - cce：cce服务。  **默认取值**： 不涉及 
        :type invoked_service: str
        :param registry_info: 
        :type registry_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseRegistryInfo`
        """
        
        

        self._latest_version = None
        self._agent_version = None
        self._cluster_name = None
        self._cluster_id = None
        self._namespace = None
        self._cluster_type = None
        self._node_num = None
        self._ds_info = None
        self._cluster_status = None
        self._installed_status = None
        self._access_status = None
        self._combined_status = None
        self._failed_message = None
        self._cluster_log_status = None
        self._invoked_service = None
        self._registry_info = None
        self.discriminator = None

        if latest_version is not None:
            self.latest_version = latest_version
        if agent_version is not None:
            self.agent_version = agent_version
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if namespace is not None:
            self.namespace = namespace
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if node_num is not None:
            self.node_num = node_num
        if ds_info is not None:
            self.ds_info = ds_info
        if cluster_status is not None:
            self.cluster_status = cluster_status
        if installed_status is not None:
            self.installed_status = installed_status
        if access_status is not None:
            self.access_status = access_status
        if combined_status is not None:
            self.combined_status = combined_status
        if failed_message is not None:
            self.failed_message = failed_message
        if cluster_log_status is not None:
            self.cluster_log_status = cluster_log_status
        if invoked_service is not None:
            self.invoked_service = invoked_service
        if registry_info is not None:
            self.registry_info = registry_info

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ClusterInfoResponse.

        **参数解释** 是否最新版本 **取值范围** - true：是。 - false：否。

        :return: The latest_version of this ClusterInfoResponse.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ClusterInfoResponse.

        **参数解释** 是否最新版本 **取值范围** - true：是。 - false：否。

        :param latest_version: The latest_version of this ClusterInfoResponse.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ClusterInfoResponse.

        **参数解释** 集群agent版本 **取值范围** 字符长度0-32位

        :return: The agent_version of this ClusterInfoResponse.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ClusterInfoResponse.

        **参数解释** 集群agent版本 **取值范围** 字符长度0-32位

        :param agent_version: The agent_version of this ClusterInfoResponse.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterInfoResponse.

        **参数解释** 集群名称 **取值范围** 字符长度0-256位

        :return: The cluster_name of this ClusterInfoResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterInfoResponse.

        **参数解释** 集群名称 **取值范围** 字符长度0-256位

        :param cluster_name: The cluster_name of this ClusterInfoResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterInfoResponse.

        **参数解释** 集群id **取值范围** 字符长度1-256位

        :return: The cluster_id of this ClusterInfoResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterInfoResponse.

        **参数解释** 集群id **取值范围** 字符长度1-256位

        :param cluster_id: The cluster_id of this ClusterInfoResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ClusterInfoResponse.

        **参数解释** 命名空间 **取值范围** 字符长度1-32位

        :return: The namespace of this ClusterInfoResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ClusterInfoResponse.

        **参数解释** 命名空间 **取值范围** 字符长度1-32位

        :param namespace: The namespace of this ClusterInfoResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterInfoResponse.

        **参数解释** 集群类型 **取值范围** 字符长度1-32位

        :return: The cluster_type of this ClusterInfoResponse.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterInfoResponse.

        **参数解释** 集群类型 **取值范围** 字符长度1-32位

        :param cluster_type: The cluster_type of this ClusterInfoResponse.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def node_num(self):
        r"""Gets the node_num of this ClusterInfoResponse.

        **参数解释** 节点总数 **取值范围** 取值0-65535

        :return: The node_num of this ClusterInfoResponse.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ClusterInfoResponse.

        **参数解释** 节点总数 **取值范围** 取值0-65535

        :param node_num: The node_num of this ClusterInfoResponse.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def ds_info(self):
        r"""Gets the ds_info of this ClusterInfoResponse.

        :return: The ds_info of this ClusterInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        """
        return self._ds_info

    @ds_info.setter
    def ds_info(self, ds_info):
        r"""Sets the ds_info of this ClusterInfoResponse.

        :param ds_info: The ds_info of this ClusterInfoResponse.
        :type ds_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        """
        self._ds_info = ds_info

    @property
    def cluster_status(self):
        r"""Gets the cluster_status of this ClusterInfoResponse.

        **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。 - Empty：集群无任何资源。  **默认取值**: 不涉及 

        :return: The cluster_status of this ClusterInfoResponse.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        r"""Sets the cluster_status of this ClusterInfoResponse.

        **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。 - Empty：集群无任何资源。  **默认取值**: 不涉及 

        :param cluster_status: The cluster_status of this ClusterInfoResponse.
        :type cluster_status: str
        """
        self._cluster_status = cluster_status

    @property
    def installed_status(self):
        r"""Gets the installed_status of this ClusterInfoResponse.

        **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。 - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 

        :return: The installed_status of this ClusterInfoResponse.
        :rtype: str
        """
        return self._installed_status

    @installed_status.setter
    def installed_status(self, installed_status):
        r"""Sets the installed_status of this ClusterInfoResponse.

        **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。 - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 

        :param installed_status: The installed_status of this ClusterInfoResponse.
        :type installed_status: str
        """
        self._installed_status = installed_status

    @property
    def access_status(self):
        r"""Gets the access_status of this ClusterInfoResponse.

        **参数解释**： 集群anp接入状态 **约束限制**： 不涉及 **取值范围**： - not_connect：未连接。 - connect_success：连接成功。 - connect_fail：连接失败。 - connect_disruption：连接中断。  **默认取值**： 不涉及 

        :return: The access_status of this ClusterInfoResponse.
        :rtype: str
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this ClusterInfoResponse.

        **参数解释**： 集群anp接入状态 **约束限制**： 不涉及 **取值范围**： - not_connect：未连接。 - connect_success：连接成功。 - connect_fail：连接失败。 - connect_disruption：连接中断。  **默认取值**： 不涉及 

        :param access_status: The access_status of this ClusterInfoResponse.
        :type access_status: str
        """
        self._access_status = access_status

    @property
    def combined_status(self):
        r"""Gets the combined_status of this ClusterInfoResponse.

        **参数解释**： 集群anp与ds的组合状态 **约束限制**： 不涉及 **取值范围**： - accessing：接入中。 - access_error：接入异常。 - running：运行中。 - run_error：运行异常。 - upgrading：升级中。 - upgrade_error：升级失败。  **默认取值**： 不涉及 

        :return: The combined_status of this ClusterInfoResponse.
        :rtype: str
        """
        return self._combined_status

    @combined_status.setter
    def combined_status(self, combined_status):
        r"""Sets the combined_status of this ClusterInfoResponse.

        **参数解释**： 集群anp与ds的组合状态 **约束限制**： 不涉及 **取值范围**： - accessing：接入中。 - access_error：接入异常。 - running：运行中。 - run_error：运行异常。 - upgrading：升级中。 - upgrade_error：升级失败。  **默认取值**： 不涉及 

        :param combined_status: The combined_status of this ClusterInfoResponse.
        :type combined_status: str
        """
        self._combined_status = combined_status

    @property
    def failed_message(self):
        r"""Gets the failed_message of this ClusterInfoResponse.

        **参数解释** 集群插件接入失败的原因 **取值范围** 字符长度1-256位

        :return: The failed_message of this ClusterInfoResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this ClusterInfoResponse.

        **参数解释** 集群插件接入失败的原因 **取值范围** 字符长度1-256位

        :param failed_message: The failed_message of this ClusterInfoResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def cluster_log_status(self):
        r"""Gets the cluster_log_status of this ClusterInfoResponse.

        **参数解释**： 集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功。 - partial_success：部分接入。  **默认取值**： 不涉及 

        :return: The cluster_log_status of this ClusterInfoResponse.
        :rtype: str
        """
        return self._cluster_log_status

    @cluster_log_status.setter
    def cluster_log_status(self, cluster_log_status):
        r"""Sets the cluster_log_status of this ClusterInfoResponse.

        **参数解释**： 集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功。 - partial_success：部分接入。  **默认取值**： 不涉及 

        :param cluster_log_status: The cluster_log_status of this ClusterInfoResponse.
        :type cluster_log_status: str
        """
        self._cluster_log_status = cluster_log_status

    @property
    def invoked_service(self):
        r"""Gets the invoked_service of this ClusterInfoResponse.

        **参数解释**： 调用服务，标识cce免费体检报告 **约束限制**： 不涉及 **取值范围**： - hss：hss服务。 - cce：cce服务。  **默认取值**： 不涉及 

        :return: The invoked_service of this ClusterInfoResponse.
        :rtype: str
        """
        return self._invoked_service

    @invoked_service.setter
    def invoked_service(self, invoked_service):
        r"""Sets the invoked_service of this ClusterInfoResponse.

        **参数解释**： 调用服务，标识cce免费体检报告 **约束限制**： 不涉及 **取值范围**： - hss：hss服务。 - cce：cce服务。  **默认取值**： 不涉及 

        :param invoked_service: The invoked_service of this ClusterInfoResponse.
        :type invoked_service: str
        """
        self._invoked_service = invoked_service

    @property
    def registry_info(self):
        r"""Gets the registry_info of this ClusterInfoResponse.

        :return: The registry_info of this ClusterInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseRegistryInfo`
        """
        return self._registry_info

    @registry_info.setter
    def registry_info(self, registry_info):
        r"""Sets the registry_info of this ClusterInfoResponse.

        :param registry_info: The registry_info of this ClusterInfoResponse.
        :type registry_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseRegistryInfo`
        """
        self._registry_info = registry_info

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
        if not isinstance(other, ClusterInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
