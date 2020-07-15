# coding: utf-8

import pprint
import re

import six





class InstanceConfigResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'image_ref': 'str',
        'disk': 'list[Disk]',
        'key_name': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'admin_pass': 'str',
        'personality': 'Personality',
        'public_ip': 'PublicIp',
        'user_data': 'str',
        'metadata': 'MetaData',
        'security_groups': 'list[SecurityGroups]',
        'server_group_id': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'image_ref': 'imageRef',
        'disk': 'disk',
        'key_name': 'key_name',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'admin_pass': 'adminPass',
        'personality': 'personality',
        'public_ip': 'public_ip',
        'user_data': 'user_data',
        'metadata': 'metadata',
        'security_groups': 'security_groups',
        'server_group_id': 'server_group_id',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, flavor_ref=None, image_ref=None, disk=None, key_name=None, instance_name=None, instance_id=None, admin_pass=None, personality=None, public_ip=None, user_data=None, metadata=None, security_groups=None, server_group_id=None, tenancy=None, dedicated_host_id=None):
        """InstanceConfigResult - a model defined in huaweicloud sdk"""
        
        

        self._flavor_ref = None
        self._image_ref = None
        self._disk = None
        self._key_name = None
        self._instance_name = None
        self._instance_id = None
        self._admin_pass = None
        self._personality = None
        self._public_ip = None
        self._user_data = None
        self._metadata = None
        self._security_groups = None
        self._server_group_id = None
        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if image_ref is not None:
            self.image_ref = image_ref
        if disk is not None:
            self.disk = disk
        if key_name is not None:
            self.key_name = key_name
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if personality is not None:
            self.personality = personality
        if public_ip is not None:
            self.public_ip = public_ip
        if user_data is not None:
            self.user_data = user_data
        if metadata is not None:
            self.metadata = metadata
        if security_groups is not None:
            self.security_groups = security_groups
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this InstanceConfigResult.

        云服务器的规格ID。

        :return: The flavor_ref of this InstanceConfigResult.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this InstanceConfigResult.

        云服务器的规格ID。

        :param flavor_ref: The flavor_ref of this InstanceConfigResult.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def image_ref(self):
        """Gets the image_ref of this InstanceConfigResult.

        镜像ID，同image_id。

        :return: The image_ref of this InstanceConfigResult.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this InstanceConfigResult.

        镜像ID，同image_id。

        :param image_ref: The image_ref of this InstanceConfigResult.
        :type: str
        """
        self._image_ref = image_ref

    @property
    def disk(self):
        """Gets the disk of this InstanceConfigResult.

        磁盘组信息。

        :return: The disk of this InstanceConfigResult.
        :rtype: list[Disk]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this InstanceConfigResult.

        磁盘组信息。

        :param disk: The disk of this InstanceConfigResult.
        :type: list[Disk]
        """
        self._disk = disk

    @property
    def key_name(self):
        """Gets the key_name of this InstanceConfigResult.

        登录云服务器的SSH密钥名称。

        :return: The key_name of this InstanceConfigResult.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this InstanceConfigResult.

        登录云服务器的SSH密钥名称。

        :param key_name: The key_name of this InstanceConfigResult.
        :type: str
        """
        self._key_name = key_name

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceConfigResult.

        该参数为预留字段。

        :return: The instance_name of this InstanceConfigResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceConfigResult.

        该参数为预留字段。

        :param instance_name: The instance_name of this InstanceConfigResult.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceConfigResult.

        该参数为预留字段。

        :return: The instance_id of this InstanceConfigResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceConfigResult.

        该参数为预留字段。

        :param instance_id: The instance_id of this InstanceConfigResult.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def admin_pass(self):
        """Gets the admin_pass of this InstanceConfigResult.

        登录云服务器的密码，非明文回显。

        :return: The admin_pass of this InstanceConfigResult.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this InstanceConfigResult.

        登录云服务器的密码，非明文回显。

        :param admin_pass: The admin_pass of this InstanceConfigResult.
        :type: str
        """
        self._admin_pass = admin_pass

    @property
    def personality(self):
        """Gets the personality of this InstanceConfigResult.


        :return: The personality of this InstanceConfigResult.
        :rtype: Personality
        """
        return self._personality

    @personality.setter
    def personality(self, personality):
        """Sets the personality of this InstanceConfigResult.


        :param personality: The personality of this InstanceConfigResult.
        :type: Personality
        """
        self._personality = personality

    @property
    def public_ip(self):
        """Gets the public_ip of this InstanceConfigResult.


        :return: The public_ip of this InstanceConfigResult.
        :rtype: PublicIp
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this InstanceConfigResult.


        :param public_ip: The public_ip of this InstanceConfigResult.
        :type: PublicIp
        """
        self._public_ip = public_ip

    @property
    def user_data(self):
        """Gets the user_data of this InstanceConfigResult.

        cloud-init用户数据，base64格式编码。

        :return: The user_data of this InstanceConfigResult.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this InstanceConfigResult.

        cloud-init用户数据，base64格式编码。

        :param user_data: The user_data of this InstanceConfigResult.
        :type: str
        """
        self._user_data = user_data

    @property
    def metadata(self):
        """Gets the metadata of this InstanceConfigResult.


        :return: The metadata of this InstanceConfigResult.
        :rtype: MetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InstanceConfigResult.


        :param metadata: The metadata of this InstanceConfigResult.
        :type: MetaData
        """
        self._metadata = metadata

    @property
    def security_groups(self):
        """Gets the security_groups of this InstanceConfigResult.

        安全组信息。

        :return: The security_groups of this InstanceConfigResult.
        :rtype: list[SecurityGroups]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this InstanceConfigResult.

        安全组信息。

        :param security_groups: The security_groups of this InstanceConfigResult.
        :type: list[SecurityGroups]
        """
        self._security_groups = security_groups

    @property
    def server_group_id(self):
        """Gets the server_group_id of this InstanceConfigResult.

        云服务器组ID。

        :return: The server_group_id of this InstanceConfigResult.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this InstanceConfigResult.

        云服务器组ID。

        :param server_group_id: The server_group_id of this InstanceConfigResult.
        :type: str
        """
        self._server_group_id = server_group_id

    @property
    def tenancy(self):
        """Gets the tenancy of this InstanceConfigResult.

        在专属主机上创建弹性云服务器。

        :return: The tenancy of this InstanceConfigResult.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this InstanceConfigResult.

        在专属主机上创建弹性云服务器。

        :param tenancy: The tenancy of this InstanceConfigResult.
        :type: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this InstanceConfigResult.

        专属主机的ID。

        :return: The dedicated_host_id of this InstanceConfigResult.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this InstanceConfigResult.

        专属主机的ID。

        :param dedicated_host_id: The dedicated_host_id of this InstanceConfigResult.
        :type: str
        """
        self._dedicated_host_id = dedicated_host_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
