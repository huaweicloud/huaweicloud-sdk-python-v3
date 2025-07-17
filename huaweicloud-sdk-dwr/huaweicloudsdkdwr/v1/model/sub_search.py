# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubSearch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vector_field': 'str',
        'vector': 'list[object]',
        'top_k': 'int',
        'offset': 'int',
        'filter': 'str',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'vector_field': 'vector_field',
        'vector': 'vector',
        'top_k': 'top_k',
        'offset': 'offset',
        'filter': 'filter',
        'params': 'params'
    }

    def __init__(self, vector_field=None, vector=None, top_k=None, offset=None, filter=None, params=None):
        r"""SubSearch

        The model defined in huaweicloud sdk

        :param vector_field: **参数解释：** 要搜索的向量字段名称。 **约束限制：** 必须是collection field schema中存在的向量字段名称。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type vector_field: str
        :param vector: **参数解释：** 要搜索的向量字段数据。 **约束限制：** 与collection field schema中定义的对应向量字段的类型和维度一致。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vector: list[object]
        :param top_k: **参数解释：** 返回的entity个数限制。可以将此参数与offset结合使用以启用分页。 **约束限制：** 当sub_search数量为1时，top_k与offset取值的总和应小于16384。 **取值范围：** &#x60;[1, 16384]&#x60; **默认取值：** 10
        :type top_k: int
        :param offset: **参数解释：** 在搜索结果中跳过的记录数。可以将此参数与 top_k 参数结合使用以启用分页。 **约束限制：** 1.与top_k取值的总和应小于16384。 2.当sub_search数量为1时才生效。 **取值范围：** 大于等于0 **默认取值:** 0
        :type offset: int
        :param filter: **参数解释：** 用于过滤匹配entity的标量过滤条件。可以将此设置为空字符串以跳过标量过滤。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 空字符串，不就行标量过滤。
        :type filter: str
        :param params: **参数解释：** 额外的搜索参数配置。 可以配置的参数： * ef: 每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（仅对HNSW索引类型生效） * search_list: 候选列表的大小，越大召回率越高，但性能会下降。（仅对HANNS索引类型生效） * cut_off_frequency: 通过停用词出现频率决定是否作为查询结果。（仅对稀疏向量搜索生效）  **约束限制：** 不涉及。 **取值范围：** 当sub_search数量为1时：  ef: [top_k + offset, int32_max]  search_list: [top_k + offset, int32_max]  cut_off_frequency：[0, 1.0] 当sub_search数量大于1时：  ef: [top_k, int32_max]  search_list: [top_k, int32_max]  cut_off_frequency：[0, 1.0]  **默认取值:**  当sub_search数量为1时：  ef: top_k + offset  search_list: top_k + offset  cut_off_frequency: 0 当sub_search数量大于1时：  ef: top_k  search_list: top_k  cut_off_frequency: 0
        :type params: dict(str, object)
        """
        
        

        self._vector_field = None
        self._vector = None
        self._top_k = None
        self._offset = None
        self._filter = None
        self._params = None
        self.discriminator = None

        self.vector_field = vector_field
        self.vector = vector
        if top_k is not None:
            self.top_k = top_k
        if offset is not None:
            self.offset = offset
        if filter is not None:
            self.filter = filter
        if params is not None:
            self.params = params

    @property
    def vector_field(self):
        r"""Gets the vector_field of this SubSearch.

        **参数解释：** 要搜索的向量字段名称。 **约束限制：** 必须是collection field schema中存在的向量字段名称。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The vector_field of this SubSearch.
        :rtype: str
        """
        return self._vector_field

    @vector_field.setter
    def vector_field(self, vector_field):
        r"""Sets the vector_field of this SubSearch.

        **参数解释：** 要搜索的向量字段名称。 **约束限制：** 必须是collection field schema中存在的向量字段名称。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param vector_field: The vector_field of this SubSearch.
        :type vector_field: str
        """
        self._vector_field = vector_field

    @property
    def vector(self):
        r"""Gets the vector of this SubSearch.

        **参数解释：** 要搜索的向量字段数据。 **约束限制：** 与collection field schema中定义的对应向量字段的类型和维度一致。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vector of this SubSearch.
        :rtype: list[object]
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        r"""Sets the vector of this SubSearch.

        **参数解释：** 要搜索的向量字段数据。 **约束限制：** 与collection field schema中定义的对应向量字段的类型和维度一致。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vector: The vector of this SubSearch.
        :type vector: list[object]
        """
        self._vector = vector

    @property
    def top_k(self):
        r"""Gets the top_k of this SubSearch.

        **参数解释：** 返回的entity个数限制。可以将此参数与offset结合使用以启用分页。 **约束限制：** 当sub_search数量为1时，top_k与offset取值的总和应小于16384。 **取值范围：** `[1, 16384]` **默认取值：** 10

        :return: The top_k of this SubSearch.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        r"""Sets the top_k of this SubSearch.

        **参数解释：** 返回的entity个数限制。可以将此参数与offset结合使用以启用分页。 **约束限制：** 当sub_search数量为1时，top_k与offset取值的总和应小于16384。 **取值范围：** `[1, 16384]` **默认取值：** 10

        :param top_k: The top_k of this SubSearch.
        :type top_k: int
        """
        self._top_k = top_k

    @property
    def offset(self):
        r"""Gets the offset of this SubSearch.

        **参数解释：** 在搜索结果中跳过的记录数。可以将此参数与 top_k 参数结合使用以启用分页。 **约束限制：** 1.与top_k取值的总和应小于16384。 2.当sub_search数量为1时才生效。 **取值范围：** 大于等于0 **默认取值:** 0

        :return: The offset of this SubSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SubSearch.

        **参数解释：** 在搜索结果中跳过的记录数。可以将此参数与 top_k 参数结合使用以启用分页。 **约束限制：** 1.与top_k取值的总和应小于16384。 2.当sub_search数量为1时才生效。 **取值范围：** 大于等于0 **默认取值:** 0

        :param offset: The offset of this SubSearch.
        :type offset: int
        """
        self._offset = offset

    @property
    def filter(self):
        r"""Gets the filter of this SubSearch.

        **参数解释：** 用于过滤匹配entity的标量过滤条件。可以将此设置为空字符串以跳过标量过滤。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 空字符串，不就行标量过滤。

        :return: The filter of this SubSearch.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this SubSearch.

        **参数解释：** 用于过滤匹配entity的标量过滤条件。可以将此设置为空字符串以跳过标量过滤。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 空字符串，不就行标量过滤。

        :param filter: The filter of this SubSearch.
        :type filter: str
        """
        self._filter = filter

    @property
    def params(self):
        r"""Gets the params of this SubSearch.

        **参数解释：** 额外的搜索参数配置。 可以配置的参数： * ef: 每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（仅对HNSW索引类型生效） * search_list: 候选列表的大小，越大召回率越高，但性能会下降。（仅对HANNS索引类型生效） * cut_off_frequency: 通过停用词出现频率决定是否作为查询结果。（仅对稀疏向量搜索生效）  **约束限制：** 不涉及。 **取值范围：** 当sub_search数量为1时：  ef: [top_k + offset, int32_max]  search_list: [top_k + offset, int32_max]  cut_off_frequency：[0, 1.0] 当sub_search数量大于1时：  ef: [top_k, int32_max]  search_list: [top_k, int32_max]  cut_off_frequency：[0, 1.0]  **默认取值:**  当sub_search数量为1时：  ef: top_k + offset  search_list: top_k + offset  cut_off_frequency: 0 当sub_search数量大于1时：  ef: top_k  search_list: top_k  cut_off_frequency: 0

        :return: The params of this SubSearch.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this SubSearch.

        **参数解释：** 额外的搜索参数配置。 可以配置的参数： * ef: 每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（仅对HNSW索引类型生效） * search_list: 候选列表的大小，越大召回率越高，但性能会下降。（仅对HANNS索引类型生效） * cut_off_frequency: 通过停用词出现频率决定是否作为查询结果。（仅对稀疏向量搜索生效）  **约束限制：** 不涉及。 **取值范围：** 当sub_search数量为1时：  ef: [top_k + offset, int32_max]  search_list: [top_k + offset, int32_max]  cut_off_frequency：[0, 1.0] 当sub_search数量大于1时：  ef: [top_k, int32_max]  search_list: [top_k, int32_max]  cut_off_frequency：[0, 1.0]  **默认取值:**  当sub_search数量为1时：  ef: top_k + offset  search_list: top_k + offset  cut_off_frequency: 0 当sub_search数量大于1时：  ef: top_k  search_list: top_k  cut_off_frequency: 0

        :param params: The params of this SubSearch.
        :type params: dict(str, object)
        """
        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
