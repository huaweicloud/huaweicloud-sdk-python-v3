# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanNamePrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_plan_name': 'str'
    }

    attribute_map = {
        'execution_plan_name': 'execution_plan_name'
    }

    def __init__(self, execution_plan_name=None):
        r"""ExecutionPlanNamePrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param execution_plan_name: 执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type execution_plan_name: str
        """
        
        

        self._execution_plan_name = None
        self.discriminator = None

        self.execution_plan_name = execution_plan_name

    @property
    def execution_plan_name(self):
        r"""Gets the execution_plan_name of this ExecutionPlanNamePrimitiveTypeHolder.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The execution_plan_name of this ExecutionPlanNamePrimitiveTypeHolder.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        r"""Sets the execution_plan_name of this ExecutionPlanNamePrimitiveTypeHolder.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param execution_plan_name: The execution_plan_name of this ExecutionPlanNamePrimitiveTypeHolder.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

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
        if not isinstance(other, ExecutionPlanNamePrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
