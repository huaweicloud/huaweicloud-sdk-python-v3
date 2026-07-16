# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreRuntimeEndpointsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'tag_key_exists': 'str',
        'tag_key_matches': 'str',
        'tag_value_matches': 'str',
        'tag_match_policy': 'str'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'offset': 'offset',
        'limit': 'limit',
        'tag_key_exists': 'tag_key_exists',
        'tag_key_matches': 'tag_key_matches',
        'tag_value_matches': 'tag_value_matches',
        'tag_match_policy': 'tag_match_policy'
    }

    def __init__(self, runtime_id=None, offset=None, limit=None, tag_key_exists=None, tag_key_matches=None, tag_value_matches=None, tag_match_policy=None):
        r"""ListCoreRuntimeEndpointsRequest

        The model defined in huaweicloud sdk

        :param runtime_id: 运行时ID，用于唯一标识一个Agent运行时实例。
        :type runtime_id: str
        :param offset: **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1
        :type offset: int
        :param limit: **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10
        :type limit: int
        :param tag_key_exists: **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists&#x3D;env&amp;tag_key_exists&#x3D;team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_key_exists: str
        :param tag_key_matches: **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches&#x3D;env&amp;tag_key_matches&#x3D;team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_key_matches: str
        :param tag_value_matches: **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches&#x3D;env&amp;tag_value_matches&#x3D;prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。
        :type tag_value_matches: str
        :param tag_match_policy: **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： - ALL - ANY **默认取值**: ALL
        :type tag_match_policy: str
        """
        
        

        self._runtime_id = None
        self._offset = None
        self._limit = None
        self._tag_key_exists = None
        self._tag_key_matches = None
        self._tag_value_matches = None
        self._tag_match_policy = None
        self.discriminator = None

        self.runtime_id = runtime_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
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
    def runtime_id(self):
        r"""Gets the runtime_id of this ListCoreRuntimeEndpointsRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :return: The runtime_id of this ListCoreRuntimeEndpointsRequest.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ListCoreRuntimeEndpointsRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :param runtime_id: The runtime_id of this ListCoreRuntimeEndpointsRequest.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1

        :return: The offset of this ListCoreRuntimeEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1

        :param offset: The offset of this ListCoreRuntimeEndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10

        :return: The limit of this ListCoreRuntimeEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10

        :param limit: The limit of this ListCoreRuntimeEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def tag_key_exists(self):
        r"""Gets the tag_key_exists of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists=env&tag_key_exists=team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_key_exists of this ListCoreRuntimeEndpointsRequest.
        :rtype: str
        """
        return self._tag_key_exists

    @tag_key_exists.setter
    def tag_key_exists(self, tag_key_exists):
        r"""Sets the tag_key_exists of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签名称的资源, 多个值通过重复参数名传递，如：tag_key_exists=env&tag_key_exists=team。 **约束限制**: 支持批量查询多个标签名，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_key_exists: The tag_key_exists of this ListCoreRuntimeEndpointsRequest.
        :type tag_key_exists: str
        """
        self._tag_key_exists = tag_key_exists

    @property
    def tag_key_matches(self):
        r"""Gets the tag_key_matches of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_key_matches=team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_key_matches of this ListCoreRuntimeEndpointsRequest.
        :rtype: str
        """
        return self._tag_key_matches

    @tag_key_matches.setter
    def tag_key_matches(self, tag_key_matches):
        r"""Sets the tag_key_matches of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_key_matches=team。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_key_matches: The tag_key_matches of this ListCoreRuntimeEndpointsRequest.
        :type tag_key_matches: str
        """
        self._tag_key_matches = tag_key_matches

    @property
    def tag_value_matches(self):
        r"""Gets the tag_value_matches of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_value_matches=prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :return: The tag_value_matches of this ListCoreRuntimeEndpointsRequest.
        :rtype: str
        """
        return self._tag_value_matches

    @tag_value_matches.setter
    def tag_value_matches(self, tag_value_matches):
        r"""Sets the tag_value_matches of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串, 如：tag_key_matches=env&tag_value_matches=prod。 **约束限制**: 支持批量查询多个标签，最多支持10个标签。 **取值范围**： 最小数量 1，最大数量 10 **默认取值**: 不涉及。

        :param tag_value_matches: The tag_value_matches of this ListCoreRuntimeEndpointsRequest.
        :type tag_value_matches: str
        """
        self._tag_value_matches = tag_value_matches

    @property
    def tag_match_policy(self):
        r"""Gets the tag_match_policy of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： - ALL - ANY **默认取值**: ALL

        :return: The tag_match_policy of this ListCoreRuntimeEndpointsRequest.
        :rtype: str
        """
        return self._tag_match_policy

    @tag_match_policy.setter
    def tag_match_policy(self, tag_match_policy):
        r"""Sets the tag_match_policy of this ListCoreRuntimeEndpointsRequest.

        **参数解释**：  标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 **约束限制**: 不涉及。 **取值范围**： - ALL - ANY **默认取值**: ALL

        :param tag_match_policy: The tag_match_policy of this ListCoreRuntimeEndpointsRequest.
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
        if not isinstance(other, ListCoreRuntimeEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
