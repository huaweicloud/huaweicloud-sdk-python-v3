# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServer:

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
        'user_data': 'str',
        'admin_pass': 'str',
        'key_name': 'str',
        'vpcid': 'str',
        'nics': 'list[PrePaidServerNic]',
        'publicip': 'PrePaidServerPublicip',
        'count': 'int',
        'is_auto_rename': 'bool',
        'root_volume': 'PrePaidServerRootVolume',
        'data_volumes': 'list[PrePaidServerDataVolume]',
        'security_groups': 'list[PrePaidServerSecurityGroup]',
        'availability_zone': 'str',
        'batch_create_in_multi_az': 'bool',
        'extendparam': 'PrePaidServerExtendParam',
        'metadata': 'dict(str, str)',
        'osscheduler_hints': 'PrePaidServerSchedulerHints',
        'tags': 'list[str]',
        'server_tags': 'list[PrePaidServerTag]',
        'description': 'str',
        'cpu_options': 'CpuOptions'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time',
        'image_ref': 'imageRef',
        'flavor_ref': 'flavorRef',
        'name': 'name',
        'user_data': 'user_data',
        'admin_pass': 'adminPass',
        'key_name': 'key_name',
        'vpcid': 'vpcid',
        'nics': 'nics',
        'publicip': 'publicip',
        'count': 'count',
        'is_auto_rename': 'isAutoRename',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'security_groups': 'security_groups',
        'availability_zone': 'availability_zone',
        'batch_create_in_multi_az': 'batch_create_in_multi_az',
        'extendparam': 'extendparam',
        'metadata': 'metadata',
        'osscheduler_hints': 'os:scheduler_hints',
        'tags': 'tags',
        'server_tags': 'server_tags',
        'description': 'description',
        'cpu_options': 'cpu_options'
    }

    def __init__(self, auto_terminate_time=None, image_ref=None, flavor_ref=None, name=None, user_data=None, admin_pass=None, key_name=None, vpcid=None, nics=None, publicip=None, count=None, is_auto_rename=None, root_volume=None, data_volumes=None, security_groups=None, availability_zone=None, batch_create_in_multi_az=None, extendparam=None, metadata=None, osscheduler_hints=None, tags=None, server_tags=None, description=None, cpu_options=None):
        """PrePaidServer

        The model defined in huaweicloud sdk

        :param auto_terminate_time: 弹性云服务器定时删除时间。  时间格式例如：2020-01-19T03:30:52Z
        :type auto_terminate_time: str
        :param image_ref: 待创建云服务器的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。  镜像的ID可以从镜像服务的 [查询镜像列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;IMS&amp;api&#x3D;ListImages) 接口获取，该接口可根据 __imagetype、__os_type 等参数过滤选择合适镜像。
        :type image_ref: str
        :param flavor_ref: 待创建云服务器的系统规格的ID。  可通过 [规格列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;ECS&amp;api&#x3D;ListFlavors) 查询，该接口支持通过 availability_zone 参数过滤出待创建云服务器可用区下可用的规格。  已上线的规格请参见《[弹性云服务器产品介绍](https://support.huaweicloud.com/ecs/index.html)》的“实例类型与规格”章节。
        :type flavor_ref: str
        :param name: 云服务器名称。  取值范围：  - 只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。 - 创建的云服务器器数量（count字段对应的值）大于1时，为区分不同云服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-59]个字符。  &gt; 说明： &gt;  &gt; 云服务器虚拟机内部(hostname)命名规则遵循 RFC 952和RFC 1123命名规范，建议使用a-zA-z或0-9以及中划线\&quot;-\&quot;组成的名称命名，\&quot;_\&quot;将在弹性云服务器内部默认转化为\&quot;-\&quot;。
        :type name: str
        :param user_data: 创建云服务器过程中待注入用户数据。支持注入文本、文本文件或gzip文件。  更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。  约束：  - 注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。 - 创建密码方式鉴权的Linux弹性云服务器时，该字段可为root用户注入自定义初始化密码，具体注入密码的使用方法请参见背景信息（设置登录鉴权方式）。 示例（base64编码前）：  - Linux弹性云服务器  &#x60;&#x60;&#x60; #! /bin/bash echo user_test &gt;&gt; /home/user.txt &#x60;&#x60;&#x60;  - Windows弹性云服务器  &#x60;&#x60;&#x60; rem cmd echo 111 &gt; c:\\\\aaa.tx &#x60;&#x60;&#x60;
        :type user_data: str
        :param admin_pass: 如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。具体使用方法请参见背景信息（设置登录鉴权方式）。  密码复杂度要求：   - 长度为8-26位。  - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。 - 密码不能包含用户名或用户名的逆序。  - Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。
        :type admin_pass: str
        :param key_name: 如果需要使用SSH密钥方式登录云服务器，请指定已创建密钥的名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。
        :type key_name: str
        :param vpcid: 待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  可通过 [查询VPC列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;VPC&amp;api&#x3D;ListVpcs) 接口查询。
        :type vpcid: str
        :param nics: 待创建云服务器的网卡信息。  约束：  - 网卡对应的子网（subnet）必须属于vpcid对应的VPC。 - 当前单个云服务器支持最多挂载12张网卡。 - 不同的规格对网卡上限有一定的区别，参考[规格清单](https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0159822360.html)。
        :type nics: list[:class:`huaweicloudsdkecs.v2.PrePaidServerNic`]
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkecs.v2.PrePaidServerPublicip`
        :param count: 创建云服务器数量。  约束：  - 不传该字段时默认取值为1。 - 租户的配额足够时，最大值为500。
        :type count: int
        :param is_auto_rename: 当批量创建弹性云服务器时，云服务器名称是否允许重名，当count大于1的时候该参数生效。默认为True。  - True，表示允许重名。 - False，表示不允许重名。
        :type is_auto_rename: bool
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkecs.v2.PrePaidServerRootVolume`
        :param data_volumes: 云服务器对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。   约束：目前新创建的弹性云服务器最多可挂载23块数据盘。
        :type data_volumes: list[:class:`huaweicloudsdkecs.v2.PrePaidServerDataVolume`]
        :param security_groups: 云服务器对应安全组信息。  约束：当该值指定为空时，默认给云服务器绑定default安全组。
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.PrePaidServerSecurityGroup`]
        :param availability_zone: 待创建云服务器所在的可用分区，需要指定可用分区（AZ）的名称。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;ECS&amp;api&#x3D;NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type availability_zone: str
        :param batch_create_in_multi_az: 是否支持随机多AZ部署。  - “true”：批量创建的ecs部署在多个AZ上 - “false”：批量创建的ecs部署在单个AZ上  &gt; 说明： &gt;  &gt; 当availability_zone为空时该字段生效。
        :type batch_create_in_multi_az: bool
        :param extendparam: 
        :type extendparam: :class:`huaweicloudsdkecs.v2.PrePaidServerExtendParam`
        :param metadata: 用户自定义字段键值对。  &gt; 说明： &gt;  &gt; - 最多可注入10对键值（Key/Value）。 &gt; - 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）组成，长度为[1-255]个字符。 &gt; - 值（value）最大长度为255个字符。  系统预留字段  1. op_svc_userid : 用户ID      当extendparam结构中的chargingMode为prePaid（即创建包年包月付费的云服务器），且使用SSH秘钥方式登录云服务器时，该字段为必选字段。  2. agency_name  :  委托的名称   委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。  &gt; 说明： &gt;  &gt; 委托获取、更新请参考如下步骤： &gt;  &gt; 1. 使用IAM服务提供的[查询委托列表](https://support.huaweicloud.com/api-iam/zh-cn_topic_0079467614.html)接口，获取有效可用的委托名称。 &gt; 2. 使用[更新云服务器元数](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0025560298.html)据接口，更新metadata中agency_name字段为新的委托名称。 
        :type metadata: dict(str, str)
        :param osscheduler_hints: 
        :type osscheduler_hints: :class:`huaweicloudsdkecs.v2.PrePaidServerSchedulerHints`
        :param tags: 弹性云服务器的标签。  标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。  标签命名时，需满足如下要求：  - 标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）以及中文字符。 - 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）、小数点（.）以及中文字符。  &gt; 说明： &gt;  &gt; 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 &gt; 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。
        :type tags: list[str]
        :param server_tags: 弹性云服务器的标签。  &gt; 说明： &gt;  &gt; 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 &gt; 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。
        :type server_tags: list[:class:`huaweicloudsdkecs.v2.PrePaidServerTag`]
        :param description: 云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“&lt;” 和 “&gt;”。
        :type description: str
        :param cpu_options: 
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        
        

        self._auto_terminate_time = None
        self._image_ref = None
        self._flavor_ref = None
        self._name = None
        self._user_data = None
        self._admin_pass = None
        self._key_name = None
        self._vpcid = None
        self._nics = None
        self._publicip = None
        self._count = None
        self._is_auto_rename = None
        self._root_volume = None
        self._data_volumes = None
        self._security_groups = None
        self._availability_zone = None
        self._batch_create_in_multi_az = None
        self._extendparam = None
        self._metadata = None
        self._osscheduler_hints = None
        self._tags = None
        self._server_tags = None
        self._description = None
        self._cpu_options = None
        self.discriminator = None

        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.name = name
        if user_data is not None:
            self.user_data = user_data
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if key_name is not None:
            self.key_name = key_name
        self.vpcid = vpcid
        self.nics = nics
        if publicip is not None:
            self.publicip = publicip
        if count is not None:
            self.count = count
        if is_auto_rename is not None:
            self.is_auto_rename = is_auto_rename
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if security_groups is not None:
            self.security_groups = security_groups
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if batch_create_in_multi_az is not None:
            self.batch_create_in_multi_az = batch_create_in_multi_az
        if extendparam is not None:
            self.extendparam = extendparam
        if metadata is not None:
            self.metadata = metadata
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints
        if tags is not None:
            self.tags = tags
        if server_tags is not None:
            self.server_tags = server_tags
        if description is not None:
            self.description = description
        if cpu_options is not None:
            self.cpu_options = cpu_options

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this PrePaidServer.

        弹性云服务器定时删除时间。  时间格式例如：2020-01-19T03:30:52Z

        :return: The auto_terminate_time of this PrePaidServer.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this PrePaidServer.

        弹性云服务器定时删除时间。  时间格式例如：2020-01-19T03:30:52Z

        :param auto_terminate_time: The auto_terminate_time of this PrePaidServer.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def image_ref(self):
        """Gets the image_ref of this PrePaidServer.

        待创建云服务器的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。  镜像的ID可以从镜像服务的 [查询镜像列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IMS&api=ListImages) 接口获取，该接口可根据 __imagetype、__os_type 等参数过滤选择合适镜像。

        :return: The image_ref of this PrePaidServer.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this PrePaidServer.

        待创建云服务器的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。  镜像的ID可以从镜像服务的 [查询镜像列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IMS&api=ListImages) 接口获取，该接口可根据 __imagetype、__os_type 等参数过滤选择合适镜像。

        :param image_ref: The image_ref of this PrePaidServer.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this PrePaidServer.

        待创建云服务器的系统规格的ID。  可通过 [规格列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=ListFlavors) 查询，该接口支持通过 availability_zone 参数过滤出待创建云服务器可用区下可用的规格。  已上线的规格请参见《[弹性云服务器产品介绍](https://support.huaweicloud.com/ecs/index.html)》的“实例类型与规格”章节。

        :return: The flavor_ref of this PrePaidServer.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this PrePaidServer.

        待创建云服务器的系统规格的ID。  可通过 [规格列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=ListFlavors) 查询，该接口支持通过 availability_zone 参数过滤出待创建云服务器可用区下可用的规格。  已上线的规格请参见《[弹性云服务器产品介绍](https://support.huaweicloud.com/ecs/index.html)》的“实例类型与规格”章节。

        :param flavor_ref: The flavor_ref of this PrePaidServer.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this PrePaidServer.

        云服务器名称。  取值范围：  - 只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。 - 创建的云服务器器数量（count字段对应的值）大于1时，为区分不同云服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-59]个字符。  > 说明： >  > 云服务器虚拟机内部(hostname)命名规则遵循 RFC 952和RFC 1123命名规范，建议使用a-zA-z或0-9以及中划线\"-\"组成的名称命名，\"_\"将在弹性云服务器内部默认转化为\"-\"。

        :return: The name of this PrePaidServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrePaidServer.

        云服务器名称。  取值范围：  - 只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。 - 创建的云服务器器数量（count字段对应的值）大于1时，为区分不同云服务器，创建过程中系统会自动在名称后加“-0000”的类似标记。故此时名称的长度为[1-59]个字符。  > 说明： >  > 云服务器虚拟机内部(hostname)命名规则遵循 RFC 952和RFC 1123命名规范，建议使用a-zA-z或0-9以及中划线\"-\"组成的名称命名，\"_\"将在弹性云服务器内部默认转化为\"-\"。

        :param name: The name of this PrePaidServer.
        :type name: str
        """
        self._name = name

    @property
    def user_data(self):
        """Gets the user_data of this PrePaidServer.

        创建云服务器过程中待注入用户数据。支持注入文本、文本文件或gzip文件。  更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。  约束：  - 注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。 - 创建密码方式鉴权的Linux弹性云服务器时，该字段可为root用户注入自定义初始化密码，具体注入密码的使用方法请参见背景信息（设置登录鉴权方式）。 示例（base64编码前）：  - Linux弹性云服务器  ``` #! /bin/bash echo user_test >> /home/user.txt ```  - Windows弹性云服务器  ``` rem cmd echo 111 > c:\\\\aaa.tx ```

        :return: The user_data of this PrePaidServer.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this PrePaidServer.

        创建云服务器过程中待注入用户数据。支持注入文本、文本文件或gzip文件。  更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。  约束：  - 注入内容，需要进行base64格式编码。注入内容（编码之前的内容）最大长度32KB。 - 创建密码方式鉴权的Linux弹性云服务器时，该字段可为root用户注入自定义初始化密码，具体注入密码的使用方法请参见背景信息（设置登录鉴权方式）。 示例（base64编码前）：  - Linux弹性云服务器  ``` #! /bin/bash echo user_test >> /home/user.txt ```  - Windows弹性云服务器  ``` rem cmd echo 111 > c:\\\\aaa.tx ```

        :param user_data: The user_data of this PrePaidServer.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def admin_pass(self):
        """Gets the admin_pass of this PrePaidServer.

        如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。具体使用方法请参见背景信息（设置登录鉴权方式）。  密码复杂度要求：   - 长度为8-26位。  - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。 - 密码不能包含用户名或用户名的逆序。  - Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :return: The admin_pass of this PrePaidServer.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this PrePaidServer.

        如果需要使用密码方式登录云服务器，可使用adminPass字段指定云服务器管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。具体使用方法请参见背景信息（设置登录鉴权方式）。  密码复杂度要求：   - 长度为8-26位。  - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。 - 密码不能包含用户名或用户名的逆序。  - Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :param admin_pass: The admin_pass of this PrePaidServer.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def key_name(self):
        """Gets the key_name of this PrePaidServer.

        如果需要使用SSH密钥方式登录云服务器，请指定已创建密钥的名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。

        :return: The key_name of this PrePaidServer.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this PrePaidServer.

        如果需要使用SSH密钥方式登录云服务器，请指定已创建密钥的名称。  密钥可以通过密钥创建接口进行创建（请参见[创建和导入SSH密钥](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212678.html)），或使用SSH密钥查询接口查询已有的密钥（请参见[查询SSH密钥列表](https://support.huaweicloud.com/api-ecs/ecs_03_1201.html) ）。

        :param key_name: The key_name of this PrePaidServer.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def vpcid(self):
        """Gets the vpcid of this PrePaidServer.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  可通过 [查询VPC列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=VPC&api=ListVpcs) 接口查询。

        :return: The vpcid of this PrePaidServer.
        :rtype: str
        """
        return self._vpcid

    @vpcid.setter
    def vpcid(self, vpcid):
        """Sets the vpcid of this PrePaidServer.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。  可通过 [查询VPC列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=VPC&api=ListVpcs) 接口查询。

        :param vpcid: The vpcid of this PrePaidServer.
        :type vpcid: str
        """
        self._vpcid = vpcid

    @property
    def nics(self):
        """Gets the nics of this PrePaidServer.

        待创建云服务器的网卡信息。  约束：  - 网卡对应的子网（subnet）必须属于vpcid对应的VPC。 - 当前单个云服务器支持最多挂载12张网卡。 - 不同的规格对网卡上限有一定的区别，参考[规格清单](https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0159822360.html)。

        :return: The nics of this PrePaidServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PrePaidServerNic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this PrePaidServer.

        待创建云服务器的网卡信息。  约束：  - 网卡对应的子网（subnet）必须属于vpcid对应的VPC。 - 当前单个云服务器支持最多挂载12张网卡。 - 不同的规格对网卡上限有一定的区别，参考[规格清单](https://support.huaweicloud.com/productdesc-ecs/zh-cn_topic_0159822360.html)。

        :param nics: The nics of this PrePaidServer.
        :type nics: list[:class:`huaweicloudsdkecs.v2.PrePaidServerNic`]
        """
        self._nics = nics

    @property
    def publicip(self):
        """Gets the publicip of this PrePaidServer.

        :return: The publicip of this PrePaidServer.
        :rtype: :class:`huaweicloudsdkecs.v2.PrePaidServerPublicip`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this PrePaidServer.

        :param publicip: The publicip of this PrePaidServer.
        :type publicip: :class:`huaweicloudsdkecs.v2.PrePaidServerPublicip`
        """
        self._publicip = publicip

    @property
    def count(self):
        """Gets the count of this PrePaidServer.

        创建云服务器数量。  约束：  - 不传该字段时默认取值为1。 - 租户的配额足够时，最大值为500。

        :return: The count of this PrePaidServer.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PrePaidServer.

        创建云服务器数量。  约束：  - 不传该字段时默认取值为1。 - 租户的配额足够时，最大值为500。

        :param count: The count of this PrePaidServer.
        :type count: int
        """
        self._count = count

    @property
    def is_auto_rename(self):
        """Gets the is_auto_rename of this PrePaidServer.

        当批量创建弹性云服务器时，云服务器名称是否允许重名，当count大于1的时候该参数生效。默认为True。  - True，表示允许重名。 - False，表示不允许重名。

        :return: The is_auto_rename of this PrePaidServer.
        :rtype: bool
        """
        return self._is_auto_rename

    @is_auto_rename.setter
    def is_auto_rename(self, is_auto_rename):
        """Sets the is_auto_rename of this PrePaidServer.

        当批量创建弹性云服务器时，云服务器名称是否允许重名，当count大于1的时候该参数生效。默认为True。  - True，表示允许重名。 - False，表示不允许重名。

        :param is_auto_rename: The is_auto_rename of this PrePaidServer.
        :type is_auto_rename: bool
        """
        self._is_auto_rename = is_auto_rename

    @property
    def root_volume(self):
        """Gets the root_volume of this PrePaidServer.

        :return: The root_volume of this PrePaidServer.
        :rtype: :class:`huaweicloudsdkecs.v2.PrePaidServerRootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this PrePaidServer.

        :param root_volume: The root_volume of this PrePaidServer.
        :type root_volume: :class:`huaweicloudsdkecs.v2.PrePaidServerRootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this PrePaidServer.

        云服务器对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。   约束：目前新创建的弹性云服务器最多可挂载23块数据盘。

        :return: The data_volumes of this PrePaidServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PrePaidServerDataVolume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this PrePaidServer.

        云服务器对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。   约束：目前新创建的弹性云服务器最多可挂载23块数据盘。

        :param data_volumes: The data_volumes of this PrePaidServer.
        :type data_volumes: list[:class:`huaweicloudsdkecs.v2.PrePaidServerDataVolume`]
        """
        self._data_volumes = data_volumes

    @property
    def security_groups(self):
        """Gets the security_groups of this PrePaidServer.

        云服务器对应安全组信息。  约束：当该值指定为空时，默认给云服务器绑定default安全组。

        :return: The security_groups of this PrePaidServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PrePaidServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this PrePaidServer.

        云服务器对应安全组信息。  约束：当该值指定为空时，默认给云服务器绑定default安全组。

        :param security_groups: The security_groups of this PrePaidServer.
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.PrePaidServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def availability_zone(self):
        """Gets the availability_zone of this PrePaidServer.

        待创建云服务器所在的可用分区，需要指定可用分区（AZ）的名称。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The availability_zone of this PrePaidServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this PrePaidServer.

        待创建云服务器所在的可用分区，需要指定可用分区（AZ）的名称。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param availability_zone: The availability_zone of this PrePaidServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def batch_create_in_multi_az(self):
        """Gets the batch_create_in_multi_az of this PrePaidServer.

        是否支持随机多AZ部署。  - “true”：批量创建的ecs部署在多个AZ上 - “false”：批量创建的ecs部署在单个AZ上  > 说明： >  > 当availability_zone为空时该字段生效。

        :return: The batch_create_in_multi_az of this PrePaidServer.
        :rtype: bool
        """
        return self._batch_create_in_multi_az

    @batch_create_in_multi_az.setter
    def batch_create_in_multi_az(self, batch_create_in_multi_az):
        """Sets the batch_create_in_multi_az of this PrePaidServer.

        是否支持随机多AZ部署。  - “true”：批量创建的ecs部署在多个AZ上 - “false”：批量创建的ecs部署在单个AZ上  > 说明： >  > 当availability_zone为空时该字段生效。

        :param batch_create_in_multi_az: The batch_create_in_multi_az of this PrePaidServer.
        :type batch_create_in_multi_az: bool
        """
        self._batch_create_in_multi_az = batch_create_in_multi_az

    @property
    def extendparam(self):
        """Gets the extendparam of this PrePaidServer.

        :return: The extendparam of this PrePaidServer.
        :rtype: :class:`huaweicloudsdkecs.v2.PrePaidServerExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PrePaidServer.

        :param extendparam: The extendparam of this PrePaidServer.
        :type extendparam: :class:`huaweicloudsdkecs.v2.PrePaidServerExtendParam`
        """
        self._extendparam = extendparam

    @property
    def metadata(self):
        """Gets the metadata of this PrePaidServer.

        用户自定义字段键值对。  > 说明： >  > - 最多可注入10对键值（Key/Value）。 > - 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）组成，长度为[1-255]个字符。 > - 值（value）最大长度为255个字符。  系统预留字段  1. op_svc_userid : 用户ID      当extendparam结构中的chargingMode为prePaid（即创建包年包月付费的云服务器），且使用SSH秘钥方式登录云服务器时，该字段为必选字段。  2. agency_name  :  委托的名称   委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。  > 说明： >  > 委托获取、更新请参考如下步骤： >  > 1. 使用IAM服务提供的[查询委托列表](https://support.huaweicloud.com/api-iam/zh-cn_topic_0079467614.html)接口，获取有效可用的委托名称。 > 2. 使用[更新云服务器元数](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0025560298.html)据接口，更新metadata中agency_name字段为新的委托名称。 

        :return: The metadata of this PrePaidServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrePaidServer.

        用户自定义字段键值对。  > 说明： >  > - 最多可注入10对键值（Key/Value）。 > - 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）组成，长度为[1-255]个字符。 > - 值（value）最大长度为255个字符。  系统预留字段  1. op_svc_userid : 用户ID      当extendparam结构中的chargingMode为prePaid（即创建包年包月付费的云服务器），且使用SSH秘钥方式登录云服务器时，该字段为必选字段。  2. agency_name  :  委托的名称   委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。  > 说明： >  > 委托获取、更新请参考如下步骤： >  > 1. 使用IAM服务提供的[查询委托列表](https://support.huaweicloud.com/api-iam/zh-cn_topic_0079467614.html)接口，获取有效可用的委托名称。 > 2. 使用[更新云服务器元数](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0025560298.html)据接口，更新metadata中agency_name字段为新的委托名称。 

        :param metadata: The metadata of this PrePaidServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this PrePaidServer.

        :return: The osscheduler_hints of this PrePaidServer.
        :rtype: :class:`huaweicloudsdkecs.v2.PrePaidServerSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this PrePaidServer.

        :param osscheduler_hints: The osscheduler_hints of this PrePaidServer.
        :type osscheduler_hints: :class:`huaweicloudsdkecs.v2.PrePaidServerSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def tags(self):
        """Gets the tags of this PrePaidServer.

        弹性云服务器的标签。  标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。  标签命名时，需满足如下要求：  - 标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）以及中文字符。 - 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）、小数点（.）以及中文字符。  > 说明： >  > 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 > 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。

        :return: The tags of this PrePaidServer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PrePaidServer.

        弹性云服务器的标签。  标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。  标签命名时，需满足如下要求：  - 标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）以及中文字符。 - 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（_）、中划线（-）、小数点（.）以及中文字符。  > 说明： >  > 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 > 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。

        :param tags: The tags of this PrePaidServer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def server_tags(self):
        """Gets the server_tags of this PrePaidServer.

        弹性云服务器的标签。  > 说明： >  > 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 > 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。

        :return: The server_tags of this PrePaidServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.PrePaidServerTag`]
        """
        return self._server_tags

    @server_tags.setter
    def server_tags(self, server_tags):
        """Sets the server_tags of this PrePaidServer.

        弹性云服务器的标签。  > 说明： >  > 创建弹性云服务器时，一台弹性云服务器最多可以添加10个标签。 > 公有云新增server_tags字段，该字段与tags字段功能相同，支持的key、value取值范围更广，建议使用server_tags字段。

        :param server_tags: The server_tags of this PrePaidServer.
        :type server_tags: list[:class:`huaweicloudsdkecs.v2.PrePaidServerTag`]
        """
        self._server_tags = server_tags

    @property
    def description(self):
        """Gets the description of this PrePaidServer.

        云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“<” 和 “>”。

        :return: The description of this PrePaidServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrePaidServer.

        云服务器描述信息，默认为空字符串。  - 长度最多允许85个字符。 - 不能包含“<” 和 “>”。

        :param description: The description of this PrePaidServer.
        :type description: str
        """
        self._description = description

    @property
    def cpu_options(self):
        """Gets the cpu_options of this PrePaidServer.

        :return: The cpu_options of this PrePaidServer.
        :rtype: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        return self._cpu_options

    @cpu_options.setter
    def cpu_options(self, cpu_options):
        """Sets the cpu_options of this PrePaidServer.

        :param cpu_options: The cpu_options of this PrePaidServer.
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        self._cpu_options = cpu_options

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
        if not isinstance(other, PrePaidServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
