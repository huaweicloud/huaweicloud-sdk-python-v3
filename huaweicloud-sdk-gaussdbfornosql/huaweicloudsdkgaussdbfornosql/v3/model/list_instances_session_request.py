# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesSessionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'addr_prefix': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'offset': 'offset',
        'limit': 'limit',
        'addr_prefix': 'addr_prefix'
    }

    def __init__(self, node_id=None, offset=None, limit=None, addr_prefix=None):
        r"""ListInstancesSessionRequest

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param offset: 索引位置，偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新创建的实例节点连接开始查询。
        :type offset: int
        :param limit: 分页查询页数。不传该参数时，默认每页50条实例节点连接信息，最大100条。
        :type limit: int
        :param addr_prefix: 用户端地址前缀匹配字符串。完整的地址由ip和端口号组成。不传默认查询所有。
        :type addr_prefix: str
        """
        
        

        self._node_id = None
        self._offset = None
        self._limit = None
        self._addr_prefix = None
        self.discriminator = None

        self.node_id = node_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if addr_prefix is not None:
            self.addr_prefix = addr_prefix

    @property
    def node_id(self):
        r"""Gets the node_id of this ListInstancesSessionRequest.

        节点ID。

        :return: The node_id of this ListInstancesSessionRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListInstancesSessionRequest.

        节点ID。

        :param node_id: The node_id of this ListInstancesSessionRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesSessionRequest.

        索引位置，偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新创建的实例节点连接开始查询。

        :return: The offset of this ListInstancesSessionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesSessionRequest.

        索引位置，偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新创建的实例节点连接开始查询。

        :param offset: The offset of this ListInstancesSessionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesSessionRequest.

        分页查询页数。不传该参数时，默认每页50条实例节点连接信息，最大100条。

        :return: The limit of this ListInstancesSessionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesSessionRequest.

        分页查询页数。不传该参数时，默认每页50条实例节点连接信息，最大100条。

        :param limit: The limit of this ListInstancesSessionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def addr_prefix(self):
        r"""Gets the addr_prefix of this ListInstancesSessionRequest.

        用户端地址前缀匹配字符串。完整的地址由ip和端口号组成。不传默认查询所有。

        :return: The addr_prefix of this ListInstancesSessionRequest.
        :rtype: str
        """
        return self._addr_prefix

    @addr_prefix.setter
    def addr_prefix(self, addr_prefix):
        r"""Sets the addr_prefix of this ListInstancesSessionRequest.

        用户端地址前缀匹配字符串。完整的地址由ip和端口号组成。不传默认查询所有。

        :param addr_prefix: The addr_prefix of this ListInstancesSessionRequest.
        :type addr_prefix: str
        """
        self._addr_prefix = addr_prefix

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
        if not isinstance(other, ListInstancesSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
