# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVirsubnetsRequest:

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
        'id': 'list[str]',
        'name': 'list[str]',
        'vpc_id': 'list[str]',
        'status': 'str',
        'scope': 'list[str]',
        'zone_id': 'list[str]',
        'description': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'status': 'status',
        'scope': 'scope',
        'zone_id': 'zone_id',
        'description': 'description'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, vpc_id=None, status=None, scope=None, zone_id=None, description=None):
        r"""ListVirsubnetsRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。
        :type limit: int
        :param marker: **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网的资源ID。
        :type marker: str
        :param id: **参数解释**： 子网的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type id: list[str]
        :param name: **参数解释**： 子网的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。
        :type name: list[str]
        :param vpc_id: **参数解释**： 子网所在VPC的资源ID，填写后按照VPC资源ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type vpc_id: list[str]
        :param status: **参数解释**： 子网的状态，填写后按照状态进行过滤，只支持传入单个状态过滤。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。
        :type status: str
        :param scope: **参数解释**： 子网的作用域，填写后按照作用域进行过滤，支持传入多个作用域过滤。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。
        :type scope: list[str]
        :param zone_id: **参数解释**： 子网的可用区ID，填写后按照可用区ID进行过滤，支持传入多个可用区ID过滤。 **取值范围**： 不涉及
        :type zone_id: list[str]
        :param description: **参数解释**： 子网的描述信息，填写后按照描述信息进行过滤，支持传入多个描述信息过滤。 **取值范围**： 不涉及。
        :type description: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._vpc_id = None
        self._status = None
        self._scope = None
        self._zone_id = None
        self._description = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if status is not None:
            self.status = status
        if scope is not None:
            self.scope = scope
        if zone_id is not None:
            self.zone_id = zone_id
        if description is not None:
            self.description = description

    @property
    def limit(self):
        r"""Gets the limit of this ListVirsubnetsRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。

        :return: The limit of this ListVirsubnetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVirsubnetsRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000。

        :param limit: The limit of this ListVirsubnetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVirsubnetsRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网的资源ID。

        :return: The marker of this ListVirsubnetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVirsubnetsRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网的资源ID。

        :param marker: The marker of this ListVirsubnetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListVirsubnetsRequest.

        **参数解释**： 子网的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The id of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVirsubnetsRequest.

        **参数解释**： 子网的资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param id: The id of this ListVirsubnetsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListVirsubnetsRequest.

        **参数解释**： 子网的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :return: The name of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVirsubnetsRequest.

        **参数解释**： 子网的名称，填写后按照名称进行过滤，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :param name: The name of this ListVirsubnetsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListVirsubnetsRequest.

        **参数解释**： 子网所在VPC的资源ID，填写后按照VPC资源ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The vpc_id of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListVirsubnetsRequest.

        **参数解释**： 子网所在VPC的资源ID，填写后按照VPC资源ID进行过滤，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this ListVirsubnetsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def status(self):
        r"""Gets the status of this ListVirsubnetsRequest.

        **参数解释**： 子网的状态，填写后按照状态进行过滤，只支持传入单个状态过滤。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。

        :return: The status of this ListVirsubnetsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVirsubnetsRequest.

        **参数解释**： 子网的状态，填写后按照状态进行过滤，只支持传入单个状态过滤。 **取值范围**： - ACTIVE：表示子网已挂载到VPC上。 - UNKNOWN：表示子网还未挂载到VPC上。 - ERROR：表示子网状态故障。

        :param status: The status of this ListVirsubnetsRequest.
        :type status: str
        """
        self._status = status

    @property
    def scope(self):
        r"""Gets the scope of this ListVirsubnetsRequest.

        **参数解释**： 子网的作用域，填写后按照作用域进行过滤，支持传入多个作用域过滤。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :return: The scope of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListVirsubnetsRequest.

        **参数解释**： 子网的作用域，填写后按照作用域进行过滤，支持传入多个作用域过滤。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :param scope: The scope of this ListVirsubnetsRequest.
        :type scope: list[str]
        """
        self._scope = scope

    @property
    def zone_id(self):
        r"""Gets the zone_id of this ListVirsubnetsRequest.

        **参数解释**： 子网的可用区ID，填写后按照可用区ID进行过滤，支持传入多个可用区ID过滤。 **取值范围**： 不涉及

        :return: The zone_id of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this ListVirsubnetsRequest.

        **参数解释**： 子网的可用区ID，填写后按照可用区ID进行过滤，支持传入多个可用区ID过滤。 **取值范围**： 不涉及

        :param zone_id: The zone_id of this ListVirsubnetsRequest.
        :type zone_id: list[str]
        """
        self._zone_id = zone_id

    @property
    def description(self):
        r"""Gets the description of this ListVirsubnetsRequest.

        **参数解释**： 子网的描述信息，填写后按照描述信息进行过滤，支持传入多个描述信息过滤。 **取值范围**： 不涉及。

        :return: The description of this ListVirsubnetsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListVirsubnetsRequest.

        **参数解释**： 子网的描述信息，填写后按照描述信息进行过滤，支持传入多个描述信息过滤。 **取值范围**： 不涉及。

        :param description: The description of this ListVirsubnetsRequest.
        :type description: list[str]
        """
        self._description = description

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
        if not isinstance(other, ListVirsubnetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
