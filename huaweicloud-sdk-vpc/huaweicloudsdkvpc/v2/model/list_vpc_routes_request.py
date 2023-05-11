# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcRoutesRequest:

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
        'type': 'str',
        'vpc_id': 'str',
        'destination': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'destination': 'destination',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=None, marker=None, id=None, type=None, vpc_id=None, destination=None, tenant_id=None):
        """ListVpcRoutesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 按照routes_id过滤查询
        :type id: str
        :param type: 功能说明：按照路由类型过滤查询  取值范围：peering
        :type type: str
        :param vpc_id: 按照vpc_id过滤查询
        :type vpc_id: str
        :param destination: 按照路由目的地址CIDR过滤查询
        :type destination: str
        :param tenant_id: 按照项目ID过滤查询
        :type tenant_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._type = None
        self._vpc_id = None
        self._destination = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if destination is not None:
            self.destination = destination
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this ListVpcRoutesRequest.

        每页返回的个数

        :return: The limit of this ListVpcRoutesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcRoutesRequest.

        每页返回的个数

        :param limit: The limit of this ListVpcRoutesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpcRoutesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpcRoutesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListVpcRoutesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListVpcRoutesRequest.

        按照routes_id过滤查询

        :return: The id of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcRoutesRequest.

        按照routes_id过滤查询

        :param id: The id of this ListVpcRoutesRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ListVpcRoutesRequest.

        功能说明：按照路由类型过滤查询  取值范围：peering

        :return: The type of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListVpcRoutesRequest.

        功能说明：按照路由类型过滤查询  取值范围：peering

        :param type: The type of this ListVpcRoutesRequest.
        :type type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListVpcRoutesRequest.

        按照vpc_id过滤查询

        :return: The vpc_id of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListVpcRoutesRequest.

        按照vpc_id过滤查询

        :param vpc_id: The vpc_id of this ListVpcRoutesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def destination(self):
        """Gets the destination of this ListVpcRoutesRequest.

        按照路由目的地址CIDR过滤查询

        :return: The destination of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ListVpcRoutesRequest.

        按照路由目的地址CIDR过滤查询

        :param destination: The destination of this ListVpcRoutesRequest.
        :type destination: str
        """
        self._destination = destination

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListVpcRoutesRequest.

        按照项目ID过滤查询

        :return: The tenant_id of this ListVpcRoutesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListVpcRoutesRequest.

        按照项目ID过滤查询

        :param tenant_id: The tenant_id of this ListVpcRoutesRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, ListVpcRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
