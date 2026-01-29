# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'enable_acl': 'bool',
        'storage_space': 'int',
        'access_user': 'str',
        'password': 'str',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'available_zones': 'list[str]',
        'product_id': 'str',
        'broker_num': 'int',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'enable_publicip': 'bool',
        'publicip_id': 'str',
        'ssl_enable': 'bool',
        'storage_spec_code': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[TagEntity]',
        'bss_param': 'BssParam'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'enable_acl': 'enable_acl',
        'storage_space': 'storage_space',
        'access_user': 'access_user',
        'password': 'password',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'available_zones': 'available_zones',
        'product_id': 'product_id',
        'broker_num': 'broker_num',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id',
        'ssl_enable': 'ssl_enable',
        'storage_spec_code': 'storage_spec_code',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'bss_param': 'bss_param'
    }

    def __init__(self, name=None, description=None, engine=None, engine_version=None, enable_acl=None, storage_space=None, access_user=None, password=None, vpc_id=None, security_group_id=None, subnet_id=None, available_zones=None, product_id=None, broker_num=None, maintain_begin=None, maintain_end=None, enable_publicip=None, publicip_id=None, ssl_enable=None, storage_spec_code=None, enterprise_project_id=None, tags=None, bss_param=None):
        r"""CreateInstanceReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param description: **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\&quot;&gt;\&quot;与\&quot;&lt;\&quot;，字符串首字符不能为\&quot;&#x3D;\&quot;,\&quot;+\&quot;,\&quot;-\&quot;,\&quot;@\&quot;的全角和半角字符。](tag:hcs,fcs)  \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\&quot;。  **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type description: str
        :param engine: **参数解释**： 消息引擎。 **约束限制**： 不涉及 **取值范围**： rabbitmq：RabbitMQ引擎。 **默认取值**： 不涉及。
        :type engine: str
        :param engine_version: **参数解释**： 消息引擎的版本。 **约束限制**： 不涉及 **取值范围**： [- 3.8.35](tag:hws,hws_hk,hws_eu,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,ax,srg) [- 3.12.13](tag:srg) [- 3.13.7](tag:dt) [- AMQP-0-9-1](tag:hws,hws_hk,hws_eu) **默认取值**： 不涉及。
        :type engine_version: str
        :param enable_acl: **参数解释**： ACL访问控制 **约束限制**： 仅AMQP版本支持此参数。 **取值范围**： - true：开启ACL访问控制。 - false：不开启ACL访问控制。 **默认取值**： 不涉及。
        :type enable_acl: bool
        :param storage_space: **参数解释**： 消息存储空间，单位GB。 **约束限制**： 磁盘容量仅支持设置为100的整数倍。 **取值范围**： - 单机实例：100GB~30000GB。  - 集群实例：100GB * 节点数 ~ 30000GB * 节点数。 **默认取值**： 不涉及。
        :type storage_space: int
        :param access_user: **参数解释**：  认证用户名。 **约束限制**： 只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type access_user: str
        :param password: **参数解释**： 实例的认证密码。 **约束限制**： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|[{}]:&#39;\&quot;,&lt;.&gt;/?）和空格，并且不能以-开头 - 当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type password: str
        :param vpc_id: **参数解释**：  虚拟私有云ID。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type vpc_id: str
        :param security_group_id: **参数解释**： 指定实例所属的安全组。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0011.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0011.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0011.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type security_group_id: str
        :param subnet_id: **参数解释**： 子网信息。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_subnet01_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type subnet_id: str
        :param available_zones: **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 **约束限制**： 该参数不能为空数组或者数组的值为空。  创建RabbitMQ实例，节点需要部署在1个或3个及以上可用区中。如果部署在多个可用区中，以英文逗号隔开多个可用区ID。
        :type available_zones: list[str]
        :param product_id: **参数解释**： 产品ID。产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type product_id: str
        :param broker_num: **参数解释**： 代理个数。 **约束限制**： 当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。 **取值范围**： - 1 - 3 - 5 - 7 **默认取值**： 不涉及。
        :type broker_num: int
        :param maintain_begin: **参数解释**： 维护时间窗开始时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type maintain_begin: str
        :param maintain_end: **参数解释**： 维护时间窗结束时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type maintain_end: str
        :param enable_publicip: **参数解释**： 是否开启公网访问功能。 **约束限制**： 不涉及。 **取值范围**： - true：开启 - false：不开启 **默认取值**： false。
        :type enable_publicip: bool
        :param publicip_id: **参数解释**： 实例绑定的弹性IP地址的ID。获取方法：参考[[《弹性公网IP API参考》](https://support.huaweicloud.com/api-eip/ListPublicipsV3.html)](tag:hws)[[《弹性公网IP API参考》](https://support.huaweicloud.com/intl/zh-cn/api-eip/ListPublicipsV3.html)](tag:hws_hk)[[《弹性公网IP API参考》](https://support.huaweicloud.com/eu/api-eip/ListPublicipsV3.html)](tag:hws_eu)[《弹性公网IP API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询弹性公网IP列表”接口，从响应体中获取弹性公网IP的ID。 **约束限制**： 以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type publicip_id: str
        :param ssl_enable: **参数解释**： 是否开启SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：开启SSL加密访问。 - false：关闭SSL加密访问。 **默认取值**： 不涉及。
        :type ssl_enable: bool
        :param storage_spec_code: **参数解释**： 存储IO规格。  [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws_hk) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/eu/productdesc-evs/en-us_topic_0014580744.html)。](tag:hws_eu) **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO云硬盘。 - dms.physical.storage.ultra.v2：超高IO云硬盘。 [- dms.physical.storage.general：通用型SSD云硬盘。](tag:hws,hws_hk,dt,ax) [- dms.physical.storage.extreme：极速型SSD云硬盘。](tag:hws,hws_hk,dt,ax) **默认取值**： 不涉及。
        :type storage_spec_code: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。 **约束限制**： 若为企业项目账号，该参数必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type enterprise_project_id: str
        :param tags: **参数解释**： 标签列表。 **约束限制**： 一个RabbitMQ实例最多添加20个标签。
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
        """
        
        

        self._name = None
        self._description = None
        self._engine = None
        self._engine_version = None
        self._enable_acl = None
        self._storage_space = None
        self._access_user = None
        self._password = None
        self._vpc_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._available_zones = None
        self._product_id = None
        self._broker_num = None
        self._maintain_begin = None
        self._maintain_end = None
        self._enable_publicip = None
        self._publicip_id = None
        self._ssl_enable = None
        self._storage_spec_code = None
        self._enterprise_project_id = None
        self._tags = None
        self._bss_param = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.engine = engine
        self.engine_version = engine_version
        if enable_acl is not None:
            self.enable_acl = enable_acl
        self.storage_space = storage_space
        if access_user is not None:
            self.access_user = access_user
        if password is not None:
            self.password = password
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.subnet_id = subnet_id
        self.available_zones = available_zones
        self.product_id = product_id
        if broker_num is not None:
            self.broker_num = broker_num
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        self.storage_spec_code = storage_spec_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceReq.

        **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this CreateInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceReq.

        **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this CreateInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateInstanceReq.

        **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs,fcs)  \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\"。  **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The description of this CreateInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstanceReq.

        **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs,fcs)  \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\"。  **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param description: The description of this CreateInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        r"""Gets the engine of this CreateInstanceReq.

        **参数解释**： 消息引擎。 **约束限制**： 不涉及 **取值范围**： rabbitmq：RabbitMQ引擎。 **默认取值**： 不涉及。

        :return: The engine of this CreateInstanceReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateInstanceReq.

        **参数解释**： 消息引擎。 **约束限制**： 不涉及 **取值范围**： rabbitmq：RabbitMQ引擎。 **默认取值**： 不涉及。

        :param engine: The engine of this CreateInstanceReq.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CreateInstanceReq.

        **参数解释**： 消息引擎的版本。 **约束限制**： 不涉及 **取值范围**： [- 3.8.35](tag:hws,hws_hk,hws_eu,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,ax,srg) [- 3.12.13](tag:srg) [- 3.13.7](tag:dt) [- AMQP-0-9-1](tag:hws,hws_hk,hws_eu) **默认取值**： 不涉及。

        :return: The engine_version of this CreateInstanceReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CreateInstanceReq.

        **参数解释**： 消息引擎的版本。 **约束限制**： 不涉及 **取值范围**： [- 3.8.35](tag:hws,hws_hk,hws_eu,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,ax,srg) [- 3.12.13](tag:srg) [- 3.13.7](tag:dt) [- AMQP-0-9-1](tag:hws,hws_hk,hws_eu) **默认取值**： 不涉及。

        :param engine_version: The engine_version of this CreateInstanceReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this CreateInstanceReq.

        **参数解释**： ACL访问控制 **约束限制**： 仅AMQP版本支持此参数。 **取值范围**： - true：开启ACL访问控制。 - false：不开启ACL访问控制。 **默认取值**： 不涉及。

        :return: The enable_acl of this CreateInstanceReq.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this CreateInstanceReq.

        **参数解释**： ACL访问控制 **约束限制**： 仅AMQP版本支持此参数。 **取值范围**： - true：开启ACL访问控制。 - false：不开启ACL访问控制。 **默认取值**： 不涉及。

        :param enable_acl: The enable_acl of this CreateInstanceReq.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def storage_space(self):
        r"""Gets the storage_space of this CreateInstanceReq.

        **参数解释**： 消息存储空间，单位GB。 **约束限制**： 磁盘容量仅支持设置为100的整数倍。 **取值范围**： - 单机实例：100GB~30000GB。  - 集群实例：100GB * 节点数 ~ 30000GB * 节点数。 **默认取值**： 不涉及。

        :return: The storage_space of this CreateInstanceReq.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        r"""Sets the storage_space of this CreateInstanceReq.

        **参数解释**： 消息存储空间，单位GB。 **约束限制**： 磁盘容量仅支持设置为100的整数倍。 **取值范围**： - 单机实例：100GB~30000GB。  - 集群实例：100GB * 节点数 ~ 30000GB * 节点数。 **默认取值**： 不涉及。

        :param storage_space: The storage_space of this CreateInstanceReq.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def access_user(self):
        r"""Gets the access_user of this CreateInstanceReq.

        **参数解释**：  认证用户名。 **约束限制**： 只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The access_user of this CreateInstanceReq.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        r"""Sets the access_user of this CreateInstanceReq.

        **参数解释**：  认证用户名。 **约束限制**： 只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param access_user: The access_user of this CreateInstanceReq.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def password(self):
        r"""Gets the password of this CreateInstanceReq.

        **参数解释**： 实例的认证密码。 **约束限制**： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）和空格，并且不能以-开头 - 当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The password of this CreateInstanceReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateInstanceReq.

        **参数解释**： 实例的认证密码。 **约束限制**： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）和空格，并且不能以-开头 - 当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param password: The password of this CreateInstanceReq.
        :type password: str
        """
        self._password = password

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceReq.

        **参数解释**：  虚拟私有云ID。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The vpc_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceReq.

        **参数解释**：  虚拟私有云ID。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param vpc_id: The vpc_id of this CreateInstanceReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateInstanceReq.

        **参数解释**： 指定实例所属的安全组。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0011.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0011.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0011.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_group_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateInstanceReq.

        **参数解释**： 指定实例所属的安全组。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0011.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_apiv3_0011.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_apiv3_0011.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param security_group_id: The security_group_id of this CreateInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceReq.

        **参数解释**： 子网信息。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_subnet01_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The subnet_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceReq.

        **参数解释**： 子网信息。获取方法如下：参考[[《虚拟私有云 API参考》](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)](tag:hws)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)](tag:hws_hk)[[《虚拟私有云 API参考》](https://support.huaweicloud.com/eu/api-vpc/vpc_subnet01_0003.html)](tag:hws_eu)[《虚拟私有云 API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param subnet_id: The subnet_id of this CreateInstanceReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def available_zones(self):
        r"""Gets the available_zones of this CreateInstanceReq.

        **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 **约束限制**： 该参数不能为空数组或者数组的值为空。  创建RabbitMQ实例，节点需要部署在1个或3个及以上可用区中。如果部署在多个可用区中，以英文逗号隔开多个可用区ID。

        :return: The available_zones of this CreateInstanceReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this CreateInstanceReq.

        **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 **约束限制**： 该参数不能为空数组或者数组的值为空。  创建RabbitMQ实例，节点需要部署在1个或3个及以上可用区中。如果部署在多个可用区中，以英文逗号隔开多个可用区ID。

        :param available_zones: The available_zones of this CreateInstanceReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateInstanceReq.

        **参数解释**： 产品ID。产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The product_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateInstanceReq.

        **参数解释**： 产品ID。产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param product_id: The product_id of this CreateInstanceReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def broker_num(self):
        r"""Gets the broker_num of this CreateInstanceReq.

        **参数解释**： 代理个数。 **约束限制**： 当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。 **取值范围**： - 1 - 3 - 5 - 7 **默认取值**： 不涉及。

        :return: The broker_num of this CreateInstanceReq.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this CreateInstanceReq.

        **参数解释**： 代理个数。 **约束限制**： 当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。 **取值范围**： - 1 - 3 - 5 - 7 **默认取值**： 不涉及。

        :param broker_num: The broker_num of this CreateInstanceReq.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def maintain_begin(self):
        r"""Gets the maintain_begin of this CreateInstanceReq.

        **参数解释**： 维护时间窗开始时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The maintain_begin of this CreateInstanceReq.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        r"""Sets the maintain_begin of this CreateInstanceReq.

        **参数解释**： 维护时间窗开始时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param maintain_begin: The maintain_begin of this CreateInstanceReq.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        r"""Gets the maintain_end of this CreateInstanceReq.

        **参数解释**： 维护时间窗结束时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The maintain_end of this CreateInstanceReq.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        r"""Sets the maintain_end of this CreateInstanceReq.

        **参数解释**： 维护时间窗结束时间。 **约束限制**： 格式为HH:mm。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param maintain_end: The maintain_end of this CreateInstanceReq.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this CreateInstanceReq.

        **参数解释**： 是否开启公网访问功能。 **约束限制**： 不涉及。 **取值范围**： - true：开启 - false：不开启 **默认取值**： false。

        :return: The enable_publicip of this CreateInstanceReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this CreateInstanceReq.

        **参数解释**： 是否开启公网访问功能。 **约束限制**： 不涉及。 **取值范围**： - true：开启 - false：不开启 **默认取值**： false。

        :param enable_publicip: The enable_publicip of this CreateInstanceReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this CreateInstanceReq.

        **参数解释**： 实例绑定的弹性IP地址的ID。获取方法：参考[[《弹性公网IP API参考》](https://support.huaweicloud.com/api-eip/ListPublicipsV3.html)](tag:hws)[[《弹性公网IP API参考》](https://support.huaweicloud.com/intl/zh-cn/api-eip/ListPublicipsV3.html)](tag:hws_hk)[[《弹性公网IP API参考》](https://support.huaweicloud.com/eu/api-eip/ListPublicipsV3.html)](tag:hws_eu)[《弹性公网IP API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询弹性公网IP列表”接口，从响应体中获取弹性公网IP的ID。 **约束限制**： 以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The publicip_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this CreateInstanceReq.

        **参数解释**： 实例绑定的弹性IP地址的ID。获取方法：参考[[《弹性公网IP API参考》](https://support.huaweicloud.com/api-eip/ListPublicipsV3.html)](tag:hws)[[《弹性公网IP API参考》](https://support.huaweicloud.com/intl/zh-cn/api-eip/ListPublicipsV3.html)](tag:hws_hk)[[《弹性公网IP API参考》](https://support.huaweicloud.com/eu/api-eip/ListPublicipsV3.html)](tag:hws_eu)[《弹性公网IP API参考》](tag:ax,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm,srg,dt)，调用“查询弹性公网IP列表”接口，从响应体中获取弹性公网IP的ID。 **约束限制**： 以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param publicip_id: The publicip_id of this CreateInstanceReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this CreateInstanceReq.

        **参数解释**： 是否开启SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：开启SSL加密访问。 - false：关闭SSL加密访问。 **默认取值**： 不涉及。

        :return: The ssl_enable of this CreateInstanceReq.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this CreateInstanceReq.

        **参数解释**： 是否开启SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：开启SSL加密访问。 - false：关闭SSL加密访问。 **默认取值**： 不涉及。

        :param ssl_enable: The ssl_enable of this CreateInstanceReq.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this CreateInstanceReq.

        **参数解释**： 存储IO规格。  [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws_hk) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/eu/productdesc-evs/en-us_topic_0014580744.html)。](tag:hws_eu) **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO云硬盘。 - dms.physical.storage.ultra.v2：超高IO云硬盘。 [- dms.physical.storage.general：通用型SSD云硬盘。](tag:hws,hws_hk,dt,ax) [- dms.physical.storage.extreme：极速型SSD云硬盘。](tag:hws,hws_hk,dt,ax) **默认取值**： 不涉及。

        :return: The storage_spec_code of this CreateInstanceReq.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this CreateInstanceReq.

        **参数解释**： 存储IO规格。  [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0014580744.html)。](tag:hws_hk) [如何选择磁盘类型请参考[磁盘类型及性能介绍](https://support.huaweicloud.com/eu/productdesc-evs/en-us_topic_0014580744.html)。](tag:hws_eu) **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO云硬盘。 - dms.physical.storage.ultra.v2：超高IO云硬盘。 [- dms.physical.storage.general：通用型SSD云硬盘。](tag:hws,hws_hk,dt,ax) [- dms.physical.storage.extreme：极速型SSD云硬盘。](tag:hws,hws_hk,dt,ax) **默认取值**： 不涉及。

        :param storage_spec_code: The storage_spec_code of this CreateInstanceReq.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceReq.

        **参数解释**： 企业项目ID。 **约束限制**： 若为企业项目账号，该参数必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The enterprise_project_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceReq.

        **参数解释**： 企业项目ID。 **约束限制**： 若为企业项目账号，该参数必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateInstanceReq.

        **参数解释**： 标签列表。 **约束限制**： 一个RabbitMQ实例最多添加20个标签。

        :return: The tags of this CreateInstanceReq.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateInstanceReq.

        **参数解释**： 标签列表。 **约束限制**： 一个RabbitMQ实例最多添加20个标签。

        :param tags: The tags of this CreateInstanceReq.
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def bss_param(self):
        r"""Gets the bss_param of this CreateInstanceReq.

        :return: The bss_param of this CreateInstanceReq.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        r"""Sets the bss_param of this CreateInstanceReq.

        :param bss_param: The bss_param of this CreateInstanceReq.
        :type bss_param: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, CreateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
