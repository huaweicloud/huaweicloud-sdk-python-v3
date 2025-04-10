# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'flavor_ref': 'str',
        'image_ref': 'str',
        'disk': 'list[DiskInfo]',
        'key_name': 'str',
        'personality': 'list[PersonalityInfo]',
        'public_ip': 'PublicIp',
        'user_data': 'str',
        'metadata': 'VmMetaData',
        'security_groups': 'list[SecurityGroups]',
        'server_group_id': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str',
        'multi_flavor_priority_policy': 'str',
        'market_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'flavor_ref': 'flavorRef',
        'image_ref': 'imageRef',
        'disk': 'disk',
        'key_name': 'key_name',
        'personality': 'personality',
        'public_ip': 'public_ip',
        'user_data': 'user_data',
        'metadata': 'metadata',
        'security_groups': 'security_groups',
        'server_group_id': 'server_group_id',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id',
        'multi_flavor_priority_policy': 'multi_flavor_priority_policy',
        'market_type': 'market_type'
    }

    def __init__(self, instance_id=None, flavor_ref=None, image_ref=None, disk=None, key_name=None, personality=None, public_ip=None, user_data=None, metadata=None, security_groups=None, server_group_id=None, tenancy=None, dedicated_host_id=None, multi_flavor_priority_policy=None, market_type=None):
        r"""InstanceConfig

        The model defined in huaweicloud sdk

        :param instance_id: 云服务器ID，当使用已存在的云服务器的规格为模板创建弹性伸缩配置时传入该字段，此时flavorRef、imageRef、disk、security_groups、tenancy和dedicated_host_id字段不生效。当不传入instance_id字段时flavorRef、imageRef、disk字段为必选。
        :type instance_id: str
        :param flavor_ref: 云服务器的规格ID。最多支持选择10个规格，多个规格ID以逗号分隔。云服务器的ID通过查询弹性云服务器规格详情和扩展信息列表接口获取，详情请参考 [查询云服务器规格详情和扩展信息列表](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212656.html)。
        :type flavor_ref: str
        :param image_ref: 镜像ID，同image_id，指定创建实例时选择的镜像资源。通过查询镜像服务镜像列表接口获取，请参考[查询镜像列表](https://support.huaweicloud.com/api-ims/ims_03_0602.html)。
        :type image_ref: str
        :param disk: 磁盘组信息，系统盘必选，数据盘可选。
        :type disk: list[:class:`huaweicloudsdkas.v1.DiskInfo`]
        :param key_name: 登录云服务器的SSH密钥名称。获取密钥对方式请参考[创建及导入SSH密钥对](https://support.huaweicloud.com/api-dew/CreateKeypair.html)。说明：当key_name与user_data同时指定时，user_data只做用户数据注入。
        :type key_name: str
        :param personality: 注入文件信息。仅支持注入文本文件，最大支持注入5个文件，每个文件最大1KB。
        :type personality: list[:class:`huaweicloudsdkas.v1.PersonalityInfo`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkas.v1.PublicIp`
        :param user_data: cloud-init用户数据。支持注入文本、文本文件或gzip文件。文件内容需要进行base64格式编码，注入内容（编码之前的内容）最大为32KB。说明：当key_name没有指定时，user_data注入的数据默认为云服务器root账号的登录密码。创建密码方式鉴权的Linux弹性云服务器时为必填项，为root用户注入自定义初始化密码。
        :type user_data: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkas.v1.VmMetaData`
        :param security_groups: 安全组信息。使用vpc_id通过查询VPC服务安全组列表接口获取，详见《虚拟私有云API参考》的“查询安全组列表”。当伸缩配置和伸缩组同时指定安全组时，将以伸缩配置中的安全组为准；当伸缩配置和伸缩组都没有指定安全组时，将使用默认安全组。为了使用灵活性更高，推荐在伸缩配置中指定安全组。
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
        :param server_group_id: 云服务器组ID。
        :type server_group_id: str
        :param tenancy: 在专属主机上创建弹性云服务器。参数取值为dedicated。
        :type tenancy: str
        :param dedicated_host_id: 专属主机的ID。 说明：该字段仅在tenancy为dedicated时生效；如果指定该字段，云服务器将被创建到指定的专属主机上；如果不指定该字段，此时系统会将云服务器创建在符合规格的专属主机中剩余内存最大的那一台上，以使各专属主机尽量均衡负载。
        :type dedicated_host_id: str
        :param multi_flavor_priority_policy: 使用伸缩配置创建云主机的时候，多规格使用的优先级策略。PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。
        :type multi_flavor_priority_policy: str
        :param market_type: 云服务器的计费模式，可以选择竞价计费或按需计费，取值如下：按需计费：不指定该字段。竞价计费：spot
        :type market_type: str
        """
        
        

        self._instance_id = None
        self._flavor_ref = None
        self._image_ref = None
        self._disk = None
        self._key_name = None
        self._personality = None
        self._public_ip = None
        self._user_data = None
        self._metadata = None
        self._security_groups = None
        self._server_group_id = None
        self._tenancy = None
        self._dedicated_host_id = None
        self._multi_flavor_priority_policy = None
        self._market_type = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if image_ref is not None:
            self.image_ref = image_ref
        if disk is not None:
            self.disk = disk
        if key_name is not None:
            self.key_name = key_name
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
        if multi_flavor_priority_policy is not None:
            self.multi_flavor_priority_policy = multi_flavor_priority_policy
        if market_type is not None:
            self.market_type = market_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceConfig.

        云服务器ID，当使用已存在的云服务器的规格为模板创建弹性伸缩配置时传入该字段，此时flavorRef、imageRef、disk、security_groups、tenancy和dedicated_host_id字段不生效。当不传入instance_id字段时flavorRef、imageRef、disk字段为必选。

        :return: The instance_id of this InstanceConfig.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceConfig.

        云服务器ID，当使用已存在的云服务器的规格为模板创建弹性伸缩配置时传入该字段，此时flavorRef、imageRef、disk、security_groups、tenancy和dedicated_host_id字段不生效。当不传入instance_id字段时flavorRef、imageRef、disk字段为必选。

        :param instance_id: The instance_id of this InstanceConfig.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this InstanceConfig.

        云服务器的规格ID。最多支持选择10个规格，多个规格ID以逗号分隔。云服务器的ID通过查询弹性云服务器规格详情和扩展信息列表接口获取，详情请参考 [查询云服务器规格详情和扩展信息列表](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212656.html)。

        :return: The flavor_ref of this InstanceConfig.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this InstanceConfig.

        云服务器的规格ID。最多支持选择10个规格，多个规格ID以逗号分隔。云服务器的ID通过查询弹性云服务器规格详情和扩展信息列表接口获取，详情请参考 [查询云服务器规格详情和扩展信息列表](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212656.html)。

        :param flavor_ref: The flavor_ref of this InstanceConfig.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def image_ref(self):
        r"""Gets the image_ref of this InstanceConfig.

        镜像ID，同image_id，指定创建实例时选择的镜像资源。通过查询镜像服务镜像列表接口获取，请参考[查询镜像列表](https://support.huaweicloud.com/api-ims/ims_03_0602.html)。

        :return: The image_ref of this InstanceConfig.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        r"""Sets the image_ref of this InstanceConfig.

        镜像ID，同image_id，指定创建实例时选择的镜像资源。通过查询镜像服务镜像列表接口获取，请参考[查询镜像列表](https://support.huaweicloud.com/api-ims/ims_03_0602.html)。

        :param image_ref: The image_ref of this InstanceConfig.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def disk(self):
        r"""Gets the disk of this InstanceConfig.

        磁盘组信息，系统盘必选，数据盘可选。

        :return: The disk of this InstanceConfig.
        :rtype: list[:class:`huaweicloudsdkas.v1.DiskInfo`]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this InstanceConfig.

        磁盘组信息，系统盘必选，数据盘可选。

        :param disk: The disk of this InstanceConfig.
        :type disk: list[:class:`huaweicloudsdkas.v1.DiskInfo`]
        """
        self._disk = disk

    @property
    def key_name(self):
        r"""Gets the key_name of this InstanceConfig.

        登录云服务器的SSH密钥名称。获取密钥对方式请参考[创建及导入SSH密钥对](https://support.huaweicloud.com/api-dew/CreateKeypair.html)。说明：当key_name与user_data同时指定时，user_data只做用户数据注入。

        :return: The key_name of this InstanceConfig.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this InstanceConfig.

        登录云服务器的SSH密钥名称。获取密钥对方式请参考[创建及导入SSH密钥对](https://support.huaweicloud.com/api-dew/CreateKeypair.html)。说明：当key_name与user_data同时指定时，user_data只做用户数据注入。

        :param key_name: The key_name of this InstanceConfig.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def personality(self):
        r"""Gets the personality of this InstanceConfig.

        注入文件信息。仅支持注入文本文件，最大支持注入5个文件，每个文件最大1KB。

        :return: The personality of this InstanceConfig.
        :rtype: list[:class:`huaweicloudsdkas.v1.PersonalityInfo`]
        """
        return self._personality

    @personality.setter
    def personality(self, personality):
        r"""Sets the personality of this InstanceConfig.

        注入文件信息。仅支持注入文本文件，最大支持注入5个文件，每个文件最大1KB。

        :param personality: The personality of this InstanceConfig.
        :type personality: list[:class:`huaweicloudsdkas.v1.PersonalityInfo`]
        """
        self._personality = personality

    @property
    def public_ip(self):
        r"""Gets the public_ip of this InstanceConfig.

        :return: The public_ip of this InstanceConfig.
        :rtype: :class:`huaweicloudsdkas.v1.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this InstanceConfig.

        :param public_ip: The public_ip of this InstanceConfig.
        :type public_ip: :class:`huaweicloudsdkas.v1.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def user_data(self):
        r"""Gets the user_data of this InstanceConfig.

        cloud-init用户数据。支持注入文本、文本文件或gzip文件。文件内容需要进行base64格式编码，注入内容（编码之前的内容）最大为32KB。说明：当key_name没有指定时，user_data注入的数据默认为云服务器root账号的登录密码。创建密码方式鉴权的Linux弹性云服务器时为必填项，为root用户注入自定义初始化密码。

        :return: The user_data of this InstanceConfig.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this InstanceConfig.

        cloud-init用户数据。支持注入文本、文本文件或gzip文件。文件内容需要进行base64格式编码，注入内容（编码之前的内容）最大为32KB。说明：当key_name没有指定时，user_data注入的数据默认为云服务器root账号的登录密码。创建密码方式鉴权的Linux弹性云服务器时为必填项，为root用户注入自定义初始化密码。

        :param user_data: The user_data of this InstanceConfig.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def metadata(self):
        r"""Gets the metadata of this InstanceConfig.

        :return: The metadata of this InstanceConfig.
        :rtype: :class:`huaweicloudsdkas.v1.VmMetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this InstanceConfig.

        :param metadata: The metadata of this InstanceConfig.
        :type metadata: :class:`huaweicloudsdkas.v1.VmMetaData`
        """
        self._metadata = metadata

    @property
    def security_groups(self):
        r"""Gets the security_groups of this InstanceConfig.

        安全组信息。使用vpc_id通过查询VPC服务安全组列表接口获取，详见《虚拟私有云API参考》的“查询安全组列表”。当伸缩配置和伸缩组同时指定安全组时，将以伸缩配置中的安全组为准；当伸缩配置和伸缩组都没有指定安全组时，将使用默认安全组。为了使用灵活性更高，推荐在伸缩配置中指定安全组。

        :return: The security_groups of this InstanceConfig.
        :rtype: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this InstanceConfig.

        安全组信息。使用vpc_id通过查询VPC服务安全组列表接口获取，详见《虚拟私有云API参考》的“查询安全组列表”。当伸缩配置和伸缩组同时指定安全组时，将以伸缩配置中的安全组为准；当伸缩配置和伸缩组都没有指定安全组时，将使用默认安全组。为了使用灵活性更高，推荐在伸缩配置中指定安全组。

        :param security_groups: The security_groups of this InstanceConfig.
        :type security_groups: list[:class:`huaweicloudsdkas.v1.SecurityGroups`]
        """
        self._security_groups = security_groups

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this InstanceConfig.

        云服务器组ID。

        :return: The server_group_id of this InstanceConfig.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this InstanceConfig.

        云服务器组ID。

        :param server_group_id: The server_group_id of this InstanceConfig.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def tenancy(self):
        r"""Gets the tenancy of this InstanceConfig.

        在专属主机上创建弹性云服务器。参数取值为dedicated。

        :return: The tenancy of this InstanceConfig.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        r"""Sets the tenancy of this InstanceConfig.

        在专属主机上创建弹性云服务器。参数取值为dedicated。

        :param tenancy: The tenancy of this InstanceConfig.
        :type tenancy: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this InstanceConfig.

        专属主机的ID。 说明：该字段仅在tenancy为dedicated时生效；如果指定该字段，云服务器将被创建到指定的专属主机上；如果不指定该字段，此时系统会将云服务器创建在符合规格的专属主机中剩余内存最大的那一台上，以使各专属主机尽量均衡负载。

        :return: The dedicated_host_id of this InstanceConfig.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this InstanceConfig.

        专属主机的ID。 说明：该字段仅在tenancy为dedicated时生效；如果指定该字段，云服务器将被创建到指定的专属主机上；如果不指定该字段，此时系统会将云服务器创建在符合规格的专属主机中剩余内存最大的那一台上，以使各专属主机尽量均衡负载。

        :param dedicated_host_id: The dedicated_host_id of this InstanceConfig.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def multi_flavor_priority_policy(self):
        r"""Gets the multi_flavor_priority_policy of this InstanceConfig.

        使用伸缩配置创建云主机的时候，多规格使用的优先级策略。PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。

        :return: The multi_flavor_priority_policy of this InstanceConfig.
        :rtype: str
        """
        return self._multi_flavor_priority_policy

    @multi_flavor_priority_policy.setter
    def multi_flavor_priority_policy(self, multi_flavor_priority_policy):
        r"""Sets the multi_flavor_priority_policy of this InstanceConfig.

        使用伸缩配置创建云主机的时候，多规格使用的优先级策略。PICK_FIRST（默认）：选择优先，虚拟机扩容时规格的选择按照flavorRef列表的顺序进行优先级排序。COST_FIRST：成本优化，虚拟机扩容时规格的选择按照价格最优原则进行优先级排序。

        :param multi_flavor_priority_policy: The multi_flavor_priority_policy of this InstanceConfig.
        :type multi_flavor_priority_policy: str
        """
        self._multi_flavor_priority_policy = multi_flavor_priority_policy

    @property
    def market_type(self):
        r"""Gets the market_type of this InstanceConfig.

        云服务器的计费模式，可以选择竞价计费或按需计费，取值如下：按需计费：不指定该字段。竞价计费：spot

        :return: The market_type of this InstanceConfig.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        r"""Sets the market_type of this InstanceConfig.

        云服务器的计费模式，可以选择竞价计费或按需计费，取值如下：按需计费：不指定该字段。竞价计费：spot

        :param market_type: The market_type of this InstanceConfig.
        :type market_type: str
        """
        self._market_type = market_type

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
        if not isinstance(other, InstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
