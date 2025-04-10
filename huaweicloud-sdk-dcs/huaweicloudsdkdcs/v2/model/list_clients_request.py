# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClientsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'addr': 'str',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'offset': 'offset',
        'limit': 'limit',
        'addr': 'addr',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, instance_id=None, node_id=None, offset=None, limit=None, addr=None, sort=None, order=None):
        r"""ListClientsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param node_id: 节点ID。
        :type node_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， 偏移量大于等于0。
        :type offset: int
        :param limit: 每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10.
        :type limit: int
        :param addr: 按客户端连接地址过滤。
        :type addr: str
        :param sort: 排序字段。
        :type sort: str
        :param order: 排序方式
        :type order: str
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._offset = None
        self._limit = None
        self._addr = None
        self._sort = None
        self._order = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_id = node_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if addr is not None:
            self.addr = addr
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListClientsRequest.

        实例ID。

        :return: The instance_id of this ListClientsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListClientsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListClientsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListClientsRequest.

        节点ID。

        :return: The node_id of this ListClientsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListClientsRequest.

        节点ID。

        :param node_id: The node_id of this ListClientsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def offset(self):
        r"""Gets the offset of this ListClientsRequest.

        偏移量，表示从此偏移量开始查询， 偏移量大于等于0。

        :return: The offset of this ListClientsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClientsRequest.

        偏移量，表示从此偏移量开始查询， 偏移量大于等于0。

        :param offset: The offset of this ListClientsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListClientsRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10.

        :return: The limit of this ListClientsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClientsRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10.

        :param limit: The limit of this ListClientsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def addr(self):
        r"""Gets the addr of this ListClientsRequest.

        按客户端连接地址过滤。

        :return: The addr of this ListClientsRequest.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this ListClientsRequest.

        按客户端连接地址过滤。

        :param addr: The addr of this ListClientsRequest.
        :type addr: str
        """
        self._addr = addr

    @property
    def sort(self):
        r"""Gets the sort of this ListClientsRequest.

        排序字段。

        :return: The sort of this ListClientsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListClientsRequest.

        排序字段。

        :param sort: The sort of this ListClientsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        r"""Gets the order of this ListClientsRequest.

        排序方式

        :return: The order of this ListClientsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListClientsRequest.

        排序方式

        :param order: The order of this ListClientsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListClientsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
