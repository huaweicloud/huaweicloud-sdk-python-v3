# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFlinkSavepointRequest:

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
        'savepoint_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'job_id': 'job_id',
        'savepoint_id': 'savepoint_id'
    }

    def __init__(self, workspace_id=None, job_id=None, savepoint_id=None):
        r"""DeleteFlinkSavepointRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type workspace_id: str
        :param job_id: **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。
        :type job_id: str
        :param savepoint_id: **参数解释**：Savepoint唯一标识，用于唯一标识一个Flink快照，可通过[查询Flink作业Savepoint列表](ListFlinkSavepoint.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。
        :type savepoint_id: str
        """
        
        

        self._workspace_id = None
        self._job_id = None
        self._savepoint_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.job_id = job_id
        self.savepoint_id = savepoint_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteFlinkSavepointRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The workspace_id of this DeleteFlinkSavepointRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteFlinkSavepointRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this DeleteFlinkSavepointRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this DeleteFlinkSavepointRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :return: The job_id of this DeleteFlinkSavepointRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DeleteFlinkSavepointRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :param job_id: The job_id of this DeleteFlinkSavepointRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def savepoint_id(self):
        r"""Gets the savepoint_id of this DeleteFlinkSavepointRequest.

        **参数解释**：Savepoint唯一标识，用于唯一标识一个Flink快照，可通过[查询Flink作业Savepoint列表](ListFlinkSavepoint.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :return: The savepoint_id of this DeleteFlinkSavepointRequest.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        r"""Sets the savepoint_id of this DeleteFlinkSavepointRequest.

        **参数解释**：Savepoint唯一标识，用于唯一标识一个Flink快照，可通过[查询Flink作业Savepoint列表](ListFlinkSavepoint.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :param savepoint_id: The savepoint_id of this DeleteFlinkSavepointRequest.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

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
        if not isinstance(other, DeleteFlinkSavepointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
