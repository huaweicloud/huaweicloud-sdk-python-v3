# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkflowRequestBody:


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
        'triggers': 'list[Trigger]',
        'start': 'str',
        'functions': 'list[Function]',
        'states': 'list[OperationState]',
        'constants': 'object',
        'retries': 'list[Retry]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'triggers': 'triggers',
        'start': 'start',
        'functions': 'functions',
        'states': 'states',
        'constants': 'constants',
        'retries': 'retries',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, triggers=None, start=None, functions=None, states=None, constants=None, retries=None, enterprise_project_id=None):
        """CreateWorkflowRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._triggers = None
        self._start = None
        self._functions = None
        self._states = None
        self._constants = None
        self._retries = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if triggers is not None:
            self.triggers = triggers
        if start is not None:
            self.start = start
        if functions is not None:
            self.functions = functions
        if states is not None:
            self.states = states
        if constants is not None:
            self.constants = constants
        if retries is not None:
            self.retries = retries
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateWorkflowRequestBody.

        流程定义名称

        :return: The name of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWorkflowRequestBody.

        流程定义名称

        :param name: The name of this CreateWorkflowRequestBody.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateWorkflowRequestBody.

        流程定义描述

        :return: The description of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateWorkflowRequestBody.

        流程定义描述

        :param description: The description of this CreateWorkflowRequestBody.
        :type: str
        """
        self._description = description

    @property
    def triggers(self):
        """Gets the triggers of this CreateWorkflowRequestBody.

        触发器列表

        :return: The triggers of this CreateWorkflowRequestBody.
        :rtype: list[Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this CreateWorkflowRequestBody.

        触发器列表

        :param triggers: The triggers of this CreateWorkflowRequestBody.
        :type: list[Trigger]
        """
        self._triggers = triggers

    @property
    def start(self):
        """Gets the start of this CreateWorkflowRequestBody.

        流程开始节点ID

        :return: The start of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this CreateWorkflowRequestBody.

        流程开始节点ID

        :param start: The start of this CreateWorkflowRequestBody.
        :type: str
        """
        self._start = start

    @property
    def functions(self):
        """Gets the functions of this CreateWorkflowRequestBody.

        函数清单

        :return: The functions of this CreateWorkflowRequestBody.
        :rtype: list[Function]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this CreateWorkflowRequestBody.

        函数清单

        :param functions: The functions of this CreateWorkflowRequestBody.
        :type: list[Function]
        """
        self._functions = functions

    @property
    def states(self):
        """Gets the states of this CreateWorkflowRequestBody.

        工作流节点清单，定义参考SleepState和OperationState

        :return: The states of this CreateWorkflowRequestBody.
        :rtype: list[OperationState]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this CreateWorkflowRequestBody.

        工作流节点清单，定义参考SleepState和OperationState

        :param states: The states of this CreateWorkflowRequestBody.
        :type: list[OperationState]
        """
        self._states = states

    @property
    def constants(self):
        """Gets the constants of this CreateWorkflowRequestBody.

        工作流中的常量

        :return: The constants of this CreateWorkflowRequestBody.
        :rtype: object
        """
        return self._constants

    @constants.setter
    def constants(self, constants):
        """Sets the constants of this CreateWorkflowRequestBody.

        工作流中的常量

        :param constants: The constants of this CreateWorkflowRequestBody.
        :type: object
        """
        self._constants = constants

    @property
    def retries(self):
        """Gets the retries of this CreateWorkflowRequestBody.

        重试策略清单

        :return: The retries of this CreateWorkflowRequestBody.
        :rtype: list[Retry]
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this CreateWorkflowRequestBody.

        重试策略清单

        :param retries: The retries of this CreateWorkflowRequestBody.
        :type: list[Retry]
        """
        self._retries = retries

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateWorkflowRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateWorkflowRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateWorkflowRequestBody.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateWorkflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
