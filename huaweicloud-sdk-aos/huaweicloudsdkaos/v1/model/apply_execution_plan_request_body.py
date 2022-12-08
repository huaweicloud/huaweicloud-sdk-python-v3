# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyExecutionPlanRequestBody:

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
        'execution_plan_id': 'str'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'execution_plan_id': 'execution_plan_id'
    }

    def __init__(self, stack_id=None, execution_plan_id=None):
        """ApplyExecutionPlanRequestBody

        The model defined in huaweicloud sdk

        :param stack_id: 资源栈id
        :type stack_id: str
        :param execution_plan_id: 执行计划Id，在domain_id+region+project_id+stack_id下应唯一
        :type execution_plan_id: str
        """
        
        

        self._stack_id = None
        self._execution_plan_id = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id

    @property
    def stack_id(self):
        """Gets the stack_id of this ApplyExecutionPlanRequestBody.

        资源栈id

        :return: The stack_id of this ApplyExecutionPlanRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ApplyExecutionPlanRequestBody.

        资源栈id

        :param stack_id: The stack_id of this ApplyExecutionPlanRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this ApplyExecutionPlanRequestBody.

        执行计划Id，在domain_id+region+project_id+stack_id下应唯一

        :return: The execution_plan_id of this ApplyExecutionPlanRequestBody.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this ApplyExecutionPlanRequestBody.

        执行计划Id，在domain_id+region+project_id+stack_id下应唯一

        :param execution_plan_id: The execution_plan_id of this ApplyExecutionPlanRequestBody.
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
        if not isinstance(other, ApplyExecutionPlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
