# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpec:

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
        'public_ip': 'NodePublicIP',
        'node_nic_spec': 'NodeNicSpec',
        'count': 'int',
        'billing_mode': 'int',
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'ecs_group_id': 'str',
        'dedicated_host_id': 'str',
        'user_tags': 'list[UserTag]',
        'runtime': 'Runtime',
        'initialized_conditions': 'list[str]',
        'extend_param': 'NodeExtendParam',
        'hostname_config': 'HostnameConfig',
        'server_enterprise_project_id': 'str',
        'partition': 'str'
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
        'k8s_tags': 'k8sTags',
        'ecs_group_id': 'ecsGroupId',
        'dedicated_host_id': 'dedicatedHostId',
        'user_tags': 'userTags',
        'runtime': 'runtime',
        'initialized_conditions': 'initializedConditions',
        'extend_param': 'extendParam',
        'hostname_config': 'hostnameConfig',
        'server_enterprise_project_id': 'serverEnterpriseProjectID',
        'partition': 'partition'
    }

    def __init__(self, flavor=None, az=None, os=None, login=None, root_volume=None, data_volumes=None, storage=None, public_ip=None, node_nic_spec=None, count=None, billing_mode=None, taints=None, k8s_tags=None, ecs_group_id=None, dedicated_host_id=None, user_tags=None, runtime=None, initialized_conditions=None, extend_param=None, hostname_config=None, server_enterprise_project_id=None, partition=None):
        r"""NodeSpec

        The model defined in huaweicloud sdk

        :param flavor: 节点的规格，CCE支持的节点规格请参考[节点规格说明](https://support.huaweicloud.com/api-cce/cce_02_0368.html)获取。 
        :type flavor: str
        :param az: 待创建节点所在的可用区，需要指定可用区（AZ）的名称，不填或者填random选择随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 
        :type az: str
        :param os: [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/api-cce/node-os.html)。](tag:hws) [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/intl/zh-cn/api-cce/node-os.html)。](tag:hws_hk) &gt; - 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。 &gt; - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 &gt; - 创建节点池时，该参数为必选。 &gt; - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。 
        :type os: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        :param data_volumes: 节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 针对专属云节点，参数解释与rootVolume一致
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodePublicIP`
        :param node_nic_spec: 
        :type node_nic_spec: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        :param count: 批量创建时节点的个数，必须为大于等于1，小于等于最大限额的正整数。作用于节点池时该项可以不填写。
        :type count: int
        :param billing_mode: 节点的计费模式： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk) 
        :type billing_mode: int
        :param taints: 支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  &#x60;&#x60;&#x60; \&quot;taints\&quot;: [{   \&quot;key\&quot;: \&quot;status\&quot;,   \&quot;value\&quot;: \&quot;unavailable\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }, {   \&quot;key\&quot;: \&quot;looks\&quot;,   \&quot;value\&quot;: \&quot;bad\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }] &#x60;&#x60;&#x60; 
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        :param k8s_tags: 格式为key/value键值对。键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60; 
        :type k8s_tags: dict(str, str)
        :param ecs_group_id: 云服务器组ID，若指定，将节点创建在该云服务器组下 &gt; 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置
        :type ecs_group_id: str
        :param dedicated_host_id: 指定DeH主机的ID，将节点调度到自己的DeH上。 &gt;创建节点池添加节点时不支持该参数。 
        :type dedicated_host_id: str
        :param user_tags: 云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 &gt; 标签键只能包含大写字母.小写字母、数字和特殊字符(-_)以及Unicode字符，长度不超过36个字符。 
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        :param initialized_conditions: 自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions&#x3D;CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 
        :type initialized_conditions: list[str]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        :param hostname_config: 
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        :param server_enterprise_project_id: 服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。
        :type server_enterprise_project_id: str
        :param partition: **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及
        :type partition: str
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
        self.discriminator = None

        self.flavor = flavor
        self.az = az
        if os is not None:
            self.os = os
        self.login = login
        self.root_volume = root_volume
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

    @property
    def flavor(self):
        r"""Gets the flavor of this NodeSpec.

        节点的规格，CCE支持的节点规格请参考[节点规格说明](https://support.huaweicloud.com/api-cce/cce_02_0368.html)获取。 

        :return: The flavor of this NodeSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NodeSpec.

        节点的规格，CCE支持的节点规格请参考[节点规格说明](https://support.huaweicloud.com/api-cce/cce_02_0368.html)获取。 

        :param flavor: The flavor of this NodeSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az(self):
        r"""Gets the az of this NodeSpec.

        待创建节点所在的可用区，需要指定可用区（AZ）的名称，不填或者填random选择随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :return: The az of this NodeSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this NodeSpec.

        待创建节点所在的可用区，需要指定可用区（AZ）的名称，不填或者填random选择随机可用区。 [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :param az: The az of this NodeSpec.
        :type az: str
        """
        self._az = az

    @property
    def os(self):
        r"""Gets the os of this NodeSpec.

        [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/api-cce/node-os.html)。](tag:hws) [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/intl/zh-cn/api-cce/node-os.html)。](tag:hws_hk) > - 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。 > - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 > - 创建节点池时，该参数为必选。 > - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。 

        :return: The os of this NodeSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeSpec.

        [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/api-cce/node-os.html)。](tag:hws) [节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](https://support.huaweicloud.com/intl/zh-cn/api-cce/node-os.html)。](tag:hws_hk) > - 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。 > - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。 > - 创建节点池时，该参数为必选。 > - 若创建节点时使用共享磁盘空间，即磁盘初始化配置管理参数使用storage，且StorageGroups中virtualSpaces的name字段指定为share，该参数为必选。 

        :param os: The os of this NodeSpec.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        r"""Gets the login of this NodeSpec.

        :return: The login of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this NodeSpec.

        :param login: The login of this NodeSpec.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def root_volume(self):
        r"""Gets the root_volume of this NodeSpec.

        :return: The root_volume of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this NodeSpec.

        :param root_volume: The root_volume of this NodeSpec.
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 针对专属云节点，参数解释与rootVolume一致

        :return: The data_volumes of this NodeSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。 如果数据盘正供容器运行时和Kubelet组件使用，则不可被卸载，否则将导致节点不可用。 针对专属云节点，参数解释与rootVolume一致

        :param data_volumes: The data_volumes of this NodeSpec.
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def storage(self):
        r"""Gets the storage of this NodeSpec.

        :return: The storage of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this NodeSpec.

        :param storage: The storage of this NodeSpec.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NodeSpec.

        :return: The public_ip of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodePublicIP`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NodeSpec.

        :param public_ip: The public_ip of this NodeSpec.
        :type public_ip: :class:`huaweicloudsdkcce.v3.NodePublicIP`
        """
        self._public_ip = public_ip

    @property
    def node_nic_spec(self):
        r"""Gets the node_nic_spec of this NodeSpec.

        :return: The node_nic_spec of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        """
        return self._node_nic_spec

    @node_nic_spec.setter
    def node_nic_spec(self, node_nic_spec):
        r"""Sets the node_nic_spec of this NodeSpec.

        :param node_nic_spec: The node_nic_spec of this NodeSpec.
        :type node_nic_spec: :class:`huaweicloudsdkcce.v3.NodeNicSpec`
        """
        self._node_nic_spec = node_nic_spec

    @property
    def count(self):
        r"""Gets the count of this NodeSpec.

        批量创建时节点的个数，必须为大于等于1，小于等于最大限额的正整数。作用于节点池时该项可以不填写。

        :return: The count of this NodeSpec.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this NodeSpec.

        批量创建时节点的个数，必须为大于等于1，小于等于最大限额的正整数。作用于节点池时该项可以不填写。

        :param count: The count of this NodeSpec.
        :type count: int
        """
        self._count = count

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this NodeSpec.

        节点的计费模式： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk) 

        :return: The billing_mode of this NodeSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this NodeSpec.

        节点的计费模式： -  0: 按需付费 [- 1: 包周期](tag:hws,hws_hk) [- 2: 已废弃：自动付费包周期](tag:hws,hws_hk) 

        :param billing_mode: The billing_mode of this NodeSpec.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def taints(self):
        r"""Gets the taints of this NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :return: The taints of this NodeSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :param taints: The taints of this NodeSpec.
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def k8s_tags(self):
        r"""Gets the k8s_tags of this NodeSpec.

        格式为key/value键值对。键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` 

        :return: The k8s_tags of this NodeSpec.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        r"""Sets the k8s_tags of this NodeSpec.

        格式为key/value键值对。键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。   示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` 

        :param k8s_tags: The k8s_tags of this NodeSpec.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def ecs_group_id(self):
        r"""Gets the ecs_group_id of this NodeSpec.

        云服务器组ID，若指定，将节点创建在该云服务器组下 > 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置

        :return: The ecs_group_id of this NodeSpec.
        :rtype: str
        """
        return self._ecs_group_id

    @ecs_group_id.setter
    def ecs_group_id(self, ecs_group_id):
        r"""Sets the ecs_group_id of this NodeSpec.

        云服务器组ID，若指定，将节点创建在该云服务器组下 > 创建节点池时该配置不会生效，若要保持节点池中的节点都在同一个云服务器组内，请在节点池 nodeManagement 字段中配置

        :param ecs_group_id: The ecs_group_id of this NodeSpec.
        :type ecs_group_id: str
        """
        self._ecs_group_id = ecs_group_id

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this NodeSpec.

        指定DeH主机的ID，将节点调度到自己的DeH上。 >创建节点池添加节点时不支持该参数。 

        :return: The dedicated_host_id of this NodeSpec.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this NodeSpec.

        指定DeH主机的ID，将节点调度到自己的DeH上。 >创建节点池添加节点时不支持该参数。 

        :param dedicated_host_id: The dedicated_host_id of this NodeSpec.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def user_tags(self):
        r"""Gets the user_tags of this NodeSpec.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 > 标签键只能包含大写字母.小写字母、数字和特殊字符(-_)以及Unicode字符，长度不超过36个字符。 

        :return: The user_tags of this NodeSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        r"""Sets the user_tags of this NodeSpec.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。 字段使用场景：在节点创建场景下，支持指定初始值，查询时不返回该字段；在节点池场景下，其中节点模板中支持指定初始值，查询时支持返回该字段；在其余场景下，查询时都不会返回该字段。 > 标签键只能包含大写字母.小写字母、数字和特殊字符(-_)以及Unicode字符，长度不超过36个字符。 

        :param user_tags: The user_tags of this NodeSpec.
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def runtime(self):
        r"""Gets the runtime of this NodeSpec.

        :return: The runtime of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this NodeSpec.

        :param runtime: The runtime of this NodeSpec.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def initialized_conditions(self):
        r"""Gets the initialized_conditions of this NodeSpec.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :return: The initialized_conditions of this NodeSpec.
        :rtype: list[str]
        """
        return self._initialized_conditions

    @initialized_conditions.setter
    def initialized_conditions(self, initialized_conditions):
        r"""Sets the initialized_conditions of this NodeSpec.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :param initialized_conditions: The initialized_conditions of this NodeSpec.
        :type initialized_conditions: list[str]
        """
        self._initialized_conditions = initialized_conditions

    @property
    def extend_param(self):
        r"""Gets the extend_param of this NodeSpec.

        :return: The extend_param of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this NodeSpec.

        :param extend_param: The extend_param of this NodeSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        self._extend_param = extend_param

    @property
    def hostname_config(self):
        r"""Gets the hostname_config of this NodeSpec.

        :return: The hostname_config of this NodeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        return self._hostname_config

    @hostname_config.setter
    def hostname_config(self, hostname_config):
        r"""Sets the hostname_config of this NodeSpec.

        :param hostname_config: The hostname_config of this NodeSpec.
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        self._hostname_config = hostname_config

    @property
    def server_enterprise_project_id(self):
        r"""Gets the server_enterprise_project_id of this NodeSpec.

        服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :return: The server_enterprise_project_id of this NodeSpec.
        :rtype: str
        """
        return self._server_enterprise_project_id

    @server_enterprise_project_id.setter
    def server_enterprise_project_id(self, server_enterprise_project_id):
        r"""Sets the server_enterprise_project_id of this NodeSpec.

        服务器企业项目ID。CCE服务不实现EPS相关特性，该字段仅用于同步服务器企业项目ID。 创建节点/节点池场景：可指定已存在企业项目，当取值为空时，该字段继承集群企业项目属性。 更新节点池场景：配置修改后仅会对新增节点的服务器生效，存量节点需前往EPS界面迁移。 如果更新时不指定值，不会更新该字段。 当该字段为空时，返回集群企业项目。

        :param server_enterprise_project_id: The server_enterprise_project_id of this NodeSpec.
        :type server_enterprise_project_id: str
        """
        self._server_enterprise_project_id = server_enterprise_project_id

    @property
    def partition(self):
        r"""Gets the partition of this NodeSpec.

        **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及

        :return: The partition of this NodeSpec.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this NodeSpec.

        **参数解释**： 表示节点所属分区。分区可以选择中心云[或者[边缘小站](https://support.huaweicloud.com/usermanual-cloudpond/ies_02_0401.html)。](tag:hws)[或者[边缘小站](https://support.huaweicloud.com/intl/zh-cn/usermanual-cloudpond/ies_02_0401.html)。](tag:hws_hk) **约束限制**： 仅开启了对分布式云支持的Turbo集群支持指定该字段。 **取值范围**： - center: 中心云 - 边缘小站的可用区ID  **默认取值**： 不涉及

        :param partition: The partition of this NodeSpec.
        :type partition: str
        """
        self._partition = partition

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
        if not isinstance(other, NodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
