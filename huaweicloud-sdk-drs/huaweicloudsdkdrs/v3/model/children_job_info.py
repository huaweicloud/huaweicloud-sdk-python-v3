# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChildrenJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing_tag': 'bool',
        'create_time': 'str',
        'db_use_type': 'str',
        'description': 'str',
        'engine_type': 'str',
        'error_msg': 'str',
        'id': 'str',
        'job_direction': 'str',
        'name': 'str',
        'net_type': 'str',
        'node_new_framework': 'bool',
        'status': 'str',
        'task_type': 'str',
        'job_action': 'JobActionResp'
    }

    attribute_map = {
        'billing_tag': 'billing_tag',
        'create_time': 'create_time',
        'db_use_type': 'db_use_type',
        'description': 'description',
        'engine_type': 'engine_type',
        'error_msg': 'error_msg',
        'id': 'id',
        'job_direction': 'job_direction',
        'name': 'name',
        'net_type': 'net_type',
        'node_new_framework': 'node_newFramework',
        'status': 'status',
        'task_type': 'task_type',
        'job_action': 'job_action'
    }

    def __init__(self, billing_tag=None, create_time=None, db_use_type=None, description=None, engine_type=None, error_msg=None, id=None, job_direction=None, name=None, net_type=None, node_new_framework=None, status=None, task_type=None, job_action=None):
        r"""ChildrenJobInfo

        The model defined in huaweicloud sdk

        :param billing_tag: 计费字段
        :type billing_tag: bool
        :param create_time: 任务创建时间
        :type create_time: str
        :param db_use_type: 复制场景
        :type db_use_type: str
        :param description: 任务描述
        :type description: str
        :param engine_type: 引擎类型
        :type engine_type: str
        :param error_msg: 任务失败原因
        :type error_msg: str
        :param id: 任务id
        :type id: str
        :param job_direction: 迁移方向
        :type job_direction: str
        :param name: 任务名称
        :type name: str
        :param net_type: 网络类型
        :type net_type: str
        :param node_new_framework: 新框架
        :type node_new_framework: bool
        :param status: 任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败
        :type status: str
        :param task_type: 迁移模式
        :type task_type: str
        :param job_action: 
        :type job_action: :class:`huaweicloudsdkdrs.v3.JobActionResp`
        """
        
        

        self._billing_tag = None
        self._create_time = None
        self._db_use_type = None
        self._description = None
        self._engine_type = None
        self._error_msg = None
        self._id = None
        self._job_direction = None
        self._name = None
        self._net_type = None
        self._node_new_framework = None
        self._status = None
        self._task_type = None
        self._job_action = None
        self.discriminator = None

        self.billing_tag = billing_tag
        self.create_time = create_time
        self.db_use_type = db_use_type
        self.description = description
        self.engine_type = engine_type
        self.error_msg = error_msg
        self.id = id
        self.job_direction = job_direction
        self.name = name
        self.net_type = net_type
        self.node_new_framework = node_new_framework
        self.status = status
        self.task_type = task_type
        if job_action is not None:
            self.job_action = job_action

    @property
    def billing_tag(self):
        r"""Gets the billing_tag of this ChildrenJobInfo.

        计费字段

        :return: The billing_tag of this ChildrenJobInfo.
        :rtype: bool
        """
        return self._billing_tag

    @billing_tag.setter
    def billing_tag(self, billing_tag):
        r"""Sets the billing_tag of this ChildrenJobInfo.

        计费字段

        :param billing_tag: The billing_tag of this ChildrenJobInfo.
        :type billing_tag: bool
        """
        self._billing_tag = billing_tag

    @property
    def create_time(self):
        r"""Gets the create_time of this ChildrenJobInfo.

        任务创建时间

        :return: The create_time of this ChildrenJobInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ChildrenJobInfo.

        任务创建时间

        :param create_time: The create_time of this ChildrenJobInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def db_use_type(self):
        r"""Gets the db_use_type of this ChildrenJobInfo.

        复制场景

        :return: The db_use_type of this ChildrenJobInfo.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        r"""Sets the db_use_type of this ChildrenJobInfo.

        复制场景

        :param db_use_type: The db_use_type of this ChildrenJobInfo.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def description(self):
        r"""Gets the description of this ChildrenJobInfo.

        任务描述

        :return: The description of this ChildrenJobInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChildrenJobInfo.

        任务描述

        :param description: The description of this ChildrenJobInfo.
        :type description: str
        """
        self._description = description

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ChildrenJobInfo.

        引擎类型

        :return: The engine_type of this ChildrenJobInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ChildrenJobInfo.

        引擎类型

        :param engine_type: The engine_type of this ChildrenJobInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ChildrenJobInfo.

        任务失败原因

        :return: The error_msg of this ChildrenJobInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ChildrenJobInfo.

        任务失败原因

        :param error_msg: The error_msg of this ChildrenJobInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def id(self):
        r"""Gets the id of this ChildrenJobInfo.

        任务id

        :return: The id of this ChildrenJobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChildrenJobInfo.

        任务id

        :param id: The id of this ChildrenJobInfo.
        :type id: str
        """
        self._id = id

    @property
    def job_direction(self):
        r"""Gets the job_direction of this ChildrenJobInfo.

        迁移方向

        :return: The job_direction of this ChildrenJobInfo.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this ChildrenJobInfo.

        迁移方向

        :param job_direction: The job_direction of this ChildrenJobInfo.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def name(self):
        r"""Gets the name of this ChildrenJobInfo.

        任务名称

        :return: The name of this ChildrenJobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChildrenJobInfo.

        任务名称

        :param name: The name of this ChildrenJobInfo.
        :type name: str
        """
        self._name = name

    @property
    def net_type(self):
        r"""Gets the net_type of this ChildrenJobInfo.

        网络类型

        :return: The net_type of this ChildrenJobInfo.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this ChildrenJobInfo.

        网络类型

        :param net_type: The net_type of this ChildrenJobInfo.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def node_new_framework(self):
        r"""Gets the node_new_framework of this ChildrenJobInfo.

        新框架

        :return: The node_new_framework of this ChildrenJobInfo.
        :rtype: bool
        """
        return self._node_new_framework

    @node_new_framework.setter
    def node_new_framework(self, node_new_framework):
        r"""Sets the node_new_framework of this ChildrenJobInfo.

        新框架

        :param node_new_framework: The node_new_framework of this ChildrenJobInfo.
        :type node_new_framework: bool
        """
        self._node_new_framework = node_new_framework

    @property
    def status(self):
        r"""Gets the status of this ChildrenJobInfo.

        任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败

        :return: The status of this ChildrenJobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChildrenJobInfo.

        任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败

        :param status: The status of this ChildrenJobInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_type(self):
        r"""Gets the task_type of this ChildrenJobInfo.

        迁移模式

        :return: The task_type of this ChildrenJobInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ChildrenJobInfo.

        迁移模式

        :param task_type: The task_type of this ChildrenJobInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def job_action(self):
        r"""Gets the job_action of this ChildrenJobInfo.

        :return: The job_action of this ChildrenJobInfo.
        :rtype: :class:`huaweicloudsdkdrs.v3.JobActionResp`
        """
        return self._job_action

    @job_action.setter
    def job_action(self, job_action):
        r"""Sets the job_action of this ChildrenJobInfo.

        :param job_action: The job_action of this ChildrenJobInfo.
        :type job_action: :class:`huaweicloudsdkdrs.v3.JobActionResp`
        """
        self._job_action = job_action

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
        if not isinstance(other, ChildrenJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
