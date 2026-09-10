# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAnalysisTaskFailureAffectedSessionsRequest:

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
        'analysis_task_id': 'str',
        'error_sub_category_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'analysis_task_id': 'analysis_task_id',
        'error_sub_category_name': 'error_sub_category_name'
    }

    def __init__(self, offset=None, limit=None, analysis_task_id=None, error_sub_category_name=None):
        r"""ListOpsAnalysisTaskFailureAffectedSessionsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。
        :type limit: int
        :param analysis_task_id: **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type analysis_task_id: str
        :param error_sub_category_name: 
        :type error_sub_category_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._analysis_task_id = None
        self._error_sub_category_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.analysis_task_id = analysis_task_id
        self.error_sub_category_name = error_sub_category_name

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :return: The limit of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :param limit: The limit of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def analysis_task_id(self):
        r"""Gets the analysis_task_id of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The analysis_task_id of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :rtype: str
        """
        return self._analysis_task_id

    @analysis_task_id.setter
    def analysis_task_id(self, analysis_task_id):
        r"""Sets the analysis_task_id of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        **参数解释：** 分析任务ID，标识任务的唯一标识符。获取方法请参考查询分析任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param analysis_task_id: The analysis_task_id of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :type analysis_task_id: str
        """
        self._analysis_task_id = analysis_task_id

    @property
    def error_sub_category_name(self):
        r"""Gets the error_sub_category_name of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        :return: The error_sub_category_name of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :rtype: str
        """
        return self._error_sub_category_name

    @error_sub_category_name.setter
    def error_sub_category_name(self, error_sub_category_name):
        r"""Sets the error_sub_category_name of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.

        :param error_sub_category_name: The error_sub_category_name of this ListOpsAnalysisTaskFailureAffectedSessionsRequest.
        :type error_sub_category_name: str
        """
        self._error_sub_category_name = error_sub_category_name

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
        if not isinstance(other, ListOpsAnalysisTaskFailureAffectedSessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
