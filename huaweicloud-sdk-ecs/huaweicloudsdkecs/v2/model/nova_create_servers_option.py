# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateServersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auto_terminate_time': 'str',
        'image_ref': 'str',
        'flavor_ref': 'str',
        'name': 'str',
        'metadata': 'dict(str, str)',
        'admin_pass': 'str',
        'block_device_mapping_v2': 'list[NovaServerBlockDeviceMapping]',
        'config_drive': 'str',
        'security_groups': 'list[NovaServerSecurityGroup]',
        'networks': 'list[NovaServerNetwork]',
        'key_name': 'str',
        'user_data': 'str',
        'availability_zone': 'str',
        'return_reservation_id': 'bool',
        'min_count': 'int',
        'max_count': 'int',
        'os_dc_fdisk_config': 'str',
        'description': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time',
        'image_ref': 'imageRef',
        'flavor_ref': 'flavorRef',
        'name': 'name',
        'metadata': 'metadata',
        'admin_pass': 'adminPass',
        'block_device_mapping_v2': 'block_device_mapping_v2',
        'config_drive': 'config_drive',
        'security_groups': 'security_groups',
        'networks': 'networks',
        'key_name': 'key_name',
        'user_data': 'user_data',
        'availability_zone': 'availability_zone',
        'return_reservation_id': 'return_reservation_id',
        'min_count': 'min_count',
        'max_count': 'max_count',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'description': 'description'
    }

    def __init__(self, auto_terminate_time=None, image_ref=None, flavor_ref=None, name=None, metadata=None, admin_pass=None, block_device_mapping_v2=None, config_drive=None, security_groups=None, networks=None, key_name=None, user_data=None, availability_zone=None, return_reservation_id=None, min_count=None, max_count=None, os_dc_fdisk_config=None, description=None):
        """NovaCreateServersOption

        The model defined in huaweicloud sdk

        :param auto_terminate_time: 弹性云服务器自动释放时间。  时间格式例如：2020-01-19T03:30:52Z
        :type auto_terminate_time: str
        :param image_ref: 镜像ID或者镜像资源的URL。  - 镜像ID示例：3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 镜像URL示例：http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 指定卷作为系统卷创弹性云服务器时，不需填写该参数；非卷创建弹性云服务器时需填写有效的UUID参数，否则API将返回400错误。  &gt; 说明： &gt; - 对于部分规格的弹性云服务器，不能支持公有云平台提供的所有公共镜像。具体规格的镜像支持列表，请登录管理控制台，以“创建弹性云服务器”页面系统自动过滤的镜像信息为准，并在镜像服务页面查询镜像ID。 &gt; - 如果创建失败，请尝试修改参数配置。
        :type image_ref: str
        :param flavor_ref: 规格ID或URL。
        :type flavor_ref: str
        :param name: 弹性云服务器名称，长度大于0小于256字节。  &gt; 说明： &gt;  &gt; 云服务器内部主机名(hostname)命名规则遵循 [RFC 952](https://tools.ietf.org/html/rfc952)和[RFC 1123](https://tools.ietf.org/html/rfc1123)命名规范，建议使用a-zA-z或0-9以及中划线\&quot;-\&quot;组成的名称命名，\&quot;_\&quot;将在弹性云服务器内部默认转化为\&quot;-\&quot;。
        :type name: str
        :param metadata: 用户自定义字段键值对。  &gt; - key的长度大于0小于256字节 &gt; - value的长度大于等于0小于256字节   系统预留字段  1. admin_pass：弹性云服务器密码        Windows弹性云服务器Administrator用户的密码。     &gt; 说明：     &gt; 创建密码方式鉴权的Windows弹性云服务器时为必选字段。
        :type metadata: dict(str, str)
        :param admin_pass: 如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。
        :type admin_pass: str
        :param block_device_mapping_v2: 扩展属性，指定弹性云服务器存储设备的v2接口。是存储资源的新版本接口，指定卷场景不能批创弹性云服务器。  裸金属服务器场景不支持。
        :type block_device_mapping_v2: list[:class:`huaweicloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        :param config_drive: 扩展属性，开启后在弹性云服务器创建时挂载config_drive向弹性云服务器内部传递信息。  当前不支持该功能。
        :type config_drive: str
        :param security_groups: 扩展属性，指定弹性云服务器的安全组，默认为default。  指定network创建弹性云服务器时该字段有效。对于已存在端口，安全组请求无效。
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.NovaServerSecurityGroup`]
        :param networks: 扩展属性，指定弹性云服务器的网卡信息。有多个租户网络时必须指定。 
        :type networks: list[:class:`huaweicloudsdkecs.v2.NovaServerNetwork`]
        :param key_name: 扩展属性，指定keypair的名称。
        :type key_name: str
        :param user_data: 扩展属性，字符串长度小于65535，且必须是base64加密的。
        :type user_data: str
        :param availability_zone: 扩展属性，指定弹性云服务器所在的AZ。  创建弹性云服务器时需要填入该参数。
        :type availability_zone: str
        :param return_reservation_id: 扩展属性，是否支持返回批量创建弹性云服务器的reservation_id。通过返回的reservation_id，可以过滤查询到本次创建的弹性云服务器。  - true，返回reservation_id。 - false，返回弹性云服务器信息。  &gt; 说明： &gt;  &gt; 批量创建弹性云服务器时，支持使用该字段。
        :type return_reservation_id: bool
        :param min_count: 扩展属性，表示创建弹性云服务器最小数量。  默认值为1。  &gt; 说明： &gt;  &gt; 指定镜像创建弹性云服务器时，支持使用该字段。
        :type min_count: int
        :param max_count: 表示创建弹性云服务器最大数量。  默认值与min_count的取值一致。  约束：  参数max_count的取值必须大于参数min_count的取值。  当min_count、max_count同时设置时，创弹性云服务器的数量取决于服务器的资源情况。根据资源情况，在min_count至max_count的取值范围内创建最大数量的弹性云服务器。  - 说明： -  - 指定镜像创建弹性云服务器时，支持使用该字段。
        :type max_count: int
        :param os_dc_fdisk_config: diskConfig的方式，取值为AUTO、MANUAL。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。  当前不支持该功能。
        :type os_dc_fdisk_config: str
        :param description: 扩展属性，表示弹性云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“&lt;” 和 “&gt;”等特殊符号。  &gt; 说明： &gt;  &gt; - V2接口不支持该字段。 &gt; - V2.1接口支持该字段，此时，需在请求Header中增加一组Key-Value值。其中，Key固定为“X-OpenStack-Nova-API-Version” ，Value为微版本号，当Value的值为2.19时，支持使用该字段。
        :type description: str
        """
        
        

        self._auto_terminate_time = None
        self._image_ref = None
        self._flavor_ref = None
        self._name = None
        self._metadata = None
        self._admin_pass = None
        self._block_device_mapping_v2 = None
        self._config_drive = None
        self._security_groups = None
        self._networks = None
        self._key_name = None
        self._user_data = None
        self._availability_zone = None
        self._return_reservation_id = None
        self._min_count = None
        self._max_count = None
        self._os_dc_fdisk_config = None
        self._description = None
        self.discriminator = None

        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        if image_ref is not None:
            self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.name = name
        if metadata is not None:
            self.metadata = metadata
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if block_device_mapping_v2 is not None:
            self.block_device_mapping_v2 = block_device_mapping_v2
        if config_drive is not None:
            self.config_drive = config_drive
        if security_groups is not None:
            self.security_groups = security_groups
        self.networks = networks
        if key_name is not None:
            self.key_name = key_name
        if user_data is not None:
            self.user_data = user_data
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if return_reservation_id is not None:
            self.return_reservation_id = return_reservation_id
        if min_count is not None:
            self.min_count = min_count
        if max_count is not None:
            self.max_count = max_count
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        if description is not None:
            self.description = description

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this NovaCreateServersOption.

        弹性云服务器自动释放时间。  时间格式例如：2020-01-19T03:30:52Z

        :return: The auto_terminate_time of this NovaCreateServersOption.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this NovaCreateServersOption.

        弹性云服务器自动释放时间。  时间格式例如：2020-01-19T03:30:52Z

        :param auto_terminate_time: The auto_terminate_time of this NovaCreateServersOption.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def image_ref(self):
        """Gets the image_ref of this NovaCreateServersOption.

        镜像ID或者镜像资源的URL。  - 镜像ID示例：3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 镜像URL示例：http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 指定卷作为系统卷创弹性云服务器时，不需填写该参数；非卷创建弹性云服务器时需填写有效的UUID参数，否则API将返回400错误。  > 说明： > - 对于部分规格的弹性云服务器，不能支持公有云平台提供的所有公共镜像。具体规格的镜像支持列表，请登录管理控制台，以“创建弹性云服务器”页面系统自动过滤的镜像信息为准，并在镜像服务页面查询镜像ID。 > - 如果创建失败，请尝试修改参数配置。

        :return: The image_ref of this NovaCreateServersOption.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this NovaCreateServersOption.

        镜像ID或者镜像资源的URL。  - 镜像ID示例：3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 镜像URL示例：http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2 - 指定卷作为系统卷创弹性云服务器时，不需填写该参数；非卷创建弹性云服务器时需填写有效的UUID参数，否则API将返回400错误。  > 说明： > - 对于部分规格的弹性云服务器，不能支持公有云平台提供的所有公共镜像。具体规格的镜像支持列表，请登录管理控制台，以“创建弹性云服务器”页面系统自动过滤的镜像信息为准，并在镜像服务页面查询镜像ID。 > - 如果创建失败，请尝试修改参数配置。

        :param image_ref: The image_ref of this NovaCreateServersOption.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this NovaCreateServersOption.

        规格ID或URL。

        :return: The flavor_ref of this NovaCreateServersOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this NovaCreateServersOption.

        规格ID或URL。

        :param flavor_ref: The flavor_ref of this NovaCreateServersOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this NovaCreateServersOption.

        弹性云服务器名称，长度大于0小于256字节。  > 说明： >  > 云服务器内部主机名(hostname)命名规则遵循 [RFC 952](https://tools.ietf.org/html/rfc952)和[RFC 1123](https://tools.ietf.org/html/rfc1123)命名规范，建议使用a-zA-z或0-9以及中划线\"-\"组成的名称命名，\"_\"将在弹性云服务器内部默认转化为\"-\"。

        :return: The name of this NovaCreateServersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaCreateServersOption.

        弹性云服务器名称，长度大于0小于256字节。  > 说明： >  > 云服务器内部主机名(hostname)命名规则遵循 [RFC 952](https://tools.ietf.org/html/rfc952)和[RFC 1123](https://tools.ietf.org/html/rfc1123)命名规范，建议使用a-zA-z或0-9以及中划线\"-\"组成的名称命名，\"_\"将在弹性云服务器内部默认转化为\"-\"。

        :param name: The name of this NovaCreateServersOption.
        :type name: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this NovaCreateServersOption.

        用户自定义字段键值对。  > - key的长度大于0小于256字节 > - value的长度大于等于0小于256字节   系统预留字段  1. admin_pass：弹性云服务器密码        Windows弹性云服务器Administrator用户的密码。     > 说明：     > 创建密码方式鉴权的Windows弹性云服务器时为必选字段。

        :return: The metadata of this NovaCreateServersOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaCreateServersOption.

        用户自定义字段键值对。  > - key的长度大于0小于256字节 > - value的长度大于等于0小于256字节   系统预留字段  1. admin_pass：弹性云服务器密码        Windows弹性云服务器Administrator用户的密码。     > 说明：     > 创建密码方式鉴权的Windows弹性云服务器时为必选字段。

        :param metadata: The metadata of this NovaCreateServersOption.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def admin_pass(self):
        """Gets the admin_pass of this NovaCreateServersOption.

        如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。

        :return: The admin_pass of this NovaCreateServersOption.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this NovaCreateServersOption.

        如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。

        :param admin_pass: The admin_pass of this NovaCreateServersOption.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def block_device_mapping_v2(self):
        """Gets the block_device_mapping_v2 of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器存储设备的v2接口。是存储资源的新版本接口，指定卷场景不能批创弹性云服务器。  裸金属服务器场景不支持。

        :return: The block_device_mapping_v2 of this NovaCreateServersOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        """
        return self._block_device_mapping_v2

    @block_device_mapping_v2.setter
    def block_device_mapping_v2(self, block_device_mapping_v2):
        """Sets the block_device_mapping_v2 of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器存储设备的v2接口。是存储资源的新版本接口，指定卷场景不能批创弹性云服务器。  裸金属服务器场景不支持。

        :param block_device_mapping_v2: The block_device_mapping_v2 of this NovaCreateServersOption.
        :type block_device_mapping_v2: list[:class:`huaweicloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        """
        self._block_device_mapping_v2 = block_device_mapping_v2

    @property
    def config_drive(self):
        """Gets the config_drive of this NovaCreateServersOption.

        扩展属性，开启后在弹性云服务器创建时挂载config_drive向弹性云服务器内部传递信息。  当前不支持该功能。

        :return: The config_drive of this NovaCreateServersOption.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this NovaCreateServersOption.

        扩展属性，开启后在弹性云服务器创建时挂载config_drive向弹性云服务器内部传递信息。  当前不支持该功能。

        :param config_drive: The config_drive of this NovaCreateServersOption.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器的安全组，默认为default。  指定network创建弹性云服务器时该字段有效。对于已存在端口，安全组请求无效。

        :return: The security_groups of this NovaCreateServersOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器的安全组，默认为default。  指定network创建弹性云服务器时该字段有效。对于已存在端口，安全组请求无效。

        :param security_groups: The security_groups of this NovaCreateServersOption.
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def networks(self):
        """Gets the networks of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器的网卡信息。有多个租户网络时必须指定。 

        :return: The networks of this NovaCreateServersOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaServerNetwork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器的网卡信息。有多个租户网络时必须指定。 

        :param networks: The networks of this NovaCreateServersOption.
        :type networks: list[:class:`huaweicloudsdkecs.v2.NovaServerNetwork`]
        """
        self._networks = networks

    @property
    def key_name(self):
        """Gets the key_name of this NovaCreateServersOption.

        扩展属性，指定keypair的名称。

        :return: The key_name of this NovaCreateServersOption.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this NovaCreateServersOption.

        扩展属性，指定keypair的名称。

        :param key_name: The key_name of this NovaCreateServersOption.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def user_data(self):
        """Gets the user_data of this NovaCreateServersOption.

        扩展属性，字符串长度小于65535，且必须是base64加密的。

        :return: The user_data of this NovaCreateServersOption.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this NovaCreateServersOption.

        扩展属性，字符串长度小于65535，且必须是base64加密的。

        :param user_data: The user_data of this NovaCreateServersOption.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器所在的AZ。  创建弹性云服务器时需要填入该参数。

        :return: The availability_zone of this NovaCreateServersOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NovaCreateServersOption.

        扩展属性，指定弹性云服务器所在的AZ。  创建弹性云服务器时需要填入该参数。

        :param availability_zone: The availability_zone of this NovaCreateServersOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def return_reservation_id(self):
        """Gets the return_reservation_id of this NovaCreateServersOption.

        扩展属性，是否支持返回批量创建弹性云服务器的reservation_id。通过返回的reservation_id，可以过滤查询到本次创建的弹性云服务器。  - true，返回reservation_id。 - false，返回弹性云服务器信息。  > 说明： >  > 批量创建弹性云服务器时，支持使用该字段。

        :return: The return_reservation_id of this NovaCreateServersOption.
        :rtype: bool
        """
        return self._return_reservation_id

    @return_reservation_id.setter
    def return_reservation_id(self, return_reservation_id):
        """Sets the return_reservation_id of this NovaCreateServersOption.

        扩展属性，是否支持返回批量创建弹性云服务器的reservation_id。通过返回的reservation_id，可以过滤查询到本次创建的弹性云服务器。  - true，返回reservation_id。 - false，返回弹性云服务器信息。  > 说明： >  > 批量创建弹性云服务器时，支持使用该字段。

        :param return_reservation_id: The return_reservation_id of this NovaCreateServersOption.
        :type return_reservation_id: bool
        """
        self._return_reservation_id = return_reservation_id

    @property
    def min_count(self):
        """Gets the min_count of this NovaCreateServersOption.

        扩展属性，表示创建弹性云服务器最小数量。  默认值为1。  > 说明： >  > 指定镜像创建弹性云服务器时，支持使用该字段。

        :return: The min_count of this NovaCreateServersOption.
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        """Sets the min_count of this NovaCreateServersOption.

        扩展属性，表示创建弹性云服务器最小数量。  默认值为1。  > 说明： >  > 指定镜像创建弹性云服务器时，支持使用该字段。

        :param min_count: The min_count of this NovaCreateServersOption.
        :type min_count: int
        """
        self._min_count = min_count

    @property
    def max_count(self):
        """Gets the max_count of this NovaCreateServersOption.

        表示创建弹性云服务器最大数量。  默认值与min_count的取值一致。  约束：  参数max_count的取值必须大于参数min_count的取值。  当min_count、max_count同时设置时，创弹性云服务器的数量取决于服务器的资源情况。根据资源情况，在min_count至max_count的取值范围内创建最大数量的弹性云服务器。  - 说明： -  - 指定镜像创建弹性云服务器时，支持使用该字段。

        :return: The max_count of this NovaCreateServersOption.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        """Sets the max_count of this NovaCreateServersOption.

        表示创建弹性云服务器最大数量。  默认值与min_count的取值一致。  约束：  参数max_count的取值必须大于参数min_count的取值。  当min_count、max_count同时设置时，创弹性云服务器的数量取决于服务器的资源情况。根据资源情况，在min_count至max_count的取值范围内创建最大数量的弹性云服务器。  - 说明： -  - 指定镜像创建弹性云服务器时，支持使用该字段。

        :param max_count: The max_count of this NovaCreateServersOption.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this NovaCreateServersOption.

        diskConfig的方式，取值为AUTO、MANUAL。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。  当前不支持该功能。

        :return: The os_dc_fdisk_config of this NovaCreateServersOption.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this NovaCreateServersOption.

        diskConfig的方式，取值为AUTO、MANUAL。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。  当前不支持该功能。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this NovaCreateServersOption.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def description(self):
        """Gets the description of this NovaCreateServersOption.

        扩展属性，表示弹性云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“<” 和 “>”等特殊符号。  > 说明： >  > - V2接口不支持该字段。 > - V2.1接口支持该字段，此时，需在请求Header中增加一组Key-Value值。其中，Key固定为“X-OpenStack-Nova-API-Version” ，Value为微版本号，当Value的值为2.19时，支持使用该字段。

        :return: The description of this NovaCreateServersOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaCreateServersOption.

        扩展属性，表示弹性云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“<” 和 “>”等特殊符号。  > 说明： >  > - V2接口不支持该字段。 > - V2.1接口支持该字段，此时，需在请求Header中增加一组Key-Value值。其中，Key固定为“X-OpenStack-Nova-API-Version” ，Value为微版本号，当Value的值为2.19时，支持使用该字段。

        :param description: The description of this NovaCreateServersOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, NovaCreateServersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
