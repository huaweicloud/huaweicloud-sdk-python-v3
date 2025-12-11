# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirsubnetCidrReservation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'virsubnet_id': 'str',
        'vpc_id': 'str',
        'ip_version': 'int',
        'cidr': 'str',
        'name': 'str',
        'description': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'vpc_id': 'vpc_id',
        'ip_version': 'ip_version',
        'cidr': 'cidr',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, virsubnet_id=None, vpc_id=None, ip_version=None, cidr=None, name=None, description=None, project_id=None, created_at=None, updated_at=None):
        r"""VirsubnetCidrReservation

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 子网预留网段的资源ID。子网预留网段创建成功后，会生成一个子网预留网段 ID，是子网预留网段对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。
        :type id: str
        :param virsubnet_id: **参数解释**： 子网预留网段所在子网的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type virsubnet_id: str
        :param vpc_id: **参数解释**： 子网预留网段所在VPC的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type vpc_id: str
        :param ip_version: **参数解释**： 子网预留网段的IP版本。 **取值范围**： - 4：IPv4 - 6：IPv6
        :type ip_version: int
        :param cidr: **参数解释**： 子网预留网段的IP网段。 **取值范围**： CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。
        :type cidr: str
        :param name: **参数解释**： 子网预留网段的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。
        :type name: str
        :param description: **参数解释**： 子网预留网段的描述信息。 **取值范围**： 0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param project_id: **参数解释**： 子网预留网段所属的项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param created_at: **参数解释**： 子网预留网段的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。
        :type created_at: datetime
        :param updated_at: **参数解释**： 子网预留网段最近一次更新的时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._virsubnet_id = None
        self._vpc_id = None
        self._ip_version = None
        self._cidr = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.virsubnet_id = virsubnet_id
        self.vpc_id = vpc_id
        self.ip_version = ip_version
        self.cidr = cidr
        self.name = name
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的资源ID。子网预留网段创建成功后，会生成一个子网预留网段 ID，是子网预留网段对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的资源ID。子网预留网段创建成功后，会生成一个子网预留网段 ID，是子网预留网段对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this VirsubnetCidrReservation.
        :type id: str
        """
        self._id = id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所在子网的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The virsubnet_id of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所在子网的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param virsubnet_id: The virsubnet_id of this VirsubnetCidrReservation.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所在VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The vpc_id of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所在VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param vpc_id: The vpc_id of this VirsubnetCidrReservation.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的IP版本。 **取值范围**： - 4：IPv4 - 6：IPv6

        :return: The ip_version of this VirsubnetCidrReservation.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的IP版本。 **取值范围**： - 4：IPv4 - 6：IPv6

        :param ip_version: The ip_version of this VirsubnetCidrReservation.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        r"""Gets the cidr of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的IP网段。 **取值范围**： CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。

        :return: The cidr of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的IP网段。 **取值范围**： CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。

        :param cidr: The cidr of this VirsubnetCidrReservation.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def name(self):
        r"""Gets the name of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。

        :return: The name of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的名称。 **取值范围**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。

        :param name: The name of this VirsubnetCidrReservation.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :return: The description of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :param description: The description of this VirsubnetCidrReservation.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所属的项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this VirsubnetCidrReservation.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段所属的项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this VirsubnetCidrReservation.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。

        :return: The created_at of this VirsubnetCidrReservation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段的创建时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。

        :param created_at: The created_at of this VirsubnetCidrReservation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段最近一次更新的时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。

        :return: The updated_at of this VirsubnetCidrReservation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this VirsubnetCidrReservation.

        **参数解释**： 子网预留网段最近一次更新的时间。 **取值范围**： UTC时间格式，yyyy-MM-ddTHH:mm:ssZ。

        :param updated_at: The updated_at of this VirsubnetCidrReservation.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, VirsubnetCidrReservation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
