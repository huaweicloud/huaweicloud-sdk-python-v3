# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlExecutionPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_plans': 'list[ExecutionPlan]',
        'error_message': 'str'
    }

    attribute_map = {
        'execution_plans': 'execution_plans',
        'error_message': 'error_message'
    }

    def __init__(self, execution_plans=None, error_message=None):
        """ShowSqlExecutionPlanResponse

        The model defined in huaweicloud sdk

        :param execution_plans: SQL执行计划列表
        :type execution_plans: list[:class:`huaweicloudsdkdas.v3.ExecutionPlan`]
        :param error_message: SQL执行失败时，显示执行错误信息
        :type error_message: str
        """
        
        super(ShowSqlExecutionPlanResponse, self).__init__()

        self._execution_plans = None
        self._error_message = None
        self.discriminator = None

        if execution_plans is not None:
            self.execution_plans = execution_plans
        if error_message is not None:
            self.error_message = error_message

    @property
    def execution_plans(self):
        """Gets the execution_plans of this ShowSqlExecutionPlanResponse.

        SQL执行计划列表

        :return: The execution_plans of this ShowSqlExecutionPlanResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ExecutionPlan`]
        """
        return self._execution_plans

    @execution_plans.setter
    def execution_plans(self, execution_plans):
        """Sets the execution_plans of this ShowSqlExecutionPlanResponse.

        SQL执行计划列表

        :param execution_plans: The execution_plans of this ShowSqlExecutionPlanResponse.
        :type execution_plans: list[:class:`huaweicloudsdkdas.v3.ExecutionPlan`]
        """
        self._execution_plans = execution_plans

    @property
    def error_message(self):
        """Gets the error_message of this ShowSqlExecutionPlanResponse.

        SQL执行失败时，显示执行错误信息

        :return: The error_message of this ShowSqlExecutionPlanResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ShowSqlExecutionPlanResponse.

        SQL执行失败时，显示执行错误信息

        :param error_message: The error_message of this ShowSqlExecutionPlanResponse.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ShowSqlExecutionPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
