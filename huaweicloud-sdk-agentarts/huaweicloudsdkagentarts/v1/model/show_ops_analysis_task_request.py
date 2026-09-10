# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAnalysisTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'analysis_task_id': 'str'
    }

    attribute_map = {
        'analysis_task_id': 'analysis_task_id'
    }

    def __init__(self, analysis_task_id=None):
        r"""ShowOpsAnalysisTaskRequest

        The model defined in huaweicloud sdk

        :param analysis_task_id: **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type analysis_task_id: str
        """
        
        

        self._analysis_task_id = None
        self.discriminator = None

        self.analysis_task_id = analysis_task_id

    @property
    def analysis_task_id(self):
        r"""Gets the analysis_task_id of this ShowOpsAnalysisTaskRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The analysis_task_id of this ShowOpsAnalysisTaskRequest.
        :rtype: str
        """
        return self._analysis_task_id

    @analysis_task_id.setter
    def analysis_task_id(self, analysis_task_id):
        r"""Sets the analysis_task_id of this ShowOpsAnalysisTaskRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param analysis_task_id: The analysis_task_id of this ShowOpsAnalysisTaskRequest.
        :type analysis_task_id: str
        """
        self._analysis_task_id = analysis_task_id

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
        if not isinstance(other, ShowOpsAnalysisTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
