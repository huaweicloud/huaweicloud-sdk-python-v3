# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcPeeringInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'status': 'str',
        'tenant_id': 'str',
        'vpc_id': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, id=None, limit=None, marker=None, name=None, status=None, tenant_id=None, vpc_id=None):
        r"""ListVpcPeeringInfosRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 对等连接的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type id: list[str]
        :param limit: **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。
        :type limit: int
        :param marker: **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 对等连接的资源ID。
        :type marker: str
        :param name: **参数解释**： 对等连接的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。
        :type name: list[str]
        :param status: **参数解释**： 对等连接的状态，填写后按照状态进行过滤。 **取值范围**： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：生效的。
        :type status: str
        :param tenant_id: **参数解释**： 对等连接的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param vpc_id: **参数解释**： 对等连接两端的VPC ID，填写后按照VPC ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type vpc_id: list[str]
        """
        
        

        self._id = None
        self._limit = None
        self._marker = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._vpc_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def id(self):
        r"""Gets the id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The id of this ListVpcPeeringInfosRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param id: The id of this ListVpcPeeringInfosRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListVpcPeeringInfosRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。

        :return: The limit of this ListVpcPeeringInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVpcPeeringInfosRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。

        :param limit: The limit of this ListVpcPeeringInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVpcPeeringInfosRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 对等连接的资源ID。

        :return: The marker of this ListVpcPeeringInfosRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVpcPeeringInfosRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 对等连接的资源ID。

        :param marker: The marker of this ListVpcPeeringInfosRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        r"""Gets the name of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :return: The name of this ListVpcPeeringInfosRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :param name: The name of this ListVpcPeeringInfosRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的状态，填写后按照状态进行过滤。 **取值范围**： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：生效的。

        :return: The status of this ListVpcPeeringInfosRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的状态，填写后按照状态进行过滤。 **取值范围**： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：生效的。

        :param status: The status of this ListVpcPeeringInfosRequest.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :return: The tenant_id of this ListVpcPeeringInfosRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this ListVpcPeeringInfosRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接两端的VPC ID，填写后按照VPC ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The vpc_id of this ListVpcPeeringInfosRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListVpcPeeringInfosRequest.

        **参数解释**： 对等连接两端的VPC ID，填写后按照VPC ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this ListVpcPeeringInfosRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVpcPeeringInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
