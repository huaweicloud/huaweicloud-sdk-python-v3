# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricOpenSearchParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'architecture_guid': 'str',
        'query': 'str',
        'limit': 'int',
        'offset': 'int',
        'search_name_description': 'bool',
        'include_sub_architecture': 'bool'
    }

    attribute_map = {
        'architecture_guid': 'architecture_guid',
        'query': 'query',
        'limit': 'limit',
        'offset': 'offset',
        'search_name_description': 'search_name_description',
        'include_sub_architecture': 'include_sub_architecture'
    }

    def __init__(self, architecture_guid=None, query=None, limit=None, offset=None, search_name_description=None, include_sub_architecture=None):
        r"""MetricOpenSearchParams

        The model defined in huaweicloud sdk

        :param architecture_guid: 指标资产ID
        :type architecture_guid: str
        :param query: 查询条件
        :type query: str
        :param limit: 单次请求条数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param search_name_description: 是否按名称和描述搜索
        :type search_name_description: bool
        :param include_sub_architecture: 是否查询子指标
        :type include_sub_architecture: bool
        """
        
        

        self._architecture_guid = None
        self._query = None
        self._limit = None
        self._offset = None
        self._search_name_description = None
        self._include_sub_architecture = None
        self.discriminator = None

        if architecture_guid is not None:
            self.architecture_guid = architecture_guid
        self.query = query
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if search_name_description is not None:
            self.search_name_description = search_name_description
        if include_sub_architecture is not None:
            self.include_sub_architecture = include_sub_architecture

    @property
    def architecture_guid(self):
        r"""Gets the architecture_guid of this MetricOpenSearchParams.

        指标资产ID

        :return: The architecture_guid of this MetricOpenSearchParams.
        :rtype: str
        """
        return self._architecture_guid

    @architecture_guid.setter
    def architecture_guid(self, architecture_guid):
        r"""Sets the architecture_guid of this MetricOpenSearchParams.

        指标资产ID

        :param architecture_guid: The architecture_guid of this MetricOpenSearchParams.
        :type architecture_guid: str
        """
        self._architecture_guid = architecture_guid

    @property
    def query(self):
        r"""Gets the query of this MetricOpenSearchParams.

        查询条件

        :return: The query of this MetricOpenSearchParams.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this MetricOpenSearchParams.

        查询条件

        :param query: The query of this MetricOpenSearchParams.
        :type query: str
        """
        self._query = query

    @property
    def limit(self):
        r"""Gets the limit of this MetricOpenSearchParams.

        单次请求条数

        :return: The limit of this MetricOpenSearchParams.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this MetricOpenSearchParams.

        单次请求条数

        :param limit: The limit of this MetricOpenSearchParams.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this MetricOpenSearchParams.

        偏移量

        :return: The offset of this MetricOpenSearchParams.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this MetricOpenSearchParams.

        偏移量

        :param offset: The offset of this MetricOpenSearchParams.
        :type offset: int
        """
        self._offset = offset

    @property
    def search_name_description(self):
        r"""Gets the search_name_description of this MetricOpenSearchParams.

        是否按名称和描述搜索

        :return: The search_name_description of this MetricOpenSearchParams.
        :rtype: bool
        """
        return self._search_name_description

    @search_name_description.setter
    def search_name_description(self, search_name_description):
        r"""Sets the search_name_description of this MetricOpenSearchParams.

        是否按名称和描述搜索

        :param search_name_description: The search_name_description of this MetricOpenSearchParams.
        :type search_name_description: bool
        """
        self._search_name_description = search_name_description

    @property
    def include_sub_architecture(self):
        r"""Gets the include_sub_architecture of this MetricOpenSearchParams.

        是否查询子指标

        :return: The include_sub_architecture of this MetricOpenSearchParams.
        :rtype: bool
        """
        return self._include_sub_architecture

    @include_sub_architecture.setter
    def include_sub_architecture(self, include_sub_architecture):
        r"""Sets the include_sub_architecture of this MetricOpenSearchParams.

        是否查询子指标

        :param include_sub_architecture: The include_sub_architecture of this MetricOpenSearchParams.
        :type include_sub_architecture: bool
        """
        self._include_sub_architecture = include_sub_architecture

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
        if not isinstance(other, MetricOpenSearchParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
