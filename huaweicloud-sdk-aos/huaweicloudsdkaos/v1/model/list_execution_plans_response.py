# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecutionPlansResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_plans': 'list[ExecutionPlan]'
    }

    attribute_map = {
        'execution_plans': 'execution_plans'
    }

    def __init__(self, execution_plans=None):
        """ListExecutionPlansResponse

        The model defined in huaweicloud sdk

        :param execution_plans: 执行计划列表。默认按照生成时间降序排序，最新生成的在最前
        :type execution_plans: list[:class:`huaweicloudsdkaos.v1.ExecutionPlan`]
        """
        
        super(ListExecutionPlansResponse, self).__init__()

        self._execution_plans = None
        self.discriminator = None

        if execution_plans is not None:
            self.execution_plans = execution_plans

    @property
    def execution_plans(self):
        """Gets the execution_plans of this ListExecutionPlansResponse.

        执行计划列表。默认按照生成时间降序排序，最新生成的在最前

        :return: The execution_plans of this ListExecutionPlansResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ExecutionPlan`]
        """
        return self._execution_plans

    @execution_plans.setter
    def execution_plans(self, execution_plans):
        """Sets the execution_plans of this ListExecutionPlansResponse.

        执行计划列表。默认按照生成时间降序排序，最新生成的在最前

        :param execution_plans: The execution_plans of this ListExecutionPlansResponse.
        :type execution_plans: list[:class:`huaweicloudsdkaos.v1.ExecutionPlan`]
        """
        self._execution_plans = execution_plans

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
        if not isinstance(other, ListExecutionPlansResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
