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
        'limit': 'int',
        'tag_key_exists': 'list[str]',
        'tag_key_matches': 'list[str]',
        'tag_value_matches': 'list[str]',
        'tag_match_policy': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'tag_key_exists': 'tag_key_exists',
        'tag_key_matches': 'tag_key_matches',
        'tag_value_matches': 'tag_value_matches',
        'tag_match_policy': 'tag_match_policy'
    }

    def __init__(self, offset=None, limit=None, tag_key_exists=None, tag_key_matches=None, tag_value_matches=None, tag_match_policy=None):
        r"""ListOpsEvaluationTasksRequestBody

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 指定每次请求返回的偏移量，即从第几条数据开始查询。 **约束限制：** 1 到10000之间的整数。 **取值范围：** 1 到 10000。 **默认取值：** 1。 
        :type offset: int
        :param limit: **参数解释：** 指定每页返回的记录数量（页大小）。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 到100。 **默认取值：** 10。 
        :type limit: int
        :param tag_key_exists: **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_key_exists: list[str]
        :param tag_key_matches: **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_key_matches: list[str]
        :param tag_value_matches: **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_value_matches: list[str]
        :param tag_match_policy: **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。 
        :type tag_match_policy: str
        """
        
        

        self._offset = None
        self._limit = None
        self._tag_key_exists = None
        self._tag_key_matches = None
        self._tag_value_matches = None
        self._tag_match_policy = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if tag_key_exists is not None:
            self.tag_key_exists = tag_key_exists
        if tag_key_matches is not None:
            self.tag_key_matches = tag_key_matches
        if tag_value_matches is not None:
            self.tag_value_matches = tag_value_matches
        if tag_match_policy is not None:
            self.tag_match_policy = tag_match_policy

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

    @property
    def tag_key_exists(self):
        r"""Gets the tag_key_exists of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_key_exists of this ListOpsEvaluationTasksRequestBody.
        :rtype: list[str]
        """
        return self._tag_key_exists

    @tag_key_exists.setter
    def tag_key_exists(self, tag_key_exists):
        r"""Sets the tag_key_exists of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_key_exists: The tag_key_exists of this ListOpsEvaluationTasksRequestBody.
        :type tag_key_exists: list[str]
        """
        self._tag_key_exists = tag_key_exists

    @property
    def tag_key_matches(self):
        r"""Gets the tag_key_matches of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_key_matches of this ListOpsEvaluationTasksRequestBody.
        :rtype: list[str]
        """
        return self._tag_key_matches

    @tag_key_matches.setter
    def tag_key_matches(self, tag_key_matches):
        r"""Sets the tag_key_matches of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_key_matches: The tag_key_matches of this ListOpsEvaluationTasksRequestBody.
        :type tag_key_matches: list[str]
        """
        self._tag_key_matches = tag_key_matches

    @property
    def tag_value_matches(self):
        r"""Gets the tag_value_matches of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_value_matches of this ListOpsEvaluationTasksRequestBody.
        :rtype: list[str]
        """
        return self._tag_value_matches

    @tag_value_matches.setter
    def tag_value_matches(self, tag_value_matches):
        r"""Sets the tag_value_matches of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_value_matches: The tag_value_matches of this ListOpsEvaluationTasksRequestBody.
        :type tag_value_matches: list[str]
        """
        self._tag_value_matches = tag_value_matches

    @property
    def tag_match_policy(self):
        r"""Gets the tag_match_policy of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。 

        :return: The tag_match_policy of this ListOpsEvaluationTasksRequestBody.
        :rtype: str
        """
        return self._tag_match_policy

    @tag_match_policy.setter
    def tag_match_policy(self, tag_match_policy):
        r"""Sets the tag_match_policy of this ListOpsEvaluationTasksRequestBody.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。 

        :param tag_match_policy: The tag_match_policy of this ListOpsEvaluationTasksRequestBody.
        :type tag_match_policy: str
        """
        self._tag_match_policy = tag_match_policy

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
