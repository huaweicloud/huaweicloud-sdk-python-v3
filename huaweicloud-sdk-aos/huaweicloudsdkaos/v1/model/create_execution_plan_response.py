# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExecutionPlanResponse(SdkResponse):

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
        'execution_plan_name': 'str',
        'execution_plan_id': 'str'
    }

    attribute_map = {
        'stack_name': 'stack_name',
        'stack_id': 'stack_id',
        'execution_plan_name': 'execution_plan_name',
        'execution_plan_id': 'execution_plan_id'
    }

    def __init__(self, stack_name=None, stack_id=None, execution_plan_name=None, execution_plan_id=None):
        """CreateExecutionPlanResponse

        The model defined in huaweicloud sdk

        :param stack_name: 栈的名字
        :type stack_name: str
        :param stack_id: 栈的唯一Id
        :type stack_id: str
        :param execution_plan_name: 执行计划的名字。如果未指定，则使用execution_plan_id作为execution_plan_name。
        :type execution_plan_name: str
        :param execution_plan_id: 执行计划的唯一Id，由IaC随机生成
        :type execution_plan_id: str
        """
        
        super(CreateExecutionPlanResponse, self).__init__()

        self._stack_name = None
        self._stack_id = None
        self._execution_plan_name = None
        self._execution_plan_id = None
        self.discriminator = None

        if stack_name is not None:
            self.stack_name = stack_name
        if stack_id is not None:
            self.stack_id = stack_id
        if execution_plan_name is not None:
            self.execution_plan_name = execution_plan_name
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id

    @property
    def stack_name(self):
        """Gets the stack_name of this CreateExecutionPlanResponse.

        栈的名字

        :return: The stack_name of this CreateExecutionPlanResponse.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this CreateExecutionPlanResponse.

        栈的名字

        :param stack_name: The stack_name of this CreateExecutionPlanResponse.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_id(self):
        """Gets the stack_id of this CreateExecutionPlanResponse.

        栈的唯一Id

        :return: The stack_id of this CreateExecutionPlanResponse.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this CreateExecutionPlanResponse.

        栈的唯一Id

        :param stack_id: The stack_id of this CreateExecutionPlanResponse.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this CreateExecutionPlanResponse.

        执行计划的名字。如果未指定，则使用execution_plan_id作为execution_plan_name。

        :return: The execution_plan_name of this CreateExecutionPlanResponse.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this CreateExecutionPlanResponse.

        执行计划的名字。如果未指定，则使用execution_plan_id作为execution_plan_name。

        :param execution_plan_name: The execution_plan_name of this CreateExecutionPlanResponse.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this CreateExecutionPlanResponse.

        执行计划的唯一Id，由IaC随机生成

        :return: The execution_plan_id of this CreateExecutionPlanResponse.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this CreateExecutionPlanResponse.

        执行计划的唯一Id，由IaC随机生成

        :param execution_plan_id: The execution_plan_id of this CreateExecutionPlanResponse.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

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
        if not isinstance(other, CreateExecutionPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
