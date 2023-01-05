# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowCreateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'start': 'str',
        'triggers': 'list[Trigger]',
        'functions': 'list[Function]',
        'states': 'list[OperationState]',
        'constants': 'object',
        'retries': 'list[Retry]',
        'mode': 'str',
        'express_config': 'ExpressConfig',
        'enterprise_project_id': 'str',
        'enable_stream_response': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'start': 'start',
        'triggers': 'triggers',
        'functions': 'functions',
        'states': 'states',
        'constants': 'constants',
        'retries': 'retries',
        'mode': 'mode',
        'express_config': 'express_config',
        'enterprise_project_id': 'enterprise_project_id',
        'enable_stream_response': 'enable_stream_response'
    }

    def __init__(self, name=None, description=None, start=None, triggers=None, functions=None, states=None, constants=None, retries=None, mode=None, express_config=None, enterprise_project_id=None, enable_stream_response=None):
        """WorkflowCreateBody

        The model defined in huaweicloud sdk

        :param name: 函数流名称
        :type name: str
        :param description: 函数流描述
        :type description: str
        :param start: 流程开始节点ID
        :type start: str
        :param triggers: 触发器列表
        :type triggers: list[:class:`huaweicloudsdkfunctiongraph.v2.Trigger`]
        :param functions: 函数列表
        :type functions: list[:class:`huaweicloudsdkfunctiongraph.v2.Function`]
        :param states: 函数流节点清单，定义参考SleepState和OperationState
        :type states: list[:class:`huaweicloudsdkfunctiongraph.v2.OperationState`]
        :param constants: 函数流中的常量
        :type constants: object
        :param retries: 重试策略清单
        :type retries: list[:class:`huaweicloudsdkfunctiongraph.v2.Retry`]
        :param mode: 函数流模式，当前支持两种模式 NORMAL: 标准模式，普通模式面向普通的业务场景，支持长时间任务，支持执行历史持久化和查询，只支持异步调用 EXPRESS: 快速模式，快速模式面向业务执行时长较短，需要极致性能的场景，只支持流程执行时长低于5分钟的场景，不支持执行历史持久化，支持同步和异步调用 默认为标准模式
        :type mode: str
        :param express_config: 
        :type express_config: :class:`huaweicloudsdkfunctiongraph.v2.ExpressConfig`
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param enable_stream_response: 是否返回流数据
        :type enable_stream_response: bool
        """
        
        

        self._name = None
        self._description = None
        self._start = None
        self._triggers = None
        self._functions = None
        self._states = None
        self._constants = None
        self._retries = None
        self._mode = None
        self._express_config = None
        self._enterprise_project_id = None
        self._enable_stream_response = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.start = start
        if triggers is not None:
            self.triggers = triggers
        self.functions = functions
        self.states = states
        self.constants = constants
        self.retries = retries
        if mode is not None:
            self.mode = mode
        if express_config is not None:
            self.express_config = express_config
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enable_stream_response is not None:
            self.enable_stream_response = enable_stream_response

    @property
    def name(self):
        """Gets the name of this WorkflowCreateBody.

        函数流名称

        :return: The name of this WorkflowCreateBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowCreateBody.

        函数流名称

        :param name: The name of this WorkflowCreateBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkflowCreateBody.

        函数流描述

        :return: The description of this WorkflowCreateBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowCreateBody.

        函数流描述

        :param description: The description of this WorkflowCreateBody.
        :type description: str
        """
        self._description = description

    @property
    def start(self):
        """Gets the start of this WorkflowCreateBody.

        流程开始节点ID

        :return: The start of this WorkflowCreateBody.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this WorkflowCreateBody.

        流程开始节点ID

        :param start: The start of this WorkflowCreateBody.
        :type start: str
        """
        self._start = start

    @property
    def triggers(self):
        """Gets the triggers of this WorkflowCreateBody.

        触发器列表

        :return: The triggers of this WorkflowCreateBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Trigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this WorkflowCreateBody.

        触发器列表

        :param triggers: The triggers of this WorkflowCreateBody.
        :type triggers: list[:class:`huaweicloudsdkfunctiongraph.v2.Trigger`]
        """
        self._triggers = triggers

    @property
    def functions(self):
        """Gets the functions of this WorkflowCreateBody.

        函数列表

        :return: The functions of this WorkflowCreateBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Function`]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this WorkflowCreateBody.

        函数列表

        :param functions: The functions of this WorkflowCreateBody.
        :type functions: list[:class:`huaweicloudsdkfunctiongraph.v2.Function`]
        """
        self._functions = functions

    @property
    def states(self):
        """Gets the states of this WorkflowCreateBody.

        函数流节点清单，定义参考SleepState和OperationState

        :return: The states of this WorkflowCreateBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.OperationState`]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this WorkflowCreateBody.

        函数流节点清单，定义参考SleepState和OperationState

        :param states: The states of this WorkflowCreateBody.
        :type states: list[:class:`huaweicloudsdkfunctiongraph.v2.OperationState`]
        """
        self._states = states

    @property
    def constants(self):
        """Gets the constants of this WorkflowCreateBody.

        函数流中的常量

        :return: The constants of this WorkflowCreateBody.
        :rtype: object
        """
        return self._constants

    @constants.setter
    def constants(self, constants):
        """Sets the constants of this WorkflowCreateBody.

        函数流中的常量

        :param constants: The constants of this WorkflowCreateBody.
        :type constants: object
        """
        self._constants = constants

    @property
    def retries(self):
        """Gets the retries of this WorkflowCreateBody.

        重试策略清单

        :return: The retries of this WorkflowCreateBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Retry`]
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this WorkflowCreateBody.

        重试策略清单

        :param retries: The retries of this WorkflowCreateBody.
        :type retries: list[:class:`huaweicloudsdkfunctiongraph.v2.Retry`]
        """
        self._retries = retries

    @property
    def mode(self):
        """Gets the mode of this WorkflowCreateBody.

        函数流模式，当前支持两种模式 NORMAL: 标准模式，普通模式面向普通的业务场景，支持长时间任务，支持执行历史持久化和查询，只支持异步调用 EXPRESS: 快速模式，快速模式面向业务执行时长较短，需要极致性能的场景，只支持流程执行时长低于5分钟的场景，不支持执行历史持久化，支持同步和异步调用 默认为标准模式

        :return: The mode of this WorkflowCreateBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this WorkflowCreateBody.

        函数流模式，当前支持两种模式 NORMAL: 标准模式，普通模式面向普通的业务场景，支持长时间任务，支持执行历史持久化和查询，只支持异步调用 EXPRESS: 快速模式，快速模式面向业务执行时长较短，需要极致性能的场景，只支持流程执行时长低于5分钟的场景，不支持执行历史持久化，支持同步和异步调用 默认为标准模式

        :param mode: The mode of this WorkflowCreateBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def express_config(self):
        """Gets the express_config of this WorkflowCreateBody.

        :return: The express_config of this WorkflowCreateBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ExpressConfig`
        """
        return self._express_config

    @express_config.setter
    def express_config(self, express_config):
        """Sets the express_config of this WorkflowCreateBody.

        :param express_config: The express_config of this WorkflowCreateBody.
        :type express_config: :class:`huaweicloudsdkfunctiongraph.v2.ExpressConfig`
        """
        self._express_config = express_config

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this WorkflowCreateBody.

        企业项目ID

        :return: The enterprise_project_id of this WorkflowCreateBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this WorkflowCreateBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this WorkflowCreateBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_stream_response(self):
        """Gets the enable_stream_response of this WorkflowCreateBody.

        是否返回流数据

        :return: The enable_stream_response of this WorkflowCreateBody.
        :rtype: bool
        """
        return self._enable_stream_response

    @enable_stream_response.setter
    def enable_stream_response(self, enable_stream_response):
        """Sets the enable_stream_response of this WorkflowCreateBody.

        是否返回流数据

        :param enable_stream_response: The enable_stream_response of this WorkflowCreateBody.
        :type enable_stream_response: bool
        """
        self._enable_stream_response = enable_stream_response

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
        if not isinstance(other, WorkflowCreateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
