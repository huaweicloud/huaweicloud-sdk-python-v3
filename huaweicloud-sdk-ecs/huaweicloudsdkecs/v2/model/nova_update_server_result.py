# coding: utf-8

import pprint
import re

import six


class NovaUpdateServerResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'tenant_id': 'str',
        'image': 'str',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'metadata': 'dict(str, str)',
        'addresses': 'dict(str, list[NovaNetwork])',
        'created': 'str',
        'host_id': 'str',
        'flavor': 'NovaServerFlavor',
        'os_dc_fdisk_config': 'str',
        'user_id': 'str',
        'name': 'str',
        'progress': 'int',
        'links': 'list[NovaLink]',
        'id': 'str',
        'updated': 'str',
        'locked': 'bool',
        'description': 'str',
        'tags': 'list[str]',
        'status': 'str'
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
        'status': 'status'
    }

    def __init__(self, tenant_id=None, image=None, access_i_pv4=None, access_i_pv6=None, metadata=None, addresses=None, created=None, host_id=None, flavor=None, os_dc_fdisk_config=None, user_id=None, name=None, progress=None, links=None, id=None, updated=None, locked=None, description=None, tags=None, status=None):  # noqa: E501
        """NovaUpdateServerResult - a model defined in huaweicloud sdk"""

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

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NovaUpdateServerResult.

        项目ID。

        :return: The tenant_id of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NovaUpdateServerResult.

        项目ID。

        :param tenant_id: The tenant_id of this NovaUpdateServerResult.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def image(self):
        """Gets the image of this NovaUpdateServerResult.

        镜像ID。

        :return: The image of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NovaUpdateServerResult.

        镜像ID。

        :param image: The image of this NovaUpdateServerResult.
        :type: str
        """
        self._image = image

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this NovaUpdateServerResult.

        预留属性。

        :return: The access_i_pv4 of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this NovaUpdateServerResult.

        预留属性。

        :param access_i_pv4: The access_i_pv4 of this NovaUpdateServerResult.
        :type: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this NovaUpdateServerResult.

        预留属性。

        :return: The access_i_pv6 of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this NovaUpdateServerResult.

        预留属性。

        :param access_i_pv6: The access_i_pv6 of this NovaUpdateServerResult.
        :type: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def metadata(self):
        """Gets the metadata of this NovaUpdateServerResult.

        云服务器元数据。

        :return: The metadata of this NovaUpdateServerResult.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaUpdateServerResult.

        云服务器元数据。

        :param metadata: The metadata of this NovaUpdateServerResult.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def addresses(self):
        """Gets the addresses of this NovaUpdateServerResult.

        云服务器对应的网络地址信息。

        :return: The addresses of this NovaUpdateServerResult.
        :rtype: dict(str, list[NovaNetwork])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this NovaUpdateServerResult.

        云服务器对应的网络地址信息。

        :param addresses: The addresses of this NovaUpdateServerResult.
        :type: dict(str, list[NovaNetwork])
        """
        self._addresses = addresses

    @property
    def created(self):
        """Gets the created of this NovaUpdateServerResult.

        云服务器创建时间。

        :return: The created of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NovaUpdateServerResult.

        云服务器创建时间。

        :param created: The created of this NovaUpdateServerResult.
        :type: str
        """
        self._created = created

    @property
    def host_id(self):
        """Gets the host_id of this NovaUpdateServerResult.

        云服务器对应的主机ID。

        :return: The host_id of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this NovaUpdateServerResult.

        云服务器对应的主机ID。

        :param host_id: The host_id of this NovaUpdateServerResult.
        :type: str
        """
        self._host_id = host_id

    @property
    def flavor(self):
        """Gets the flavor of this NovaUpdateServerResult.


        :return: The flavor of this NovaUpdateServerResult.
        :rtype: NovaServerFlavor
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this NovaUpdateServerResult.


        :param flavor: The flavor of this NovaUpdateServerResult.
        :type: NovaServerFlavor
        """
        self._flavor = flavor

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this NovaUpdateServerResult.

        扩展属性，磁盘配置方式。对镜像启动云服务器生效。

        :return: The os_dc_fdisk_config of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this NovaUpdateServerResult.

        扩展属性，磁盘配置方式。对镜像启动云服务器生效。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this NovaUpdateServerResult.
        :type: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def user_id(self):
        """Gets the user_id of this NovaUpdateServerResult.

        云服务器所属用户ID。

        :return: The user_id of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaUpdateServerResult.

        云服务器所属用户ID。

        :param user_id: The user_id of this NovaUpdateServerResult.
        :type: str
        """
        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this NovaUpdateServerResult.

        云服务器名称。

        :return: The name of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaUpdateServerResult.

        云服务器名称。

        :param name: The name of this NovaUpdateServerResult.
        :type: str
        """
        self._name = name

    @property
    def progress(self):
        """Gets the progress of this NovaUpdateServerResult.

        预留属性

        :return: The progress of this NovaUpdateServerResult.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this NovaUpdateServerResult.

        预留属性

        :param progress: The progress of this NovaUpdateServerResult.
        :type: int
        """
        self._progress = progress

    @property
    def links(self):
        """Gets the links of this NovaUpdateServerResult.

        云服务器相关标记快捷链接信息。

        :return: The links of this NovaUpdateServerResult.
        :rtype: list[NovaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaUpdateServerResult.

        云服务器相关标记快捷链接信息。

        :param links: The links of this NovaUpdateServerResult.
        :type: list[NovaLink]
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this NovaUpdateServerResult.

        云服务器唯一标识。

        :return: The id of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaUpdateServerResult.

        云服务器唯一标识。

        :param id: The id of this NovaUpdateServerResult.
        :type: str
        """
        self._id = id

    @property
    def updated(self):
        """Gets the updated of this NovaUpdateServerResult.

        云服务器上一次更新时间。  时间格式例如：2019-05-22T03:19:19Z

        :return: The updated of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NovaUpdateServerResult.

        云服务器上一次更新时间。  时间格式例如：2019-05-22T03:19:19Z

        :param updated: The updated of this NovaUpdateServerResult.
        :type: str
        """
        self._updated = updated

    @property
    def locked(self):
        """Gets the locked of this NovaUpdateServerResult.

          当云服务器被锁时为True，否则为False。  微版本2.9后支持

        :return: The locked of this NovaUpdateServerResult.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this NovaUpdateServerResult.

          当云服务器被锁时为True，否则为False。  微版本2.9后支持

        :param locked: The locked of this NovaUpdateServerResult.
        :type: bool
        """
        self._locked = locked

    @property
    def description(self):
        """Gets the description of this NovaUpdateServerResult.

          弹性云服务器的描述信息。  微版本2.19后支持

        :return: The description of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaUpdateServerResult.

          弹性云服务器的描述信息。  微版本2.19后支持

        :param description: The description of this NovaUpdateServerResult.
        :type: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this NovaUpdateServerResult.

        云服务器的标签列表。  微版本2.26后支持，如果不使用微版本查询，响应中无tags字段。  系统近期对标签功能进行了升级，升级后，返回的tag值遵循如下规则：  - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。 - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。

        :return: The tags of this NovaUpdateServerResult.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NovaUpdateServerResult.

        云服务器的标签列表。  微版本2.26后支持，如果不使用微版本查询，响应中无tags字段。  系统近期对标签功能进行了升级，升级后，返回的tag值遵循如下规则：  - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。 - key与value使用“=”连接，如“key=value”。 - 如果value为空字符串，则仅返回key。

        :param tags: The tags of this NovaUpdateServerResult.
        :type: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this NovaUpdateServerResult.

        云服务器当前状态信息。  取值范围： ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE

        :return: The status of this NovaUpdateServerResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaUpdateServerResult.

        云服务器当前状态信息。  取值范围： ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE

        :param status: The status of this NovaUpdateServerResult.
        :type: str
        """
        self._status = status

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaUpdateServerResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
