# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluationTasksRequestBody:

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
        'limit': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, offset=None, limit=None):
        r"""ListOpsEvaluationTasksRequestBody

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 指定每次请求返回的偏移量，即从第几条数据开始查询。 **约束限制：** 1 到10000之间的整数。 **取值范围：** 1 到 10000。 **默认取值：** 1。 
        :type offset: int
        :param limit: **参数解释：** 指定每页返回的记录数量（页大小）。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 到100。 **默认取值：** 10。 
        :type limit: int
        """
        
        

        self._offset = None
        self._limit = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 指定每次请求返回的偏移量，即从第几条数据开始查询。 **约束限制：** 1 到10000之间的整数。 **取值范围：** 1 到 10000。 **默认取值：** 1。 

        :return: The offset of this ListOpsEvaluationTasksRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 指定每次请求返回的偏移量，即从第几条数据开始查询。 **约束限制：** 1 到10000之间的整数。 **取值范围：** 1 到 10000。 **默认取值：** 1。 

        :param offset: The offset of this ListOpsEvaluationTasksRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 指定每页返回的记录数量（页大小）。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 到100。 **默认取值：** 10。 

        :return: The limit of this ListOpsEvaluationTasksRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 指定每页返回的记录数量（页大小）。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 到100。 **默认取值：** 10。 

        :param limit: The limit of this ListOpsEvaluationTasksRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListOpsEvaluationTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
