# coding: utf-8

import pprint
import re

import six





class V3NodeSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'az': 'str',
        'billing_mode': 'int',
        'count': 'int',
        'data_volumes': 'list[V3DataVolume]',
        'dedicated_host_id': 'str',
        'ecs_group_id': 'str',
        'extend_param': 'dict(str, object)',
        'flavor': 'str',
        'k8s_tags': 'dict(str, str)',
        'login': 'Login',
        'node_nic_spec': 'NodeNicSpec',
        'offload_node': 'bool',
        'os': 'str',
        'public_ip': 'V3NodePublicIP',
        'root_volume': 'V3RootVolume',
        'taints': 'list[Taint]',
        'user_tags': 'list[UserTag]'
    }

    attribute_map = {
        'az': 'az',
        'billing_mode': 'billingMode',
        'count': 'count',
        'data_volumes': 'dataVolumes',
        'dedicated_host_id': 'dedicatedHostId',
        'ecs_group_id': 'ecsGroupId',
        'extend_param': 'extendParam',
        'flavor': 'flavor',
        'k8s_tags': 'k8sTags',
        'login': 'login',
        'node_nic_spec': 'nodeNicSpec',
        'offload_node': 'offloadNode',
        'os': 'os',
        'public_ip': 'publicIP',
        'root_volume': 'rootVolume',
        'taints': 'taints',
        'user_tags': 'userTags'
    }

    def __init__(self, az=None, billing_mode=None, count=None, data_volumes=None, dedicated_host_id=None, ecs_group_id=None, extend_param=None, flavor=None, k8s_tags=None, login=None, node_nic_spec=None, offload_node=None, os=None, public_ip=None, root_volume=None, taints=None, user_tags=None):
        """V3NodeSpec - a model defined in huaweicloud sdk"""
        
        

        self._az = None
        self._billing_mode = None
        self._count = None
        self._data_volumes = None
        self._dedicated_host_id = None
        self._ecs_group_id = None
        self._extend_param = None
        self._flavor = None
        self._k8s_tags = None
        self._login = None
        self._node_nic_spec = None
        self._offload_node = None
        self._os = None
        self._public_ip = None
        self._root_volume = None
        self._taints = None
        self._user_tags = None
        self.discriminator = None

        self.az = az
        if billing_mode is not None:
            self.billing_mode = billing_mode
        self.count = count
        self.data_volumes = data_volumes
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if ecs_group_id is not None:
            self.ecs_group_id = ecs_group_id
        if extend_param is not None:
            self.extend_param = extend_param
        self.flavor = flavor
        if k8s_tags is not None:
            self.k8s_tags = k8s_tags
        self.login = login
        if node_nic_spec is not None:
            self.node_nic_spec = node_nic_spec
        if offload_node is not None:
            self.offload_node = offload_node
        self.os = os
        if public_ip is not None:
            self.public_ip = public_ip
        self.root_volume = root_volume
        if taints is not None:
            self.taints = taints
        if user_tags is not None:
            self.user_tags = user_tags

    @property
    def az(self):
        """Gets the az of this V3NodeSpec.

          节点所在的可用区名. 底层实际存在，位于该用户物理可用区组之内的可用区

        :return: The az of this V3NodeSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this V3NodeSpec.

          节点所在的可用区名. 底层实际存在，位于该用户物理可用区组之内的可用区

        :param az: The az of this V3NodeSpec.
        :type: str
        """
        self._az = az

    @property
    def billing_mode(self):
        """Gets the billing_mode of this V3NodeSpec.

        节点的计费模式：取值为 0（按需付费）、2（自动付费包周期）  自动付费包周期支持普通用户token。 >创建按需节点不影响集群状态；创建包周期节点时，集群状态会转换为“扩容中”。

        :return: The billing_mode of this V3NodeSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this V3NodeSpec.

        节点的计费模式：取值为 0（按需付费）、2（自动付费包周期）  自动付费包周期支持普通用户token。 >创建按需节点不影响集群状态；创建包周期节点时，集群状态会转换为“扩容中”。

        :param billing_mode: The billing_mode of this V3NodeSpec.
        :type: int
        """
        self._billing_mode = billing_mode

    @property
    def count(self):
        """Gets the count of this V3NodeSpec.

        批量创建时节点的个数，必须为大于等于1，小于等于最大限额的正整数。作用于节点池时该项允许为0

        :return: The count of this V3NodeSpec.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V3NodeSpec.

        批量创建时节点的个数，必须为大于等于1，小于等于最大限额的正整数。作用于节点池时该项允许为0

        :param count: The count of this V3NodeSpec.
        :type: int
        """
        self._count = count

    @property
    def data_volumes(self):
        """Gets the data_volumes of this V3NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。  针对专属云节点，参数解释与rootVolume一致

        :return: The data_volumes of this V3NodeSpec.
        :rtype: list[V3DataVolume]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this V3NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。  针对专属云节点，参数解释与rootVolume一致

        :param data_volumes: The data_volumes of this V3NodeSpec.
        :type: list[V3DataVolume]
        """
        self._data_volumes = data_volumes

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this V3NodeSpec.

        指定DeH主机的ID，将节点调度到自己的DeH上。\\n>创建节点池添加节点时不支持该参数。 

        :return: The dedicated_host_id of this V3NodeSpec.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this V3NodeSpec.

        指定DeH主机的ID，将节点调度到自己的DeH上。\\n>创建节点池添加节点时不支持该参数。 

        :param dedicated_host_id: The dedicated_host_id of this V3NodeSpec.
        :type: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def ecs_group_id(self):
        """Gets the ecs_group_id of this V3NodeSpec.

        云服务器组ID，若指定，将节点创建在该云服务器组下

        :return: The ecs_group_id of this V3NodeSpec.
        :rtype: str
        """
        return self._ecs_group_id

    @ecs_group_id.setter
    def ecs_group_id(self, ecs_group_id):
        """Sets the ecs_group_id of this V3NodeSpec.

        云服务器组ID，若指定，将节点创建在该云服务器组下

        :param ecs_group_id: The ecs_group_id of this V3NodeSpec.
        :type: str
        """
        self._ecs_group_id = ecs_group_id

    @property
    def extend_param(self):
        """Gets the extend_param of this V3NodeSpec.

        创建节点时的扩展参数，可选参数如下： - chargingMode: 节点的计费模式。按需计费，取值为“0”，若不填，则默认为“0”。 - ecs:performancetype：云服务器规格的分类。裸金属节点无该字段。 - orderID: 订单ID，节点付费类型为自动付费包周期类型时必选。 - productID: 产品ID。 - maxPods: 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。   该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 - periodType:    订购周期类型，取值范围：     - month：月     - year：年   > billingMode为2（自动付费包周期）时生效，且为必选。 - periodNum:   订购周期数，取值范围：     - periodType=month（周期类型为月）时，取值为[1-9]。     - periodType=year（周期类型为年）时，取值为1。   > billingMode为2时生效，且为必选。 - isAutoRenew:   是否自动续订     - “true”：自动续订     - “false”：不自动续订   > billingMode为2时生效，且为必选。 - isAutoPay:   是否自动扣款     - “true”：自动扣款     - “false”：不自动扣款   > billingMode为2时生效，不填写此参数时默认会自动扣款。 - DockerLVMConfigOverride:   Docker数据盘配置项。默认配置示例如下：   ```   \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\"   ```   包含如下字段：     - userLV：用户空间的大小，示例格式：vgpaas/20%VG     - userPath：用户空间挂载路径，示例格式：/home/wqt-test     - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式     - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped     - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG     - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG - dockerBaseSize:   Device mapper 模式下，节点上 docker  单容器的可用磁盘空间大小 - init-node-password: 节点初始密码 - offloadNode: 是否为CCE Turbo集群节点 - publicKey: 节点的公钥。 - alpha.cce/preInstall:    安装前执行脚本   > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 - alpha.cce/postInstall:   安装后执行脚本   > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 - alpha.cce/NodeImageID: 如果创建裸金属节点，需要使用自定义镜像时用此参数。 - interruption_policy:   竞享实例中断策略，当前仅支持immediate。   - 仅marketType=spot时，该字段才可配置。   - 当interruption_policy=immediate时表示释放策略为立即释放。 - spot_duration_hours:   购买的竞享实例时长。   - 仅interruption_policy=immediate 时该字段才可配置。   - spot_duration_hours须大于0。   - spot_duration_hours的前端最大值从flavor的extra_specs的cond:spot_block:operation:longest_duration_hours字段中查询。 - spot_duration_count：   购买的“竞享实例时长”的个数。   - 仅spot_duration_hours>0时该字段才可配置。   - spot_duration_hours小于6时，spot_duration_count必须等于1。   - spot_duration_hours等于6时，spot_duration_count大于等于1。   - spot_duration_count的前端最大值从flavor的extra_specs的cond:spot_block:operation:longest_duration_count字段中查询。 

        :return: The extend_param of this V3NodeSpec.
        :rtype: dict(str, object)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this V3NodeSpec.

        创建节点时的扩展参数，可选参数如下： - chargingMode: 节点的计费模式。按需计费，取值为“0”，若不填，则默认为“0”。 - ecs:performancetype：云服务器规格的分类。裸金属节点无该字段。 - orderID: 订单ID，节点付费类型为自动付费包周期类型时必选。 - productID: 产品ID。 - maxPods: 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。   该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 - periodType:    订购周期类型，取值范围：     - month：月     - year：年   > billingMode为2（自动付费包周期）时生效，且为必选。 - periodNum:   订购周期数，取值范围：     - periodType=month（周期类型为月）时，取值为[1-9]。     - periodType=year（周期类型为年）时，取值为1。   > billingMode为2时生效，且为必选。 - isAutoRenew:   是否自动续订     - “true”：自动续订     - “false”：不自动续订   > billingMode为2时生效，且为必选。 - isAutoPay:   是否自动扣款     - “true”：自动扣款     - “false”：不自动扣款   > billingMode为2时生效，不填写此参数时默认会自动扣款。 - DockerLVMConfigOverride:   Docker数据盘配置项。默认配置示例如下：   ```   \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\"   ```   包含如下字段：     - userLV：用户空间的大小，示例格式：vgpaas/20%VG     - userPath：用户空间挂载路径，示例格式：/home/wqt-test     - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式     - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped     - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG     - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG - dockerBaseSize:   Device mapper 模式下，节点上 docker  单容器的可用磁盘空间大小 - init-node-password: 节点初始密码 - offloadNode: 是否为CCE Turbo集群节点 - publicKey: 节点的公钥。 - alpha.cce/preInstall:    安装前执行脚本   > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 - alpha.cce/postInstall:   安装后执行脚本   > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 - alpha.cce/NodeImageID: 如果创建裸金属节点，需要使用自定义镜像时用此参数。 - interruption_policy:   竞享实例中断策略，当前仅支持immediate。   - 仅marketType=spot时，该字段才可配置。   - 当interruption_policy=immediate时表示释放策略为立即释放。 - spot_duration_hours:   购买的竞享实例时长。   - 仅interruption_policy=immediate 时该字段才可配置。   - spot_duration_hours须大于0。   - spot_duration_hours的前端最大值从flavor的extra_specs的cond:spot_block:operation:longest_duration_hours字段中查询。 - spot_duration_count：   购买的“竞享实例时长”的个数。   - 仅spot_duration_hours>0时该字段才可配置。   - spot_duration_hours小于6时，spot_duration_count必须等于1。   - spot_duration_hours等于6时，spot_duration_count大于等于1。   - spot_duration_count的前端最大值从flavor的extra_specs的cond:spot_block:operation:longest_duration_count字段中查询。 

        :param extend_param: The extend_param of this V3NodeSpec.
        :type: dict(str, object)
        """
        self._extend_param = extend_param

    @property
    def flavor(self):
        """Gets the flavor of this V3NodeSpec.

        节点的规格

        :return: The flavor of this V3NodeSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this V3NodeSpec.

        节点的规格

        :param flavor: The flavor of this V3NodeSpec.
        :type: str
        """
        self._flavor = flavor

    @property
    def k8s_tags(self):
        """Gets the k8s_tags of this V3NodeSpec.

        格式为key/value键值对。键值对个数不超过20条。  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key， DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例：  ``` \"k8sTags\": {  \"key\": \"value\" } ```

        :return: The k8s_tags of this V3NodeSpec.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        """Sets the k8s_tags of this V3NodeSpec.

        格式为key/value键值对。键值对个数不超过20条。  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key， DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例：  ``` \"k8sTags\": {  \"key\": \"value\" } ```

        :param k8s_tags: The k8s_tags of this V3NodeSpec.
        :type: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def login(self):
        """Gets the login of this V3NodeSpec.


        :return: The login of this V3NodeSpec.
        :rtype: Login
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this V3NodeSpec.


        :param login: The login of this V3NodeSpec.
        :type: Login
        """
        self._login = login

    @property
    def node_nic_spec(self):
        """Gets the node_nic_spec of this V3NodeSpec.


        :return: The node_nic_spec of this V3NodeSpec.
        :rtype: NodeNicSpec
        """
        return self._node_nic_spec

    @node_nic_spec.setter
    def node_nic_spec(self, node_nic_spec):
        """Sets the node_nic_spec of this V3NodeSpec.


        :param node_nic_spec: The node_nic_spec of this V3NodeSpec.
        :type: NodeNicSpec
        """
        self._node_nic_spec = node_nic_spec

    @property
    def offload_node(self):
        """Gets the offload_node of this V3NodeSpec.

        是否CCE Turbo集群节点 >创建节点池添加节点时不支持该参数。

        :return: The offload_node of this V3NodeSpec.
        :rtype: bool
        """
        return self._offload_node

    @offload_node.setter
    def offload_node(self, offload_node):
        """Sets the offload_node of this V3NodeSpec.

        是否CCE Turbo集群节点 >创建节点池添加节点时不支持该参数。

        :param offload_node: The offload_node of this V3NodeSpec.
        :type: bool
        """
        self._offload_node = offload_node

    @property
    def os(self):
        """Gets the os of this V3NodeSpec.

        节点的操作系统类型。  - 对于虚拟机节点，可以配置为“EulerOS”、“CentOS”、“Debian”、“Ubuntu”。默认为\"EulerOS\"。  > 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。  - 对于自动付费包周期的裸金属节点，只支持EulerOS 2.3、EulerOS 2.5、EulerOS 2.8。

        :return: The os of this V3NodeSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this V3NodeSpec.

        节点的操作系统类型。  - 对于虚拟机节点，可以配置为“EulerOS”、“CentOS”、“Debian”、“Ubuntu”。默认为\"EulerOS\"。  > 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。  - 对于自动付费包周期的裸金属节点，只支持EulerOS 2.3、EulerOS 2.5、EulerOS 2.8。

        :param os: The os of this V3NodeSpec.
        :type: str
        """
        self._os = os

    @property
    def public_ip(self):
        """Gets the public_ip of this V3NodeSpec.


        :return: The public_ip of this V3NodeSpec.
        :rtype: V3NodePublicIP
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this V3NodeSpec.


        :param public_ip: The public_ip of this V3NodeSpec.
        :type: V3NodePublicIP
        """
        self._public_ip = public_ip

    @property
    def root_volume(self):
        """Gets the root_volume of this V3NodeSpec.


        :return: The root_volume of this V3NodeSpec.
        :rtype: V3RootVolume
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this V3NodeSpec.


        :param root_volume: The root_volume of this V3NodeSpec.
        :type: V3RootVolume
        """
        self._root_volume = root_volume

    @property
    def taints(self):
        """Gets the taints of this V3NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{ \"key\": \"status\", \"value\": \"unavailable\", \"effect\": \"NoSchedule\" }, { \"key\": \"looks\", \"value\": \"bad\", \"effect\": \"NoSchedule\" }] ```

        :return: The taints of this V3NodeSpec.
        :rtype: list[Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this V3NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{ \"key\": \"status\", \"value\": \"unavailable\", \"effect\": \"NoSchedule\" }, { \"key\": \"looks\", \"value\": \"bad\", \"effect\": \"NoSchedule\" }] ```

        :param taints: The taints of this V3NodeSpec.
        :type: list[Taint]
        """
        self._taints = taints

    @property
    def user_tags(self):
        """Gets the user_tags of this V3NodeSpec.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限最少为5个。

        :return: The user_tags of this V3NodeSpec.
        :rtype: list[UserTag]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        """Sets the user_tags of this V3NodeSpec.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限最少为5个。

        :param user_tags: The user_tags of this V3NodeSpec.
        :type: list[UserTag]
        """
        self._user_tags = user_tags

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3NodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
