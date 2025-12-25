# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'az': 'str',
        'os': 'str',
        'login': 'Login',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'storage': 'Storage',
        'public_ip': 'NodeEIPSpec',
        'node_nic_spec': 'NodeNicSpec',
        'count': 'int',
        'billing_mode': 'int',
        'taints': 'list[Taint]',
        'wait_post_install_finish': 'bool',
        'k8s_tags': 'dict(str, str)',
        'ecs_group_id': 'str',
        'dedicated_host_id': 'str',
        'user_tags': 'list[UserTag]',
        'runtime': 'Runtime',
        'initialized_conditions': 'list[str]',
        'extend_param': 'NodeExtendParam',
        'hostname_config': 'HostnameConfig',
        'server_enterprise_project_id': 'str',
        'partition': 'str',
        'configurations_override': 'list[PackageConfiguration]',
        'node_name_template': 'NodeSpecNodeNameTemplate'
    }

    attribute_map = {
        'flavor': 'flavor',
        'az': 'az',
        'os': 'os',
        'login': 'login',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'storage': 'storage',
        'public_ip': 'publicIP',
        'node_nic_spec': 'nodeNicSpec',
        'count': 'count',
        'billing_mode': 'billingMode',
        'taints': 'taints',
        'wait_post_install_finish': 'waitPostInstallFinish',
        'k8s_tags': 'k8sTags',
        'ecs_group_id': 'ecsGroupId',
        'dedicated_host_id': 'dedicatedHostId',
        'user_tags': 'userTags',
        'runtime': 'runtime',
        'initialized_conditions': 'initializedConditions',
        'extend_param': 'extendParam',
        'hostname_config': 'hostnameConfig',
        'server_enterprise_project_id': 'serverEnterpriseProjectID',
        'partition': 'partition',
        'configurations_override': 'configurationsOverride',
        'node_name_template': 'nodeNameTemplate'
    }

    def __init__(self, flavor=None, az=None, os=None, login=None, root_volume=None, data_volumes=None, storage=None, public_ip=None, node_nic_spec=None, count=None, billing_mode=None, taints=None, wait_post_install_finish=None, k8s_tags=None, ecs_group_id=None, dedicated_host_id=None, user_tags=None, runtime=None, initialized_conditions=None, extend_param=None, hostname_config=None, server_enterprise_project_id=None, partition=None, configurations_override=None, node_name_template=None):
        r"""NodeTemplate

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**： 节点的规格，CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type flavor: str
        :param az: **参数解释**： 待创建节点所在的可用区，需要指定可用区（AZ）的名称，通过api创建节点不支持随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk) **约束限制**： 创建节点池并设置伸缩组时，该参数不允许填写为random。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type az: str
        :param os: **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若在创建节点时未指定该配置，CCE会根据集群版本自动选择支持的OS版本。 - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，节点将使用私有镜像，则该参数为非必选参数。 [- 若在创建节点时指定了extendParam中的securityReinforcementType参数为cybersecurity，节点将开启安全等保加固功能，则节点的操作系统类型必须使用HCE2.0。当用户未配置私有镜像时，该参数必须为“Huawei Cloud EulerOS 2.0”；当用户配置了私有镜像且私有镜像操作系统类型为HCE2.0，则该参数为非必选参数。](tag:hws)  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type os: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        :param data_volumes: **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： - 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 - 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 - 仅在选择系统盘作为系统组件存储磁盘时，允许为空。
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        :param node_nic_spec: 
        :type node_nic_spec: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        :param count: **参数解释**： 批量创建时节点的个数。 **约束限制**： - 作用于节点池时该项可以不填写。 - 创建、更新节点池场景返回中无该参数。 - 创建节点时该参数为必填参数  **取值范围**： 必须为大于等于1，小于等于最大限额的正整数。 **默认取值**： 不涉及
        :type count: int
        :param billing_mode: **参数解释**： 节点的计费模式。 **约束限制**： 不涉及 **取值范围**： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk)  **默认取值**： 0
        :type billing_mode: int
        :param taints: **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  &#x60;&#x60;&#x60; \&quot;taints\&quot;: [{   \&quot;key\&quot;: \&quot;status\&quot;,   \&quot;value\&quot;: \&quot;unavailable\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }, {   \&quot;key\&quot;: \&quot;looks\&quot;,   \&quot;value\&quot;: \&quot;bad\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }] &#x60;&#x60;&#x60;  **约束限制**： taints配置不超过20条。
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        :param wait_post_install_finish: **参数解释：** 该参数用于控制创建节点时 **post-install脚本执行完成前允许节点调度** 行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false
        :type wait_post_install_finish: bool
        :param k8s_tags: **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60;  **约束限制**： 键值对个数不超过20条。
        :type k8s_tags: dict(str, str)
        :param ecs_group_id: **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建、更新节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type ecs_group_id: str
        :param dedicated_host_id: **参数解释**： 指定DeH主机的ID，将节点调度到自己的DeH上。 **约束限制**： 创建节点池添加节点时不支持该参数。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type dedicated_host_id: str
        :param user_tags: **参数解释**： 云服务器标签（资源标签）。字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        :param initialized_conditions: **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \&quot;initializedConditions\&quot;: [\&quot;CCEInitial\&quot;, \&quot;CustomedInitial\&quot;]； 2. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   &#x60;&#x60;&#x60;   status:     conditions:     - type: CCEInitial       status: &#39;True&#39;     - type: CustomedInitial       status: &#39;True&#39;   &#x60;&#x60;&#x60; 3. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 4. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\&quot;initializedConditions\&quot;: [\&quot;CCEInitial:15m\&quot;, \&quot;CustomedInitial:15m\&quot;]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。
        :type initialized_conditions: list[str]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        :param hostname_config: 
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        :param server_enterprise_project_id: **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。
        :type server_enterprise_project_id: str
        :param partition: **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及
        :type partition: str
        :param configurations_override: **参数解释：** 覆盖节点默认组件配置。  [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0652.htmll)。](tag:hws) [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0652.html)。](tag:hws_hk) **约束限制：** 若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。 
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        :param node_name_template: 
        :type node_name_template: :class:`huaweicloudsdkcce.v3.NodeSpecNodeNameTemplate`
        """
        
        

        self._flavor = None
        self._az = None
        self._os = None
        self._login = None
        self._root_volume = None
        self._data_volumes = None
        self._storage = None
        self._public_ip = None
        self._node_nic_spec = None
        self._count = None
        self._billing_mode = None
        self._taints = None
        self._wait_post_install_finish = None
        self._k8s_tags = None
        self._ecs_group_id = None
        self._dedicated_host_id = None
        self._user_tags = None
        self._runtime = None
        self._initialized_conditions = None
        self._extend_param = None
        self._hostname_config = None
        self._server_enterprise_project_id = None
        self._partition = None
        self._configurations_override = None
        self._node_name_template = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if az is not None:
            self.az = az
        if os is not None:
            self.os = os
        if login is not None:
            self.login = login
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if storage is not None:
            self.storage = storage
        if public_ip is not None:
            self.public_ip = public_ip
        if node_nic_spec is not None:
            self.node_nic_spec = node_nic_spec
        if count is not None:
            self.count = count
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if taints is not None:
            self.taints = taints
        if wait_post_install_finish is not None:
            self.wait_post_install_finish = wait_post_install_finish
        if k8s_tags is not None:
            self.k8s_tags = k8s_tags
        if ecs_group_id is not None:
            self.ecs_group_id = ecs_group_id
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if user_tags is not None:
            self.user_tags = user_tags
        if runtime is not None:
            self.runtime = runtime
        if initialized_conditions is not None:
            self.initialized_conditions = initialized_conditions
        if extend_param is not None:
            self.extend_param = extend_param
        if hostname_config is not None:
            self.hostname_config = hostname_config
        if server_enterprise_project_id is not None:
            self.server_enterprise_project_id = server_enterprise_project_id
        if partition is not None:
            self.partition = partition
        if configurations_override is not None:
            self.configurations_override = configurations_override
        if node_name_template is not None:
            self.node_name_template = node_name_template

    @property
    def flavor(self):
        r"""Gets the flavor of this NodeTemplate.

        **参数解释**： 节点的规格，CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The flavor of this NodeTemplate.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NodeTemplate.

        **参数解释**： 节点的规格，CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param flavor: The flavor of this NodeTemplate.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az(self):
        r"""Gets the az of this NodeTemplate.

        **参数解释**： 待创建节点所在的可用区，需要指定可用区（AZ）的名称，通过api创建节点不支持随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk) **约束限制**： 创建节点池并设置伸缩组时，该参数不允许填写为random。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The az of this NodeTemplate.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this NodeTemplate.

        **参数解释**： 待创建节点所在的可用区，需要指定可用区（AZ）的名称，通过api创建节点不支持随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk) **约束限制**： 创建节点池并设置伸缩组时，该参数不允许填写为random。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param az: The az of this NodeTemplate.
        :type az: str
        """
        self._az = az

    @property
    def os(self):
        r"""Gets the os of this NodeTemplate.

        **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若在创建节点时未指定该配置，CCE会根据集群版本自动选择支持的OS版本。 - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，节点将使用私有镜像，则该参数为非必选参数。 [- 若在创建节点时指定了extendParam中的securityReinforcementType参数为cybersecurity，节点将开启安全等保加固功能，则节点的操作系统类型必须使用HCE2.0。当用户未配置私有镜像时，该参数必须为“Huawei Cloud EulerOS 2.0”；当用户配置了私有镜像且私有镜像操作系统类型为HCE2.0，则该参数为非必选参数。](tag:hws)  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The os of this NodeTemplate.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeTemplate.

        **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若在创建节点时未指定该配置，CCE会根据集群版本自动选择支持的OS版本。 - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，节点将使用私有镜像，则该参数为非必选参数。 [- 若在创建节点时指定了extendParam中的securityReinforcementType参数为cybersecurity，节点将开启安全等保加固功能，则节点的操作系统类型必须使用HCE2.0。当用户未配置私有镜像时，该参数必须为“Huawei Cloud EulerOS 2.0”；当用户配置了私有镜像且私有镜像操作系统类型为HCE2.0，则该参数为非必选参数。](tag:hws)  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param os: The os of this NodeTemplate.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        r"""Gets the login of this NodeTemplate.

        :return: The login of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this NodeTemplate.

        :param login: The login of this NodeTemplate.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def root_volume(self):
        r"""Gets the root_volume of this NodeTemplate.

        :return: The root_volume of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this NodeTemplate.

        :param root_volume: The root_volume of this NodeTemplate.
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NodeTemplate.

        **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： - 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 - 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 - 仅在选择系统盘作为系统组件存储磁盘时，允许为空。

        :return: The data_volumes of this NodeTemplate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NodeTemplate.

        **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： - 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 - 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 - 仅在选择系统盘作为系统组件存储磁盘时，允许为空。

        :param data_volumes: The data_volumes of this NodeTemplate.
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def storage(self):
        r"""Gets the storage of this NodeTemplate.

        :return: The storage of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this NodeTemplate.

        :param storage: The storage of this NodeTemplate.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NodeTemplate.

        :return: The public_ip of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NodeTemplate.

        :param public_ip: The public_ip of this NodeTemplate.
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        self._public_ip = public_ip

    @property
    def node_nic_spec(self):
        r"""Gets the node_nic_spec of this NodeTemplate.

        :return: The node_nic_spec of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        """
        return self._node_nic_spec

    @node_nic_spec.setter
    def node_nic_spec(self, node_nic_spec):
        r"""Sets the node_nic_spec of this NodeTemplate.

        :param node_nic_spec: The node_nic_spec of this NodeTemplate.
        :type node_nic_spec: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        """
        self._node_nic_spec = node_nic_spec

    @property
    def count(self):
        r"""Gets the count of this NodeTemplate.

        **参数解释**： 批量创建时节点的个数。 **约束限制**： - 作用于节点池时该项可以不填写。 - 创建、更新节点池场景返回中无该参数。 - 创建节点时该参数为必填参数  **取值范围**： 必须为大于等于1，小于等于最大限额的正整数。 **默认取值**： 不涉及

        :return: The count of this NodeTemplate.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this NodeTemplate.

        **参数解释**： 批量创建时节点的个数。 **约束限制**： - 作用于节点池时该项可以不填写。 - 创建、更新节点池场景返回中无该参数。 - 创建节点时该参数为必填参数  **取值范围**： 必须为大于等于1，小于等于最大限额的正整数。 **默认取值**： 不涉及

        :param count: The count of this NodeTemplate.
        :type count: int
        """
        self._count = count

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this NodeTemplate.

        **参数解释**： 节点的计费模式。 **约束限制**： 不涉及 **取值范围**： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk)  **默认取值**： 0

        :return: The billing_mode of this NodeTemplate.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this NodeTemplate.

        **参数解释**： 节点的计费模式。 **约束限制**： 不涉及 **取值范围**： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk)  **默认取值**： 0

        :param billing_mode: The billing_mode of this NodeTemplate.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def taints(self):
        r"""Gets the taints of this NodeTemplate.

        **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ```  **约束限制**： taints配置不超过20条。

        :return: The taints of this NodeTemplate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this NodeTemplate.

        **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ```  **约束限制**： taints配置不超过20条。

        :param taints: The taints of this NodeTemplate.
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def wait_post_install_finish(self):
        r"""Gets the wait_post_install_finish of this NodeTemplate.

        **参数解释：** 该参数用于控制创建节点时 **post-install脚本执行完成前允许节点调度** 行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :return: The wait_post_install_finish of this NodeTemplate.
        :rtype: bool
        """
        return self._wait_post_install_finish

    @wait_post_install_finish.setter
    def wait_post_install_finish(self, wait_post_install_finish):
        r"""Sets the wait_post_install_finish of this NodeTemplate.

        **参数解释：** 该参数用于控制创建节点时 **post-install脚本执行完成前允许节点调度** 行为。当该参数未设置或者为false时，在kubernetes节点就绪时，容器即可被调度到可用节点。当该参数为true时，在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **约束限制：** 不涉及  **取值范围：** - false：在kubernetes节点就绪时，容器即可被调度到可用节点。           - true：在kubernetes节点就绪时且post-install脚本执行完成时，容器才可被调度到可用节点。  **默认取值：** false

        :param wait_post_install_finish: The wait_post_install_finish of this NodeTemplate.
        :type wait_post_install_finish: bool
        """
        self._wait_post_install_finish = wait_post_install_finish

    @property
    def k8s_tags(self):
        r"""Gets the k8s_tags of this NodeTemplate.

        **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```  **约束限制**： 键值对个数不超过20条。

        :return: The k8s_tags of this NodeTemplate.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        r"""Sets the k8s_tags of this NodeTemplate.

        **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```  **约束限制**： 键值对个数不超过20条。

        :param k8s_tags: The k8s_tags of this NodeTemplate.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def ecs_group_id(self):
        r"""Gets the ecs_group_id of this NodeTemplate.

        **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建、更新节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The ecs_group_id of this NodeTemplate.
        :rtype: str
        """
        return self._ecs_group_id

    @ecs_group_id.setter
    def ecs_group_id(self, ecs_group_id):
        r"""Sets the ecs_group_id of this NodeTemplate.

        **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建、更新节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param ecs_group_id: The ecs_group_id of this NodeTemplate.
        :type ecs_group_id: str
        """
        self._ecs_group_id = ecs_group_id

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this NodeTemplate.

        **参数解释**： 指定DeH主机的ID，将节点调度到自己的DeH上。 **约束限制**： 创建节点池添加节点时不支持该参数。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The dedicated_host_id of this NodeTemplate.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this NodeTemplate.

        **参数解释**： 指定DeH主机的ID，将节点调度到自己的DeH上。 **约束限制**： 创建节点池添加节点时不支持该参数。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param dedicated_host_id: The dedicated_host_id of this NodeTemplate.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def user_tags(self):
        r"""Gets the user_tags of this NodeTemplate.

        **参数解释**： 云服务器标签（资源标签）。字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。

        :return: The user_tags of this NodeTemplate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        r"""Sets the user_tags of this NodeTemplate.

        **参数解释**： 云服务器标签（资源标签）。字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，创建节点池时节点模板参数中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。

        :param user_tags: The user_tags of this NodeTemplate.
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def runtime(self):
        r"""Gets the runtime of this NodeTemplate.

        :return: The runtime of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this NodeTemplate.

        :param runtime: The runtime of this NodeTemplate.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def initialized_conditions(self):
        r"""Gets the initialized_conditions of this NodeTemplate.

        **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \"initializedConditions\": [\"CCEInitial\", \"CustomedInitial\"]； 2. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   ```   status:     conditions:     - type: CCEInitial       status: 'True'     - type: CustomedInitial       status: 'True'   ``` 3. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 4. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\"initializedConditions\": [\"CCEInitial:15m\", \"CustomedInitial:15m\"]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。

        :return: The initialized_conditions of this NodeTemplate.
        :rtype: list[str]
        """
        return self._initialized_conditions

    @initialized_conditions.setter
    def initialized_conditions(self, initialized_conditions):
        r"""Sets the initialized_conditions of this NodeTemplate.

        **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \"initializedConditions\": [\"CCEInitial\", \"CustomedInitial\"]； 2. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   ```   status:     conditions:     - type: CCEInitial       status: 'True'     - type: CustomedInitial       status: 'True'   ``` 3. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 4. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\"initializedConditions\": [\"CCEInitial:15m\", \"CustomedInitial:15m\"]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。

        :param initialized_conditions: The initialized_conditions of this NodeTemplate.
        :type initialized_conditions: list[str]
        """
        self._initialized_conditions = initialized_conditions

    @property
    def extend_param(self):
        r"""Gets the extend_param of this NodeTemplate.

        :return: The extend_param of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this NodeTemplate.

        :param extend_param: The extend_param of this NodeTemplate.
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        self._extend_param = extend_param

    @property
    def hostname_config(self):
        r"""Gets the hostname_config of this NodeTemplate.

        :return: The hostname_config of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        return self._hostname_config

    @hostname_config.setter
    def hostname_config(self, hostname_config):
        r"""Sets the hostname_config of this NodeTemplate.

        :param hostname_config: The hostname_config of this NodeTemplate.
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        self._hostname_config = hostname_config

    @property
    def server_enterprise_project_id(self):
        r"""Gets the server_enterprise_project_id of this NodeTemplate.

        **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :return: The server_enterprise_project_id of this NodeTemplate.
        :rtype: str
        """
        return self._server_enterprise_project_id

    @server_enterprise_project_id.setter
    def server_enterprise_project_id(self, server_enterprise_project_id):
        r"""Sets the server_enterprise_project_id of this NodeTemplate.

        **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :param server_enterprise_project_id: The server_enterprise_project_id of this NodeTemplate.
        :type server_enterprise_project_id: str
        """
        self._server_enterprise_project_id = server_enterprise_project_id

    @property
    def partition(self):
        r"""Gets the partition of this NodeTemplate.

        **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及

        :return: The partition of this NodeTemplate.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this NodeTemplate.

        **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及

        :param partition: The partition of this NodeTemplate.
        :type partition: str
        """
        self._partition = partition

    @property
    def configurations_override(self):
        r"""Gets the configurations_override of this NodeTemplate.

        **参数解释：** 覆盖节点默认组件配置。  [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0652.htmll)。](tag:hws) [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0652.html)。](tag:hws_hk) **约束限制：** 若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。 

        :return: The configurations_override of this NodeTemplate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        """
        return self._configurations_override

    @configurations_override.setter
    def configurations_override(self, configurations_override):
        r"""Sets the configurations_override of this NodeTemplate.

        **参数解释：** 覆盖节点默认组件配置。  [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0652.htmll)。](tag:hws) [当前支持的可配置组件及其参数详见[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0652.html)。](tag:hws_hk) **约束限制：** 若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。 

        :param configurations_override: The configurations_override of this NodeTemplate.
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        """
        self._configurations_override = configurations_override

    @property
    def node_name_template(self):
        r"""Gets the node_name_template of this NodeTemplate.

        :return: The node_name_template of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpecNodeNameTemplate`
        """
        return self._node_name_template

    @node_name_template.setter
    def node_name_template(self, node_name_template):
        r"""Sets the node_name_template of this NodeTemplate.

        :param node_name_template: The node_name_template of this NodeTemplate.
        :type node_name_template: :class:`huaweicloudsdkcce.v3.NodeSpecNodeNameTemplate`
        """
        self._node_name_template = node_name_template

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
        if not isinstance(other, NodeTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
