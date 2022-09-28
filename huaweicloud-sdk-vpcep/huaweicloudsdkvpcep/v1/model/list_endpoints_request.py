# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsRequest:

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
        'vpc_id': 'str',
        'id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'endpoint_service_name': 'endpoint_service_name',
        'vpc_id': 'vpc_id',
        'id': 'id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, endpoint_service_name=None, vpc_id=None, id=None, limit=None, offset=None, sort_key=None, sort_dir=None, public_border_group=None):
        """ListEndpointsRequest

        The model defined in huaweicloud sdk

        :param endpoint_service_name: 终端节点服务的名称，支持大小写，前后模糊匹配。
        :type endpoint_service_name: str
        :param vpc_id: 终端节点所在的VPC的ID。
        :type vpc_id: str
        :param id: 终端节点的ID，唯一标识。
        :type id: str
        :param limit: 查询返回终端节点的数量限制，即每页返回的资源个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。
        :type limit: int
        :param offset: 偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。
        :type offset: int
        :param sort_key: 查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。
        :type sort_key: str
        :param sort_dir: 查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。
        :type sort_dir: str
        :param public_border_group: 筛选结果中匹配边缘属性的EPS
        :type public_border_group: str
        """
        
        

        self._endpoint_service_name = None
        self._vpc_id = None
        self._id = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self._public_border_group = None
        self.discriminator = None

        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this ListEndpointsRequest.

        终端节点服务的名称，支持大小写，前后模糊匹配。

        :return: The endpoint_service_name of this ListEndpointsRequest.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this ListEndpointsRequest.

        终端节点服务的名称，支持大小写，前后模糊匹配。

        :param endpoint_service_name: The endpoint_service_name of this ListEndpointsRequest.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListEndpointsRequest.

        终端节点所在的VPC的ID。

        :return: The vpc_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListEndpointsRequest.

        终端节点所在的VPC的ID。

        :param vpc_id: The vpc_id of this ListEndpointsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def id(self):
        """Gets the id of this ListEndpointsRequest.

        终端节点的ID，唯一标识。

        :return: The id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEndpointsRequest.

        终端节点的ID，唯一标识。

        :param id: The id of this ListEndpointsRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListEndpointsRequest.

        查询返回终端节点的数量限制，即每页返回的资源个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :return: The limit of this ListEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEndpointsRequest.

        查询返回终端节点的数量限制，即每页返回的资源个数。 取值范围：0~1000，取值一般为10，20或者50，默认为10。

        :param limit: The limit of this ListEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEndpointsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :return: The offset of this ListEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEndpointsRequest.

        偏移量。 偏移量为一个大于0小于终端节点服务总个数的整数， 表示从偏移量后面的终端节点服务开始查询。

        :param offset: The offset of this ListEndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        """Gets the sort_key of this ListEndpointsRequest.

        查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。

        :return: The sort_key of this ListEndpointsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListEndpointsRequest.

        查询结果中终端节点列表的排序字段，取值为： ● create_at：终端节点的创建时间 ● update_at：终端节点的更新时间 默认值为create_at。

        :param sort_key: The sort_key of this ListEndpointsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListEndpointsRequest.

        查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :return: The sort_dir of this ListEndpointsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListEndpointsRequest.

        查询结果中终端节点列表的排序方式，取值为： ● desc：降序排序 ● asc：升序排序 默认值为desc。

        :param sort_dir: The sort_dir of this ListEndpointsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListEndpointsRequest.

        筛选结果中匹配边缘属性的EPS

        :return: The public_border_group of this ListEndpointsRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListEndpointsRequest.

        筛选结果中匹配边缘属性的EPS

        :param public_border_group: The public_border_group of this ListEndpointsRequest.
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
        if not isinstance(other, ListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
