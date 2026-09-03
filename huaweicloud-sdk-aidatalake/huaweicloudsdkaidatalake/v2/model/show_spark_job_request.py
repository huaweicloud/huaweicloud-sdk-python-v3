# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'job_id': 'job_id'
    }

    def __init__(self, workspace_id=None, job_id=None):
        r"""ShowSparkJobRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param job_id: **参数解释**：Spark作业ID，用于唯一标识作业。 **约束限制**：不涉及。 **取值范围**：只能由英文字母、数字、下划线和中划线组成，且长度为1~64个字符。 **默认取值**：不涉及。 
        :type job_id: str
        """
        
        

        self._workspace_id = None
        self._job_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.job_id = job_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowSparkJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ShowSparkJobRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowSparkJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ShowSparkJobRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowSparkJobRequest.

        **参数解释**：Spark作业ID，用于唯一标识作业。 **约束限制**：不涉及。 **取值范围**：只能由英文字母、数字、下划线和中划线组成，且长度为1~64个字符。 **默认取值**：不涉及。 

        :return: The job_id of this ShowSparkJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowSparkJobRequest.

        **参数解释**：Spark作业ID，用于唯一标识作业。 **约束限制**：不涉及。 **取值范围**：只能由英文字母、数字、下划线和中划线组成，且长度为1~64个字符。 **默认取值**：不涉及。 

        :param job_id: The job_id of this ShowSparkJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowSparkJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
