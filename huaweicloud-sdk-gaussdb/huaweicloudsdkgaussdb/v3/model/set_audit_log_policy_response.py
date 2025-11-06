# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAuditLogPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'job_id': 'job_id'
    }

    def __init__(self, result=None, job_id=None):
        r"""SetAuditLogPolicyResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释**：  设置审计日志策略的操作结果。  **取值范围**：  COMPLETED|FAILED。
        :type result: str
        :param job_id: **参数解释**：  任务流id。  **取值范围**：  不涉及。
        :type job_id: str
        """
        
        super().__init__()

        self._result = None
        self._job_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if job_id is not None:
            self.job_id = job_id

    @property
    def result(self):
        r"""Gets the result of this SetAuditLogPolicyResponse.

        **参数解释**：  设置审计日志策略的操作结果。  **取值范围**：  COMPLETED|FAILED。

        :return: The result of this SetAuditLogPolicyResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this SetAuditLogPolicyResponse.

        **参数解释**：  设置审计日志策略的操作结果。  **取值范围**：  COMPLETED|FAILED。

        :param result: The result of this SetAuditLogPolicyResponse.
        :type result: str
        """
        self._result = result

    @property
    def job_id(self):
        r"""Gets the job_id of this SetAuditLogPolicyResponse.

        **参数解释**：  任务流id。  **取值范围**：  不涉及。

        :return: The job_id of this SetAuditLogPolicyResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SetAuditLogPolicyResponse.

        **参数解释**：  任务流id。  **取值范围**：  不涉及。

        :param job_id: The job_id of this SetAuditLogPolicyResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("SetAuditLogPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SetAuditLogPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
