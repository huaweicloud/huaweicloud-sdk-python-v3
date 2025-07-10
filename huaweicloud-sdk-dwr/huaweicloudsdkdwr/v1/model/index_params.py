# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'field_name': 'str',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'index_name': 'index_name',
        'field_name': 'field_name',
        'params': 'params'
    }

    def __init__(self, index_name=None, field_name=None, params=None):
        r"""IndexParams

        The model defined in huaweicloud sdk

        :param index_name: **参数解释：** 创建的索引名称，collection内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type index_name: str
        :param field_name: **参数解释：** 要创建索引的目标字段名称。 **约束限制：** - 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 - field_name必须是collection field schema中存在的字段。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type field_name: str
        :param params: **参数解释：** 创建的索引的参数配置。 可以设置的参数： -  metric_type：向量度量方式，只有向量索引需要配置。 - index_type：创建的索引类型。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：节点的最大度。   - efConstruction：构建索引时每个节点邻居数。  2. HANNS索引相关参数：   - max_degree：节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。   - search_list_size：候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。   - encoding_type: SQ/PQ，默认SQ。   - pq_code_budget_gb_ratio：PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为PQ时生效。   - beamwidth：每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。  3. IVF_FLAT索引相关参数：   - nlist：聚类的数量。   - nprobe：查询聚类的数量。  **约束限制：** 不涉及。  **取值范围：**  - metric_type:   1. 稠密向量支持度量方式：\&quot;L2\&quot;和\&quot;COSINE\&quot;。  2. 稀疏向量支持度量方式：\&quot;IP\&quot;。 - index_type:  1. 稠密向量支持索引类型：\&quot;HNSW\&quot;、\&quot;HANNS\&quot;和\&quot;IVF_FLAT\&quot;。  2. 稀疏向量支持索引类型：\&quot;SPARSE_INVERTED_INDEX\&quot;和\&quot;SPARSE_WAND\&quot;。  3. 标量字段支持索引类型：\&quot;IVF_FLAT\&quot;。 - params：  1. HNSW索引类型参数：   - M：[2, 2048]   - efConstruction：[1, int32_max]  2. HANNS索引相关参数：   - max_degree：[1, 512]   - search_list_size：[1, int32_max]   - encoding_type: SQ/PQ   - pq_code_budget_gb_ratio：[0.0, 0.25]   - beamwidth：[1, 16]  3. IVF_FLAT索引相关参数：   - nlist：[1, 65536]   - nprobe：[1, nlist]          **默认值：** - metric_type:   1. 稠密向量：\&quot;L2\&quot;。  2. 稀疏向量：\&quot;IP\&quot;。  3. 标量：无须配置 - index_type:  1. 稠密向量：\&quot;HANNS\&quot;。  2. 稀疏向量：\&quot;SPARSE_INVERTED_INDEX\&quot;。  3. 标量：\&quot;IVF_FLAT\&quot;。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：16。   - efConstruction：200。  2. HANNS索引相关参数：   - max_degree：56。   - search_list_size：100。   - encoding_type: 默认SQ。   - pq_code_budget_gb_ratio：0.125。   - beamwidth：0.0  3. IVF_FLAT索引相关参数：   - nlist：128   - nprobe：8
        :type params: dict(str, object)
        """
        
        

        self._index_name = None
        self._field_name = None
        self._params = None
        self.discriminator = None

        self.index_name = index_name
        self.field_name = field_name
        if params is not None:
            self.params = params

    @property
    def index_name(self):
        r"""Gets the index_name of this IndexParams.

        **参数解释：** 创建的索引名称，collection内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The index_name of this IndexParams.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this IndexParams.

        **参数解释：** 创建的索引名称，collection内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param index_name: The index_name of this IndexParams.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def field_name(self):
        r"""Gets the field_name of this IndexParams.

        **参数解释：** 要创建索引的目标字段名称。 **约束限制：** - 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 - field_name必须是collection field schema中存在的字段。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The field_name of this IndexParams.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this IndexParams.

        **参数解释：** 要创建索引的目标字段名称。 **约束限制：** - 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 - field_name必须是collection field schema中存在的字段。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param field_name: The field_name of this IndexParams.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def params(self):
        r"""Gets the params of this IndexParams.

        **参数解释：** 创建的索引的参数配置。 可以设置的参数： -  metric_type：向量度量方式，只有向量索引需要配置。 - index_type：创建的索引类型。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：节点的最大度。   - efConstruction：构建索引时每个节点邻居数。  2. HANNS索引相关参数：   - max_degree：节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。   - search_list_size：候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。   - encoding_type: SQ/PQ，默认SQ。   - pq_code_budget_gb_ratio：PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为PQ时生效。   - beamwidth：每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。  3. IVF_FLAT索引相关参数：   - nlist：聚类的数量。   - nprobe：查询聚类的数量。  **约束限制：** 不涉及。  **取值范围：**  - metric_type:   1. 稠密向量支持度量方式：\"L2\"和\"COSINE\"。  2. 稀疏向量支持度量方式：\"IP\"。 - index_type:  1. 稠密向量支持索引类型：\"HNSW\"、\"HANNS\"和\"IVF_FLAT\"。  2. 稀疏向量支持索引类型：\"SPARSE_INVERTED_INDEX\"和\"SPARSE_WAND\"。  3. 标量字段支持索引类型：\"IVF_FLAT\"。 - params：  1. HNSW索引类型参数：   - M：[2, 2048]   - efConstruction：[1, int32_max]  2. HANNS索引相关参数：   - max_degree：[1, 512]   - search_list_size：[1, int32_max]   - encoding_type: SQ/PQ   - pq_code_budget_gb_ratio：[0.0, 0.25]   - beamwidth：[1, 16]  3. IVF_FLAT索引相关参数：   - nlist：[1, 65536]   - nprobe：[1, nlist]          **默认值：** - metric_type:   1. 稠密向量：\"L2\"。  2. 稀疏向量：\"IP\"。  3. 标量：无须配置 - index_type:  1. 稠密向量：\"HANNS\"。  2. 稀疏向量：\"SPARSE_INVERTED_INDEX\"。  3. 标量：\"IVF_FLAT\"。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：16。   - efConstruction：200。  2. HANNS索引相关参数：   - max_degree：56。   - search_list_size：100。   - encoding_type: 默认SQ。   - pq_code_budget_gb_ratio：0.125。   - beamwidth：0.0  3. IVF_FLAT索引相关参数：   - nlist：128   - nprobe：8

        :return: The params of this IndexParams.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this IndexParams.

        **参数解释：** 创建的索引的参数配置。 可以设置的参数： -  metric_type：向量度量方式，只有向量索引需要配置。 - index_type：创建的索引类型。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：节点的最大度。   - efConstruction：构建索引时每个节点邻居数。  2. HANNS索引相关参数：   - max_degree：节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。   - search_list_size：候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。   - encoding_type: SQ/PQ，默认SQ。   - pq_code_budget_gb_ratio：PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为PQ时生效。   - beamwidth：每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。  3. IVF_FLAT索引相关参数：   - nlist：聚类的数量。   - nprobe：查询聚类的数量。  **约束限制：** 不涉及。  **取值范围：**  - metric_type:   1. 稠密向量支持度量方式：\"L2\"和\"COSINE\"。  2. 稀疏向量支持度量方式：\"IP\"。 - index_type:  1. 稠密向量支持索引类型：\"HNSW\"、\"HANNS\"和\"IVF_FLAT\"。  2. 稀疏向量支持索引类型：\"SPARSE_INVERTED_INDEX\"和\"SPARSE_WAND\"。  3. 标量字段支持索引类型：\"IVF_FLAT\"。 - params：  1. HNSW索引类型参数：   - M：[2, 2048]   - efConstruction：[1, int32_max]  2. HANNS索引相关参数：   - max_degree：[1, 512]   - search_list_size：[1, int32_max]   - encoding_type: SQ/PQ   - pq_code_budget_gb_ratio：[0.0, 0.25]   - beamwidth：[1, 16]  3. IVF_FLAT索引相关参数：   - nlist：[1, 65536]   - nprobe：[1, nlist]          **默认值：** - metric_type:   1. 稠密向量：\"L2\"。  2. 稀疏向量：\"IP\"。  3. 标量：无须配置 - index_type:  1. 稠密向量：\"HANNS\"。  2. 稀疏向量：\"SPARSE_INVERTED_INDEX\"。  3. 标量：\"IVF_FLAT\"。 - params：对应索引类型的配置参数。  1. HNSW索引类型参数：   - M：16。   - efConstruction：200。  2. HANNS索引相关参数：   - max_degree：56。   - search_list_size：100。   - encoding_type: 默认SQ。   - pq_code_budget_gb_ratio：0.125。   - beamwidth：0.0  3. IVF_FLAT索引相关参数：   - nlist：128   - nprobe：8

        :param params: The params of this IndexParams.
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
        if not isinstance(other, IndexParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
