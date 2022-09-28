# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_endpoint_service_id': 'str',
        'id': 'str',
        'marker_id': 'str',
        'status': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'vpc_endpoint_service_id': 'vpc_endpoint_service_id',
        'id': 'id',
        'marker_id': 'marker_id',
        'status': 'status',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, vpc_endpoint_service_id=None, id=None, marker_id=None, status=None, sort_key=None, sort_dir=None, limit=None, offset=None):
        """ListServiceConnectionsRequest

        The model defined in huaweicloud sdk

        :param vpc_endpoint_service_id: 终端节点服务的ID。
        :type vpc_endpoint_service_id: str
        :param id: 终端节点的ID，唯一标识。
        :type id: str
        :param marker_id: 终端节点的报文标识。
        :type marker_id: str
        :param status: 终端节点的连接状态。 ● pendingAcceptance：待接受 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败
        :type status: str
        :param sort_key: 查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。
        :type sort_key: str
        :param sort_dir: 查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。
        :type sort_dir: str
        :param limit: 查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。
        :type limit: int
        :param offset: 偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。
        :type offset: int
        """
        
        

        self._vpc_endpoint_service_id = None
        self._id = None
        self._marker_id = None
        self._status = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.vpc_endpoint_service_id = vpc_endpoint_service_id
        if id is not None:
            self.id = id
        if marker_id is not None:
            self.marker_id = marker_id
        if status is not None:
            self.status = status
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def vpc_endpoint_service_id(self):
        """Gets the vpc_endpoint_service_id of this ListServiceConnectionsRequest.

        终端节点服务的ID。

        :return: The vpc_endpoint_service_id of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._vpc_endpoint_service_id

    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, vpc_endpoint_service_id):
        """Sets the vpc_endpoint_service_id of this ListServiceConnectionsRequest.

        终端节点服务的ID。

        :param vpc_endpoint_service_id: The vpc_endpoint_service_id of this ListServiceConnectionsRequest.
        :type vpc_endpoint_service_id: str
        """
        self._vpc_endpoint_service_id = vpc_endpoint_service_id

    @property
    def id(self):
        """Gets the id of this ListServiceConnectionsRequest.

        终端节点的ID，唯一标识。

        :return: The id of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListServiceConnectionsRequest.

        终端节点的ID，唯一标识。

        :param id: The id of this ListServiceConnectionsRequest.
        :type id: str
        """
        self._id = id

    @property
    def marker_id(self):
        """Gets the marker_id of this ListServiceConnectionsRequest.

        终端节点的报文标识。

        :return: The marker_id of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        """Sets the marker_id of this ListServiceConnectionsRequest.

        终端节点的报文标识。

        :param marker_id: The marker_id of this ListServiceConnectionsRequest.
        :type marker_id: str
        """
        self._marker_id = marker_id

    @property
    def status(self):
        """Gets the status of this ListServiceConnectionsRequest.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败

        :return: The status of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListServiceConnectionsRequest.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败

        :param status: The status of this ListServiceConnectionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_key(self):
        """Gets the sort_key of this ListServiceConnectionsRequest.

        查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。

        :return: The sort_key of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListServiceConnectionsRequest.

        查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。

        :param sort_key: The sort_key of this ListServiceConnectionsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListServiceConnectionsRequest.

        查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :return: The sort_dir of this ListServiceConnectionsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListServiceConnectionsRequest.

        查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :param sort_dir: The sort_dir of this ListServiceConnectionsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListServiceConnectionsRequest.

        查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :return: The limit of this ListServiceConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServiceConnectionsRequest.

        查询返回终端节点服务的连接列表限制每页个数，即每页返回的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :param limit: The limit of this ListServiceConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServiceConnectionsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :return: The offset of this ListServiceConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServiceConnectionsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :param offset: The offset of this ListServiceConnectionsRequest.
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
        if not isinstance(other, ListServiceConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
