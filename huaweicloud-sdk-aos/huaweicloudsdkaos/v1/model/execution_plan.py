# coding: utf-8

import re
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
        'stack_id': 'str',
        'stack_name': 'str',
        'execution_plan_id': 'str',
        'execution_plan_name': 'str',
        'description': 'str',
        'create_time': 'str',
        'apply_time': 'str',
        'status': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'stack_name': 'stack_name',
        'execution_plan_id': 'execution_plan_id',
        'execution_plan_name': 'execution_plan_name',
        'description': 'description',
        'create_time': 'create_time',
        'apply_time': 'apply_time',
        'status': 'status',
        'status_message': 'status_message'
    }

    def __init__(self, stack_id=None, stack_name=None, execution_plan_id=None, execution_plan_name=None, description=None, create_time=None, apply_time=None, status=None, status_message=None):
        """ExecutionPlan

        The model defined in huaweicloud sdk

        :param stack_id: 栈的唯一Id,为uuid
        :type stack_id: str
        :param stack_name: 栈的名字
        :type stack_name: str
        :param execution_plan_id: 执行计划的唯一Id，由资源编排服务随机生成,为uuid
        :type execution_plan_id: str
        :param execution_plan_name: 执行计划的名字
        :type execution_plan_name: str
        :param description: 执行计划的描述，此描述为用户在生成时指定
        :type description: str
        :param create_time: 执行计划的生成时间
        :type create_time: str
        :param apply_time: 执行时间
        :type apply_time: str
        :param status: 执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行     * &#x60;CREATION_IN_PROGRESS&#x60; - 正在生成     * &#x60;CREATION_FAILED&#x60; - 生成失败     * &#x60;AVAILABLE&#x60; - 执行计划已经生成完成。可以使用apply进行执行     * &#x60;APPLIED&#x60; - 执行完成
        :type status: str
        :param status_message: 展示执行计划状态更多细节的信息
        :type status_message: str
        """
        
        

        self._stack_id = None
        self._stack_name = None
        self._execution_plan_id = None
        self._execution_plan_name = None
        self._description = None
        self._create_time = None
        self._apply_time = None
        self._status = None
        self._status_message = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if stack_name is not None:
            self.stack_name = stack_name
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id
        if execution_plan_name is not None:
            self.execution_plan_name = execution_plan_name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if apply_time is not None:
            self.apply_time = apply_time
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message

    @property
    def stack_id(self):
        """Gets the stack_id of this ExecutionPlan.

        栈的唯一Id,为uuid

        :return: The stack_id of this ExecutionPlan.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ExecutionPlan.

        栈的唯一Id,为uuid

        :param stack_id: The stack_id of this ExecutionPlan.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def stack_name(self):
        """Gets the stack_name of this ExecutionPlan.

        栈的名字

        :return: The stack_name of this ExecutionPlan.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this ExecutionPlan.

        栈的名字

        :param stack_name: The stack_name of this ExecutionPlan.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this ExecutionPlan.

        执行计划的唯一Id，由资源编排服务随机生成,为uuid

        :return: The execution_plan_id of this ExecutionPlan.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this ExecutionPlan.

        执行计划的唯一Id，由资源编排服务随机生成,为uuid

        :param execution_plan_id: The execution_plan_id of this ExecutionPlan.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this ExecutionPlan.

        执行计划的名字

        :return: The execution_plan_name of this ExecutionPlan.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this ExecutionPlan.

        执行计划的名字

        :param execution_plan_name: The execution_plan_name of this ExecutionPlan.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def description(self):
        """Gets the description of this ExecutionPlan.

        执行计划的描述，此描述为用户在生成时指定

        :return: The description of this ExecutionPlan.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExecutionPlan.

        执行计划的描述，此描述为用户在生成时指定

        :param description: The description of this ExecutionPlan.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this ExecutionPlan.

        执行计划的生成时间

        :return: The create_time of this ExecutionPlan.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ExecutionPlan.

        执行计划的生成时间

        :param create_time: The create_time of this ExecutionPlan.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def apply_time(self):
        """Gets the apply_time of this ExecutionPlan.

        执行时间

        :return: The apply_time of this ExecutionPlan.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ExecutionPlan.

        执行时间

        :param apply_time: The apply_time of this ExecutionPlan.
        :type apply_time: str
        """
        self._apply_time = apply_time

    @property
    def status(self):
        """Gets the status of this ExecutionPlan.

        执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行     * `CREATION_IN_PROGRESS` - 正在生成     * `CREATION_FAILED` - 生成失败     * `AVAILABLE` - 执行计划已经生成完成。可以使用apply进行执行     * `APPLIED` - 执行完成

        :return: The status of this ExecutionPlan.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionPlan.

        执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行     * `CREATION_IN_PROGRESS` - 正在生成     * `CREATION_FAILED` - 生成失败     * `AVAILABLE` - 执行计划已经生成完成。可以使用apply进行执行     * `APPLIED` - 执行完成

        :param status: The status of this ExecutionPlan.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this ExecutionPlan.

        展示执行计划状态更多细节的信息

        :return: The status_message of this ExecutionPlan.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this ExecutionPlan.

        展示执行计划状态更多细节的信息

        :param status_message: The status_message of this ExecutionPlan.
        :type status_message: str
        """
        self._status_message = status_message

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
