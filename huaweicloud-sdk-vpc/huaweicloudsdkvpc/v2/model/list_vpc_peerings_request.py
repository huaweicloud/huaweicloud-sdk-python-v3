# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcPeeringsRequest:

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
        'name': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, status=None, tenant_id=None, vpc_id=None):
        """ListVpcPeeringsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 按照peering_id过滤查询
        :type id: str
        :param name: 功能说明：按照peering_name过查询  取值范围：最大长度不超过64
        :type name: str
        :param status: 根据status进行过滤  - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。
        :type status: str
        :param tenant_id: 按照项目ID过滤查询
        :type tenant_id: str
        :param vpc_id: 根据vpc ID过滤查询
        :type vpc_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._vpc_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListVpcPeeringsRequest.

        每页返回的个数

        :return: The limit of this ListVpcPeeringsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcPeeringsRequest.

        每页返回的个数

        :param limit: The limit of this ListVpcPeeringsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpcPeeringsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpcPeeringsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListVpcPeeringsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListVpcPeeringsRequest.

        按照peering_id过滤查询

        :return: The id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcPeeringsRequest.

        按照peering_id过滤查询

        :param id: The id of this ListVpcPeeringsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListVpcPeeringsRequest.

        功能说明：按照peering_name过查询  取值范围：最大长度不超过64

        :return: The name of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVpcPeeringsRequest.

        功能说明：按照peering_name过查询  取值范围：最大长度不超过64

        :param name: The name of this ListVpcPeeringsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListVpcPeeringsRequest.

        根据status进行过滤  - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。

        :return: The status of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVpcPeeringsRequest.

        根据status进行过滤  - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。

        :param status: The status of this ListVpcPeeringsRequest.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListVpcPeeringsRequest.

        按照项目ID过滤查询

        :return: The tenant_id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListVpcPeeringsRequest.

        按照项目ID过滤查询

        :param tenant_id: The tenant_id of this ListVpcPeeringsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListVpcPeeringsRequest.

        根据vpc ID过滤查询

        :return: The vpc_id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListVpcPeeringsRequest.

        根据vpc ID过滤查询

        :param vpc_id: The vpc_id of this ListVpcPeeringsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListVpcPeeringsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
