# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image_ref': 'str',
        'flavor_ref': 'str',
        'name': 'str',
        'metadata': 'MetaDataInfo',
        'user_data': 'str',
        'admin_pass': 'str',
        'key_name': 'str',
        'security_groups': 'list[SecurityGroupsInfo]',
        'nics': 'list[Nics]',
        'availability_zone': 'str',
        'vpcid': 'str',
        'publicip': 'PublicIp',
        'count': 'int',
        'root_volume': 'RootVolume',
        'data_volumes': 'list[DataVolumes]',
        'extendparam': 'ExtendParam',
        'scheduler_hints': 'CreateSchedulerHints',
        'server_tags': 'list[SystemTags]'
    }

    attribute_map = {
        'image_ref': 'imageRef',
        'flavor_ref': 'flavorRef',
        'name': 'name',
        'metadata': 'metadata',
        'user_data': 'user_data',
        'admin_pass': 'adminPass',
        'key_name': 'key_name',
        'security_groups': 'security_groups',
        'nics': 'nics',
        'availability_zone': 'availability_zone',
        'vpcid': 'vpcid',
        'publicip': 'publicip',
        'count': 'count',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'extendparam': 'extendparam',
        'scheduler_hints': 'schedulerHints',
        'server_tags': 'server_tags'
    }

    def __init__(self, image_ref=None, flavor_ref=None, name=None, metadata=None, user_data=None, admin_pass=None, key_name=None, security_groups=None, nics=None, availability_zone=None, vpcid=None, publicip=None, count=None, root_volume=None, data_volumes=None, extendparam=None, scheduler_hints=None, server_tags=None):
        """CreateServers

        The model defined in huaweicloud sdk

        :param image_ref: 裸金属服务器使用的镜像ID或者镜像资源的URL。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type&#x3D;Ironic”来筛选裸金属服务器镜像。
        :type image_ref: str
        :param flavor_ref: 裸金属服务器使用的规格ID，格式为physical.x.x。规格ID可以从裸金属服务器控制台获取，也可以通过7.7.1-查询裸金属服务器规格信息列表（OpenStack原生）API查询。 说明：裸金属服务器规格与镜像间的约束关系请参见裸金属服务器类型与支持的操作系统版本。对于physical.x.x.hba类型的规格，申请的租户只能是DeC租户，且只能挂载DESS卷。
        :type flavor_ref: str
        :param name: 裸金属服务器名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。创建的裸金属服务器数量大于1时，为区分不同裸金属服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-58]个字符。
        :type name: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkbms.v1.MetaDataInfo`
        :param user_data: 创建裸金属服务器过程中待注入的用户数据。支持注入文本、文本文件或gzip文件。约束：注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。当key_name没有指定时，user_data注入的数据默认为裸金属服务器root帐户的登录密码。创建密码方式鉴权的Linux裸金属服务器时为必填项，为root用户注入自定义初始化密码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。示例：使用明文密码（存在安全风险），以密码cloud.1234为例：#!/bin/bash echo &#39;root:Cloud.1234&#39; | chpasswd ;使用密码：#!/bin/bash echo &#39;root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig&#39; | chpasswd -e其中，$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig为密文密码
        :type user_data: str
        :param admin_pass: 如果需要使用密码方式登录裸金属服务器，可使用adminPass字段指定裸金属服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。密码复杂度要求：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。Linux系统密码不能包含用户名或用户名的逆序。Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。
        :type admin_pass: str
        :param key_name: 扩展属性，指定密钥的名称。如果需要使用SSH密钥方式登录裸金属服务器，请指定已有密钥的名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。约束：当key_name和user_data同时指定时，user_data只能用做用户数据注入。Windows裸金属服务器登录时，首先需要将密钥解析为密码，然后通过远程登录工具进行登录。具体请参见“MSTSC密码方式登录”“MSTSC密码方式登录”。
        :type key_name: str
        :param security_groups: 指定裸金属服务器的安全组。详情请参见表 security_groups字段数据结构说明。
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsInfo`]
        :param nics: 指定裸金属服务器的网卡信息。详情请参见表 nics字段数据结构说明。约束：一个裸金属服务器最多挂载2个网卡，参数中第一个网卡会作为裸金属服务器的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。
        :type nics: list[:class:`huaweicloudsdkbms.v1.Nics`]
        :param availability_zone: 裸金属服务器对应可用区信息，需要指定可用区（AZ）的名称。请参考地区和终端节点获取。
        :type availability_zone: str
        :param vpcid: 创建裸金属服务器所属虚拟私有云（VPC），需要指定已有VPC的ID，UUID格式。VPC的ID可以从网络控制台或者参考《虚拟私有云API参考》的“查询VPC”。
        :type vpcid: str
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkbms.v1.PublicIp`
        :param count: 创建裸金属服务器的数量。约束：不传该字段时默认取值为1。租户的配额足够时，最大值为24。
        :type count: int
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkbms.v1.RootVolume`
        :param data_volumes: 裸金属服务器对应数据盘相关配置。每一个数据结构代表一个待创建的数据盘。详情请参见表 data_volumes字段数据结构说明。约束：目前裸金属服务器最多可挂载60块云硬盘（包括系统盘和数据盘）。
        :type data_volumes: list[:class:`huaweicloudsdkbms.v1.DataVolumes`]
        :param extendparam: 
        :type extendparam: :class:`huaweicloudsdkbms.v1.ExtendParam`
        :param scheduler_hints: 
        :type scheduler_hints: :class:`huaweicloudsdkbms.v1.CreateSchedulerHints`
        :param server_tags: 裸金属服务器的标签。详情请参见表 server_tags字段数据结构说明。 说明：创建裸金属服务器时，一台裸金属服务器最多可以添加10个标签。其中，__type_baremetal为系统内部标签，因此实际能添加的标签为9个。
        :type server_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        
        

        self._image_ref = None
        self._flavor_ref = None
        self._name = None
        self._metadata = None
        self._user_data = None
        self._admin_pass = None
        self._key_name = None
        self._security_groups = None
        self._nics = None
        self._availability_zone = None
        self._vpcid = None
        self._publicip = None
        self._count = None
        self._root_volume = None
        self._data_volumes = None
        self._extendparam = None
        self._scheduler_hints = None
        self._server_tags = None
        self.discriminator = None

        self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.name = name
        self.metadata = metadata
        if user_data is not None:
            self.user_data = user_data
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if key_name is not None:
            self.key_name = key_name
        if security_groups is not None:
            self.security_groups = security_groups
        self.nics = nics
        self.availability_zone = availability_zone
        self.vpcid = vpcid
        if publicip is not None:
            self.publicip = publicip
        if count is not None:
            self.count = count
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        self.extendparam = extendparam
        if scheduler_hints is not None:
            self.scheduler_hints = scheduler_hints
        if server_tags is not None:
            self.server_tags = server_tags

    @property
    def image_ref(self):
        """Gets the image_ref of this CreateServers.

        裸金属服务器使用的镜像ID或者镜像资源的URL。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type=Ironic”来筛选裸金属服务器镜像。

        :return: The image_ref of this CreateServers.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this CreateServers.

        裸金属服务器使用的镜像ID或者镜像资源的URL。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像ID可以从镜像服务控制台获取，或者参考《镜像服务API参考》的“查询镜像列表”章节查询。在使用“查询镜像列表”API查询时，可以添加过滤字段“?virtual_env_type=Ironic”来筛选裸金属服务器镜像。

        :param image_ref: The image_ref of this CreateServers.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateServers.

        裸金属服务器使用的规格ID，格式为physical.x.x。规格ID可以从裸金属服务器控制台获取，也可以通过7.7.1-查询裸金属服务器规格信息列表（OpenStack原生）API查询。 说明：裸金属服务器规格与镜像间的约束关系请参见裸金属服务器类型与支持的操作系统版本。对于physical.x.x.hba类型的规格，申请的租户只能是DeC租户，且只能挂载DESS卷。

        :return: The flavor_ref of this CreateServers.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateServers.

        裸金属服务器使用的规格ID，格式为physical.x.x。规格ID可以从裸金属服务器控制台获取，也可以通过7.7.1-查询裸金属服务器规格信息列表（OpenStack原生）API查询。 说明：裸金属服务器规格与镜像间的约束关系请参见裸金属服务器类型与支持的操作系统版本。对于physical.x.x.hba类型的规格，申请的租户只能是DeC租户，且只能挂载DESS卷。

        :param flavor_ref: The flavor_ref of this CreateServers.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this CreateServers.

        裸金属服务器名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。创建的裸金属服务器数量大于1时，为区分不同裸金属服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-58]个字符。

        :return: The name of this CreateServers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateServers.

        裸金属服务器名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。创建的裸金属服务器数量大于1时，为区分不同裸金属服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-58]个字符。

        :param name: The name of this CreateServers.
        :type name: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this CreateServers.


        :return: The metadata of this CreateServers.
        :rtype: :class:`huaweicloudsdkbms.v1.MetaDataInfo`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateServers.


        :param metadata: The metadata of this CreateServers.
        :type metadata: :class:`huaweicloudsdkbms.v1.MetaDataInfo`
        """
        self._metadata = metadata

    @property
    def user_data(self):
        """Gets the user_data of this CreateServers.

        创建裸金属服务器过程中待注入的用户数据。支持注入文本、文本文件或gzip文件。约束：注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。当key_name没有指定时，user_data注入的数据默认为裸金属服务器root帐户的登录密码。创建密码方式鉴权的Linux裸金属服务器时为必填项，为root用户注入自定义初始化密码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。示例：使用明文密码（存在安全风险），以密码cloud.1234为例：#!/bin/bash echo 'root:Cloud.1234' | chpasswd ;使用密码：#!/bin/bash echo 'root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig' | chpasswd -e其中，$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig为密文密码

        :return: The user_data of this CreateServers.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateServers.

        创建裸金属服务器过程中待注入的用户数据。支持注入文本、文本文件或gzip文件。约束：注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。当key_name没有指定时，user_data注入的数据默认为裸金属服务器root帐户的登录密码。创建密码方式鉴权的Linux裸金属服务器时为必填项，为root用户注入自定义初始化密码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。示例：使用明文密码（存在安全风险），以密码cloud.1234为例：#!/bin/bash echo 'root:Cloud.1234' | chpasswd ;使用密码：#!/bin/bash echo 'root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig' | chpasswd -e其中，$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig为密文密码

        :param user_data: The user_data of this CreateServers.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def admin_pass(self):
        """Gets the admin_pass of this CreateServers.

        如果需要使用密码方式登录裸金属服务器，可使用adminPass字段指定裸金属服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。密码复杂度要求：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。Linux系统密码不能包含用户名或用户名的逆序。Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :return: The admin_pass of this CreateServers.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this CreateServers.

        如果需要使用密码方式登录裸金属服务器，可使用adminPass字段指定裸金属服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。密码复杂度要求：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。Linux系统密码不能包含用户名或用户名的逆序。Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :param admin_pass: The admin_pass of this CreateServers.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def key_name(self):
        """Gets the key_name of this CreateServers.

        扩展属性，指定密钥的名称。如果需要使用SSH密钥方式登录裸金属服务器，请指定已有密钥的名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。约束：当key_name和user_data同时指定时，user_data只能用做用户数据注入。Windows裸金属服务器登录时，首先需要将密钥解析为密码，然后通过远程登录工具进行登录。具体请参见“MSTSC密码方式登录”“MSTSC密码方式登录”。

        :return: The key_name of this CreateServers.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this CreateServers.

        扩展属性，指定密钥的名称。如果需要使用SSH密钥方式登录裸金属服务器，请指定已有密钥的名称。密钥可以通过7.10.3-创建和导入SSH密钥（OpenStack原生）API创建，或者使用7.10.1-查询SSH密钥列表（OpenStack原生）API查询已有的密钥。约束：当key_name和user_data同时指定时，user_data只能用做用户数据注入。Windows裸金属服务器登录时，首先需要将密钥解析为密码，然后通过远程登录工具进行登录。具体请参见“MSTSC密码方式登录”“MSTSC密码方式登录”。

        :param key_name: The key_name of this CreateServers.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateServers.

        指定裸金属服务器的安全组。详情请参见表 security_groups字段数据结构说明。

        :return: The security_groups of this CreateServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateServers.

        指定裸金属服务器的安全组。详情请参见表 security_groups字段数据结构说明。

        :param security_groups: The security_groups of this CreateServers.
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsInfo`]
        """
        self._security_groups = security_groups

    @property
    def nics(self):
        """Gets the nics of this CreateServers.

        指定裸金属服务器的网卡信息。详情请参见表 nics字段数据结构说明。约束：一个裸金属服务器最多挂载2个网卡，参数中第一个网卡会作为裸金属服务器的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :return: The nics of this CreateServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateServers.

        指定裸金属服务器的网卡信息。详情请参见表 nics字段数据结构说明。约束：一个裸金属服务器最多挂载2个网卡，参数中第一个网卡会作为裸金属服务器的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :param nics: The nics of this CreateServers.
        :type nics: list[:class:`huaweicloudsdkbms.v1.Nics`]
        """
        self._nics = nics

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateServers.

        裸金属服务器对应可用区信息，需要指定可用区（AZ）的名称。请参考地区和终端节点获取。

        :return: The availability_zone of this CreateServers.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateServers.

        裸金属服务器对应可用区信息，需要指定可用区（AZ）的名称。请参考地区和终端节点获取。

        :param availability_zone: The availability_zone of this CreateServers.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpcid(self):
        """Gets the vpcid of this CreateServers.

        创建裸金属服务器所属虚拟私有云（VPC），需要指定已有VPC的ID，UUID格式。VPC的ID可以从网络控制台或者参考《虚拟私有云API参考》的“查询VPC”。

        :return: The vpcid of this CreateServers.
        :rtype: str
        """
        return self._vpcid

    @vpcid.setter
    def vpcid(self, vpcid):
        """Sets the vpcid of this CreateServers.

        创建裸金属服务器所属虚拟私有云（VPC），需要指定已有VPC的ID，UUID格式。VPC的ID可以从网络控制台或者参考《虚拟私有云API参考》的“查询VPC”。

        :param vpcid: The vpcid of this CreateServers.
        :type vpcid: str
        """
        self._vpcid = vpcid

    @property
    def publicip(self):
        """Gets the publicip of this CreateServers.


        :return: The publicip of this CreateServers.
        :rtype: :class:`huaweicloudsdkbms.v1.PublicIp`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreateServers.


        :param publicip: The publicip of this CreateServers.
        :type publicip: :class:`huaweicloudsdkbms.v1.PublicIp`
        """
        self._publicip = publicip

    @property
    def count(self):
        """Gets the count of this CreateServers.

        创建裸金属服务器的数量。约束：不传该字段时默认取值为1。租户的配额足够时，最大值为24。

        :return: The count of this CreateServers.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateServers.

        创建裸金属服务器的数量。约束：不传该字段时默认取值为1。租户的配额足够时，最大值为24。

        :param count: The count of this CreateServers.
        :type count: int
        """
        self._count = count

    @property
    def root_volume(self):
        """Gets the root_volume of this CreateServers.


        :return: The root_volume of this CreateServers.
        :rtype: :class:`huaweicloudsdkbms.v1.RootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CreateServers.


        :param root_volume: The root_volume of this CreateServers.
        :type root_volume: :class:`huaweicloudsdkbms.v1.RootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this CreateServers.

        裸金属服务器对应数据盘相关配置。每一个数据结构代表一个待创建的数据盘。详情请参见表 data_volumes字段数据结构说明。约束：目前裸金属服务器最多可挂载60块云硬盘（包括系统盘和数据盘）。

        :return: The data_volumes of this CreateServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.DataVolumes`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this CreateServers.

        裸金属服务器对应数据盘相关配置。每一个数据结构代表一个待创建的数据盘。详情请参见表 data_volumes字段数据结构说明。约束：目前裸金属服务器最多可挂载60块云硬盘（包括系统盘和数据盘）。

        :param data_volumes: The data_volumes of this CreateServers.
        :type data_volumes: list[:class:`huaweicloudsdkbms.v1.DataVolumes`]
        """
        self._data_volumes = data_volumes

    @property
    def extendparam(self):
        """Gets the extendparam of this CreateServers.


        :return: The extendparam of this CreateServers.
        :rtype: :class:`huaweicloudsdkbms.v1.ExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this CreateServers.


        :param extendparam: The extendparam of this CreateServers.
        :type extendparam: :class:`huaweicloudsdkbms.v1.ExtendParam`
        """
        self._extendparam = extendparam

    @property
    def scheduler_hints(self):
        """Gets the scheduler_hints of this CreateServers.


        :return: The scheduler_hints of this CreateServers.
        :rtype: :class:`huaweicloudsdkbms.v1.CreateSchedulerHints`
        """
        return self._scheduler_hints

    @scheduler_hints.setter
    def scheduler_hints(self, scheduler_hints):
        """Sets the scheduler_hints of this CreateServers.


        :param scheduler_hints: The scheduler_hints of this CreateServers.
        :type scheduler_hints: :class:`huaweicloudsdkbms.v1.CreateSchedulerHints`
        """
        self._scheduler_hints = scheduler_hints

    @property
    def server_tags(self):
        """Gets the server_tags of this CreateServers.

        裸金属服务器的标签。详情请参见表 server_tags字段数据结构说明。 说明：创建裸金属服务器时，一台裸金属服务器最多可以添加10个标签。其中，__type_baremetal为系统内部标签，因此实际能添加的标签为9个。

        :return: The server_tags of this CreateServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        return self._server_tags

    @server_tags.setter
    def server_tags(self, server_tags):
        """Sets the server_tags of this CreateServers.

        裸金属服务器的标签。详情请参见表 server_tags字段数据结构说明。 说明：创建裸金属服务器时，一台裸金属服务器最多可以添加10个标签。其中，__type_baremetal为系统内部标签，因此实际能添加的标签为9个。

        :param server_tags: The server_tags of this CreateServers.
        :type server_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        self._server_tags = server_tags

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
        if not isinstance(other, CreateServers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
