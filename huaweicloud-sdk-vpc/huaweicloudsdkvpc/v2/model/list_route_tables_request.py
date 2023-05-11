# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRouteTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, limit=None, marker=None, id=None, vpc_id=None, subnet_id=None):
        """ListRouteTablesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时为查询第一页
        :type marker: str
        :param id: 路由表ID，可过滤对应ID的路由表
        :type id: str
        :param vpc_id: 虚拟私有云ID，可过滤对应虚拟私有云包含的路由表
        :type vpc_id: str
        :param subnet_id: 子网ID，可过滤对应子网关联的路由表
        :type subnet_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._vpc_id = None
        self._subnet_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def limit(self):
        """Gets the limit of this ListRouteTablesRequest.

        每页返回的个数

        :return: The limit of this ListRouteTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRouteTablesRequest.

        每页返回的个数

        :param limit: The limit of this ListRouteTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRouteTablesRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :return: The marker of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRouteTablesRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :param marker: The marker of this ListRouteTablesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListRouteTablesRequest.

        路由表ID，可过滤对应ID的路由表

        :return: The id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRouteTablesRequest.

        路由表ID，可过滤对应ID的路由表

        :param id: The id of this ListRouteTablesRequest.
        :type id: str
        """
        self._id = id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListRouteTablesRequest.

        虚拟私有云ID，可过滤对应虚拟私有云包含的路由表

        :return: The vpc_id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListRouteTablesRequest.

        虚拟私有云ID，可过滤对应虚拟私有云包含的路由表

        :param vpc_id: The vpc_id of this ListRouteTablesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListRouteTablesRequest.

        子网ID，可过滤对应子网关联的路由表

        :return: The subnet_id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListRouteTablesRequest.

        子网ID，可过滤对应子网关联的路由表

        :param subnet_id: The subnet_id of this ListRouteTablesRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ListRouteTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
