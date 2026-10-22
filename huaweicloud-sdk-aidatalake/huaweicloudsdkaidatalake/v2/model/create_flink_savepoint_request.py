# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSavepointRequest:

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
        'job_id': 'str',
        'body': 'CreateFlinkSavepointRequestBody'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'job_id': 'job_id',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, job_id=None, body=None):
        r"""CreateFlinkSavepointRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type workspace_id: str
        :param job_id: **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。
        :type job_id: str
        :param body: Body of the CreateFlinkSavepointRequest
        :type body: :class:`huaweicloudsdkaidatalake.v2.CreateFlinkSavepointRequestBody`
        """
        
        

        self._workspace_id = None
        self._job_id = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.job_id = job_id
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateFlinkSavepointRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The workspace_id of this CreateFlinkSavepointRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateFlinkSavepointRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this CreateFlinkSavepointRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateFlinkSavepointRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :return: The job_id of this CreateFlinkSavepointRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateFlinkSavepointRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :param job_id: The job_id of this CreateFlinkSavepointRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def body(self):
        r"""Gets the body of this CreateFlinkSavepointRequest.

        :return: The body of this CreateFlinkSavepointRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateFlinkSavepointRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateFlinkSavepointRequest.

        :param body: The body of this CreateFlinkSavepointRequest.
        :type body: :class:`huaweicloudsdkaidatalake.v2.CreateFlinkSavepointRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateFlinkSavepointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
