# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'tag_key_exists': 'str',
        'tag_key_matches': 'str',
        'tag_value_matches': 'str',
        'tag_match_policy': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'tag_key_exists': 'tag_key_exists',
        'tag_key_matches': 'tag_key_matches',
        'tag_value_matches': 'tag_value_matches',
        'tag_match_policy': 'tag_match_policy'
    }

    def __init__(self, limit=None, offset=None, tag_key_exists=None, tag_key_matches=None, tag_value_matches=None, tag_match_policy=None):
        r"""ListCoreSpacesRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 
        :type limit: int
        :param offset: **参数解释：** 查询游标，即偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param tag_key_exists: **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists&#x3D;env&amp;tag_key_exists&#x3D;team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_key_exists: str
        :param tag_key_matches: **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches&#x3D;env&amp;tag_key_matches&#x3D;team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_key_matches: str
        :param tag_value_matches: **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串,  如：tag_key_matches&#x3D;env&amp;tag_value_matches&#x3D;prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_value_matches: str
        :param tag_match_policy: **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： 长度为1-3个字符。允许的值为： - ALL - ANY **默认取值**: ALL
        :type tag_match_policy: str
        """
        
        

        self._limit = None
        self._offset = None
        self._tag_key_exists = None
        self._tag_key_matches = None
        self._tag_value_matches = None
        self._tag_match_policy = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tag_key_exists is not None:
            self.tag_key_exists = tag_key_exists
        if tag_key_matches is not None:
            self.tag_key_matches = tag_key_matches
        if tag_value_matches is not None:
            self.tag_value_matches = tag_value_matches
        if tag_match_policy is not None:
            self.tag_match_policy = tag_match_policy

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreSpacesRequest.

        **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 

        :return: The limit of this ListCoreSpacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreSpacesRequest.

        **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 

        :param limit: The limit of this ListCoreSpacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreSpacesRequest.

        **参数解释：** 查询游标，即偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListCoreSpacesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreSpacesRequest.

        **参数解释：** 查询游标，即偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListCoreSpacesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def tag_key_exists(self):
        r"""Gets the tag_key_exists of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists=env&tag_key_exists=team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_key_exists of this ListCoreSpacesRequest.
        :rtype: str
        """
        return self._tag_key_exists

    @tag_key_exists.setter
    def tag_key_exists(self, tag_key_exists):
        r"""Sets the tag_key_exists of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists=env&tag_key_exists=team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_key_exists: The tag_key_exists of this ListCoreSpacesRequest.
        :type tag_key_exists: str
        """
        self._tag_key_exists = tag_key_exists

    @property
    def tag_key_matches(self):
        r"""Gets the tag_key_matches of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_key_matches=team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_key_matches of this ListCoreSpacesRequest.
        :rtype: str
        """
        return self._tag_key_matches

    @tag_key_matches.setter
    def tag_key_matches(self, tag_key_matches):
        r"""Sets the tag_key_matches of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_key_matches=team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_key_matches: The tag_key_matches of this ListCoreSpacesRequest.
        :type tag_key_matches: str
        """
        self._tag_key_matches = tag_key_matches

    @property
    def tag_value_matches(self):
        r"""Gets the tag_value_matches of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串,  如：tag_key_matches=env&tag_value_matches=prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_value_matches of this ListCoreSpacesRequest.
        :rtype: str
        """
        return self._tag_value_matches

    @tag_value_matches.setter
    def tag_value_matches(self, tag_value_matches):
        r"""Sets the tag_value_matches of this ListCoreSpacesRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串,  如：tag_key_matches=env&tag_value_matches=prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_value_matches: The tag_value_matches of this ListCoreSpacesRequest.
        :type tag_value_matches: str
        """
        self._tag_value_matches = tag_value_matches

    @property
    def tag_match_policy(self):
        r"""Gets the tag_match_policy of this ListCoreSpacesRequest.

        **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： 长度为1-3个字符。允许的值为： - ALL - ANY **默认取值**: ALL

        :return: The tag_match_policy of this ListCoreSpacesRequest.
        :rtype: str
        """
        return self._tag_match_policy

    @tag_match_policy.setter
    def tag_match_policy(self, tag_match_policy):
        r"""Sets the tag_match_policy of this ListCoreSpacesRequest.

        **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： 长度为1-3个字符。允许的值为： - ALL - ANY **默认取值**: ALL

        :param tag_match_policy: The tag_match_policy of this ListCoreSpacesRequest.
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
        if not isinstance(other, ListCoreSpacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
