# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecUpdate:

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
        'os': 'str',
        'login': 'Login',
        'root_volume_update': 'Volume',
        'data_volumes_update': 'list[Volume]',
        'storage': 'Storage',
        'runtime': 'Runtime',
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'ecs_group_id': 'str',
        'user_tags': 'list[UserTag]',
        'node_name_template': 'NodeSpecUpdateNodeNameTemplate',
        'initialized_conditions': 'list[str]',
        'server_enterprise_project_id': 'str',
        'node_nic_spec_update': 'NodeSpecUpdateNodeNicSpecUpdate',
        'extend_param': 'NodePoolUpdateExtendParam',
        'public_ip': 'NodeEIPSpec'
    }

    attribute_map = {
        'flavor': 'flavor',
        'os': 'os',
        'login': 'login',
        'root_volume_update': 'rootVolumeUpdate',
        'data_volumes_update': 'dataVolumesUpdate',
        'storage': 'storage',
        'runtime': 'runtime',
        'taints': 'taints',
        'k8s_tags': 'k8sTags',
        'ecs_group_id': 'ecsGroupId',
        'user_tags': 'userTags',
        'node_name_template': 'nodeNameTemplate',
        'initialized_conditions': 'initializedConditions',
        'server_enterprise_project_id': 'serverEnterpriseProjectID',
        'node_nic_spec_update': 'nodeNicSpecUpdate',
        'extend_param': 'extendParam',
        'public_ip': 'publicIP'
    }

    def __init__(self, flavor=None, os=None, login=None, root_volume_update=None, data_volumes_update=None, storage=None, runtime=None, taints=None, k8s_tags=None, ecs_group_id=None, user_tags=None, node_name_template=None, initialized_conditions=None, server_enterprise_project_id=None, node_nic_spec_update=None, extend_param=None, public_ip=None):
        r"""NodeSpecUpdate

        The model defined in huaweicloud sdk

        :param flavor: **参数解释：** 节点的规格。  **约束限制**： 不涉及 **取值范围：** CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **默认取值：** 不涉及
        :type flavor: str
        :param os: **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 - 该参数缺省时，CCE会根据集群版本自动选择支持的OS版本。 - 创建节点池时，该参数为必选。 - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type os: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param root_volume_update: 
        :type root_volume_update: :class:`huaweicloudsdkcce.v3.Volume`
        :param data_volumes_update: **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。
        :type data_volumes_update: list[:class:`huaweicloudsdkcce.v3.Volume`]
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        :param taints: **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  &#x60;&#x60;&#x60; \&quot;taints\&quot;: [{   \&quot;key\&quot;: \&quot;status\&quot;,   \&quot;value\&quot;: \&quot;unavailable\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }, {   \&quot;key\&quot;: \&quot;looks\&quot;,   \&quot;value\&quot;: \&quot;bad\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }] &#x60;&#x60;&#x60;  **约束限制**： - taints配置不超过20条。 - 参数未指定或者为空数组时将删除节点池的自定义Taints。 - 更新节点池时，此字段为非必填字段。
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        :param k8s_tags: **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60;  **约束限制**： - 键值对个数不超过20条。 - 参数未指定或者为空对象时将删除节点池的自定义K8s标签。 - 更新节点池时，此字段为非必填字段。
        :type k8s_tags: dict(str, str)
        :param ecs_group_id: **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type ecs_group_id: str
        :param user_tags: **参数解释**： 云服务器标签（资源标签）。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 - 参数未指定或者为空数组时将删除节点池的自定义云服务器标签。 - 更新节点池时，此字段为非必填字段。  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        :param node_name_template: 
        :type node_name_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNameTemplate`
        :param initialized_conditions: **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \&quot;initializedConditions\&quot;: [\&quot;CCEInitial\&quot;, \&quot;CustomedInitial\&quot;]； 2. 更新节点，传入参数 \&quot;initializedConditions\&quot;: [\&quot;NodeInitial\&quot;]，节点池新建的节点注册到集群时默认会被设置为不可调度； 3. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   &#x60;&#x60;&#x60;   status:     conditions:     - type: CCEInitial       status: &#39;True&#39;     - type: CustomedInitial       status: &#39;True&#39;   &#x60;&#x60;&#x60; 4. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 5. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\&quot;initializedConditions\&quot;: [\&quot;CCEInitial:15m\&quot;, \&quot;CustomedInitial:15m\&quot;]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。
        :type initialized_conditions: list[str]
        :param server_enterprise_project_id: **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。
        :type server_enterprise_project_id: str
        :param node_nic_spec_update: 
        :type node_nic_spec_update: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNicSpecUpdate`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodePoolUpdateExtendParam`
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        
        

        self._flavor = None
        self._os = None
        self._login = None
        self._root_volume_update = None
        self._data_volumes_update = None
        self._storage = None
        self._runtime = None
        self._taints = None
        self._k8s_tags = None
        self._ecs_group_id = None
        self._user_tags = None
        self._node_name_template = None
        self._initialized_conditions = None
        self._server_enterprise_project_id = None
        self._node_nic_spec_update = None
        self._extend_param = None
        self._public_ip = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if os is not None:
            self.os = os
        if login is not None:
            self.login = login
        if root_volume_update is not None:
            self.root_volume_update = root_volume_update
        if data_volumes_update is not None:
            self.data_volumes_update = data_volumes_update
        if storage is not None:
            self.storage = storage
        if runtime is not None:
            self.runtime = runtime
        self.taints = taints
        self.k8s_tags = k8s_tags
        if ecs_group_id is not None:
            self.ecs_group_id = ecs_group_id
        self.user_tags = user_tags
        if node_name_template is not None:
            self.node_name_template = node_name_template
        if initialized_conditions is not None:
            self.initialized_conditions = initialized_conditions
        if server_enterprise_project_id is not None:
            self.server_enterprise_project_id = server_enterprise_project_id
        if node_nic_spec_update is not None:
            self.node_nic_spec_update = node_nic_spec_update
        if extend_param is not None:
            self.extend_param = extend_param
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def flavor(self):
        r"""Gets the flavor of this NodeSpecUpdate.

        **参数解释：** 节点的规格。  **约束限制**： 不涉及 **取值范围：** CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **默认取值：** 不涉及

        :return: The flavor of this NodeSpecUpdate.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NodeSpecUpdate.

        **参数解释：** 节点的规格。  **约束限制**： 不涉及 **取值范围：** CCE支持的节点规格请参考[节点规格说明](cce_02_0368.xml)获取。 **默认取值：** 不涉及

        :param flavor: The flavor of this NodeSpecUpdate.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def os(self):
        r"""Gets the os of this NodeSpecUpdate.

        **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 - 该参数缺省时，CCE会根据集群版本自动选择支持的OS版本。 - 创建节点池时，该参数为必选。 - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The os of this NodeSpecUpdate.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeSpecUpdate.

        **参数解释**： 节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。 **约束限制**： - 若当前集群版本不支持该OS类型，则会自动替换为当前集群版本支持的同系列OS类型。 - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 - 该参数缺省时，CCE会根据集群版本自动选择支持的OS版本。 - 创建节点池时，该参数为必选。 - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param os: The os of this NodeSpecUpdate.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        r"""Gets the login of this NodeSpecUpdate.

        :return: The login of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this NodeSpecUpdate.

        :param login: The login of this NodeSpecUpdate.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def root_volume_update(self):
        r"""Gets the root_volume_update of this NodeSpecUpdate.

        :return: The root_volume_update of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.Volume`
        """
        return self._root_volume_update

    @root_volume_update.setter
    def root_volume_update(self, root_volume_update):
        r"""Sets the root_volume_update of this NodeSpecUpdate.

        :param root_volume_update: The root_volume_update of this NodeSpecUpdate.
        :type root_volume_update: :class:`huaweicloudsdkcce.v3.Volume`
        """
        self._root_volume_update = root_volume_update

    @property
    def data_volumes_update(self):
        r"""Gets the data_volumes_update of this NodeSpecUpdate.

        **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。

        :return: The data_volumes_update of this NodeSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        return self._data_volumes_update

    @data_volumes_update.setter
    def data_volumes_update(self, data_volumes_update):
        r"""Sets the data_volumes_update of this NodeSpecUpdate.

        **参数解释**： 节点的数据盘参数。针对专属云节点，参数解释与rootVolume一致。 **约束限制**： 磁盘挂载上限为虚拟机不超过16块，裸金属不超过10块。在此基础上还受限于虚拟机/裸金属规格可挂载磁盘数上限。（目前支持通过控制台和API为CCE节点添加多块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。

        :param data_volumes_update: The data_volumes_update of this NodeSpecUpdate.
        :type data_volumes_update: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        self._data_volumes_update = data_volumes_update

    @property
    def storage(self):
        r"""Gets the storage of this NodeSpecUpdate.

        :return: The storage of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this NodeSpecUpdate.

        :param storage: The storage of this NodeSpecUpdate.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def runtime(self):
        r"""Gets the runtime of this NodeSpecUpdate.

        :return: The runtime of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this NodeSpecUpdate.

        :param runtime: The runtime of this NodeSpecUpdate.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def taints(self):
        r"""Gets the taints of this NodeSpecUpdate.

        **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ```  **约束限制**： - taints配置不超过20条。 - 参数未指定或者为空数组时将删除节点池的自定义Taints。 - 更新节点池时，此字段为非必填字段。

        :return: The taints of this NodeSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this NodeSpecUpdate.

        **参数解释**： 支持给创建出来的节点加Taints来设置反亲和性。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ```  **约束限制**： - taints配置不超过20条。 - 参数未指定或者为空数组时将删除节点池的自定义Taints。 - 更新节点池时，此字段为非必填字段。

        :param taints: The taints of this NodeSpecUpdate.
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def k8s_tags(self):
        r"""Gets the k8s_tags of this NodeSpecUpdate.

        **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```  **约束限制**： - 键值对个数不超过20条。 - 参数未指定或者为空对象时将删除节点池的自定义K8s标签。 - 更新节点池时，此字段为非必填字段。

        :return: The k8s_tags of this NodeSpecUpdate.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        r"""Sets the k8s_tags of this NodeSpecUpdate.

        **参数解释**： 格式为key/value键值对。 - Key：必须以字母或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```  **约束限制**： - 键值对个数不超过20条。 - 参数未指定或者为空对象时将删除节点池的自定义K8s标签。 - 更新节点池时，此字段为非必填字段。

        :param k8s_tags: The k8s_tags of this NodeSpecUpdate.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def ecs_group_id(self):
        r"""Gets the ecs_group_id of this NodeSpecUpdate.

        **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The ecs_group_id of this NodeSpecUpdate.
        :rtype: str
        """
        return self._ecs_group_id

    @ecs_group_id.setter
    def ecs_group_id(self, ecs_group_id):
        r"""Sets the ecs_group_id of this NodeSpecUpdate.

        **参数解释**： 云服务器组ID，若指定，将节点创建在该云服务器组下。 **约束限制**： 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param ecs_group_id: The ecs_group_id of this NodeSpecUpdate.
        :type ecs_group_id: str
        """
        self._ecs_group_id = ecs_group_id

    @property
    def user_tags(self):
        r"""Gets the user_tags of this NodeSpecUpdate.

        **参数解释**： 云服务器标签（资源标签）。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 - 参数未指定或者为空数组时将删除节点池的自定义云服务器标签。 - 更新节点池时，此字段为非必填字段。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The user_tags of this NodeSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        r"""Sets the user_tags of this NodeSpecUpdate.

        **参数解释**： 云服务器标签（资源标签）。 **约束限制**： - 键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 - 参数未指定或者为空数组时将删除节点池的自定义云服务器标签。 - 更新节点池时，此字段为非必填字段。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param user_tags: The user_tags of this NodeSpecUpdate.
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def node_name_template(self):
        r"""Gets the node_name_template of this NodeSpecUpdate.

        :return: The node_name_template of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNameTemplate`
        """
        return self._node_name_template

    @node_name_template.setter
    def node_name_template(self, node_name_template):
        r"""Sets the node_name_template of this NodeSpecUpdate.

        :param node_name_template: The node_name_template of this NodeSpecUpdate.
        :type node_name_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNameTemplate`
        """
        self._node_name_template = node_name_template

    @property
    def initialized_conditions(self):
        r"""Gets the initialized_conditions of this NodeSpecUpdate.

        **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \"initializedConditions\": [\"CCEInitial\", \"CustomedInitial\"]； 2. 更新节点，传入参数 \"initializedConditions\": [\"NodeInitial\"]，节点池新建的节点注册到集群时默认会被设置为不可调度； 3. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   ```   status:     conditions:     - type: CCEInitial       status: 'True'     - type: CustomedInitial       status: 'True'   ``` 4. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 5. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\"initializedConditions\": [\"CCEInitial:15m\", \"CustomedInitial:15m\"]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。

        :return: The initialized_conditions of this NodeSpecUpdate.
        :rtype: list[str]
        """
        return self._initialized_conditions

    @initialized_conditions.setter
    def initialized_conditions(self, initialized_conditions):
        r"""Sets the initialized_conditions of this NodeSpecUpdate.

        **参数解释**： 自定义初始化标记，默认值为空。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。用户在创建节点时，可以通过设置initializedConditions参数，控制污点的移除时间（默认不设置超时时间）。  使用示例如下： 1. 创建节点，传入参数 \"initializedConditions\": [\"CCEInitial\", \"CustomedInitial\"]； 2. 更新节点，传入参数 \"initializedConditions\": [\"NodeInitial\"]，节点池新建的节点注册到集群时默认会被设置为不可调度； 3. 用户在执行完自定义初始化操作后，调用k8s接口（例如PATCH /v1/nodes/{node_ip}/status）更新节点的conditions，插入type为CCEInitial、CustomedInitial的两个标记，状态为True，如下所示：   ```   status:     conditions:     - type: CCEInitial       status: 'True'     - type: CustomedInitial       status: 'True'   ``` 4. CCE组件轮询节点的status.Conditions，查看是否存在type为CCEInitial、CustomedInitial的condition，若存在且status字段值为True，认为节点初始化完成，则移除初始化污点； 5. initializedConditions支持设置超时时间，用户可以在创节点时传入，如：\"initializedConditions\": [\"CCEInitial:15m\", \"CustomedInitial:15m\"]，表示超时时间为15分钟，达到超时时间后，当CCE组件轮询到节点时会自动忽略初始化condition，移除初始化污点。  **约束限制**： - initializedConditions中超时时间取值范围为[1-99]秒 - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个。 - 超时时间仅支持分钟(m)单位。

        :param initialized_conditions: The initialized_conditions of this NodeSpecUpdate.
        :type initialized_conditions: list[str]
        """
        self._initialized_conditions = initialized_conditions

    @property
    def server_enterprise_project_id(self):
        r"""Gets the server_enterprise_project_id of this NodeSpecUpdate.

        **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :return: The server_enterprise_project_id of this NodeSpecUpdate.
        :rtype: str
        """
        return self._server_enterprise_project_id

    @server_enterprise_project_id.setter
    def server_enterprise_project_id(self, server_enterprise_project_id):
        r"""Sets the server_enterprise_project_id of this NodeSpecUpdate.

        **参数解释**： 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 **约束限制**： 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 **取值范围**： 不涉及 **默认取值**： 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :param server_enterprise_project_id: The server_enterprise_project_id of this NodeSpecUpdate.
        :type server_enterprise_project_id: str
        """
        self._server_enterprise_project_id = server_enterprise_project_id

    @property
    def node_nic_spec_update(self):
        r"""Gets the node_nic_spec_update of this NodeSpecUpdate.

        :return: The node_nic_spec_update of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNicSpecUpdate`
        """
        return self._node_nic_spec_update

    @node_nic_spec_update.setter
    def node_nic_spec_update(self, node_nic_spec_update):
        r"""Sets the node_nic_spec_update of this NodeSpecUpdate.

        :param node_nic_spec_update: The node_nic_spec_update of this NodeSpecUpdate.
        :type node_nic_spec_update: :class:`huaweicloudsdkcce.v3.NodeSpecUpdateNodeNicSpecUpdate`
        """
        self._node_nic_spec_update = node_nic_spec_update

    @property
    def extend_param(self):
        r"""Gets the extend_param of this NodeSpecUpdate.

        :return: The extend_param of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodePoolUpdateExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this NodeSpecUpdate.

        :param extend_param: The extend_param of this NodeSpecUpdate.
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodePoolUpdateExtendParam`
        """
        self._extend_param = extend_param

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NodeSpecUpdate.

        :return: The public_ip of this NodeSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NodeSpecUpdate.

        :param public_ip: The public_ip of this NodeSpecUpdate.
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        self._public_ip = public_ip

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
        if not isinstance(other, NodeSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
