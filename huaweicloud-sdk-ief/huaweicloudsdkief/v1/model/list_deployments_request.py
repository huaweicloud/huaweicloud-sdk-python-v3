# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeploymentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort': 'str',
        'name': 'str',
        'node_id': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'limit': 'limit',
        'offset': 'offset',
        'sort': 'sort',
        'name': 'name',
        'node_id': 'node_id',
        'group_id': 'group_id'
    }

    def __init__(self, ief_instance_id=None, limit=None, offset=None, sort=None, name=None, node_id=None, group_id=None):
        """ListDeploymentsRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param limit: 每页显示的条目数量，最大100，默认值10
        :type limit: int
        :param offset: 查询的起始位置，默认值0
        :type offset: int
        :param sort: 查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc
        :type sort: str
        :param name: deployment名称（支持模糊匹配）
        :type name: str
        :param node_id: 节点ID，查询部署在该节点下的应用列表，和group_id不可同时请求
        :type node_id: str
        :param group_id: 节点组ID，查询部署在该节点组的应用列表，和node_id不可同时请求
        :type group_id: str
        """
        
        

        self._ief_instance_id = None
        self._limit = None
        self._offset = None
        self._sort = None
        self._name = None
        self._node_id = None
        self._group_id = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if group_id is not None:
            self.group_id = group_id

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListDeploymentsRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListDeploymentsRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListDeploymentsRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDeploymentsRequest.

        每页显示的条目数量，最大100，默认值10

        :return: The limit of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDeploymentsRequest.

        每页显示的条目数量，最大100，默认值10

        :param limit: The limit of this ListDeploymentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDeploymentsRequest.

        查询的起始位置，默认值0

        :return: The offset of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDeploymentsRequest.

        查询的起始位置，默认值0

        :param offset: The offset of this ListDeploymentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort(self):
        """Gets the sort of this ListDeploymentsRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :return: The sort of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListDeploymentsRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :param sort: The sort of this ListDeploymentsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def name(self):
        """Gets the name of this ListDeploymentsRequest.

        deployment名称（支持模糊匹配）

        :return: The name of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDeploymentsRequest.

        deployment名称（支持模糊匹配）

        :param name: The name of this ListDeploymentsRequest.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        """Gets the node_id of this ListDeploymentsRequest.

        节点ID，查询部署在该节点下的应用列表，和group_id不可同时请求

        :return: The node_id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListDeploymentsRequest.

        节点ID，查询部署在该节点下的应用列表，和group_id不可同时请求

        :param node_id: The node_id of this ListDeploymentsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def group_id(self):
        """Gets the group_id of this ListDeploymentsRequest.

        节点组ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :return: The group_id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListDeploymentsRequest.

        节点组ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :param group_id: The group_id of this ListDeploymentsRequest.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, ListDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
