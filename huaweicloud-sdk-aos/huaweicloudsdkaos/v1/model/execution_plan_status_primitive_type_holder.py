# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanStatusPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        """ExecutionPlanStatusPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param status: 执行计划的状态    * &#x60;CREATION_IN_PROGRESS&#x60; - 正在创建，请等待    * &#x60;CREATION_FAILED&#x60; - 创建失败，请从status_message获取错误信息汇总    * &#x60;AVAILABLE&#x60; - 创建完成，可以调用ApplyExecutionPlan API进行执行    * &#x60;APPLY_IN_PROGRESS&#x60; - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * &#x60;APPLIED&#x60; - 已执行
        :type status: str
        """
        
        

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        """Gets the status of this ExecutionPlanStatusPrimitiveTypeHolder.

        执行计划的状态    * `CREATION_IN_PROGRESS` - 正在创建，请等待    * `CREATION_FAILED` - 创建失败，请从status_message获取错误信息汇总    * `AVAILABLE` - 创建完成，可以调用ApplyExecutionPlan API进行执行    * `APPLY_IN_PROGRESS` - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * `APPLIED` - 已执行

        :return: The status of this ExecutionPlanStatusPrimitiveTypeHolder.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionPlanStatusPrimitiveTypeHolder.

        执行计划的状态    * `CREATION_IN_PROGRESS` - 正在创建，请等待    * `CREATION_FAILED` - 创建失败，请从status_message获取错误信息汇总    * `AVAILABLE` - 创建完成，可以调用ApplyExecutionPlan API进行执行    * `APPLY_IN_PROGRESS` - 执行中，可通过GetStackMetadata查询资源栈状态，通过ListStackEvents获取执行过程中产生的资源栈事件    * `APPLIED` - 已执行

        :param status: The status of this ExecutionPlanStatusPrimitiveTypeHolder.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ExecutionPlanStatusPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
