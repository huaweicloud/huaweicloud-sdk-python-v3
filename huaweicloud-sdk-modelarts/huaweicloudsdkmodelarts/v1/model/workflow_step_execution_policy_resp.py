# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowStepExecutionPolicyResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_policy': 'str',
        'use_cache': 'bool'
    }

    attribute_map = {
        'execution_policy': 'execution_policy',
        'use_cache': 'use_cache'
    }

    def __init__(self, execution_policy=None, use_cache=None):
        r"""WorkflowStepExecutionPolicyResp

        The model defined in huaweicloud sdk

        :param execution_policy: **参数解释**：执行策略， **取值范围**：可选值如下： - retry：重试 - stop：停止 - continue：继续运行
        :type execution_policy: str
        :param use_cache: **参数解释**：是否使用的是缓存。 **取值范围**： - true：是缓存 - false：不是缓存
        :type use_cache: bool
        """
        
        

        self._execution_policy = None
        self._use_cache = None
        self.discriminator = None

        if execution_policy is not None:
            self.execution_policy = execution_policy
        if use_cache is not None:
            self.use_cache = use_cache

    @property
    def execution_policy(self):
        r"""Gets the execution_policy of this WorkflowStepExecutionPolicyResp.

        **参数解释**：执行策略， **取值范围**：可选值如下： - retry：重试 - stop：停止 - continue：继续运行

        :return: The execution_policy of this WorkflowStepExecutionPolicyResp.
        :rtype: str
        """
        return self._execution_policy

    @execution_policy.setter
    def execution_policy(self, execution_policy):
        r"""Sets the execution_policy of this WorkflowStepExecutionPolicyResp.

        **参数解释**：执行策略， **取值范围**：可选值如下： - retry：重试 - stop：停止 - continue：继续运行

        :param execution_policy: The execution_policy of this WorkflowStepExecutionPolicyResp.
        :type execution_policy: str
        """
        self._execution_policy = execution_policy

    @property
    def use_cache(self):
        r"""Gets the use_cache of this WorkflowStepExecutionPolicyResp.

        **参数解释**：是否使用的是缓存。 **取值范围**： - true：是缓存 - false：不是缓存

        :return: The use_cache of this WorkflowStepExecutionPolicyResp.
        :rtype: bool
        """
        return self._use_cache

    @use_cache.setter
    def use_cache(self, use_cache):
        r"""Sets the use_cache of this WorkflowStepExecutionPolicyResp.

        **参数解释**：是否使用的是缓存。 **取值范围**： - true：是缓存 - false：不是缓存

        :param use_cache: The use_cache of this WorkflowStepExecutionPolicyResp.
        :type use_cache: bool
        """
        self._use_cache = use_cache

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowStepExecutionPolicyResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
