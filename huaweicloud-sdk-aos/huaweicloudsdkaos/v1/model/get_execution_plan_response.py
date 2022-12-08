# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetExecutionPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_plan_items': 'list[ExecutionPlanItem]'
    }

    attribute_map = {
        'execution_plan_items': 'execution_plan_items'
    }

    def __init__(self, execution_plan_items=None):
        """GetExecutionPlanResponse

        The model defined in huaweicloud sdk

        :param execution_plan_items: 执行计划元素的列表，只有当状态为&#39;AVAILABLE&#39;、&#39;APPLIED&#39;、’APPLY_IN_PROGRESS‘等完成创建后的状态才会被赋值，而&#39;CREATION_IN_PROGRESS&#39;或&#39;CREATION_FAILED&#39;会返回错误。
        :type execution_plan_items: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanItem`]
        """
        
        super(GetExecutionPlanResponse, self).__init__()

        self._execution_plan_items = None
        self.discriminator = None

        if execution_plan_items is not None:
            self.execution_plan_items = execution_plan_items

    @property
    def execution_plan_items(self):
        """Gets the execution_plan_items of this GetExecutionPlanResponse.

        执行计划元素的列表，只有当状态为'AVAILABLE'、'APPLIED'、’APPLY_IN_PROGRESS‘等完成创建后的状态才会被赋值，而'CREATION_IN_PROGRESS'或'CREATION_FAILED'会返回错误。

        :return: The execution_plan_items of this GetExecutionPlanResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanItem`]
        """
        return self._execution_plan_items

    @execution_plan_items.setter
    def execution_plan_items(self, execution_plan_items):
        """Sets the execution_plan_items of this GetExecutionPlanResponse.

        执行计划元素的列表，只有当状态为'AVAILABLE'、'APPLIED'、’APPLY_IN_PROGRESS‘等完成创建后的状态才会被赋值，而'CREATION_IN_PROGRESS'或'CREATION_FAILED'会返回错误。

        :param execution_plan_items: The execution_plan_items of this GetExecutionPlanResponse.
        :type execution_plan_items: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanItem`]
        """
        self._execution_plan_items = execution_plan_items

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
        if not isinstance(other, GetExecutionPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
