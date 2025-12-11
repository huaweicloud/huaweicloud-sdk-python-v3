# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVirsubnetCidrReservationsRequest:

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
        'virsubnet_id': 'list[str]',
        'cidr': 'list[str]',
        'ip_version': 'list[int]',
        'name': 'list[str]',
        'description': 'list[str]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'cidr': 'cidr',
        'ip_version': 'ip_version',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, marker=None, id=None, virsubnet_id=None, cidr=None, ip_version=None, name=None, description=None, enterprise_project_id=None):
        r"""ListVirsubnetCidrReservationsRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000
        :type limit: int
        :param marker: **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网预留网段的资源ID。
        :type marker: str
        :param id: **参数解释**： 子网预留网段的资源ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type id: list[str]
        :param virsubnet_id: **参数解释**： 子网预留网段所在的子网ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。
        :type virsubnet_id: list[str]
        :param cidr: **参数解释**： 子网预留网段的IP网段。可以使用该字段过滤子网预留网段，支持传入多个IP网段过滤。 **取值范围**： 不涉及。
        :type cidr: list[str]
        :param ip_version: **参数解释**： 子网预留网段所在子网的IP版本。可以使用该字段过滤子网预留网段，支持传入多个IP版本过滤。 **取值范围**： - 4：过滤出IPv4子网预留网段。 - 6：过滤出IPv6子网预留网段。
        :type ip_version: list[int]
        :param name: **参数解释**： 子网预留网段的名称。可以使用该字段过滤满足条件的子网预留网段，支持传入多个名称过滤。 **取值范围**： 不涉及。
        :type name: list[str]
        :param description: **参数解释**： 子网预留网段的描述信息。可以使用该字段过滤子网预留网段，支持传入多个描述信息进行过滤。 **取值范围**： 不涉及。
        :type description: list[str]
        :param enterprise_project_id: **参数解释**： 子网预留网段所属的企业项目ID。可以使用该字段过滤某个企业项目下的子网预留网段。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有有权限查看企业项目绑定的子网预留网段，请传参all_granted_eps。
        :type enterprise_project_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._virsubnet_id = None
        self._cidr = None
        self._ip_version = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if cidr is not None:
            self.cidr = cidr
        if ip_version is not None:
            self.ip_version = ip_version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000

        :return: The limit of this ListVirsubnetCidrReservationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 每页返回的资源个数。 **取值范围**： 0~2000

        :param limit: The limit of this ListVirsubnetCidrReservationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网预留网段的资源ID。

        :return: The marker of this ListVirsubnetCidrReservationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 分页查询起始的资源ID，为空时查询第一页。 **取值范围**： 子网预留网段的资源ID。

        :param marker: The marker of this ListVirsubnetCidrReservationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的资源ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The id of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的资源ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param id: The id of this ListVirsubnetCidrReservationsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所在的子网ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :return: The virsubnet_id of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所在的子网ID。可以使用该字段过滤子网预留网段，支持传入多个ID过滤。 **取值范围**： 不涉及。

        :param virsubnet_id: The virsubnet_id of this ListVirsubnetCidrReservationsRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def cidr(self):
        r"""Gets the cidr of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的IP网段。可以使用该字段过滤子网预留网段，支持传入多个IP网段过滤。 **取值范围**： 不涉及。

        :return: The cidr of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的IP网段。可以使用该字段过滤子网预留网段，支持传入多个IP网段过滤。 **取值范围**： 不涉及。

        :param cidr: The cidr of this ListVirsubnetCidrReservationsRequest.
        :type cidr: list[str]
        """
        self._cidr = cidr

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所在子网的IP版本。可以使用该字段过滤子网预留网段，支持传入多个IP版本过滤。 **取值范围**： - 4：过滤出IPv4子网预留网段。 - 6：过滤出IPv6子网预留网段。

        :return: The ip_version of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所在子网的IP版本。可以使用该字段过滤子网预留网段，支持传入多个IP版本过滤。 **取值范围**： - 4：过滤出IPv4子网预留网段。 - 6：过滤出IPv6子网预留网段。

        :param ip_version: The ip_version of this ListVirsubnetCidrReservationsRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def name(self):
        r"""Gets the name of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的名称。可以使用该字段过滤满足条件的子网预留网段，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :return: The name of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的名称。可以使用该字段过滤满足条件的子网预留网段，支持传入多个名称过滤。 **取值范围**： 不涉及。

        :param name: The name of this ListVirsubnetCidrReservationsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的描述信息。可以使用该字段过滤子网预留网段，支持传入多个描述信息进行过滤。 **取值范围**： 不涉及。

        :return: The description of this ListVirsubnetCidrReservationsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段的描述信息。可以使用该字段过滤子网预留网段，支持传入多个描述信息进行过滤。 **取值范围**： 不涉及。

        :param description: The description of this ListVirsubnetCidrReservationsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所属的企业项目ID。可以使用该字段过滤某个企业项目下的子网预留网段。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有有权限查看企业项目绑定的子网预留网段，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListVirsubnetCidrReservationsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVirsubnetCidrReservationsRequest.

        **参数解释**： 子网预留网段所属的企业项目ID。可以使用该字段过滤某个企业项目下的子网预留网段。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有有权限查看企业项目绑定的子网预留网段，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListVirsubnetCidrReservationsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListVirsubnetCidrReservationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
