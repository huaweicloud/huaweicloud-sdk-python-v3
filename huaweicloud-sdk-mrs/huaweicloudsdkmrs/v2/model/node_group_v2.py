# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeGroupV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'node_num': 'int',
        'node_size': 'str',
        'root_volume': 'Volume',
        'data_volume': 'Volume',
        'data_volume_count': 'int',
        'charge_info': 'ChargeInfo',
        'auto_scaling_policy': 'AutoScalingPolicy',
        'assigned_roles': 'list[str]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'node_num': 'node_num',
        'node_size': 'node_size',
        'root_volume': 'root_volume',
        'data_volume': 'data_volume',
        'data_volume_count': 'data_volume_count',
        'charge_info': 'charge_info',
        'auto_scaling_policy': 'auto_scaling_policy',
        'assigned_roles': 'assigned_roles'
    }

    def __init__(self, group_name=None, node_num=None, node_size=None, root_volume=None, data_volume=None, data_volume_count=None, charge_info=None, auto_scaling_policy=None, assigned_roles=None):
        r"""NodeGroupV2

        The model defined in huaweicloud sdk

        :param group_name: 节点组名称，最大长度64，支持大小写英文、数字以及“_”。节点组配置原则如下： - master_node_default_group：Master节点组，所有集群类型均需包含该节点组。 - core_node_analysis_group：分析Core节点组，分析集群、混合集群均需包含该节点组。 - core_node_streaming_group：流式Core节点组，流式集群和混合集群均需包含该节点组。 - task_node_analysis_group：分析Task节点组，分析集群和混合集群可根据需要选择该节点组。 - task_node_streaming_group：流式Task节点组，流式集群、混合集群可根据需要选择该节点组。 - node_group{x}：自定义集群节点组，可根据需要添加多个，最多支持添加9个该节点组。
        :type group_name: str
        :param node_num: 节点数量，取值范围0～500，Core与Task节点总数最大为500个。
        :type node_num: int
        :param node_size: 节点的实例规格。 例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。
        :type node_size: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmrs.v2.Volume`
        :param data_volume: 
        :type data_volume: :class:`huaweicloudsdkmrs.v2.Volume`
        :param data_volume_count: 节点数据磁盘存储数目，取值范围：0～20。
        :type data_volume_count: int
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        :param auto_scaling_policy: 
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v2.AutoScalingPolicy`
        :param assigned_roles: 当集群类型为CUSTOM时，该参数必选。可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]” 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。
        :type assigned_roles: list[str]
        """
        
        

        self._group_name = None
        self._node_num = None
        self._node_size = None
        self._root_volume = None
        self._data_volume = None
        self._data_volume_count = None
        self._charge_info = None
        self._auto_scaling_policy = None
        self._assigned_roles = None
        self.discriminator = None

        self.group_name = group_name
        self.node_num = node_num
        self.node_size = node_size
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volume is not None:
            self.data_volume = data_volume
        if data_volume_count is not None:
            self.data_volume_count = data_volume_count
        if charge_info is not None:
            self.charge_info = charge_info
        if auto_scaling_policy is not None:
            self.auto_scaling_policy = auto_scaling_policy
        if assigned_roles is not None:
            self.assigned_roles = assigned_roles

    @property
    def group_name(self):
        r"""Gets the group_name of this NodeGroupV2.

        节点组名称，最大长度64，支持大小写英文、数字以及“_”。节点组配置原则如下： - master_node_default_group：Master节点组，所有集群类型均需包含该节点组。 - core_node_analysis_group：分析Core节点组，分析集群、混合集群均需包含该节点组。 - core_node_streaming_group：流式Core节点组，流式集群和混合集群均需包含该节点组。 - task_node_analysis_group：分析Task节点组，分析集群和混合集群可根据需要选择该节点组。 - task_node_streaming_group：流式Task节点组，流式集群、混合集群可根据需要选择该节点组。 - node_group{x}：自定义集群节点组，可根据需要添加多个，最多支持添加9个该节点组。

        :return: The group_name of this NodeGroupV2.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this NodeGroupV2.

        节点组名称，最大长度64，支持大小写英文、数字以及“_”。节点组配置原则如下： - master_node_default_group：Master节点组，所有集群类型均需包含该节点组。 - core_node_analysis_group：分析Core节点组，分析集群、混合集群均需包含该节点组。 - core_node_streaming_group：流式Core节点组，流式集群和混合集群均需包含该节点组。 - task_node_analysis_group：分析Task节点组，分析集群和混合集群可根据需要选择该节点组。 - task_node_streaming_group：流式Task节点组，流式集群、混合集群可根据需要选择该节点组。 - node_group{x}：自定义集群节点组，可根据需要添加多个，最多支持添加9个该节点组。

        :param group_name: The group_name of this NodeGroupV2.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def node_num(self):
        r"""Gets the node_num of this NodeGroupV2.

        节点数量，取值范围0～500，Core与Task节点总数最大为500个。

        :return: The node_num of this NodeGroupV2.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this NodeGroupV2.

        节点数量，取值范围0～500，Core与Task节点总数最大为500个。

        :param node_num: The node_num of this NodeGroupV2.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_size(self):
        r"""Gets the node_size of this NodeGroupV2.

        节点的实例规格。 例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :return: The node_size of this NodeGroupV2.
        :rtype: str
        """
        return self._node_size

    @node_size.setter
    def node_size(self, node_size):
        r"""Sets the node_size of this NodeGroupV2.

        节点的实例规格。 例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :param node_size: The node_size of this NodeGroupV2.
        :type node_size: str
        """
        self._node_size = node_size

    @property
    def root_volume(self):
        r"""Gets the root_volume of this NodeGroupV2.

        :return: The root_volume of this NodeGroupV2.
        :rtype: :class:`huaweicloudsdkmrs.v2.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this NodeGroupV2.

        :param root_volume: The root_volume of this NodeGroupV2.
        :type root_volume: :class:`huaweicloudsdkmrs.v2.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volume(self):
        r"""Gets the data_volume of this NodeGroupV2.

        :return: The data_volume of this NodeGroupV2.
        :rtype: :class:`huaweicloudsdkmrs.v2.Volume`
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        r"""Sets the data_volume of this NodeGroupV2.

        :param data_volume: The data_volume of this NodeGroupV2.
        :type data_volume: :class:`huaweicloudsdkmrs.v2.Volume`
        """
        self._data_volume = data_volume

    @property
    def data_volume_count(self):
        r"""Gets the data_volume_count of this NodeGroupV2.

        节点数据磁盘存储数目，取值范围：0～20。

        :return: The data_volume_count of this NodeGroupV2.
        :rtype: int
        """
        return self._data_volume_count

    @data_volume_count.setter
    def data_volume_count(self, data_volume_count):
        r"""Sets the data_volume_count of this NodeGroupV2.

        节点数据磁盘存储数目，取值范围：0～20。

        :param data_volume_count: The data_volume_count of this NodeGroupV2.
        :type data_volume_count: int
        """
        self._data_volume_count = data_volume_count

    @property
    def charge_info(self):
        r"""Gets the charge_info of this NodeGroupV2.

        :return: The charge_info of this NodeGroupV2.
        :rtype: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this NodeGroupV2.

        :param charge_info: The charge_info of this NodeGroupV2.
        :type charge_info: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def auto_scaling_policy(self):
        r"""Gets the auto_scaling_policy of this NodeGroupV2.

        :return: The auto_scaling_policy of this NodeGroupV2.
        :rtype: :class:`huaweicloudsdkmrs.v2.AutoScalingPolicy`
        """
        return self._auto_scaling_policy

    @auto_scaling_policy.setter
    def auto_scaling_policy(self, auto_scaling_policy):
        r"""Sets the auto_scaling_policy of this NodeGroupV2.

        :param auto_scaling_policy: The auto_scaling_policy of this NodeGroupV2.
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v2.AutoScalingPolicy`
        """
        self._auto_scaling_policy = auto_scaling_policy

    @property
    def assigned_roles(self):
        r"""Gets the assigned_roles of this NodeGroupV2.

        当集群类型为CUSTOM时，该参数必选。可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]” 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。

        :return: The assigned_roles of this NodeGroupV2.
        :rtype: list[str]
        """
        return self._assigned_roles

    @assigned_roles.setter
    def assigned_roles(self, assigned_roles):
        r"""Sets the assigned_roles of this NodeGroupV2.

        当集群类型为CUSTOM时，该参数必选。可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]” 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。

        :param assigned_roles: The assigned_roles of this NodeGroupV2.
        :type assigned_roles: list[str]
        """
        self._assigned_roles = assigned_roles

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
        if not isinstance(other, NodeGroupV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
