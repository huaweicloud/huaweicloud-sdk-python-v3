# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAnalysisTaskInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'analysis_task_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'analysis_task_id': 'analysis_task_id'
    }

    def __init__(self, offset=None, limit=None, status=None, analysis_task_id=None):
        r"""ListOpsAnalysisTaskInstancesRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。
        :type limit: int
        :param status: **参数解释：** 任务状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。  **默认取值：** 无
        :type status: str
        :param analysis_task_id: **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type analysis_task_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._analysis_task_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        self.analysis_task_id = analysis_task_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListOpsAnalysisTaskInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsAnalysisTaskInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :return: The limit of this ListOpsAnalysisTaskInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :param limit: The limit of this ListOpsAnalysisTaskInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 任务状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。  **默认取值：** 无

        :return: The status of this ListOpsAnalysisTaskInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 任务状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。  **默认取值：** 无

        :param status: The status of this ListOpsAnalysisTaskInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def analysis_task_id(self):
        r"""Gets the analysis_task_id of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The analysis_task_id of this ListOpsAnalysisTaskInstancesRequest.
        :rtype: str
        """
        return self._analysis_task_id

    @analysis_task_id.setter
    def analysis_task_id(self, analysis_task_id):
        r"""Sets the analysis_task_id of this ListOpsAnalysisTaskInstancesRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param analysis_task_id: The analysis_task_id of this ListOpsAnalysisTaskInstancesRequest.
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
        if not isinstance(other, ListOpsAnalysisTaskInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
