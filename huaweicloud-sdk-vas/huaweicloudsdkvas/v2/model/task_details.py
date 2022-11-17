# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetails:

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
        'creator': 'str',
        'project_id': 'str',
        'description': 'str',
        'service_name': 'str',
        'service_version': 'str',
        'service_title': 'TaskDetailsServiceTitle',
        'edge_pool_id': 'str',
        'resource_order_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'state': 'str',
        'status': 'str',
        'error': 'TaskDetailsError',
        'timing_status': 'str',
        'timing': 'TaskTiming',
        'input': 'TaskInput',
        'output': 'TaskOutputForDisplay',
        'service_config': 'TaskServiceConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creator': 'creator',
        'project_id': 'project_id',
        'description': 'description',
        'service_name': 'service_name',
        'service_version': 'service_version',
        'service_title': 'service_title',
        'edge_pool_id': 'edge_pool_id',
        'resource_order_id': 'resource_order_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'state': 'state',
        'status': 'status',
        'error': 'error',
        'timing_status': 'timing_status',
        'timing': 'timing',
        'input': 'input',
        'output': 'output',
        'service_config': 'service_config'
    }

    def __init__(self, id=None, name=None, creator=None, project_id=None, description=None, service_name=None, service_version=None, service_title=None, edge_pool_id=None, resource_order_id=None, created_at=None, updated_at=None, state=None, status=None, error=None, timing_status=None, timing=None, input=None, output=None, service_config=None):
        """TaskDetails

        The model defined in huaweicloud sdk

        :param id: 作业ID
        :type id: str
        :param name: 作业的名称
        :type name: str
        :param creator: 作业创建者的用户名
        :type creator: str
        :param project_id: 作业创建者的项目ID
        :type project_id: str
        :param description: 作业的描述
        :type description: str
        :param service_name: 作业对应服务的名称
        :type service_name: str
        :param service_version: 作业对应服务的版本号
        :type service_version: str
        :param service_title: 
        :type service_title: :class:`huaweicloudsdkvas.v2.TaskDetailsServiceTitle`
        :param edge_pool_id: 仅边缘作业会出现，作业运行所在的边缘运行池ID
        :type edge_pool_id: str
        :param resource_order_id: 作业指定的算法能力包包周期订单ID
        :type resource_order_id: str
        :param created_at: 作业创建的时间
        :type created_at: datetime
        :param updated_at: 作业最近一次状态更新的时间
        :type updated_at: datetime
        :param state: 作业当前的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）
        :type state: str
        :param status: 作业状态的详情信息，仅部分状态会有详情信息
        :type status: str
        :param error: 
        :type error: :class:`huaweicloudsdkvas.v2.TaskDetailsError`
        :param timing_status: 计划任务的状态，分别为ACTIVATED（激活），INACTIVATED（未激活）
        :type timing_status: str
        :param timing: 
        :type timing: :class:`huaweicloudsdkvas.v2.TaskTiming`
        :param input: 
        :type input: :class:`huaweicloudsdkvas.v2.TaskInput`
        :param output: 
        :type output: :class:`huaweicloudsdkvas.v2.TaskOutputForDisplay`
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        
        

        self._id = None
        self._name = None
        self._creator = None
        self._project_id = None
        self._description = None
        self._service_name = None
        self._service_version = None
        self._service_title = None
        self._edge_pool_id = None
        self._resource_order_id = None
        self._created_at = None
        self._updated_at = None
        self._state = None
        self._status = None
        self._error = None
        self._timing_status = None
        self._timing = None
        self._input = None
        self._output = None
        self._service_config = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.creator = creator
        self.project_id = project_id
        if description is not None:
            self.description = description
        self.service_name = service_name
        self.service_version = service_version
        self.service_title = service_title
        if edge_pool_id is not None:
            self.edge_pool_id = edge_pool_id
        if resource_order_id is not None:
            self.resource_order_id = resource_order_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.state = state
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if timing_status is not None:
            self.timing_status = timing_status
        if timing is not None:
            self.timing = timing
        self.input = input
        self.output = output
        if service_config is not None:
            self.service_config = service_config

    @property
    def id(self):
        """Gets the id of this TaskDetails.

        作业ID

        :return: The id of this TaskDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDetails.

        作业ID

        :param id: The id of this TaskDetails.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskDetails.

        作业的名称

        :return: The name of this TaskDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskDetails.

        作业的名称

        :param name: The name of this TaskDetails.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        """Gets the creator of this TaskDetails.

        作业创建者的用户名

        :return: The creator of this TaskDetails.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TaskDetails.

        作业创建者的用户名

        :param creator: The creator of this TaskDetails.
        :type creator: str
        """
        self._creator = creator

    @property
    def project_id(self):
        """Gets the project_id of this TaskDetails.

        作业创建者的项目ID

        :return: The project_id of this TaskDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskDetails.

        作业创建者的项目ID

        :param project_id: The project_id of this TaskDetails.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this TaskDetails.

        作业的描述

        :return: The description of this TaskDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDetails.

        作业的描述

        :param description: The description of this TaskDetails.
        :type description: str
        """
        self._description = description

    @property
    def service_name(self):
        """Gets the service_name of this TaskDetails.

        作业对应服务的名称

        :return: The service_name of this TaskDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this TaskDetails.

        作业对应服务的名称

        :param service_name: The service_name of this TaskDetails.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def service_version(self):
        """Gets the service_version of this TaskDetails.

        作业对应服务的版本号

        :return: The service_version of this TaskDetails.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """Sets the service_version of this TaskDetails.

        作业对应服务的版本号

        :param service_version: The service_version of this TaskDetails.
        :type service_version: str
        """
        self._service_version = service_version

    @property
    def service_title(self):
        """Gets the service_title of this TaskDetails.

        :return: The service_title of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskDetailsServiceTitle`
        """
        return self._service_title

    @service_title.setter
    def service_title(self, service_title):
        """Sets the service_title of this TaskDetails.

        :param service_title: The service_title of this TaskDetails.
        :type service_title: :class:`huaweicloudsdkvas.v2.TaskDetailsServiceTitle`
        """
        self._service_title = service_title

    @property
    def edge_pool_id(self):
        """Gets the edge_pool_id of this TaskDetails.

        仅边缘作业会出现，作业运行所在的边缘运行池ID

        :return: The edge_pool_id of this TaskDetails.
        :rtype: str
        """
        return self._edge_pool_id

    @edge_pool_id.setter
    def edge_pool_id(self, edge_pool_id):
        """Sets the edge_pool_id of this TaskDetails.

        仅边缘作业会出现，作业运行所在的边缘运行池ID

        :param edge_pool_id: The edge_pool_id of this TaskDetails.
        :type edge_pool_id: str
        """
        self._edge_pool_id = edge_pool_id

    @property
    def resource_order_id(self):
        """Gets the resource_order_id of this TaskDetails.

        作业指定的算法能力包包周期订单ID

        :return: The resource_order_id of this TaskDetails.
        :rtype: str
        """
        return self._resource_order_id

    @resource_order_id.setter
    def resource_order_id(self, resource_order_id):
        """Sets the resource_order_id of this TaskDetails.

        作业指定的算法能力包包周期订单ID

        :param resource_order_id: The resource_order_id of this TaskDetails.
        :type resource_order_id: str
        """
        self._resource_order_id = resource_order_id

    @property
    def created_at(self):
        """Gets the created_at of this TaskDetails.

        作业创建的时间

        :return: The created_at of this TaskDetails.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskDetails.

        作业创建的时间

        :param created_at: The created_at of this TaskDetails.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskDetails.

        作业最近一次状态更新的时间

        :return: The updated_at of this TaskDetails.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskDetails.

        作业最近一次状态更新的时间

        :param updated_at: The updated_at of this TaskDetails.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def state(self):
        """Gets the state of this TaskDetails.

        作业当前的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）

        :return: The state of this TaskDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskDetails.

        作业当前的状态，分别为PENDING（等待中），RECOVERING（恢复中），STARTING（启动中），UPGRADING（升级中），CREATE_FAILED（创建失败），START_FAILED（启动失败），RUNNING（运行中），STOPPING（停止中），STOPPED（已停止），ABNORMAL（异常），SUCCEEDED（运行成功），FAILED（运行失败），DELETING（删除中），FREEZING（冻结中），FROZEN（已冻结）

        :param state: The state of this TaskDetails.
        :type state: str
        """
        self._state = state

    @property
    def status(self):
        """Gets the status of this TaskDetails.

        作业状态的详情信息，仅部分状态会有详情信息

        :return: The status of this TaskDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskDetails.

        作业状态的详情信息，仅部分状态会有详情信息

        :param status: The status of this TaskDetails.
        :type status: str
        """
        self._status = status

    @property
    def error(self):
        """Gets the error of this TaskDetails.

        :return: The error of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskDetailsError`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TaskDetails.

        :param error: The error of this TaskDetails.
        :type error: :class:`huaweicloudsdkvas.v2.TaskDetailsError`
        """
        self._error = error

    @property
    def timing_status(self):
        """Gets the timing_status of this TaskDetails.

        计划任务的状态，分别为ACTIVATED（激活），INACTIVATED（未激活）

        :return: The timing_status of this TaskDetails.
        :rtype: str
        """
        return self._timing_status

    @timing_status.setter
    def timing_status(self, timing_status):
        """Sets the timing_status of this TaskDetails.

        计划任务的状态，分别为ACTIVATED（激活），INACTIVATED（未激活）

        :param timing_status: The timing_status of this TaskDetails.
        :type timing_status: str
        """
        self._timing_status = timing_status

    @property
    def timing(self):
        """Gets the timing of this TaskDetails.

        :return: The timing of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskTiming`
        """
        return self._timing

    @timing.setter
    def timing(self, timing):
        """Sets the timing of this TaskDetails.

        :param timing: The timing of this TaskDetails.
        :type timing: :class:`huaweicloudsdkvas.v2.TaskTiming`
        """
        self._timing = timing

    @property
    def input(self):
        """Gets the input of this TaskDetails.

        :return: The input of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TaskDetails.

        :param input: The input of this TaskDetails.
        :type input: :class:`huaweicloudsdkvas.v2.TaskInput`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this TaskDetails.

        :return: The output of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputForDisplay`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TaskDetails.

        :param output: The output of this TaskDetails.
        :type output: :class:`huaweicloudsdkvas.v2.TaskOutputForDisplay`
        """
        self._output = output

    @property
    def service_config(self):
        """Gets the service_config of this TaskDetails.

        :return: The service_config of this TaskDetails.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """Sets the service_config of this TaskDetails.

        :param service_config: The service_config of this TaskDetails.
        :type service_config: :class:`huaweicloudsdkvas.v2.TaskServiceConfig`
        """
        self._service_config = service_config

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
        if not isinstance(other, TaskDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
