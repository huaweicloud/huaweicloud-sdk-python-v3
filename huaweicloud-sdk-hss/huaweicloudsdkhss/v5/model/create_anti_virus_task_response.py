# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiVirusTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'policy_id': 'str',
        'result': 'bool',
        'fail_reasons': 'list[FailReasons]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'policy_id': 'policy_id',
        'result': 'result',
        'fail_reasons': 'fail_reasons'
    }

    def __init__(self, task_id=None, policy_id=None, result=None, fail_reasons=None):
        r"""CreateAntiVirusTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**： 任务ID **取值范围**: 字符长度1-64位 
        :type task_id: str
        :param policy_id: **参数解释**: 策略ID **取值范围**: 字符长度1-64位 
        :type policy_id: str
        :param result: **参数解释** 是否全部成功 **取值范围** true: 是 false: 否 
        :type result: bool
        :param fail_reasons: **参数解释** 主机结果列表 **取值范围** 不涉及 
        :type fail_reasons: list[:class:`huaweicloudsdkhss.v5.FailReasons`]
        """
        
        super().__init__()

        self._task_id = None
        self._policy_id = None
        self._result = None
        self._fail_reasons = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if policy_id is not None:
            self.policy_id = policy_id
        if result is not None:
            self.result = result
        if fail_reasons is not None:
            self.fail_reasons = fail_reasons

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateAntiVirusTaskResponse.

        **参数解释**： 任务ID **取值范围**: 字符长度1-64位 

        :return: The task_id of this CreateAntiVirusTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateAntiVirusTaskResponse.

        **参数解释**： 任务ID **取值范围**: 字符长度1-64位 

        :param task_id: The task_id of this CreateAntiVirusTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateAntiVirusTaskResponse.

        **参数解释**: 策略ID **取值范围**: 字符长度1-64位 

        :return: The policy_id of this CreateAntiVirusTaskResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateAntiVirusTaskResponse.

        **参数解释**: 策略ID **取值范围**: 字符长度1-64位 

        :param policy_id: The policy_id of this CreateAntiVirusTaskResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def result(self):
        r"""Gets the result of this CreateAntiVirusTaskResponse.

        **参数解释** 是否全部成功 **取值范围** true: 是 false: 否 

        :return: The result of this CreateAntiVirusTaskResponse.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CreateAntiVirusTaskResponse.

        **参数解释** 是否全部成功 **取值范围** true: 是 false: 否 

        :param result: The result of this CreateAntiVirusTaskResponse.
        :type result: bool
        """
        self._result = result

    @property
    def fail_reasons(self):
        r"""Gets the fail_reasons of this CreateAntiVirusTaskResponse.

        **参数解释** 主机结果列表 **取值范围** 不涉及 

        :return: The fail_reasons of this CreateAntiVirusTaskResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.FailReasons`]
        """
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, fail_reasons):
        r"""Sets the fail_reasons of this CreateAntiVirusTaskResponse.

        **参数解释** 主机结果列表 **取值范围** 不涉及 

        :param fail_reasons: The fail_reasons of this CreateAntiVirusTaskResponse.
        :type fail_reasons: list[:class:`huaweicloudsdkhss.v5.FailReasons`]
        """
        self._fail_reasons = fail_reasons

    def to_dict(self):
        import warnings
        warnings.warn("CreateAntiVirusTaskResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateAntiVirusTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
