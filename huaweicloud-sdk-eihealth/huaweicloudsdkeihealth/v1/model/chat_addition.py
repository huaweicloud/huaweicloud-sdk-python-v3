# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatAddition:

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
        'tool_type': 'ToolType',
        'job_type': 'str',
        'data_path': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'job_id': 'job_id',
        'tool_type': 'tool_type',
        'job_type': 'job_type',
        'data_path': 'data_path'
    }

    def __init__(self, workspace_id=None, job_id=None, tool_type=None, job_type=None, data_path=None):
        r"""ChatAddition

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**： 实验问答使用的空间ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type workspace_id: str
        :param job_id: **参数解释**： 实验问答的作业ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type job_id: str
        :param tool_type: 
        :type tool_type: :class:`huaweicloudsdkeihealth.v1.ToolType`
        :param job_type: **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type job_type: str
        :param data_path: **参数解释**： 深度探究生成报告存储路径。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type data_path: str
        """
        
        

        self._workspace_id = None
        self._job_id = None
        self._tool_type = None
        self._job_type = None
        self._data_path = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if job_id is not None:
            self.job_id = job_id
        if tool_type is not None:
            self.tool_type = tool_type
        if job_type is not None:
            self.job_type = job_type
        if data_path is not None:
            self.data_path = data_path

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ChatAddition.

        **参数解释**： 实验问答使用的空间ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The workspace_id of this ChatAddition.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ChatAddition.

        **参数解释**： 实验问答使用的空间ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param workspace_id: The workspace_id of this ChatAddition.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ChatAddition.

        **参数解释**： 实验问答的作业ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The job_id of this ChatAddition.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ChatAddition.

        **参数解释**： 实验问答的作业ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param job_id: The job_id of this ChatAddition.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def tool_type(self):
        r"""Gets the tool_type of this ChatAddition.

        :return: The tool_type of this ChatAddition.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ToolType`
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        r"""Sets the tool_type of this ChatAddition.

        :param tool_type: The tool_type of this ChatAddition.
        :type tool_type: :class:`huaweicloudsdkeihealth.v1.ToolType`
        """
        self._tool_type = tool_type

    @property
    def job_type(self):
        r"""Gets the job_type of this ChatAddition.

        **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The job_type of this ChatAddition.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ChatAddition.

        **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param job_type: The job_type of this ChatAddition.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def data_path(self):
        r"""Gets the data_path of this ChatAddition.

        **参数解释**： 深度探究生成报告存储路径。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The data_path of this ChatAddition.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        r"""Sets the data_path of this ChatAddition.

        **参数解释**： 深度探究生成报告存储路径。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param data_path: The data_path of this ChatAddition.
        :type data_path: str
        """
        self._data_path = data_path

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
        if not isinstance(other, ChatAddition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
