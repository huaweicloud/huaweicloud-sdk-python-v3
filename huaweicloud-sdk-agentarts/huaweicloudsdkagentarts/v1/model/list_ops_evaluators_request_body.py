# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'builtin': 'bool',
        'filter_option': 'EvaluationOpsFilterOption',
        'page_size': 'int',
        'page_number': 'int',
        'tag_key_exists': 'list[str]',
        'tag_key_matches': 'list[str]',
        'tag_value_matches': 'list[str]',
        'tag_match_policy': 'str'
    }

    attribute_map = {
        'builtin': 'builtin',
        'filter_option': 'filter_option',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'tag_key_exists': 'tag_key_exists',
        'tag_key_matches': 'tag_key_matches',
        'tag_value_matches': 'tag_value_matches',
        'tag_match_policy': 'tag_match_policy'
    }

    def __init__(self, builtin=None, filter_option=None, page_size=None, page_number=None, tag_key_exists=None, tag_key_matches=None, tag_value_matches=None, tag_match_policy=None):
        r"""ListOpsEvaluatorsRequestBody

        The model defined in huaweicloud sdk

        :param builtin: **参数解释：** 是否为系统预置评估器的过滤开关。 **约束限制：** 布尔值。 **取值范围：** - true: 仅查询预置评估器 - false: 仅查询用户自定义评估器 **默认取值：** 无（查询全部）。 
        :type builtin: bool
        :param filter_option: 
        :type filter_option: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsFilterOption`
        :param page_size: **参数解释：** 分页查询时每页返回的记录数量。 **约束限制：** 0到10000。 **取值范围：** 0到10000之间的整数。 **默认取值：** 10。 
        :type page_size: int
        :param page_number: **参数解释：** 分页查询的当前页码。 **约束限制：** 0到10000。 **取值范围：** 0到10000 之间的整数。 **默认取值：** 1。 
        :type page_number: int
        :param tag_key_exists: **参数解释：** 需要匹配的包含该标签名称的资源。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_key_exists: list[str]
        :param tag_key_matches: **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_key_matches: list[str]
        :param tag_value_matches: **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。数组元素为字符串类型，每个元素最大长度255。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_value_matches: list[str]
        :param tag_match_policy: **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。
        :type tag_match_policy: str
        """
        
        

        self._builtin = None
        self._filter_option = None
        self._page_size = None
        self._page_number = None
        self._tag_key_exists = None
        self._tag_key_matches = None
        self._tag_value_matches = None
        self._tag_match_policy = None
        self.discriminator = None

        if builtin is not None:
            self.builtin = builtin
        if filter_option is not None:
            self.filter_option = filter_option
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if tag_key_exists is not None:
            self.tag_key_exists = tag_key_exists
        if tag_key_matches is not None:
            self.tag_key_matches = tag_key_matches
        if tag_value_matches is not None:
            self.tag_value_matches = tag_value_matches
        if tag_match_policy is not None:
            self.tag_match_policy = tag_match_policy

    @property
    def builtin(self):
        r"""Gets the builtin of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 是否为系统预置评估器的过滤开关。 **约束限制：** 布尔值。 **取值范围：** - true: 仅查询预置评估器 - false: 仅查询用户自定义评估器 **默认取值：** 无（查询全部）。 

        :return: The builtin of this ListOpsEvaluatorsRequestBody.
        :rtype: bool
        """
        return self._builtin

    @builtin.setter
    def builtin(self, builtin):
        r"""Sets the builtin of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 是否为系统预置评估器的过滤开关。 **约束限制：** 布尔值。 **取值范围：** - true: 仅查询预置评估器 - false: 仅查询用户自定义评估器 **默认取值：** 无（查询全部）。 

        :param builtin: The builtin of this ListOpsEvaluatorsRequestBody.
        :type builtin: bool
        """
        self._builtin = builtin

    @property
    def filter_option(self):
        r"""Gets the filter_option of this ListOpsEvaluatorsRequestBody.

        :return: The filter_option of this ListOpsEvaluatorsRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsFilterOption`
        """
        return self._filter_option

    @filter_option.setter
    def filter_option(self, filter_option):
        r"""Sets the filter_option of this ListOpsEvaluatorsRequestBody.

        :param filter_option: The filter_option of this ListOpsEvaluatorsRequestBody.
        :type filter_option: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsFilterOption`
        """
        self._filter_option = filter_option

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 分页查询时每页返回的记录数量。 **约束限制：** 0到10000。 **取值范围：** 0到10000之间的整数。 **默认取值：** 10。 

        :return: The page_size of this ListOpsEvaluatorsRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 分页查询时每页返回的记录数量。 **约束限制：** 0到10000。 **取值范围：** 0到10000之间的整数。 **默认取值：** 10。 

        :param page_size: The page_size of this ListOpsEvaluatorsRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 分页查询的当前页码。 **约束限制：** 0到10000。 **取值范围：** 0到10000 之间的整数。 **默认取值：** 1。 

        :return: The page_number of this ListOpsEvaluatorsRequestBody.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 分页查询的当前页码。 **约束限制：** 0到10000。 **取值范围：** 0到10000 之间的整数。 **默认取值：** 1。 

        :param page_number: The page_number of this ListOpsEvaluatorsRequestBody.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def tag_key_exists(self):
        r"""Gets the tag_key_exists of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签名称的资源。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_key_exists of this ListOpsEvaluatorsRequestBody.
        :rtype: list[str]
        """
        return self._tag_key_exists

    @tag_key_exists.setter
    def tag_key_exists(self, tag_key_exists):
        r"""Sets the tag_key_exists of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签名称的资源。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** 数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_key_exists: The tag_key_exists of this ListOpsEvaluatorsRequestBody.
        :type tag_key_exists: list[str]
        """
        self._tag_key_exists = tag_key_exists

    @property
    def tag_key_matches(self):
        r"""Gets the tag_key_matches of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_key_matches of this ListOpsEvaluatorsRequestBody.
        :rtype: list[str]
        """
        return self._tag_key_matches

    @tag_key_matches.setter
    def tag_key_matches(self, tag_key_matches):
        r"""Sets the tag_key_matches of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用。数组元素为字符串类型，每个元素最大长度128。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为128个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_key_matches: The tag_key_matches of this ListOpsEvaluatorsRequestBody.
        :type tag_key_matches: list[str]
        """
        self._tag_key_matches = tag_key_matches

    @property
    def tag_value_matches(self):
        r"""Gets the tag_value_matches of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。数组元素为字符串类型，每个元素最大长度255。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_value_matches of this ListOpsEvaluatorsRequestBody.
        :rtype: list[str]
        """
        return self._tag_value_matches

    @tag_value_matches.setter
    def tag_value_matches(self, tag_value_matches):
        r"""Sets the tag_value_matches of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 需要匹配的包含该标签值的资源，需要和tag_key_matches条件配合使用。数组元素为字符串类型，每个元素最大长度255。 **约束限制：** tag_key_matches和tag_value_matches按索引位置配对。数组元素最小数量为0，最大数量为10，每个元素最大长度为255个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_value_matches: The tag_value_matches of this ListOpsEvaluatorsRequestBody.
        :type tag_value_matches: list[str]
        """
        self._tag_value_matches = tag_value_matches

    @property
    def tag_match_policy(self):
        r"""Gets the tag_match_policy of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。

        :return: The tag_match_policy of this ListOpsEvaluatorsRequestBody.
        :rtype: str
        """
        return self._tag_match_policy

    @tag_match_policy.setter
    def tag_match_policy(self, tag_match_policy):
        r"""Sets the tag_match_policy of this ListOpsEvaluatorsRequestBody.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists、tag_key_matches、tag_value_matches参数生效。 **约束限制：** 不涉及。 **取值范围：** - ALL：所有标签都必须匹配 - ANY：任意一个标签匹配即可 **默认取值：** ALL。

        :param tag_match_policy: The tag_match_policy of this ListOpsEvaluatorsRequestBody.
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
        if not isinstance(other, ListOpsEvaluatorsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
