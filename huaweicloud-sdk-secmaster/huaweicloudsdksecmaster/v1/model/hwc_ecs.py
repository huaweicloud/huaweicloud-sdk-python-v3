# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEcs:

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
        'name': 'str',
        'protected_status': 'str',
        'description': 'str',
        'status': 'str',
        'locked': 'bool',
        'enterprise_project_id': 'str',
        'user_id': 'str',
        'project_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_status': 'str',
        'addresses': 'list[HwcEcsAddress]',
        'security_groups': 'list[HwcEcsSecurityGroup]',
        'availability_zone': 'str',
        'flavor': 'HwcEcsFlavor',
        'volumes_attached': 'list[HwcEcsVolume]',
        'metadata': 'HwcEcsMetadata',
        'updated': 'str',
        'created': 'str',
        'key_name': 'str',
        'scheduler_hints': 'HwcEcsSchedulerHint',
        'hypervisor': 'HwcEcsHypervisor'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protected_status': 'protected_status',
        'description': 'description',
        'status': 'status',
        'locked': 'locked',
        'enterprise_project_id': 'enterprise_project_id',
        'user_id': 'user_id',
        'project_id': 'project_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_status': 'host_status',
        'addresses': 'addresses',
        'security_groups': 'security_groups',
        'availability_zone': 'availability_zone',
        'flavor': 'flavor',
        'volumes_attached': 'volumes_attached',
        'metadata': 'metadata',
        'updated': 'updated',
        'created': 'created',
        'key_name': 'key_name',
        'scheduler_hints': 'scheduler_hints',
        'hypervisor': 'hypervisor'
    }

    def __init__(self, id=None, name=None, protected_status=None, description=None, status=None, locked=None, enterprise_project_id=None, user_id=None, project_id=None, host_id=None, host_name=None, host_status=None, addresses=None, security_groups=None, availability_zone=None, flavor=None, volumes_attached=None, metadata=None, updated=None, created=None, key_name=None, scheduler_hints=None, hypervisor=None):
        r"""HwcEcs

        The model defined in huaweicloud sdk

        :param id: 弹性云服务器ID，格式为UUID。
        :type id: str
        :param name: 弹性云服务器名称。
        :type name: str
        :param protected_status: 主机安全开启状态：OPEN | CLOSE
        :type protected_status: str
        :param description: 弹性云服务器的描述信息。
        :type description: str
        :param status: 弹性云服务器状态。 取值范围： ACTIVE、BUILD、ERROR、HARD_REBOOT、MIGRATING、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、VERIFY_RESIZE、DELETED
        :type status: str
        :param locked: 弹性云服务器是否为锁定状态。 true：锁定 false：未锁定
        :type locked: bool
        :param enterprise_project_id: 弹性云服务器所属的企业项目ID。
        :type enterprise_project_id: str
        :param user_id: 创建弹性云服务器的用户ID，格式为UUID。
        :type user_id: str
        :param project_id: 弹性云服务器所属项目id，格式为UUID。
        :type project_id: str
        :param host_id: 弹性云服务器所在主机的主机ID。
        :type host_id: str
        :param host_name: 弹性云服务器所在主机的主机名称。
        :type host_name: str
        :param host_status: 云服务器所在主机状态。 UP：服务正常 UNKNOWN：状态未知 DOWN：服务异常 MAINTENANCE：维护状态 空字符串：弹性云服务器无主机信息
        :type host_status: str
        :param addresses: 弹性云服务器的网络属性。
        :type addresses: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsAddress`]
        :param security_groups: 弹性云服务器所属安全组列表。
        :type security_groups: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsSecurityGroup`]
        :param availability_zone: 弹性云服务器所在可用区名称。
        :type availability_zone: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdksecmaster.v1.HwcEcsFlavor`
        :param volumes_attached: 挂载到弹性云服务器上的磁盘。
        :type volumes_attached: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsVolume`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdksecmaster.v1.HwcEcsMetadata`
        :param updated: 弹性云服务器最近一次更新时间，例如开机、关机、重启等操作。 时间格式例如：2019-05-22T03:30:52Z
        :type updated: str
        :param created: 弹性云服务器创建时间。 时间格式例如：2019-05-22T03:19:19Z
        :type created: str
        :param key_name: 弹性云服务器使用的密钥对名称。
        :type key_name: str
        :param scheduler_hints: 
        :type scheduler_hints: :class:`huaweicloudsdksecmaster.v1.HwcEcsSchedulerHint`
        :param hypervisor: 
        :type hypervisor: :class:`huaweicloudsdksecmaster.v1.HwcEcsHypervisor`
        """
        
        

        self._id = None
        self._name = None
        self._protected_status = None
        self._description = None
        self._status = None
        self._locked = None
        self._enterprise_project_id = None
        self._user_id = None
        self._project_id = None
        self._host_id = None
        self._host_name = None
        self._host_status = None
        self._addresses = None
        self._security_groups = None
        self._availability_zone = None
        self._flavor = None
        self._volumes_attached = None
        self._metadata = None
        self._updated = None
        self._created = None
        self._key_name = None
        self._scheduler_hints = None
        self._hypervisor = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.protected_status = protected_status
        self.description = description
        self.status = status
        self.locked = locked
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.user_id = user_id
        self.project_id = project_id
        self.host_id = host_id
        self.host_name = host_name
        self.host_status = host_status
        self.addresses = addresses
        self.security_groups = security_groups
        self.availability_zone = availability_zone
        if flavor is not None:
            self.flavor = flavor
        self.volumes_attached = volumes_attached
        self.metadata = metadata
        self.updated = updated
        self.created = created
        if key_name is not None:
            self.key_name = key_name
        if scheduler_hints is not None:
            self.scheduler_hints = scheduler_hints
        if hypervisor is not None:
            self.hypervisor = hypervisor

    @property
    def id(self):
        r"""Gets the id of this HwcEcs.

        弹性云服务器ID，格式为UUID。

        :return: The id of this HwcEcs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcEcs.

        弹性云服务器ID，格式为UUID。

        :param id: The id of this HwcEcs.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HwcEcs.

        弹性云服务器名称。

        :return: The name of this HwcEcs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcEcs.

        弹性云服务器名称。

        :param name: The name of this HwcEcs.
        :type name: str
        """
        self._name = name

    @property
    def protected_status(self):
        r"""Gets the protected_status of this HwcEcs.

        主机安全开启状态：OPEN | CLOSE

        :return: The protected_status of this HwcEcs.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        r"""Sets the protected_status of this HwcEcs.

        主机安全开启状态：OPEN | CLOSE

        :param protected_status: The protected_status of this HwcEcs.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def description(self):
        r"""Gets the description of this HwcEcs.

        弹性云服务器的描述信息。

        :return: The description of this HwcEcs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HwcEcs.

        弹性云服务器的描述信息。

        :param description: The description of this HwcEcs.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this HwcEcs.

        弹性云服务器状态。 取值范围： ACTIVE、BUILD、ERROR、HARD_REBOOT、MIGRATING、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、VERIFY_RESIZE、DELETED

        :return: The status of this HwcEcs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HwcEcs.

        弹性云服务器状态。 取值范围： ACTIVE、BUILD、ERROR、HARD_REBOOT、MIGRATING、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、VERIFY_RESIZE、DELETED

        :param status: The status of this HwcEcs.
        :type status: str
        """
        self._status = status

    @property
    def locked(self):
        r"""Gets the locked of this HwcEcs.

        弹性云服务器是否为锁定状态。 true：锁定 false：未锁定

        :return: The locked of this HwcEcs.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this HwcEcs.

        弹性云服务器是否为锁定状态。 true：锁定 false：未锁定

        :param locked: The locked of this HwcEcs.
        :type locked: bool
        """
        self._locked = locked

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HwcEcs.

        弹性云服务器所属的企业项目ID。

        :return: The enterprise_project_id of this HwcEcs.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HwcEcs.

        弹性云服务器所属的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this HwcEcs.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def user_id(self):
        r"""Gets the user_id of this HwcEcs.

        创建弹性云服务器的用户ID，格式为UUID。

        :return: The user_id of this HwcEcs.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this HwcEcs.

        创建弹性云服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this HwcEcs.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def project_id(self):
        r"""Gets the project_id of this HwcEcs.

        弹性云服务器所属项目id，格式为UUID。

        :return: The project_id of this HwcEcs.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HwcEcs.

        弹性云服务器所属项目id，格式为UUID。

        :param project_id: The project_id of this HwcEcs.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this HwcEcs.

        弹性云服务器所在主机的主机ID。

        :return: The host_id of this HwcEcs.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HwcEcs.

        弹性云服务器所在主机的主机ID。

        :param host_id: The host_id of this HwcEcs.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HwcEcs.

        弹性云服务器所在主机的主机名称。

        :return: The host_name of this HwcEcs.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HwcEcs.

        弹性云服务器所在主机的主机名称。

        :param host_name: The host_name of this HwcEcs.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_status(self):
        r"""Gets the host_status of this HwcEcs.

        云服务器所在主机状态。 UP：服务正常 UNKNOWN：状态未知 DOWN：服务异常 MAINTENANCE：维护状态 空字符串：弹性云服务器无主机信息

        :return: The host_status of this HwcEcs.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this HwcEcs.

        云服务器所在主机状态。 UP：服务正常 UNKNOWN：状态未知 DOWN：服务异常 MAINTENANCE：维护状态 空字符串：弹性云服务器无主机信息

        :param host_status: The host_status of this HwcEcs.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def addresses(self):
        r"""Gets the addresses of this HwcEcs.

        弹性云服务器的网络属性。

        :return: The addresses of this HwcEcs.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsAddress`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this HwcEcs.

        弹性云服务器的网络属性。

        :param addresses: The addresses of this HwcEcs.
        :type addresses: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsAddress`]
        """
        self._addresses = addresses

    @property
    def security_groups(self):
        r"""Gets the security_groups of this HwcEcs.

        弹性云服务器所属安全组列表。

        :return: The security_groups of this HwcEcs.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this HwcEcs.

        弹性云服务器所属安全组列表。

        :param security_groups: The security_groups of this HwcEcs.
        :type security_groups: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this HwcEcs.

        弹性云服务器所在可用区名称。

        :return: The availability_zone of this HwcEcs.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this HwcEcs.

        弹性云服务器所在可用区名称。

        :param availability_zone: The availability_zone of this HwcEcs.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def flavor(self):
        r"""Gets the flavor of this HwcEcs.

        :return: The flavor of this HwcEcs.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEcsFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this HwcEcs.

        :param flavor: The flavor of this HwcEcs.
        :type flavor: :class:`huaweicloudsdksecmaster.v1.HwcEcsFlavor`
        """
        self._flavor = flavor

    @property
    def volumes_attached(self):
        r"""Gets the volumes_attached of this HwcEcs.

        挂载到弹性云服务器上的磁盘。

        :return: The volumes_attached of this HwcEcs.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsVolume`]
        """
        return self._volumes_attached

    @volumes_attached.setter
    def volumes_attached(self, volumes_attached):
        r"""Sets the volumes_attached of this HwcEcs.

        挂载到弹性云服务器上的磁盘。

        :param volumes_attached: The volumes_attached of this HwcEcs.
        :type volumes_attached: list[:class:`huaweicloudsdksecmaster.v1.HwcEcsVolume`]
        """
        self._volumes_attached = volumes_attached

    @property
    def metadata(self):
        r"""Gets the metadata of this HwcEcs.

        :return: The metadata of this HwcEcs.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEcsMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this HwcEcs.

        :param metadata: The metadata of this HwcEcs.
        :type metadata: :class:`huaweicloudsdksecmaster.v1.HwcEcsMetadata`
        """
        self._metadata = metadata

    @property
    def updated(self):
        r"""Gets the updated of this HwcEcs.

        弹性云服务器最近一次更新时间，例如开机、关机、重启等操作。 时间格式例如：2019-05-22T03:30:52Z

        :return: The updated of this HwcEcs.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this HwcEcs.

        弹性云服务器最近一次更新时间，例如开机、关机、重启等操作。 时间格式例如：2019-05-22T03:30:52Z

        :param updated: The updated of this HwcEcs.
        :type updated: str
        """
        self._updated = updated

    @property
    def created(self):
        r"""Gets the created of this HwcEcs.

        弹性云服务器创建时间。 时间格式例如：2019-05-22T03:19:19Z

        :return: The created of this HwcEcs.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this HwcEcs.

        弹性云服务器创建时间。 时间格式例如：2019-05-22T03:19:19Z

        :param created: The created of this HwcEcs.
        :type created: str
        """
        self._created = created

    @property
    def key_name(self):
        r"""Gets the key_name of this HwcEcs.

        弹性云服务器使用的密钥对名称。

        :return: The key_name of this HwcEcs.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this HwcEcs.

        弹性云服务器使用的密钥对名称。

        :param key_name: The key_name of this HwcEcs.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def scheduler_hints(self):
        r"""Gets the scheduler_hints of this HwcEcs.

        :return: The scheduler_hints of this HwcEcs.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEcsSchedulerHint`
        """
        return self._scheduler_hints

    @scheduler_hints.setter
    def scheduler_hints(self, scheduler_hints):
        r"""Sets the scheduler_hints of this HwcEcs.

        :param scheduler_hints: The scheduler_hints of this HwcEcs.
        :type scheduler_hints: :class:`huaweicloudsdksecmaster.v1.HwcEcsSchedulerHint`
        """
        self._scheduler_hints = scheduler_hints

    @property
    def hypervisor(self):
        r"""Gets the hypervisor of this HwcEcs.

        :return: The hypervisor of this HwcEcs.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEcsHypervisor`
        """
        return self._hypervisor

    @hypervisor.setter
    def hypervisor(self, hypervisor):
        r"""Sets the hypervisor of this HwcEcs.

        :param hypervisor: The hypervisor of this HwcEcs.
        :type hypervisor: :class:`huaweicloudsdksecmaster.v1.HwcEcsHypervisor`
        """
        self._hypervisor = hypervisor

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
        if not isinstance(other, HwcEcs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
