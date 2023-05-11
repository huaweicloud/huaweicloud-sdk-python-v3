# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'node_id': 'str',
        'provider': 'str',
        'name': 'str',
        'sort': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_id': 'node_id',
        'provider': 'provider',
        'name': 'name',
        'sort': 'sort',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, node_id=None, provider=None, name=None, sort=None, limit=None, offset=None):
        """ShowDeploymentsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求
        :type cluster_id: str
        :param node_id: 节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求
        :type node_id: str
        :param provider: 平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据
        :type provider: str
        :param name: 部署名称(支持模糊匹配)
        :type name: str
        :param sort: 查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc
        :type sort: str
        :param limit: 每页显示的条目数量, 最大 100，默认值 10
        :type limit: int
        :param offset: 查询的起始位置, 默认值 0
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._node_id = None
        self._provider = None
        self._name = None
        self._sort = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if node_id is not None:
            self.node_id = node_id
        if provider is not None:
            self.provider = provider
        if name is not None:
            self.name = name
        if sort is not None:
            self.sort = sort
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowDeploymentsRequest.

        集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :return: The cluster_id of this ShowDeploymentsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowDeploymentsRequest.

        集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :param cluster_id: The cluster_id of this ShowDeploymentsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_id(self):
        """Gets the node_id of this ShowDeploymentsRequest.

        节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求

        :return: The node_id of this ShowDeploymentsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowDeploymentsRequest.

        节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求

        :param node_id: The node_id of this ShowDeploymentsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def provider(self):
        """Gets the provider of this ShowDeploymentsRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :return: The provider of this ShowDeploymentsRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowDeploymentsRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :param provider: The provider of this ShowDeploymentsRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def name(self):
        """Gets the name of this ShowDeploymentsRequest.

        部署名称(支持模糊匹配)

        :return: The name of this ShowDeploymentsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDeploymentsRequest.

        部署名称(支持模糊匹配)

        :param name: The name of this ShowDeploymentsRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort(self):
        """Gets the sort of this ShowDeploymentsRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :return: The sort of this ShowDeploymentsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ShowDeploymentsRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :param sort: The sort of this ShowDeploymentsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def limit(self):
        """Gets the limit of this ShowDeploymentsRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :return: The limit of this ShowDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowDeploymentsRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :param limit: The limit of this ShowDeploymentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowDeploymentsRequest.

        查询的起始位置, 默认值 0

        :return: The offset of this ShowDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowDeploymentsRequest.

        查询的起始位置, 默认值 0

        :param offset: The offset of this ShowDeploymentsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
