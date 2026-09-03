# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateTrainingJobNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, job_name=None, workspace_id=None):
        r"""ValidateTrainingJobNameRequest

        The model defined in huaweicloud sdk

        :param job_name: **参数解释**：训练作业名称。 **约束限制**：1 - 64字符，字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_name: str
        :param workspace_id: **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。
        :type workspace_id: str
        """
        
        

        self._job_name = None
        self._workspace_id = None
        self.discriminator = None

        self.job_name = job_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ValidateTrainingJobNameRequest.

        **参数解释**：训练作业名称。 **约束限制**：1 - 64字符，字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_name of this ValidateTrainingJobNameRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ValidateTrainingJobNameRequest.

        **参数解释**：训练作业名称。 **约束限制**：1 - 64字符，字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_name: The job_name of this ValidateTrainingJobNameRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ValidateTrainingJobNameRequest.

        **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The workspace_id of this ValidateTrainingJobNameRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ValidateTrainingJobNameRequest.

        **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ValidateTrainingJobNameRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ValidateTrainingJobNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
