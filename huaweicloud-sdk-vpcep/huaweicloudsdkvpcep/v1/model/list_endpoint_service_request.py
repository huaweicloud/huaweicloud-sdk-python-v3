# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointServiceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_service_name': 'str',
        'id': 'str',
        'status': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'public_border_group': 'str'
    }

    attribute_map = {
        'endpoint_service_name': 'endpoint_service_name',
        'id': 'id',
        'status': 'status',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, endpoint_service_name=None, id=None, status=None, sort_key=None, sort_dir=None, limit=None, offset=None, public_border_group=None):
        """ListEndpointServiceRequest

        The model defined in huaweicloud sdk

        :param endpoint_service_name: 终端节点服务的名称，支持大小写，前后模糊匹配。
        :type endpoint_service_name: str
        :param id: 终端节点服务的ID，唯一标识。
        :type id: str
        :param status: 终端节点服务的状态。 ● creating：创建中 ● available：可连接 ● failed：失败 ● deleting：删除中
        :type status: str
        :param sort_key: 查询结果中终端节点服务列表的排序字段，取值为： ● create_at：终端节点服务的创建时间 ● update_at：终端节点服务的更新时间 默认值为create_at。
        :type sort_key: str
        :param sort_dir: 查询结果中终端节点服务列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。
        :type sort_dir: str
        :param limit: 查询返回的终端节点服务数量限制，即每页返回的终端节点服务的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。
        :type limit: int
        :param offset: 偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。
        :type offset: int
        :param public_border_group: 筛选结果中匹配边缘属性的EPS
        :type public_border_group: str
        """
        
        

        self._endpoint_service_name = None
        self._id = None
        self._status = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._public_border_group = None
        self.discriminator = None

        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if id is not None:
            self.id = id
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
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this ListEndpointServiceRequest.

        终端节点服务的名称，支持大小写，前后模糊匹配。

        :return: The endpoint_service_name of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this ListEndpointServiceRequest.

        终端节点服务的名称，支持大小写，前后模糊匹配。

        :param endpoint_service_name: The endpoint_service_name of this ListEndpointServiceRequest.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def id(self):
        """Gets the id of this ListEndpointServiceRequest.

        终端节点服务的ID，唯一标识。

        :return: The id of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEndpointServiceRequest.

        终端节点服务的ID，唯一标识。

        :param id: The id of this ListEndpointServiceRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ListEndpointServiceRequest.

        终端节点服务的状态。 ● creating：创建中 ● available：可连接 ● failed：失败 ● deleting：删除中

        :return: The status of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEndpointServiceRequest.

        终端节点服务的状态。 ● creating：创建中 ● available：可连接 ● failed：失败 ● deleting：删除中

        :param status: The status of this ListEndpointServiceRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_key(self):
        """Gets the sort_key of this ListEndpointServiceRequest.

        查询结果中终端节点服务列表的排序字段，取值为： ● create_at：终端节点服务的创建时间 ● update_at：终端节点服务的更新时间 默认值为create_at。

        :return: The sort_key of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListEndpointServiceRequest.

        查询结果中终端节点服务列表的排序字段，取值为： ● create_at：终端节点服务的创建时间 ● update_at：终端节点服务的更新时间 默认值为create_at。

        :param sort_key: The sort_key of this ListEndpointServiceRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListEndpointServiceRequest.

        查询结果中终端节点服务列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :return: The sort_dir of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListEndpointServiceRequest.

        查询结果中终端节点服务列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :param sort_dir: The sort_dir of this ListEndpointServiceRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListEndpointServiceRequest.

        查询返回的终端节点服务数量限制，即每页返回的终端节点服务的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :return: The limit of this ListEndpointServiceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEndpointServiceRequest.

        查询返回的终端节点服务数量限制，即每页返回的终端节点服务的个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :param limit: The limit of this ListEndpointServiceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEndpointServiceRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :return: The offset of this ListEndpointServiceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEndpointServiceRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :param offset: The offset of this ListEndpointServiceRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListEndpointServiceRequest.

        筛选结果中匹配边缘属性的EPS

        :return: The public_border_group of this ListEndpointServiceRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListEndpointServiceRequest.

        筛选结果中匹配边缘属性的EPS

        :param public_border_group: The public_border_group of this ListEndpointServiceRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, ListEndpointServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
