# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluationTaskResultsRequestBody:

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
        'filters': 'object'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'filters': 'filters'
    }

    def __init__(self, offset=None, limit=None, filters=None):
        r"""ListOpsEvaluationTaskResultsRequestBody

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 指定分页查询的起始偏移量。 **约束限制：** 1到10000之间的整数。 **取值范围：** 1到10000。 **默认取值：** 1。 
        :type offset: int
        :param limit: **参数解释：** 指定单页返回的结果数量。 **约束限制：** 1到100之间的整数。 **取值范围：** 1到100。 **默认取值：** 10。 
        :type limit: int
        :param filters: **参数解释：** 任务过滤条件对象，支持模糊查询，用于精准筛选评估结果。 **约束限制：** 符合业务逻辑的JSON对象。 **取值范围：** 不涉及。 **默认取值：** 空对象。 
        :type filters: object
        """
        
        

        self._offset = None
        self._limit = None
        self._filters = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if filters is not None:
            self.filters = filters

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 指定分页查询的起始偏移量。 **约束限制：** 1到10000之间的整数。 **取值范围：** 1到10000。 **默认取值：** 1。 

        :return: The offset of this ListOpsEvaluationTaskResultsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 指定分页查询的起始偏移量。 **约束限制：** 1到10000之间的整数。 **取值范围：** 1到10000。 **默认取值：** 1。 

        :param offset: The offset of this ListOpsEvaluationTaskResultsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 指定单页返回的结果数量。 **约束限制：** 1到100之间的整数。 **取值范围：** 1到100。 **默认取值：** 10。 

        :return: The limit of this ListOpsEvaluationTaskResultsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 指定单页返回的结果数量。 **约束限制：** 1到100之间的整数。 **取值范围：** 1到100。 **默认取值：** 10。 

        :param limit: The limit of this ListOpsEvaluationTaskResultsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def filters(self):
        r"""Gets the filters of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 任务过滤条件对象，支持模糊查询，用于精准筛选评估结果。 **约束限制：** 符合业务逻辑的JSON对象。 **取值范围：** 不涉及。 **默认取值：** 空对象。 

        :return: The filters of this ListOpsEvaluationTaskResultsRequestBody.
        :rtype: object
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ListOpsEvaluationTaskResultsRequestBody.

        **参数解释：** 任务过滤条件对象，支持模糊查询，用于精准筛选评估结果。 **约束限制：** 符合业务逻辑的JSON对象。 **取值范围：** 不涉及。 **默认取值：** 空对象。 

        :param filters: The filters of this ListOpsEvaluationTaskResultsRequestBody.
        :type filters: object
        """
        self._filters = filters

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
        if not isinstance(other, ListOpsEvaluationTaskResultsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
