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

        :param index_name: 索引名
        :type index_name: str
        :param field_name: 索引对应的列
        :type field_name: str
        :param params: 1、距离度量方式：  \&quot;metric_type\&quot;:  （非必选，默认值：稠密向量L2，稀疏向量IP）(稀疏向量仅支持IP，标量不支持距离度量) - \&quot;L2\&quot; - \&quot;IP\&quot; - \&quot;COSINE\&quot; 2、支持的索引类型： (非必选，默认值：稠密向量HANNS，标量INVERTED，稀疏向量SPARSE_INVERTED_INDEX，其中Array和JSON字段不支持建立索引)  \&quot;index_type\&quot;:  向量索引： - \&quot;HNSW\&quot; - \&quot;HANNS\&quot; - \&quot;IVF_FLAT\&quot;  稀疏向量索引： - \&quot;SPARSE_INVERTED_INDEX\&quot; - \&quot;SPARSE_WAND\&quot;  标量索引： - \&quot;INVERTED\&quot;(标量字段推荐)倒排索引  3、索引的参数     (非必选)  HNSW相关参数： - M:节点的最大度 - efConstruction:构建索引时每个节点邻居数  HANNS相关参数： - max_degree:节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。 - search_list_size:候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。 - encoding_type: SQ/PQ,，默认SQ。 - pq_code_budget_gb_ratio:PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为 PQ时生效。 - beamwidth:每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。   IVF_FLAT相关参数 - nlist:聚类的数量  - nprobe:查询聚类的数量
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

        索引名

        :return: The index_name of this IndexParams.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this IndexParams.

        索引名

        :param index_name: The index_name of this IndexParams.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def field_name(self):
        r"""Gets the field_name of this IndexParams.

        索引对应的列

        :return: The field_name of this IndexParams.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this IndexParams.

        索引对应的列

        :param field_name: The field_name of this IndexParams.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def params(self):
        r"""Gets the params of this IndexParams.

        1、距离度量方式：  \"metric_type\":  （非必选，默认值：稠密向量L2，稀疏向量IP）(稀疏向量仅支持IP，标量不支持距离度量) - \"L2\" - \"IP\" - \"COSINE\" 2、支持的索引类型： (非必选，默认值：稠密向量HANNS，标量INVERTED，稀疏向量SPARSE_INVERTED_INDEX，其中Array和JSON字段不支持建立索引)  \"index_type\":  向量索引： - \"HNSW\" - \"HANNS\" - \"IVF_FLAT\"  稀疏向量索引： - \"SPARSE_INVERTED_INDEX\" - \"SPARSE_WAND\"  标量索引： - \"INVERTED\"(标量字段推荐)倒排索引  3、索引的参数     (非必选)  HNSW相关参数： - M:节点的最大度 - efConstruction:构建索引时每个节点邻居数  HANNS相关参数： - max_degree:节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。 - search_list_size:候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。 - encoding_type: SQ/PQ,，默认SQ。 - pq_code_budget_gb_ratio:PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为 PQ时生效。 - beamwidth:每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。   IVF_FLAT相关参数 - nlist:聚类的数量  - nprobe:查询聚类的数量

        :return: The params of this IndexParams.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this IndexParams.

        1、距离度量方式：  \"metric_type\":  （非必选，默认值：稠密向量L2，稀疏向量IP）(稀疏向量仅支持IP，标量不支持距离度量) - \"L2\" - \"IP\" - \"COSINE\" 2、支持的索引类型： (非必选，默认值：稠密向量HANNS，标量INVERTED，稀疏向量SPARSE_INVERTED_INDEX，其中Array和JSON字段不支持建立索引)  \"index_type\":  向量索引： - \"HNSW\" - \"HANNS\" - \"IVF_FLAT\"  稀疏向量索引： - \"SPARSE_INVERTED_INDEX\" - \"SPARSE_WAND\"  标量索引： - \"INVERTED\"(标量字段推荐)倒排索引  3、索引的参数     (非必选)  HNSW相关参数： - M:节点的最大度 - efConstruction:构建索引时每个节点邻居数  HANNS相关参数： - max_degree:节点的最大度数。较大的值提供更高的召回率但增加索引的大小和构建时间。 - search_list_size:候选列表的大小。较大的值增加构建索引的时间但提供更高的召回率。 - encoding_type: SQ/PQ,，默认SQ。 - pq_code_budget_gb_ratio:PQ 码的大小限制。较大的值提供更高的召回率但增加内存使用量，仅当encoding_type为 PQ时生效。 - beamwidth:每个搜索迭代的最大 IO 请求数与 CPU 数之间的比率，可用于提升索引性能。   IVF_FLAT相关参数 - nlist:聚类的数量  - nprobe:查询聚类的数量

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
