# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterScalingParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'scale_type': 'str',
        'node_id': 'str',
        'node_group': 'str',
        'skip_bootstrap_scripts': 'str',
        'scale_without_start': 'bool',
        'server_ids': 'list[str]',
        'instances': 'int',
        'task_node_info': 'TaskNodeInfo'
    }

    attribute_map = {
        'order_id': 'order_id',
        'scale_type': 'scale_type',
        'node_id': 'node_id',
        'node_group': 'node_group',
        'skip_bootstrap_scripts': 'skip_bootstrap_scripts',
        'scale_without_start': 'scale_without_start',
        'server_ids': 'server_ids',
        'instances': 'instances',
        'task_node_info': 'task_node_info'
    }

    def __init__(self, order_id=None, scale_type=None, node_id=None, node_group=None, skip_bootstrap_scripts=None, scale_without_start=None, server_ids=None, instances=None, task_node_info=None):
        """ClusterScalingParams

        The model defined in huaweicloud sdk

        :param order_id: 扩容/缩容时系统获取的订单号，用户不需要配置。
        :type order_id: str
        :param scale_type: - scale_in：缩容 - scale_out：扩容
        :type scale_type: str
        :param node_id: 扩容/缩容时新增或者减少节点的ID标识,参数值固定为node_orderadd。
        :type node_id: str
        :param node_group: 扩容或缩容的节点组。 - 如果node_group为core_node_default_group，表示Core节点组。 - 如果node_group为task_node_default_group，表示Task节点组。  该字段可以为空，为空时，系统默认值为core_node_default_group。
        :type node_group: str
        :param skip_bootstrap_scripts: 是否跳过引导操作，默认为false，即执行引导操作。 仅在创建集群时配置了引导操作且扩容时有意义，表示扩容时是否在新增节点上执行创建集群时指定的引导操作。
        :type skip_bootstrap_scripts: str
        :param scale_without_start: 扩容后是否启动扩容节点上的组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。
        :type scale_without_start: bool
        :param server_ids: 缩容Task节点时指定待删除Task节点的ID列表。  - 当scale_type为扩容时，该参数不生效。 - 当scale_type为缩容且该参数不为空时，删除指定的Task节点。 - 当scale_type为缩容且server_ids为空时，按照系统规则自动选择删除Task节点。
        :type server_ids: list[str]
        :param instances: 扩容或缩容的节点数。  - 扩容时的最大节点数为（500 - 集群Core/Task节点数）。例如，当前集群Core节点数为3，此处扩容的节点数必须小于等于497。     Core和Task节点总数最大值为500，如果用户需要的Core/Task节点数大于500，可以联系技术支持人员或者调用后台接口修改数据库。   - 缩容时Core节点数大于3或者Task节点数大于0可以进行节点删除。例如，当前集群Core节点和Task节点数均为5，Core节点可缩容的节点数为2（5减去3），Task节点可缩容节点数为小于等于5。
        :type instances: int
        :param task_node_info: 
        :type task_node_info: :class:`huaweicloudsdkmrs.v1.TaskNodeInfo`
        """
        
        

        self._order_id = None
        self._scale_type = None
        self._node_id = None
        self._node_group = None
        self._skip_bootstrap_scripts = None
        self._scale_without_start = None
        self._server_ids = None
        self._instances = None
        self._task_node_info = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        self.scale_type = scale_type
        self.node_id = node_id
        if node_group is not None:
            self.node_group = node_group
        if skip_bootstrap_scripts is not None:
            self.skip_bootstrap_scripts = skip_bootstrap_scripts
        if scale_without_start is not None:
            self.scale_without_start = scale_without_start
        if server_ids is not None:
            self.server_ids = server_ids
        self.instances = instances
        if task_node_info is not None:
            self.task_node_info = task_node_info

    @property
    def order_id(self):
        """Gets the order_id of this ClusterScalingParams.

        扩容/缩容时系统获取的订单号，用户不需要配置。

        :return: The order_id of this ClusterScalingParams.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ClusterScalingParams.

        扩容/缩容时系统获取的订单号，用户不需要配置。

        :param order_id: The order_id of this ClusterScalingParams.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def scale_type(self):
        """Gets the scale_type of this ClusterScalingParams.

        - scale_in：缩容 - scale_out：扩容

        :return: The scale_type of this ClusterScalingParams.
        :rtype: str
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type):
        """Sets the scale_type of this ClusterScalingParams.

        - scale_in：缩容 - scale_out：扩容

        :param scale_type: The scale_type of this ClusterScalingParams.
        :type scale_type: str
        """
        self._scale_type = scale_type

    @property
    def node_id(self):
        """Gets the node_id of this ClusterScalingParams.

        扩容/缩容时新增或者减少节点的ID标识,参数值固定为node_orderadd。

        :return: The node_id of this ClusterScalingParams.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ClusterScalingParams.

        扩容/缩容时新增或者减少节点的ID标识,参数值固定为node_orderadd。

        :param node_id: The node_id of this ClusterScalingParams.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_group(self):
        """Gets the node_group of this ClusterScalingParams.

        扩容或缩容的节点组。 - 如果node_group为core_node_default_group，表示Core节点组。 - 如果node_group为task_node_default_group，表示Task节点组。  该字段可以为空，为空时，系统默认值为core_node_default_group。

        :return: The node_group of this ClusterScalingParams.
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this ClusterScalingParams.

        扩容或缩容的节点组。 - 如果node_group为core_node_default_group，表示Core节点组。 - 如果node_group为task_node_default_group，表示Task节点组。  该字段可以为空，为空时，系统默认值为core_node_default_group。

        :param node_group: The node_group of this ClusterScalingParams.
        :type node_group: str
        """
        self._node_group = node_group

    @property
    def skip_bootstrap_scripts(self):
        """Gets the skip_bootstrap_scripts of this ClusterScalingParams.

        是否跳过引导操作，默认为false，即执行引导操作。 仅在创建集群时配置了引导操作且扩容时有意义，表示扩容时是否在新增节点上执行创建集群时指定的引导操作。

        :return: The skip_bootstrap_scripts of this ClusterScalingParams.
        :rtype: str
        """
        return self._skip_bootstrap_scripts

    @skip_bootstrap_scripts.setter
    def skip_bootstrap_scripts(self, skip_bootstrap_scripts):
        """Sets the skip_bootstrap_scripts of this ClusterScalingParams.

        是否跳过引导操作，默认为false，即执行引导操作。 仅在创建集群时配置了引导操作且扩容时有意义，表示扩容时是否在新增节点上执行创建集群时指定的引导操作。

        :param skip_bootstrap_scripts: The skip_bootstrap_scripts of this ClusterScalingParams.
        :type skip_bootstrap_scripts: str
        """
        self._skip_bootstrap_scripts = skip_bootstrap_scripts

    @property
    def scale_without_start(self):
        """Gets the scale_without_start of this ClusterScalingParams.

        扩容后是否启动扩容节点上的组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。

        :return: The scale_without_start of this ClusterScalingParams.
        :rtype: bool
        """
        return self._scale_without_start

    @scale_without_start.setter
    def scale_without_start(self, scale_without_start):
        """Sets the scale_without_start of this ClusterScalingParams.

        扩容后是否启动扩容节点上的组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。

        :param scale_without_start: The scale_without_start of this ClusterScalingParams.
        :type scale_without_start: bool
        """
        self._scale_without_start = scale_without_start

    @property
    def server_ids(self):
        """Gets the server_ids of this ClusterScalingParams.

        缩容Task节点时指定待删除Task节点的ID列表。  - 当scale_type为扩容时，该参数不生效。 - 当scale_type为缩容且该参数不为空时，删除指定的Task节点。 - 当scale_type为缩容且server_ids为空时，按照系统规则自动选择删除Task节点。

        :return: The server_ids of this ClusterScalingParams.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this ClusterScalingParams.

        缩容Task节点时指定待删除Task节点的ID列表。  - 当scale_type为扩容时，该参数不生效。 - 当scale_type为缩容且该参数不为空时，删除指定的Task节点。 - 当scale_type为缩容且server_ids为空时，按照系统规则自动选择删除Task节点。

        :param server_ids: The server_ids of this ClusterScalingParams.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def instances(self):
        """Gets the instances of this ClusterScalingParams.

        扩容或缩容的节点数。  - 扩容时的最大节点数为（500 - 集群Core/Task节点数）。例如，当前集群Core节点数为3，此处扩容的节点数必须小于等于497。     Core和Task节点总数最大值为500，如果用户需要的Core/Task节点数大于500，可以联系技术支持人员或者调用后台接口修改数据库。   - 缩容时Core节点数大于3或者Task节点数大于0可以进行节点删除。例如，当前集群Core节点和Task节点数均为5，Core节点可缩容的节点数为2（5减去3），Task节点可缩容节点数为小于等于5。

        :return: The instances of this ClusterScalingParams.
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ClusterScalingParams.

        扩容或缩容的节点数。  - 扩容时的最大节点数为（500 - 集群Core/Task节点数）。例如，当前集群Core节点数为3，此处扩容的节点数必须小于等于497。     Core和Task节点总数最大值为500，如果用户需要的Core/Task节点数大于500，可以联系技术支持人员或者调用后台接口修改数据库。   - 缩容时Core节点数大于3或者Task节点数大于0可以进行节点删除。例如，当前集群Core节点和Task节点数均为5，Core节点可缩容的节点数为2（5减去3），Task节点可缩容节点数为小于等于5。

        :param instances: The instances of this ClusterScalingParams.
        :type instances: int
        """
        self._instances = instances

    @property
    def task_node_info(self):
        """Gets the task_node_info of this ClusterScalingParams.

        :return: The task_node_info of this ClusterScalingParams.
        :rtype: :class:`huaweicloudsdkmrs.v1.TaskNodeInfo`
        """
        return self._task_node_info

    @task_node_info.setter
    def task_node_info(self, task_node_info):
        """Sets the task_node_info of this ClusterScalingParams.

        :param task_node_info: The task_node_info of this ClusterScalingParams.
        :type task_node_info: :class:`huaweicloudsdkmrs.v1.TaskNodeInfo`
        """
        self._task_node_info = task_node_info

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
        if not isinstance(other, ClusterScalingParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
