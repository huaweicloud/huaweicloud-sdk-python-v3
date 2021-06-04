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
        'flavor': 'str',
        'az': 'str',
        'os': 'str',
        'login': 'Login',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'public_ip': 'V3NodePublicIP',
        'node_nic_spec': 'NodeNicSpec',
        'count': 'int',
        'billing_mode': 'int',
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'ecs_group_id': 'str',
        'fault_domain': 'str',
        'dedicated_host_id': 'str',
        'offload_node': 'bool',
        'user_tags': 'list[UserTag]',
        'runtime': 'Runtime',
        'extend_param': 'NodeExtendParam'
    }

    attribute_map = {
        'flavor': 'flavor',
        'az': 'az',
        'os': 'os',
        'login': 'login',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'public_ip': 'publicIP',
        'node_nic_spec': 'nodeNicSpec',
        'count': 'count',
        'billing_mode': 'billingMode',
        'taints': 'taints',
        'k8s_tags': 'k8sTags',
        'ecs_group_id': 'ecsGroupId',
        'fault_domain': 'faultDomain',
        'dedicated_host_id': 'dedicatedHostId',
        'offload_node': 'offloadNode',
        'user_tags': 'userTags',
        'runtime': 'runtime',
        'extend_param': 'extendParam'
    }

    def __init__(self, flavor=None, az=None, os=None, login=None, root_volume=None, data_volumes=None, public_ip=None, node_nic_spec=None, count=None, billing_mode=None, taints=None, k8s_tags=None, ecs_group_id=None, fault_domain=None, dedicated_host_id=None, offload_node=None, user_tags=None, runtime=None, extend_param=None):
        """V3NodeSpec - a model defined in huaweicloud sdk"""
        
        

        self._flavor = None
        self._az = None
        self._os = None
        self._login = None
        self._root_volume = None
        self._data_volumes = None
        self._public_ip = None
        self._node_nic_spec = None
        self._count = None
        self._billing_mode = None
        self._taints = None
        self._k8s_tags = None
        self._ecs_group_id = None
        self._fault_domain = None
        self._dedicated_host_id = None
        self._offload_node = None
        self._user_tags = None
        self._runtime = None
        self._extend_param = None
        self.discriminator = None

        self.flavor = flavor
        self.az = az
        if os is not None:
            self.os = os
        self.login = login
        self.root_volume = root_volume
        self.data_volumes = data_volumes
        if public_ip is not None:
            self.public_ip = public_ip
        if node_nic_spec is not None:
            self.node_nic_spec = node_nic_spec
        self.count = count
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if taints is not None:
            self.taints = taints
        if k8s_tags is not None:
            self.k8s_tags = k8s_tags
        if ecs_group_id is not None:
            self.ecs_group_id = ecs_group_id
        if fault_domain is not None:
            self.fault_domain = fault_domain
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if offload_node is not None:
            self.offload_node = offload_node
        if user_tags is not None:
            self.user_tags = user_tags
        if runtime is not None:
            self.runtime = runtime
        if extend_param is not None:
            self.extend_param = extend_param

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
    def os(self):
        """Gets the os of this V3NodeSpec.

        节点的操作系统类型。  - 对于虚拟机节点，可以配置为“EulerOS”、“CentOS”、“Debian”、“Ubuntu”。默认为\"EulerOS\"。  > 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。  - 对于自动付费包周期的裸金属节点，只支持EulerOS 2.3、EulerOS 2.5、EulerOS 2.8。  - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。

        :return: The os of this V3NodeSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this V3NodeSpec.

        节点的操作系统类型。  - 对于虚拟机节点，可以配置为“EulerOS”、“CentOS”、“Debian”、“Ubuntu”。默认为\"EulerOS\"。  > 系统会根据集群版本自动选择支持的系统版本。当前集群版本不支持该系统类型，则会报错。  - 对于自动付费包周期的裸金属节点，只支持EulerOS 2.3、EulerOS 2.5、EulerOS 2.8。  - 若在创建节点时指定了extendParam中的alpha.cce/NodeImageID参数，可以不填写此参数。

        :param os: The os of this V3NodeSpec.
        :type: str
        """
        self._os = os

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
    def root_volume(self):
        """Gets the root_volume of this V3NodeSpec.


        :return: The root_volume of this V3NodeSpec.
        :rtype: Volume
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this V3NodeSpec.


        :param root_volume: The root_volume of this V3NodeSpec.
        :type: Volume
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this V3NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。  针对专属云节点，参数解释与rootVolume一致

        :return: The data_volumes of this V3NodeSpec.
        :rtype: list[Volume]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this V3NodeSpec.

        节点的数据盘参数（目前已支持通过控制台为CCE节点添加第二块数据盘）。  针对专属云节点，参数解释与rootVolume一致

        :param data_volumes: The data_volumes of this V3NodeSpec.
        :type: list[Volume]
        """
        self._data_volumes = data_volumes

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
    def taints(self):
        """Gets the taints of this V3NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{  \"key\": \"status\",  \"value\": \"unavailable\",  \"effect\": \"NoSchedule\" }, {  \"key\": \"looks\",  \"value\": \"bad\",  \"effect\": \"NoSchedule\" }] ```

        :return: The taints of this V3NodeSpec.
        :rtype: list[Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this V3NodeSpec.

        支持给创建出来的节点加Taints来设置反亲和性，每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{  \"key\": \"status\",  \"value\": \"unavailable\",  \"effect\": \"NoSchedule\" }, {  \"key\": \"looks\",  \"value\": \"bad\",  \"effect\": \"NoSchedule\" }] ```

        :param taints: The taints of this V3NodeSpec.
        :type: list[Taint]
        """
        self._taints = taints

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
    def fault_domain(self):
        """Gets the fault_domain of this V3NodeSpec.

        云服务器故障域，将节点创建在指定故障域下。\\n >必须同时指定故障域策略的云服务器ID，且需要开启故障域特性开关 

        :return: The fault_domain of this V3NodeSpec.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """Sets the fault_domain of this V3NodeSpec.

        云服务器故障域，将节点创建在指定故障域下。\\n >必须同时指定故障域策略的云服务器ID，且需要开启故障域特性开关 

        :param fault_domain: The fault_domain of this V3NodeSpec.
        :type: str
        """
        self._fault_domain = fault_domain

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

    @property
    def runtime(self):
        """Gets the runtime of this V3NodeSpec.


        :return: The runtime of this V3NodeSpec.
        :rtype: Runtime
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this V3NodeSpec.


        :param runtime: The runtime of this V3NodeSpec.
        :type: Runtime
        """
        self._runtime = runtime

    @property
    def extend_param(self):
        """Gets the extend_param of this V3NodeSpec.


        :return: The extend_param of this V3NodeSpec.
        :rtype: NodeExtendParam
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this V3NodeSpec.


        :param extend_param: The extend_param of this V3NodeSpec.
        :type: NodeExtendParam
        """
        self._extend_param = extend_param

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
