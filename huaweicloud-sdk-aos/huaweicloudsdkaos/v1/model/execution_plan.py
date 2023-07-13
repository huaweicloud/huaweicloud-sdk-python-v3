# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_name': 'str',
        'stack_id': 'str',
        'execution_plan_id': 'str',
        'execution_plan_name': 'str',
        'description': 'str',
        'status': 'str',
        'status_message': 'str',
        'create_time': 'str',
        'apply_time': 'str'
    }

    attribute_map = {
        'stack_name': 'stack_name',
        'stack_id': 'stack_id',
        'execution_plan_id': 'execution_plan_id',
        'execution_plan_name': 'execution_plan_name',
        'description': 'description',
        'status': 'status',
        'status_message': 'status_message',
        'create_time': 'create_time',
        'apply_time': 'apply_time'
    }

    def __init__(self, stack_name=None, stack_id=None, execution_plan_id=None, execution_plan_name=None, description=None, status=None, status_message=None, create_time=None, apply_time=None):
        """ExecutionPlan

        The model defined in huaweicloud sdk

        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param stack_id: 资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param execution_plan_id: 执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给与的execution_plan_id和当前执行计划的ID不一致，则返回400
        :type execution_plan_id: str
        :param execution_plan_name: 执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type execution_plan_name: str
        :param description: 执行计划的描述。可用于客户识别自己的执行计划。
        :type description: str
        :param status: 执行计划的状态    * &#x60;CREATION_IN_PROGRESS&#x60; - 正在创建，请等待    * &#x60;CREATION_FAILED&#x60; - 创建失败，请从status_message获取错误信息汇总    * &#x60;AVAILABLE&#x60; - 创建完成，可以调用ApplyExecutionPlan API进行执行    * &#x60;APPLY_IN_PROGRESS&#x60; - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * &#x60;APPLIED&#x60; - 已执行
        :type status: str
        :param status_message: 当执行计划的状态为创建失败状态（即为 &#x60;CREATION_FAILED&#x60; 时），将会展示简要的错误信息总结以供debug
        :type status_message: str
        :param create_time: 执行计划的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param apply_time: 执行计划的执行时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type apply_time: str
        """
        
        

        self._stack_name = None
        self._stack_id = None
        self._execution_plan_id = None
        self._execution_plan_name = None
        self._description = None
        self._status = None
        self._status_message = None
        self._create_time = None
        self._apply_time = None
        self.discriminator = None

        self.stack_name = stack_name
        if stack_id is not None:
            self.stack_id = stack_id
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id
        self.execution_plan_name = execution_plan_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if create_time is not None:
            self.create_time = create_time
        if apply_time is not None:
            self.apply_time = apply_time

    @property
    def stack_name(self):
        """Gets the stack_name of this ExecutionPlan.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this ExecutionPlan.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this ExecutionPlan.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this ExecutionPlan.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_id(self):
        """Gets the stack_id of this ExecutionPlan.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this ExecutionPlan.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ExecutionPlan.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this ExecutionPlan.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this ExecutionPlan.

        执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给与的execution_plan_id和当前执行计划的ID不一致，则返回400

        :return: The execution_plan_id of this ExecutionPlan.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this ExecutionPlan.

        执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给与的execution_plan_id和当前执行计划的ID不一致，则返回400

        :param execution_plan_id: The execution_plan_id of this ExecutionPlan.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this ExecutionPlan.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The execution_plan_name of this ExecutionPlan.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this ExecutionPlan.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param execution_plan_name: The execution_plan_name of this ExecutionPlan.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def description(self):
        """Gets the description of this ExecutionPlan.

        执行计划的描述。可用于客户识别自己的执行计划。

        :return: The description of this ExecutionPlan.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExecutionPlan.

        执行计划的描述。可用于客户识别自己的执行计划。

        :param description: The description of this ExecutionPlan.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ExecutionPlan.

        执行计划的状态    * `CREATION_IN_PROGRESS` - 正在创建，请等待    * `CREATION_FAILED` - 创建失败，请从status_message获取错误信息汇总    * `AVAILABLE` - 创建完成，可以调用ApplyExecutionPlan API进行执行    * `APPLY_IN_PROGRESS` - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * `APPLIED` - 已执行

        :return: The status of this ExecutionPlan.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionPlan.

        执行计划的状态    * `CREATION_IN_PROGRESS` - 正在创建，请等待    * `CREATION_FAILED` - 创建失败，请从status_message获取错误信息汇总    * `AVAILABLE` - 创建完成，可以调用ApplyExecutionPlan API进行执行    * `APPLY_IN_PROGRESS` - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * `APPLIED` - 已执行

        :param status: The status of this ExecutionPlan.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this ExecutionPlan.

        当执行计划的状态为创建失败状态（即为 `CREATION_FAILED` 时），将会展示简要的错误信息总结以供debug

        :return: The status_message of this ExecutionPlan.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this ExecutionPlan.

        当执行计划的状态为创建失败状态（即为 `CREATION_FAILED` 时），将会展示简要的错误信息总结以供debug

        :param status_message: The status_message of this ExecutionPlan.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def create_time(self):
        """Gets the create_time of this ExecutionPlan.

        执行计划的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this ExecutionPlan.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ExecutionPlan.

        执行计划的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this ExecutionPlan.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def apply_time(self):
        """Gets the apply_time of this ExecutionPlan.

        执行计划的执行时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The apply_time of this ExecutionPlan.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ExecutionPlan.

        执行计划的执行时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param apply_time: The apply_time of this ExecutionPlan.
        :type apply_time: str
        """
        self._apply_time = apply_time

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
        if not isinstance(other, ExecutionPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
