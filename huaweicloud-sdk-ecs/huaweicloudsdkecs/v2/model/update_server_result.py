# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'image': 'str',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'metadata': 'dict(str, str)',
        'addresses': 'dict(str, list[UpdateServerAddress])',
        'created': 'str',
        'host_id': 'str',
        'flavor': 'SimpleFlavor',
        'os_dc_fdisk_config': 'str',
        'user_id': 'str',
        'name': 'str',
        'progress': 'int',
        'links': 'list[Link]',
        'id': 'str',
        'updated': 'str',
        'locked': 'bool',
        'description': 'str',
        'tags': 'list[str]',
        'status': 'str',
        'os_ext_srv_att_rhostname': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'image': 'image',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'metadata': 'metadata',
        'addresses': 'addresses',
        'created': 'created',
        'host_id': 'hostId',
        'flavor': 'flavor',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'user_id': 'user_id',
        'name': 'name',
        'progress': 'progress',
        'links': 'links',
        'id': 'id',
        'updated': 'updated',
        'locked': 'locked',
        'description': 'description',
        'tags': 'tags',
        'status': 'status',
        'os_ext_srv_att_rhostname': 'OS-EXT-SRV-ATTR:hostname'
    }

    def __init__(self, tenant_id=None, image=None, access_i_pv4=None, access_i_pv6=None, metadata=None, addresses=None, created=None, host_id=None, flavor=None, os_dc_fdisk_config=None, user_id=None, name=None, progress=None, links=None, id=None, updated=None, locked=None, description=None, tags=None, status=None, os_ext_srv_att_rhostname=None):
        """UpdateServerResult

        The model defined in huaweicloud sdk

        :param tenant_id: 项目ID。
        :type tenant_id: str
        :param image: 镜像ID。
        :type image: str
        :param access_i_pv4: 预留属性。
        :type access_i_pv4: str
        :param access_i_pv6: 预留属性。
        :type access_i_pv6: str
        :param metadata: 云服务器元数据。
        :type metadata: dict(str, str)
        :param addresses: 弹性云服务器的网络属性。
        :type addresses: dict(str, list[UpdateServerAddress])
        :param created: 弹性云服务器创建时间。  时间格式例如：2019-05-22T03:19:19Z
        :type created: str
        :param host_id: 弹性云服务器所在主机的主机ID。
        :type host_id: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkecs.v2.SimpleFlavor`
        :param os_dc_fdisk_config: 扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。
        :type os_dc_fdisk_config: str
        :param user_id: 创建弹性云服务器的用户ID，格式为UUID。
        :type user_id: str
        :param name: 弹性云服务器名称。
        :type name: str
        :param progress: 弹性云服务器进度。
        :type progress: int
        :param links: 云服务器相关标记快捷链接信息。
        :type links: list[:class:`huaweicloudsdkecs.v2.Link`]
        :param id: 弹性云服务器ID，格式为UUID。
        :type id: str
        :param updated: 弹性云服务器更新时间。  时间格式例如：2019-05-22T03:30:52Z
        :type updated: str
        :param locked: 弹性云服务器是否为锁定状态。  - true：锁定 - false：未锁定
        :type locked: bool
        :param description: 弹性云服务器的描述信息。
        :type description: str
        :param tags: 云服务器的标签列表。  微版本2.26后支持，如果不使用微版本查询，响应中无tags字段。  系统近期对标签功能进行了升级，升级后，返回的tag值遵循如下规则：  - key与value使用“&#x3D;”连接，如“key&#x3D;value”。 - 如果value为空字符串，则仅返回key。 - key与value使用“&#x3D;”连接，如“key&#x3D;value”。 - 如果value为空字符串，则仅返回key。
        :type tags: list[str]
        :param status: 弹性云服务器状态。  取值范围：  ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)
        :type status: str
        :param os_ext_srv_att_rhostname: 弹性云服务器的主机名。
        :type os_ext_srv_att_rhostname: str
        """
        
        

        self._tenant_id = None
        self._image = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._metadata = None
        self._addresses = None
        self._created = None
        self._host_id = None
        self._flavor = None
        self._os_dc_fdisk_config = None
        self._user_id = None
        self._name = None
        self._progress = None
        self._links = None
        self._id = None
        self._updated = None
        self._locked = None
        self._description = None
        self._tags = None
        self._status = None
        self._os_ext_srv_att_rhostname = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.image = image
        self.access_i_pv4 = access_i_pv4
        self.access_i_pv6 = access_i_pv6
        self.metadata = metadata
        self.addresses = addresses
        self.created = created
        self.host_id = host_id
        self.flavor = flavor
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        self.user_id = user_id
        self.name = name
        self.progress = progress
        self.links = links
        self.id = id
        self.updated = updated
        if locked is not None:
            self.locked = locked
        if description is not None:
            self.description = description
        self.tags = tags
        self.status = status
        self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UpdateServerResult.

        项目ID。

        :return: The tenant_id of this UpdateServerResult.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UpdateServerResult.

        项目ID。

        :param tenant_id: The tenant_id of this UpdateServerResult.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def image(self):
        """Gets the image of this UpdateServerResult.

        镜像ID。

        :return: The image of this UpdateServerResult.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this UpdateServerResult.

        镜像ID。

        :param image: The image of this UpdateServerResult.
        :type image: str
        """
        self._image = image

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this UpdateServerResult.

        预留属性。

        :return: The access_i_pv4 of this UpdateServerResult.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this UpdateServerResult.

        预留属性。

        :param access_i_pv4: The access_i_pv4 of this UpdateServerResult.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this UpdateServerResult.

        预留属性。

        :return: The access_i_pv6 of this UpdateServerResult.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this UpdateServerResult.

        预留属性。

        :param access_i_pv6: The access_i_pv6 of this UpdateServerResult.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def metadata(self):
        """Gets the metadata of this UpdateServerResult.

        云服务器元数据。

        :return: The metadata of this UpdateServerResult.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateServerResult.

        云服务器元数据。

        :param metadata: The metadata of this UpdateServerResult.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def addresses(self):
        """Gets the addresses of this UpdateServerResult.

        弹性云服务器的网络属性。

        :return: The addresses of this UpdateServerResult.
        :rtype: dict(str, list[UpdateServerAddress])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this UpdateServerResult.

        弹性云服务器的网络属性。

        :param addresses: The addresses of this UpdateServerResult.
        :type addresses: dict(str, list[UpdateServerAddress])
        """
        self._addresses = addresses

    @property
    def created(self):
        """Gets the created of this UpdateServerResult.

        弹性云服务器创建时间。  时间格式例如：2019-05-22T03:19:19Z

        :return: The created of this UpdateServerResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UpdateServerResult.

        弹性云服务器创建时间。  时间格式例如：2019-05-22T03:19:19Z

        :param created: The created of this UpdateServerResult.
        :type created: str
        """
        self._created = created

    @property
    def host_id(self):
        """Gets the host_id of this UpdateServerResult.

        弹性云服务器所在主机的主机ID。

        :return: The host_id of this UpdateServerResult.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this UpdateServerResult.

        弹性云服务器所在主机的主机ID。

        :param host_id: The host_id of this UpdateServerResult.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def flavor(self):
        """Gets the flavor of this UpdateServerResult.


        :return: The flavor of this UpdateServerResult.
        :rtype: :class:`huaweicloudsdkecs.v2.SimpleFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this UpdateServerResult.


        :param flavor: The flavor of this UpdateServerResult.
        :type flavor: :class:`huaweicloudsdkecs.v2.SimpleFlavor`
        """
        self._flavor = flavor

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this UpdateServerResult.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :return: The os_dc_fdisk_config of this UpdateServerResult.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this UpdateServerResult.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this UpdateServerResult.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def user_id(self):
        """Gets the user_id of this UpdateServerResult.

        创建弹性云服务器的用户ID，格式为UUID。

        :return: The user_id of this UpdateServerResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UpdateServerResult.

        创建弹性云服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this UpdateServerResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this UpdateServerResult.

        弹性云服务器名称。

        :return: The name of this UpdateServerResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateServerResult.

        弹性云服务器名称。

        :param name: The name of this UpdateServerResult.
        :type name: str
        """
        self._name = name

    @property
    def progress(self):
        """Gets the progress of this UpdateServerResult.

        弹性云服务器进度。

        :return: The progress of this UpdateServerResult.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this UpdateServerResult.

        弹性云服务器进度。

        :param progress: The progress of this UpdateServerResult.
        :type progress: int
        """
        self._progress = progress

    @property
    def links(self):
        """Gets the links of this UpdateServerResult.

        云服务器相关标记快捷链接信息。

        :return: The links of this UpdateServerResult.
        :rtype: list[:class:`huaweicloudsdkecs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpdateServerResult.

        云服务器相关标记快捷链接信息。

        :param links: The links of this UpdateServerResult.
        :type links: list[:class:`huaweicloudsdkecs.v2.Link`]
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this UpdateServerResult.

        弹性云服务器ID，格式为UUID。

        :return: The id of this UpdateServerResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateServerResult.

        弹性云服务器ID，格式为UUID。

        :param id: The id of this UpdateServerResult.
        :type id: str
        """
        self._id = id

    @property
    def updated(self):
        """Gets the updated of this UpdateServerResult.

        弹性云服务器更新时间。  时间格式例如：2019-05-22T03:30:52Z

        :return: The updated of this UpdateServerResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UpdateServerResult.

        弹性云服务器更新时间。  时间格式例如：2019-05-22T03:30:52Z

        :param updated: The updated of this UpdateServerResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def locked(self):
        """Gets the locked of this UpdateServerResult.

        弹性云服务器是否为锁定状态。  - true：锁定 - false：未锁定

        :return: The locked of this UpdateServerResult.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UpdateServerResult.

        弹性云服务器是否为锁定状态。  - true：锁定 - false：未锁定

        :param locked: The locked of this UpdateServerResult.
        :type locked: bool
        """
        self._locked = locked

    @property
    def description(self):
        """Gets the description of this UpdateServerResult.

        弹性云服务器的描述信息。

        :return: The description of this UpdateServerResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateServerResult.

        弹性云服务器的描述信息。

        :param description: The description of this UpdateServerResult.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateServerResult.

        云服务器的标签列表。  微版本2.26后支持，如果不使用微版本查询，响应中无tags字段。  系统近期对标签功能进行了升级，升级后，返回的tag值遵循如下规则：  - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。 - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。

        :return: The tags of this UpdateServerResult.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateServerResult.

        云服务器的标签列表。  微版本2.26后支持，如果不使用微版本查询，响应中无tags字段。  系统近期对标签功能进行了升级，升级后，返回的tag值遵循如下规则：  - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。 - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。

        :param tags: The tags of this UpdateServerResult.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this UpdateServerResult.

        弹性云服务器状态。  取值范围：  ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :return: The status of this UpdateServerResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateServerResult.

        弹性云服务器状态。  取值范围：  ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :param status: The status of this UpdateServerResult.
        :type status: str
        """
        self._status = status

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this UpdateServerResult.

        弹性云服务器的主机名。

        :return: The os_ext_srv_att_rhostname of this UpdateServerResult.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this UpdateServerResult.

        弹性云服务器的主机名。

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this UpdateServerResult.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

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
        if not isinstance(other, UpdateServerResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
