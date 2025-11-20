# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Connection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[str]',
        'id': 'str',
        'instance_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'remote_infos': 'list[RemoteInfosResult]',
        'status': 'str',
        'virsubnet_id': 'str',
        'vpc_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'fixed_ips': 'fixed_ips',
        'id': 'id',
        'instance_id': 'instance_id',
        'name': 'name',
        'project_id': 'project_id',
        'remote_infos': 'remote_infos',
        'status': 'status',
        'virsubnet_id': 'virsubnet_id',
        'vpc_id': 'vpc_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, fixed_ips=None, id=None, instance_id=None, name=None, project_id=None, remote_infos=None, status=None, virsubnet_id=None, vpc_id=None, created_at=None, updated_at=None):
        r"""Connection

        The model defined in huaweicloud sdk

        :param fixed_ips: - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type fixed_ips: list[str]
        :param id: - 参数解释：二层连接的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type id: str
        :param instance_id: - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type instance_id: str
        :param name: - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param project_id: - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type project_id: str
        :param remote_infos: - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type remote_infos: list[:class:`huaweicloudsdkesw.v3.RemoteInfosResult`]
        :param status: - 参数解释：二层连接的状态。 - 约束限制：不涉及。 - 取值范围：   - pending：准备中   - connected：已连接   - disconnect：未连接   - failed：创建失败   - abnormal：异常 - 默认取值：不涉及。
        :type status: str
        :param virsubnet_id: - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type virsubnet_id: str
        :param vpc_id: - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type vpc_id: str
        :param created_at: - 参数解释：二层连接创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type created_at: datetime
        :param updated_at: - 参数解释：二层连接更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type updated_at: datetime
        """
        
        

        self._fixed_ips = None
        self._id = None
        self._instance_id = None
        self._name = None
        self._project_id = None
        self._remote_infos = None
        self._status = None
        self._virsubnet_id = None
        self._vpc_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.fixed_ips = fixed_ips
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.project_id = project_id
        self.remote_infos = remote_infos
        self.status = status
        self.virsubnet_id = virsubnet_id
        self.vpc_id = vpc_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this Connection.

        - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The fixed_ips of this Connection.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this Connection.

        - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param fixed_ips: The fixed_ips of this Connection.
        :type fixed_ips: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def id(self):
        r"""Gets the id of this Connection.

        - 参数解释：二层连接的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The id of this Connection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Connection.

        - 参数解释：二层连接的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param id: The id of this Connection.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Connection.

        - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The instance_id of this Connection.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Connection.

        - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param instance_id: The instance_id of this Connection.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this Connection.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this Connection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Connection.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this Connection.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Connection.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The project_id of this Connection.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Connection.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param project_id: The project_id of this Connection.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def remote_infos(self):
        r"""Gets the remote_infos of this Connection.

        - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The remote_infos of this Connection.
        :rtype: list[:class:`huaweicloudsdkesw.v3.RemoteInfosResult`]
        """
        return self._remote_infos

    @remote_infos.setter
    def remote_infos(self, remote_infos):
        r"""Sets the remote_infos of this Connection.

        - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param remote_infos: The remote_infos of this Connection.
        :type remote_infos: list[:class:`huaweicloudsdkesw.v3.RemoteInfosResult`]
        """
        self._remote_infos = remote_infos

    @property
    def status(self):
        r"""Gets the status of this Connection.

        - 参数解释：二层连接的状态。 - 约束限制：不涉及。 - 取值范围：   - pending：准备中   - connected：已连接   - disconnect：未连接   - failed：创建失败   - abnormal：异常 - 默认取值：不涉及。

        :return: The status of this Connection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Connection.

        - 参数解释：二层连接的状态。 - 约束限制：不涉及。 - 取值范围：   - pending：准备中   - connected：已连接   - disconnect：未连接   - failed：创建失败   - abnormal：异常 - 默认取值：不涉及。

        :param status: The status of this Connection.
        :type status: str
        """
        self._status = status

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this Connection.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The virsubnet_id of this Connection.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this Connection.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param virsubnet_id: The virsubnet_id of this Connection.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Connection.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The vpc_id of this Connection.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Connection.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param vpc_id: The vpc_id of this Connection.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def created_at(self):
        r"""Gets the created_at of this Connection.

        - 参数解释：二层连接创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The created_at of this Connection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Connection.

        - 参数解释：二层连接创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param created_at: The created_at of this Connection.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Connection.

        - 参数解释：二层连接更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The updated_at of this Connection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Connection.

        - 参数解释：二层连接更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param updated_at: The updated_at of this Connection.
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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
