# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelProxiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'tag_key_exists': 'list[str]',
        'tag_key_matches': 'list[str]',
        'tag_value_matches': 'list[str]',
        'tag_match_policy': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'tag_key_exists': 'tag_key_exists',
        'tag_key_matches': 'tag_key_matches',
        'tag_value_matches': 'tag_value_matches',
        'tag_match_policy': 'tag_match_policy',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, name=None, id=None, tag_key_exists=None, tag_key_matches=None, tag_value_matches=None, tag_match_policy=None, limit=None, offset=None):
        r"""ListModelProxiesRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 按名称过滤模型代理，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为 2-40 个字符。 **默认取值：** 不涉及。 
        :type name: str
        :param id: **参数解释：** 按网关ID过滤，支持多个ID（最多支持20个ID）。 示例: id&#x3D;id1&amp;id&#x3D;id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type id: str
        :param tag_key_exists: **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 支持批量查询多个标签名，最多支持10个标签。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 
        :type tag_key_exists: list[str]
        :param tag_key_matches: **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 
        :type tag_key_matches: list[str]
        :param tag_value_matches: **参数解释：** 需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 
        :type tag_value_matches: list[str]
        :param tag_match_policy: **参数解释：** 标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的交集。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的并集。 **约束限制：** 不涉及。 **取值范围：** 允许的值为： - ALL - ANY **默认取值：** ALL 
        :type tag_match_policy: str
        :param limit: **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 
        :type offset: int
        """
        
        

        self._name = None
        self._id = None
        self._tag_key_exists = None
        self._tag_key_matches = None
        self._tag_value_matches = None
        self._tag_match_policy = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if tag_key_exists is not None:
            self.tag_key_exists = tag_key_exists
        if tag_key_matches is not None:
            self.tag_key_matches = tag_key_matches
        if tag_value_matches is not None:
            self.tag_value_matches = tag_value_matches
        if tag_match_policy is not None:
            self.tag_match_policy = tag_match_policy
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListModelProxiesRequest.

        **参数解释：** 按名称过滤模型代理，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为 2-40 个字符。 **默认取值：** 不涉及。 

        :return: The name of this ListModelProxiesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListModelProxiesRequest.

        **参数解释：** 按名称过滤模型代理，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 长度为 2-40 个字符。 **默认取值：** 不涉及。 

        :param name: The name of this ListModelProxiesRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListModelProxiesRequest.

        **参数解释：** 按网关ID过滤，支持多个ID（最多支持20个ID）。 示例: id=id1&id=id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The id of this ListModelProxiesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListModelProxiesRequest.

        **参数解释：** 按网关ID过滤，支持多个ID（最多支持20个ID）。 示例: id=id1&id=id2 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param id: The id of this ListModelProxiesRequest.
        :type id: str
        """
        self._id = id

    @property
    def tag_key_exists(self):
        r"""Gets the tag_key_exists of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 支持批量查询多个标签名，最多支持10个标签。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :return: The tag_key_exists of this ListModelProxiesRequest.
        :rtype: list[str]
        """
        return self._tag_key_exists

    @tag_key_exists.setter
    def tag_key_exists(self, tag_key_exists):
        r"""Sets the tag_key_exists of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签名称的资源。 **约束限制：** 支持批量查询多个标签名，最多支持10个标签。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :param tag_key_exists: The tag_key_exists of this ListModelProxiesRequest.
        :type tag_key_exists: list[str]
        """
        self._tag_key_exists = tag_key_exists

    @property
    def tag_key_matches(self):
        r"""Gets the tag_key_matches of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :return: The tag_key_matches of this ListModelProxiesRequest.
        :rtype: list[str]
        """
        return self._tag_key_matches

    @tag_key_matches.setter
    def tag_key_matches(self, tag_key_matches):
        r"""Sets the tag_key_matches of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_value_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，不支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :param tag_key_matches: The tag_key_matches of this ListModelProxiesRequest.
        :type tag_key_matches: list[str]
        """
        self._tag_key_matches = tag_key_matches

    @property
    def tag_value_matches(self):
        r"""Gets the tag_value_matches of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :return: The tag_value_matches of this ListModelProxiesRequest.
        :rtype: list[str]
        """
        return self._tag_value_matches

    @tag_value_matches.setter
    def tag_value_matches(self, tag_value_matches):
        r"""Sets the tag_value_matches of this ListModelProxiesRequest.

        **参数解释：** 需要匹配的包含该标签的资源，需要和tag_key_matches条件配合使用，tag_key_matches和tag_value_matches的元素个数需要一致，且标签顺序需要完全匹配，支持空字符串。 **约束限制：** 支持批量查询多个标签，最多支持10个标签。tag_key_matches和tag_value_matches键值对不可重复。 **取值范围：** 最小数量 1，最大数量 10。 **默认取值：** 不涉及。 

        :param tag_value_matches: The tag_value_matches of this ListModelProxiesRequest.
        :type tag_value_matches: list[str]
        """
        self._tag_value_matches = tag_value_matches

    @property
    def tag_match_policy(self):
        r"""Gets the tag_match_policy of this ListModelProxiesRequest.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的交集。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的并集。 **约束限制：** 不涉及。 **取值范围：** 允许的值为： - ALL - ANY **默认取值：** ALL 

        :return: The tag_match_policy of this ListModelProxiesRequest.
        :rtype: str
        """
        return self._tag_match_policy

    @tag_match_policy.setter
    def tag_match_policy(self, tag_match_policy):
        r"""Sets the tag_match_policy of this ListModelProxiesRequest.

        **参数解释：** 标签匹配模式，仅针对tag_key_exists，tag_key_matches，tag_value_matches参数生效。 - ALL: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的所有元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含所有tag_key_matches以及tag_value_matches参数中指定的key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的交集。 - ANY: 若请求中包含tag_key_exists参数，查询规则为资源标签需要包含tag_key_exists中的任意一个元素，若请求中tag_key_matches以及tag_value_matches参数存在，查询规则为资源标签需要包含tag_key_matches以及tag_value_matches参数中任意一个key-value对应的标签。 三个参数都存在时，取tag_key_exists和tag_key_matches，tag_value_matches的并集。 **约束限制：** 不涉及。 **取值范围：** 允许的值为： - ALL - ANY **默认取值：** ALL 

        :param tag_match_policy: The tag_match_policy of this ListModelProxiesRequest.
        :type tag_match_policy: str
        """
        self._tag_match_policy = tag_match_policy

    @property
    def limit(self):
        r"""Gets the limit of this ListModelProxiesRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :return: The limit of this ListModelProxiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelProxiesRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :param limit: The limit of this ListModelProxiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListModelProxiesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 

        :return: The offset of this ListModelProxiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelProxiesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为0-100000。 **默认取值：** 0 

        :param offset: The offset of this ListModelProxiesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListModelProxiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
