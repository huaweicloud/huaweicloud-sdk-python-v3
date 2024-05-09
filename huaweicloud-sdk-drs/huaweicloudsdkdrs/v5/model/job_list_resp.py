# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobListResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'description': 'str',
        'create_time': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'charging_mode': 'str',
        'billing_tag': 'bool',
        'job_direction': 'str',
        'job_type': 'str',
        'task_type': 'str',
        'enterprise_project_id': 'str',
        'job_mode': 'str',
        'job_mode_role': 'str',
        'is_multi_az': 'bool',
        'node_role': 'str',
        'node_new_framework': 'bool',
        'job_action': 'JobActions',
        'children': 'list[ChildrenJobListResp]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'charging_mode': 'charging_mode',
        'billing_tag': 'billing_tag',
        'job_direction': 'job_direction',
        'job_type': 'job_type',
        'task_type': 'task_type',
        'enterprise_project_id': 'enterprise_project_id',
        'job_mode': 'job_mode',
        'job_mode_role': 'job_mode_role',
        'is_multi_az': 'is_multi_az',
        'node_role': 'node_role',
        'node_new_framework': 'node_new_framework',
        'job_action': 'job_action',
        'children': 'children'
    }

    def __init__(self, id=None, name=None, status=None, description=None, create_time=None, engine_type=None, net_type=None, charging_mode=None, billing_tag=None, job_direction=None, job_type=None, task_type=None, enterprise_project_id=None, job_mode=None, job_mode_role=None, is_multi_az=None, node_role=None, node_new_framework=None, job_action=None, children=None):
        """JobListResp

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。
        :type status: str
        :param description: 任务描述。
        :type description: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param engine_type: 引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。 - redis-to-gaussredis：redis同步到GeminiDB Redis，实时迁移场景使用。 - rediscluster-to-gaussredis：redis集群同步到GeminiDB Redis，实时迁移场景使用。
        :type engine_type: str
        :param net_type: 网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。
        :type net_type: str
        :param charging_mode: 计费模式。取值： - period：包周期。 - on_demand：按需。
        :type charging_mode: str
        :param billing_tag: 是否计费。
        :type billing_tag: bool
        :param job_direction: 任务方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。
        :type job_direction: str
        :param job_type: 任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。
        :type job_type: str
        :param task_type: 任务模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。
        :type task_type: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param job_mode: 任务模式。取值： - single：单任务。 - sync_child：同步子任务。 - multi_to_single：多对一任务。
        :type job_mode: str
        :param job_mode_role: 任务角色。取值： - parent：父任务。 - child：子任务。 - master：主任务。 - slave：备任务。
        :type job_mode_role: str
        :param is_multi_az: 是否跨AZ任务。
        :type is_multi_az: bool
        :param node_role: 任务节点角色。
        :type node_role: str
        :param node_new_framework: 是否新框架。
        :type node_new_framework: bool
        :param job_action: 
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        :param children: 子任务列表信息体。
        :type children: list[:class:`huaweicloudsdkdrs.v5.ChildrenJobListResp`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._description = None
        self._create_time = None
        self._engine_type = None
        self._net_type = None
        self._charging_mode = None
        self._billing_tag = None
        self._job_direction = None
        self._job_type = None
        self._task_type = None
        self._enterprise_project_id = None
        self._job_mode = None
        self._job_mode_role = None
        self._is_multi_az = None
        self._node_role = None
        self._node_new_framework = None
        self._job_action = None
        self._children = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.create_time = create_time
        self.engine_type = engine_type
        self.net_type = net_type
        self.charging_mode = charging_mode
        self.billing_tag = billing_tag
        self.job_direction = job_direction
        self.job_type = job_type
        self.task_type = task_type
        self.enterprise_project_id = enterprise_project_id
        self.job_mode = job_mode
        self.job_mode_role = job_mode_role
        self.is_multi_az = is_multi_az
        self.node_role = node_role
        self.node_new_framework = node_new_framework
        self.job_action = job_action
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this JobListResp.

        任务ID。

        :return: The id of this JobListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobListResp.

        任务ID。

        :param id: The id of this JobListResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobListResp.

        任务名称。

        :return: The name of this JobListResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobListResp.

        任务名称。

        :param name: The name of this JobListResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this JobListResp.

        任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。

        :return: The status of this JobListResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobListResp.

        任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。

        :param status: The status of this JobListResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this JobListResp.

        任务描述。

        :return: The description of this JobListResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobListResp.

        任务描述。

        :param description: The description of this JobListResp.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this JobListResp.

        任务创建时间。

        :return: The create_time of this JobListResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobListResp.

        任务创建时间。

        :param create_time: The create_time of this JobListResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def engine_type(self):
        """Gets the engine_type of this JobListResp.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。 - redis-to-gaussredis：redis同步到GeminiDB Redis，实时迁移场景使用。 - rediscluster-to-gaussredis：redis集群同步到GeminiDB Redis，实时迁移场景使用。

        :return: The engine_type of this JobListResp.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this JobListResp.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。 - redis-to-gaussredis：redis同步到GeminiDB Redis，实时迁移场景使用。 - rediscluster-to-gaussredis：redis集群同步到GeminiDB Redis，实时迁移场景使用。

        :param engine_type: The engine_type of this JobListResp.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        """Gets the net_type of this JobListResp.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。

        :return: The net_type of this JobListResp.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this JobListResp.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络，灾备场景不支持选择VPC网络。 - vpn：VPN、专线网络。

        :param net_type: The net_type of this JobListResp.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this JobListResp.

        计费模式。取值： - period：包周期。 - on_demand：按需。

        :return: The charging_mode of this JobListResp.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this JobListResp.

        计费模式。取值： - period：包周期。 - on_demand：按需。

        :param charging_mode: The charging_mode of this JobListResp.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def billing_tag(self):
        """Gets the billing_tag of this JobListResp.

        是否计费。

        :return: The billing_tag of this JobListResp.
        :rtype: bool
        """
        return self._billing_tag

    @billing_tag.setter
    def billing_tag(self, billing_tag):
        """Sets the billing_tag of this JobListResp.

        是否计费。

        :param billing_tag: The billing_tag of this JobListResp.
        :type billing_tag: bool
        """
        self._billing_tag = billing_tag

    @property
    def job_direction(self):
        """Gets the job_direction of this JobListResp.

        任务方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :return: The job_direction of this JobListResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this JobListResp.

        任务方向。取值： - up：入云 ，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :param job_direction: The job_direction of this JobListResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def job_type(self):
        """Gets the job_type of this JobListResp.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :return: The job_type of this JobListResp.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobListResp.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :param job_type: The job_type of this JobListResp.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def task_type(self):
        """Gets the task_type of this JobListResp.

        任务模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。

        :return: The task_type of this JobListResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this JobListResp.

        任务模式。取值： - FULL_TRANS ：全量。 - FULL_INCR_TRANS：全量+增量。 - INCR_TRANS：增量。

        :param task_type: The task_type of this JobListResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this JobListResp.

        企业项目ID。

        :return: The enterprise_project_id of this JobListResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this JobListResp.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this JobListResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def job_mode(self):
        """Gets the job_mode of this JobListResp.

        任务模式。取值： - single：单任务。 - sync_child：同步子任务。 - multi_to_single：多对一任务。

        :return: The job_mode of this JobListResp.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        """Sets the job_mode of this JobListResp.

        任务模式。取值： - single：单任务。 - sync_child：同步子任务。 - multi_to_single：多对一任务。

        :param job_mode: The job_mode of this JobListResp.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_mode_role(self):
        """Gets the job_mode_role of this JobListResp.

        任务角色。取值： - parent：父任务。 - child：子任务。 - master：主任务。 - slave：备任务。

        :return: The job_mode_role of this JobListResp.
        :rtype: str
        """
        return self._job_mode_role

    @job_mode_role.setter
    def job_mode_role(self, job_mode_role):
        """Sets the job_mode_role of this JobListResp.

        任务角色。取值： - parent：父任务。 - child：子任务。 - master：主任务。 - slave：备任务。

        :param job_mode_role: The job_mode_role of this JobListResp.
        :type job_mode_role: str
        """
        self._job_mode_role = job_mode_role

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this JobListResp.

        是否跨AZ任务。

        :return: The is_multi_az of this JobListResp.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this JobListResp.

        是否跨AZ任务。

        :param is_multi_az: The is_multi_az of this JobListResp.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def node_role(self):
        """Gets the node_role of this JobListResp.

        任务节点角色。

        :return: The node_role of this JobListResp.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        """Sets the node_role of this JobListResp.

        任务节点角色。

        :param node_role: The node_role of this JobListResp.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def node_new_framework(self):
        """Gets the node_new_framework of this JobListResp.

        是否新框架。

        :return: The node_new_framework of this JobListResp.
        :rtype: bool
        """
        return self._node_new_framework

    @node_new_framework.setter
    def node_new_framework(self, node_new_framework):
        """Sets the node_new_framework of this JobListResp.

        是否新框架。

        :param node_new_framework: The node_new_framework of this JobListResp.
        :type node_new_framework: bool
        """
        self._node_new_framework = node_new_framework

    @property
    def job_action(self):
        """Gets the job_action of this JobListResp.

        :return: The job_action of this JobListResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        return self._job_action

    @job_action.setter
    def job_action(self, job_action):
        """Sets the job_action of this JobListResp.

        :param job_action: The job_action of this JobListResp.
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        self._job_action = job_action

    @property
    def children(self):
        """Gets the children of this JobListResp.

        子任务列表信息体。

        :return: The children of this JobListResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ChildrenJobListResp`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this JobListResp.

        子任务列表信息体。

        :param children: The children of this JobListResp.
        :type children: list[:class:`huaweicloudsdkdrs.v5.ChildrenJobListResp`]
        """
        self._children = children

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
        if not isinstance(other, JobListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
