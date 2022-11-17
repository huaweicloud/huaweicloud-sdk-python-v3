# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'disk': 'list[DiskResult]',
        'key_name': 'str',
        'key_fingerprint': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'admin_pass': 'str',
        'personality': 'list[PersonalityResult]',
        'public_ip': 'PublicipResult',
        'user_data': 'str',
        'metadata': 'VmMetaData',
        'security_groups': 'list[SecurityGroups]',
        'server_group_id': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str',
        'market_type': 'str',
        'multi_flavor_priority_policy': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'image_ref': 'imageRef',
        'disk': 'disk',
        'key_name': 'key_name',
        'key_fingerprint': 'key_fingerprint',
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
        'dedicated_host_id': 'dedicated_host_id',
        'market_type': 'market_type',
        'multi_flavor_priority_policy': 'multi_flavor_priority_policy'
    }

    def __init__(self, flavor_ref=None, image_ref=None, disk=None, key_name=None, key_fingerprint=None, instance_name=None, instance_id=None, admin_pass=None, personality=None, public_ip=None, user_data=None, metadata=None, security_groups=None, server_group_id=None, tenancy=None, dedicated_host_id=None, market_type=None, multi_flavor_priority_policy=None):
        """InstanceConfigResult

        The model defined in huaweicloud sdk

        :param flavor_ref: 云服务器的规格ID。
        :type flavor_ref: str
        :param image_ref: 镜像ID，同image_id。
        :type image_ref: str
        :param disk: 磁盘组信息。
        :type disk: list[:class:`huaweicloudsdkas.v1.DiskResult`]
        :param key_name: 登录云服务器的SSH密钥名称。
        :type key_name: str
        :param key_fingerprint: 登录云服务器的SSH密钥指纹。
        :type key_fingerprint: str
        :param instance_name: 该参数为预留字段。
        :type instance_name: str
        :param instance_id: 该参数为预留字段。
        :type instance_id: str
        :param admin_pass: 登录云服务器的密码，非明文回显。
        :type admin_pass: str
        :param personality: 个人信息
        :type personality: list[:class:`huaweicloudsdkas.v1.PersonalityResult`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkas.v1.PublicipResult`
        :param user_data: cloud-init用户数据，base64格式编码。
        :type user_data: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkas.v1.VmMetaData`
        :param security_groups: 安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
        :param server_group_id: 云服务器组ID。
        :type server_group_id: str
        :param tenancy: 在专属主机上创建弹性云服务器。
        :type tenancy: str
        :param dedicated_host_id: 专属主机的ID。
        :type dedicated_host_id: str
        :param market_type: 云服务器的计费模式，可以选择竞价计费或按需计费。
        :type market_type: str
        :param multi_flavor_priority_policy: 使用伸缩配置创建云主机的时候，多规格使用的优先级策略。  PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。 COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。
        :type multi_flavor_priority_policy: str
        """
        
        

        self._flavor_ref = None
        self._image_ref = None
        self._disk = None
        self._key_name = None
        self._key_fingerprint = None
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
        self._market_type = None
        self._multi_flavor_priority_policy = None
        self.discriminator = None

        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if image_ref is not None:
            self.image_ref = image_ref
        if disk is not None:
            self.disk = disk
        if key_name is not None:
            self.key_name = key_name
        if key_fingerprint is not None:
            self.key_fingerprint = key_fingerprint
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
        if market_type is not None:
            self.market_type = market_type
        if multi_flavor_priority_policy is not None:
            self.multi_flavor_priority_policy = multi_flavor_priority_policy

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
        :type flavor_ref: str
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
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def disk(self):
        """Gets the disk of this InstanceConfigResult.

        磁盘组信息。

        :return: The disk of this InstanceConfigResult.
        :rtype: list[:class:`huaweicloudsdkas.v1.DiskResult`]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this InstanceConfigResult.

        磁盘组信息。

        :param disk: The disk of this InstanceConfigResult.
        :type disk: list[:class:`huaweicloudsdkas.v1.DiskResult`]
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
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def key_fingerprint(self):
        """Gets the key_fingerprint of this InstanceConfigResult.

        登录云服务器的SSH密钥指纹。

        :return: The key_fingerprint of this InstanceConfigResult.
        :rtype: str
        """
        return self._key_fingerprint

    @key_fingerprint.setter
    def key_fingerprint(self, key_fingerprint):
        """Sets the key_fingerprint of this InstanceConfigResult.

        登录云服务器的SSH密钥指纹。

        :param key_fingerprint: The key_fingerprint of this InstanceConfigResult.
        :type key_fingerprint: str
        """
        self._key_fingerprint = key_fingerprint

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
        :type instance_name: str
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
        :type instance_id: str
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
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def personality(self):
        """Gets the personality of this InstanceConfigResult.

        个人信息

        :return: The personality of this InstanceConfigResult.
        :rtype: list[:class:`huaweicloudsdkas.v1.PersonalityResult`]
        """
        return self._personality

    @personality.setter
    def personality(self, personality):
        """Sets the personality of this InstanceConfigResult.

        个人信息

        :param personality: The personality of this InstanceConfigResult.
        :type personality: list[:class:`huaweicloudsdkas.v1.PersonalityResult`]
        """
        self._personality = personality

    @property
    def public_ip(self):
        """Gets the public_ip of this InstanceConfigResult.

        :return: The public_ip of this InstanceConfigResult.
        :rtype: :class:`huaweicloudsdkas.v1.PublicipResult`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this InstanceConfigResult.

        :param public_ip: The public_ip of this InstanceConfigResult.
        :type public_ip: :class:`huaweicloudsdkas.v1.PublicipResult`
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
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def metadata(self):
        """Gets the metadata of this InstanceConfigResult.

        :return: The metadata of this InstanceConfigResult.
        :rtype: :class:`huaweicloudsdkas.v1.VmMetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InstanceConfigResult.

        :param metadata: The metadata of this InstanceConfigResult.
        :type metadata: :class:`huaweicloudsdkas.v1.VmMetaData`
        """
        self._metadata = metadata

    @property
    def security_groups(self):
        """Gets the security_groups of this InstanceConfigResult.

        安全组信息。

        :return: The security_groups of this InstanceConfigResult.
        :rtype: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this InstanceConfigResult.

        安全组信息。

        :param security_groups: The security_groups of this InstanceConfigResult.
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
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
        :type server_group_id: str
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
        :type tenancy: str
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
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def market_type(self):
        """Gets the market_type of this InstanceConfigResult.

        云服务器的计费模式，可以选择竞价计费或按需计费。

        :return: The market_type of this InstanceConfigResult.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        """Sets the market_type of this InstanceConfigResult.

        云服务器的计费模式，可以选择竞价计费或按需计费。

        :param market_type: The market_type of this InstanceConfigResult.
        :type market_type: str
        """
        self._market_type = market_type

    @property
    def multi_flavor_priority_policy(self):
        """Gets the multi_flavor_priority_policy of this InstanceConfigResult.

        使用伸缩配置创建云主机的时候，多规格使用的优先级策略。  PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。 COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。

        :return: The multi_flavor_priority_policy of this InstanceConfigResult.
        :rtype: str
        """
        return self._multi_flavor_priority_policy

    @multi_flavor_priority_policy.setter
    def multi_flavor_priority_policy(self, multi_flavor_priority_policy):
        """Sets the multi_flavor_priority_policy of this InstanceConfigResult.

        使用伸缩配置创建云主机的时候，多规格使用的优先级策略。  PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。 COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。

        :param multi_flavor_priority_policy: The multi_flavor_priority_policy of this InstanceConfigResult.
        :type multi_flavor_priority_policy: str
        """
        self._multi_flavor_priority_policy = multi_flavor_priority_policy

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
        if not isinstance(other, InstanceConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
