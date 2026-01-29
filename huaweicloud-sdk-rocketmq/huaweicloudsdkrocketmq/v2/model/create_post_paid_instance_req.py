# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePostPaidInstanceReq:

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
        'storage_space': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'available_zones': 'list[str]',
        'product_id': 'str',
        'ssl_enable': 'bool',
        'storage_spec_code': 'str',
        'enterprise_project_id': 'str',
        'enable_acl': 'bool',
        'ipv6_enable': 'bool',
        'proxy_enable': 'bool',
        'enable_publicip': 'bool',
        'disk_encrypted_enable': 'bool',
        'disk_encrypted_key': 'str',
        'publicip_id': 'str',
        'broker_num': 'int',
        'arch_type': 'str',
        'tls_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'storage_space': 'storage_space',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'available_zones': 'available_zones',
        'product_id': 'product_id',
        'ssl_enable': 'ssl_enable',
        'storage_spec_code': 'storage_spec_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enable_acl': 'enable_acl',
        'ipv6_enable': 'ipv6_enable',
        'proxy_enable': 'proxy_enable',
        'enable_publicip': 'enable_publicip',
        'disk_encrypted_enable': 'disk_encrypted_enable',
        'disk_encrypted_key': 'disk_encrypted_key',
        'publicip_id': 'publicip_id',
        'broker_num': 'broker_num',
        'arch_type': 'arch_type',
        'tls_mode': 'tls_mode'
    }

    def __init__(self, name=None, description=None, engine=None, engine_version=None, storage_space=None, vpc_id=None, subnet_id=None, security_group_id=None, available_zones=None, product_id=None, ssl_enable=None, storage_spec_code=None, enterprise_project_id=None, enable_acl=None, ipv6_enable=None, proxy_enable=None, enable_publicip=None, disk_encrypted_enable=None, disk_encrypted_key=None, publicip_id=None, broker_num=None, arch_type=None, tls_mode=None):
        r"""CreatePostPaidInstanceReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param description: **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\&quot;&gt;\&quot;与\&quot;&lt;\&quot;，字符串首字符不能为\&quot;&#x3D;\&quot;,\&quot;+\&quot;,\&quot;-\&quot;,\&quot;@\&quot;的全角和半角字符。](tag:hcs)  \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\&quot;。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type description: str
        :param engine: **参数解释**： 消息引擎类型。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。
        :type engine: str
        :param engine_version: **参数解释**： 消息引擎的版本。取值填写为：[4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg)[5.x](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,dt,hcs_oemout,srg)。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。
        :type engine_version: str
        :param storage_space: **参数解释**： 存储空间，单位：GB。 **约束限制**： 不涉及。 **取值范围**： 不同的实例规格支持不同的存储配置。 [- RocketMQ 5.x 单机存储取值范围：100-30000。](tag:dt) [- RocketMQ 5.x 集群存储取值范围：200-60000。](tag:dt) **默认取值**： 不涉及。
        :type storage_space: int
        :param vpc_id: **参数解释**： 虚拟私有云ID。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释**： 子网信息。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type subnet_id: str
        :param security_group_id: **参数解释**： 指定实例所属的安全组。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type security_group_id: str
        :param available_zones: **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或[3个及3个以上的可用区。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,cmcc)[2个可用区。](tag:fcs)在为节点指定可用区时，用逗号分隔开。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type available_zones: list[str]
        :param product_id: **参数解释**： RocketMQ实例规格。[x86环境后缀为.x86，arm环境为.arm。single表示单机，cluster表示集群。](tag:hcs,fcs,hcs_oemout)  **约束限制**： 不涉及。  **取值范围**： [当“type”为“single.basic”选择单机规格；当“type”为“cluster.basic”选择集群规格。](tag:dt) [- c6.2u8g.cluster.x86或c6.2u8g.cluster.arm：单个代理最大分区数50，单个代理最大消费组数100](tag:fcs) [- c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u16g.cluster.x86或c6.4u16g.cluster.arm：单个代理最大分区数100，单个代理最大消费组数200](tag:hcs,hcs_oemout) [- c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.8u32g.cluster.x86或c6.8u32g.cluster.arm：单个代理最大Topic数200，单个代理最大消费组数400](tag:hcs,fcs,hcs_oemout) [- c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.16u64g.cluster.x86或c6.16u64g.cluster.arm：单个代理最大Topic数300，单个代理最大消费组数600](tag:hcs,fcs,hcs_oemout) [- c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.32u128g.cluster.x86或c6.32u128g.cluster.arm：单个代理最大Topic数400，单个代理最大消费组数800](tag:hcs,fcs,hcs_oemout) [- rocketmq.b1.large.1：RocketMQ 5.x 基础版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.4：RocketMQ 5.x 基础版集群规格，实例TPS 2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.8：RocketMQ 5.x 基础版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.12：RocketMQ 5.x 基础版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.p1.large.1：RocketMQ 5.x 专业版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.8：RocketMQ 5.x 专业版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.12：RocketMQ 5.x 专业版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.20：RocketMQ 5.x 专业版集群规格，实例TPS 10000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.40：RocketMQ 5.x 专业版集群规格，实例TPS 20000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.100：RocketMQ 5.x 专业版集群规格，实例TPS 50000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.150：RocketMQ 5.x 专业版集群规格，实例TPS 75000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.200：RocketMQ 5.x 专业版集群规格，实例TPS 100000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.300：RocketMQ 5.x 专业版集群规格，实例TPS 150000](tag:hws,hws_eu,hws_hk,ctc,srg)  **默认取值**： 不涉及。
        :type product_id: str
        :param ssl_enable: **参数解释**： 是否打开SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：打开SSL加密访问。 - false：不打开SSL加密访问。 **默认取值**： false。
        :type ssl_enable: bool
        :param storage_spec_code: **参数解释**： 存储IO规格。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。
        :type storage_spec_code: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。若为企业项目账号，该参数必填。 **约束限制**： 不涉及。 **取值范围**：  不涉及。 **默认取值**： 不涉及。
        :type enterprise_project_id: str
        :param enable_acl: **参数解释**： 是否开启访问控制列表。 **约束限制**： 不涉及。 **取值范围**： - true：开启访问控制列表。 - false：不开启访问控制列表。 **默认取值**： false。
        :type enable_acl: bool
        :param ipv6_enable: **参数解释**： 是否支持IPv6。[华为云Stack不支持此参数。](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。
        :type ipv6_enable: bool
        :param proxy_enable: **参数解释**： 是否开启Proxy功能。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： 不涉及。
        :type proxy_enable: bool
        :param enable_publicip: **参数解释**： 是否开启公网访问功能。默认不开启公网。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。
        :type enable_publicip: bool
        :param disk_encrypted_enable: **参数解释**： 是否开启磁盘加密。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type disk_encrypted_enable: bool
        :param disk_encrypted_key: **参数解释**： 磁盘加密key，未开启磁盘加密时为空 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type disk_encrypted_key: str
        :param publicip_id: **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type publicip_id: str
        :param broker_num: **参数解释**： 代理个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type broker_num: int
        :param arch_type: **参数解释**： 架构类型。 **约束限制**： 不涉及。 **取值范围**： - X86：复杂指令集计算。 - ARM：精简指令集计算。 **默认取值**： 不涉及。
        :type arch_type: str
        :param tls_mode: **参数解释**： 实例使用的安全协议。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type tls_mode: str
        """
        
        

        self._name = None
        self._description = None
        self._engine = None
        self._engine_version = None
        self._storage_space = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._available_zones = None
        self._product_id = None
        self._ssl_enable = None
        self._storage_spec_code = None
        self._enterprise_project_id = None
        self._enable_acl = None
        self._ipv6_enable = None
        self._proxy_enable = None
        self._enable_publicip = None
        self._disk_encrypted_enable = None
        self._disk_encrypted_key = None
        self._publicip_id = None
        self._broker_num = None
        self._arch_type = None
        self._tls_mode = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.engine = engine
        self.engine_version = engine_version
        self.storage_space = storage_space
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.available_zones = available_zones
        self.product_id = product_id
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        self.storage_spec_code = storage_spec_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if proxy_enable is not None:
            self.proxy_enable = proxy_enable
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if disk_encrypted_enable is not None:
            self.disk_encrypted_enable = disk_encrypted_enable
        if disk_encrypted_key is not None:
            self.disk_encrypted_key = disk_encrypted_key
        if publicip_id is not None:
            self.publicip_id = publicip_id
        self.broker_num = broker_num
        if arch_type is not None:
            self.arch_type = arch_type
        if tls_mode is not None:
            self.tls_mode = tls_mode

    @property
    def name(self):
        r"""Gets the name of this CreatePostPaidInstanceReq.

        **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePostPaidInstanceReq.

        **参数解释**： 实例名称。 **约束限制**： 由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this CreatePostPaidInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreatePostPaidInstanceReq.

        **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs)  \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\"。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The description of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePostPaidInstanceReq.

        **参数解释**： 实例的描述信息。 **约束限制**： 长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs)  \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\\\\\或者\\\\\"。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param description: The description of this CreatePostPaidInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        r"""Gets the engine of this CreatePostPaidInstanceReq.

        **参数解释**： 消息引擎类型。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :return: The engine of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreatePostPaidInstanceReq.

        **参数解释**： 消息引擎类型。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :param engine: The engine of this CreatePostPaidInstanceReq.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CreatePostPaidInstanceReq.

        **参数解释**： 消息引擎的版本。取值填写为：[4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg)[5.x](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,dt,hcs_oemout,srg)。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :return: The engine_version of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CreatePostPaidInstanceReq.

        **参数解释**： 消息引擎的版本。取值填写为：[4.8.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg)[5.x](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,dt,hcs_oemout,srg)。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :param engine_version: The engine_version of this CreatePostPaidInstanceReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def storage_space(self):
        r"""Gets the storage_space of this CreatePostPaidInstanceReq.

        **参数解释**： 存储空间，单位：GB。 **约束限制**： 不涉及。 **取值范围**： 不同的实例规格支持不同的存储配置。 [- RocketMQ 5.x 单机存储取值范围：100-30000。](tag:dt) [- RocketMQ 5.x 集群存储取值范围：200-60000。](tag:dt) **默认取值**： 不涉及。

        :return: The storage_space of this CreatePostPaidInstanceReq.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        r"""Sets the storage_space of this CreatePostPaidInstanceReq.

        **参数解释**： 存储空间，单位：GB。 **约束限制**： 不涉及。 **取值范围**： 不同的实例规格支持不同的存储配置。 [- RocketMQ 5.x 单机存储取值范围：100-30000。](tag:dt) [- RocketMQ 5.x 集群存储取值范围：200-60000。](tag:dt) **默认取值**： 不涉及。

        :param storage_space: The storage_space of this CreatePostPaidInstanceReq.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreatePostPaidInstanceReq.

        **参数解释**： 虚拟私有云ID。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The vpc_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreatePostPaidInstanceReq.

        **参数解释**： 虚拟私有云ID。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询VPC列表”接口，从响应体中获取VPC ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param vpc_id: The vpc_id of this CreatePostPaidInstanceReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreatePostPaidInstanceReq.

        **参数解释**： 子网信息。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The subnet_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreatePostPaidInstanceReq.

        **参数解释**： 子网信息。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询子网列表”接口，从响应体中获取子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param subnet_id: The subnet_id of this CreatePostPaidInstanceReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreatePostPaidInstanceReq.

        **参数解释**： 指定实例所属的安全组。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_group_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreatePostPaidInstanceReq.

        **参数解释**： 指定实例所属的安全组。  获取方法如下：参考《虚拟私有云 API参考》，调用“查询安全组列表”接口，从响应体中获取安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param security_group_id: The security_group_id of this CreatePostPaidInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def available_zones(self):
        r"""Gets the available_zones of this CreatePostPaidInstanceReq.

        **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或[3个及3个以上的可用区。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,cmcc)[2个可用区。](tag:fcs)在为节点指定可用区时，用逗号分隔开。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The available_zones of this CreatePostPaidInstanceReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this CreatePostPaidInstanceReq.

        **参数解释**： 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。 该参数不能为空数组或者数组的值为空， 请注意查看该可用区是否有资源。  创建RocketMQ实例，支持节点部署在1个或[3个及3个以上的可用区。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,cmcc)[2个可用区。](tag:fcs)在为节点指定可用区时，用逗号分隔开。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param available_zones: The available_zones of this CreatePostPaidInstanceReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def product_id(self):
        r"""Gets the product_id of this CreatePostPaidInstanceReq.

        **参数解释**： RocketMQ实例规格。[x86环境后缀为.x86，arm环境为.arm。single表示单机，cluster表示集群。](tag:hcs,fcs,hcs_oemout)  **约束限制**： 不涉及。  **取值范围**： [当“type”为“single.basic”选择单机规格；当“type”为“cluster.basic”选择集群规格。](tag:dt) [- c6.2u8g.cluster.x86或c6.2u8g.cluster.arm：单个代理最大分区数50，单个代理最大消费组数100](tag:fcs) [- c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u16g.cluster.x86或c6.4u16g.cluster.arm：单个代理最大分区数100，单个代理最大消费组数200](tag:hcs,hcs_oemout) [- c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.8u32g.cluster.x86或c6.8u32g.cluster.arm：单个代理最大Topic数200，单个代理最大消费组数400](tag:hcs,fcs,hcs_oemout) [- c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.16u64g.cluster.x86或c6.16u64g.cluster.arm：单个代理最大Topic数300，单个代理最大消费组数600](tag:hcs,fcs,hcs_oemout) [- c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.32u128g.cluster.x86或c6.32u128g.cluster.arm：单个代理最大Topic数400，单个代理最大消费组数800](tag:hcs,fcs,hcs_oemout) [- rocketmq.b1.large.1：RocketMQ 5.x 基础版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.4：RocketMQ 5.x 基础版集群规格，实例TPS 2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.8：RocketMQ 5.x 基础版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.12：RocketMQ 5.x 基础版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.p1.large.1：RocketMQ 5.x 专业版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.8：RocketMQ 5.x 专业版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.12：RocketMQ 5.x 专业版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.20：RocketMQ 5.x 专业版集群规格，实例TPS 10000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.40：RocketMQ 5.x 专业版集群规格，实例TPS 20000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.100：RocketMQ 5.x 专业版集群规格，实例TPS 50000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.150：RocketMQ 5.x 专业版集群规格，实例TPS 75000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.200：RocketMQ 5.x 专业版集群规格，实例TPS 100000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.300：RocketMQ 5.x 专业版集群规格，实例TPS 150000](tag:hws,hws_eu,hws_hk,ctc,srg)  **默认取值**： 不涉及。

        :return: The product_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreatePostPaidInstanceReq.

        **参数解释**： RocketMQ实例规格。[x86环境后缀为.x86，arm环境为.arm。single表示单机，cluster表示集群。](tag:hcs,fcs,hcs_oemout)  **约束限制**： 不涉及。  **取值范围**： [当“type”为“single.basic”选择单机规格；当“type”为“cluster.basic”选择集群规格。](tag:dt) [- c6.2u8g.cluster.x86或c6.2u8g.cluster.arm：单个代理最大分区数50，单个代理最大消费组数100](tag:fcs) [- c6.4u8g.cluster.small：单个代理最大Topic数2000，单个代理最大消费组数2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u8g.cluster：单个代理最大Topic数4000，单个代理最大消费组数4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.4u16g.cluster.x86或c6.4u16g.cluster.arm：单个代理最大分区数100，单个代理最大消费组数200](tag:hcs,hcs_oemout) [- c6.8u16g.cluster：单个代理最大Topic数8000，单个代理最大消费组数8000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.8u32g.cluster.x86或c6.8u32g.cluster.arm：单个代理最大Topic数200，单个代理最大消费组数400](tag:hcs,fcs,hcs_oemout) [- c6.12u24g.cluster：单个代理最大Topic数12000，单个代理最大消费组数12000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.16u64g.cluster.x86或c6.16u64g.cluster.arm：单个代理最大Topic数300，单个代理最大消费组数600](tag:hcs,fcs,hcs_oemout) [- c6.16u32g.cluster：单个代理最大Topic数16000，单个代理最大消费组数16000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,cmcc,ax,srg) [- c6.32u128g.cluster.x86或c6.32u128g.cluster.arm：单个代理最大Topic数400，单个代理最大消费组数800](tag:hcs,fcs,hcs_oemout) [- rocketmq.b1.large.1：RocketMQ 5.x 基础版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.4：RocketMQ 5.x 基础版集群规格，实例TPS 2000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.8：RocketMQ 5.x 基础版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.b2.large.12：RocketMQ 5.x 基础版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,dt,srg) [- rocketmq.p1.large.1：RocketMQ 5.x 专业版单机规格，实例TPS 500](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.8：RocketMQ 5.x 专业版集群规格，实例TPS 4000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.12：RocketMQ 5.x 专业版集群规格，实例TPS 6000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.20：RocketMQ 5.x 专业版集群规格，实例TPS 10000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.40：RocketMQ 5.x 专业版集群规格，实例TPS 20000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.100：RocketMQ 5.x 专业版集群规格，实例TPS 50000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.150：RocketMQ 5.x 专业版集群规格，实例TPS 75000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.200：RocketMQ 5.x 专业版集群规格，实例TPS 100000](tag:hws,hws_eu,hws_hk,ctc,srg) [- rocketmq.p2.large.300：RocketMQ 5.x 专业版集群规格，实例TPS 150000](tag:hws,hws_eu,hws_hk,ctc,srg)  **默认取值**： 不涉及。

        :param product_id: The product_id of this CreatePostPaidInstanceReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否打开SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：打开SSL加密访问。 - false：不打开SSL加密访问。 **默认取值**： false。

        :return: The ssl_enable of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否打开SSL加密访问。 **约束限制**： 不涉及。 **取值范围**： - true：打开SSL加密访问。 - false：不打开SSL加密访问。 **默认取值**： false。

        :param ssl_enable: The ssl_enable of this CreatePostPaidInstanceReq.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this CreatePostPaidInstanceReq.

        **参数解释**： 存储IO规格。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。

        :return: The storage_spec_code of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this CreatePostPaidInstanceReq.

        **参数解释**： 存储IO规格。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。

        :param storage_spec_code: The storage_spec_code of this CreatePostPaidInstanceReq.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreatePostPaidInstanceReq.

        **参数解释**： 企业项目ID。若为企业项目账号，该参数必填。 **约束限制**： 不涉及。 **取值范围**：  不涉及。 **默认取值**： 不涉及。

        :return: The enterprise_project_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreatePostPaidInstanceReq.

        **参数解释**： 企业项目ID。若为企业项目账号，该参数必填。 **约束限制**： 不涉及。 **取值范围**：  不涉及。 **默认取值**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this CreatePostPaidInstanceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启访问控制列表。 **约束限制**： 不涉及。 **取值范围**： - true：开启访问控制列表。 - false：不开启访问控制列表。 **默认取值**： false。

        :return: The enable_acl of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启访问控制列表。 **约束限制**： 不涉及。 **取值范围**： - true：开启访问控制列表。 - false：不开启访问控制列表。 **默认取值**： false。

        :param enable_acl: The enable_acl of this CreatePostPaidInstanceReq.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否支持IPv6。[华为云Stack不支持此参数。](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。

        :return: The ipv6_enable of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否支持IPv6。[华为云Stack不支持此参数。](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。

        :param ipv6_enable: The ipv6_enable of this CreatePostPaidInstanceReq.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def proxy_enable(self):
        r"""Gets the proxy_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启Proxy功能。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： 不涉及。

        :return: The proxy_enable of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._proxy_enable

    @proxy_enable.setter
    def proxy_enable(self, proxy_enable):
        r"""Sets the proxy_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启Proxy功能。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： 不涉及。

        :param proxy_enable: The proxy_enable of this CreatePostPaidInstanceReq.
        :type proxy_enable: bool
        """
        self._proxy_enable = proxy_enable

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启公网访问功能。默认不开启公网。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。

        :return: The enable_publicip of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启公网访问功能。默认不开启公网。 **约束限制**： 不涉及。 **取值范围**： - true：支持 - false：不支持 **默认取值**： false。

        :param enable_publicip: The enable_publicip of this CreatePostPaidInstanceReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def disk_encrypted_enable(self):
        r"""Gets the disk_encrypted_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启磁盘加密。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The disk_encrypted_enable of this CreatePostPaidInstanceReq.
        :rtype: bool
        """
        return self._disk_encrypted_enable

    @disk_encrypted_enable.setter
    def disk_encrypted_enable(self, disk_encrypted_enable):
        r"""Sets the disk_encrypted_enable of this CreatePostPaidInstanceReq.

        **参数解释**： 是否开启磁盘加密。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param disk_encrypted_enable: The disk_encrypted_enable of this CreatePostPaidInstanceReq.
        :type disk_encrypted_enable: bool
        """
        self._disk_encrypted_enable = disk_encrypted_enable

    @property
    def disk_encrypted_key(self):
        r"""Gets the disk_encrypted_key of this CreatePostPaidInstanceReq.

        **参数解释**： 磁盘加密key，未开启磁盘加密时为空 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The disk_encrypted_key of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._disk_encrypted_key

    @disk_encrypted_key.setter
    def disk_encrypted_key(self, disk_encrypted_key):
        r"""Sets the disk_encrypted_key of this CreatePostPaidInstanceReq.

        **参数解释**： 磁盘加密key，未开启磁盘加密时为空 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param disk_encrypted_key: The disk_encrypted_key of this CreatePostPaidInstanceReq.
        :type disk_encrypted_key: str
        """
        self._disk_encrypted_key = disk_encrypted_key

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this CreatePostPaidInstanceReq.

        **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The publicip_id of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this CreatePostPaidInstanceReq.

        **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param publicip_id: The publicip_id of this CreatePostPaidInstanceReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def broker_num(self):
        r"""Gets the broker_num of this CreatePostPaidInstanceReq.

        **参数解释**： 代理个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The broker_num of this CreatePostPaidInstanceReq.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this CreatePostPaidInstanceReq.

        **参数解释**： 代理个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param broker_num: The broker_num of this CreatePostPaidInstanceReq.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def arch_type(self):
        r"""Gets the arch_type of this CreatePostPaidInstanceReq.

        **参数解释**： 架构类型。 **约束限制**： 不涉及。 **取值范围**： - X86：复杂指令集计算。 - ARM：精简指令集计算。 **默认取值**： 不涉及。

        :return: The arch_type of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this CreatePostPaidInstanceReq.

        **参数解释**： 架构类型。 **约束限制**： 不涉及。 **取值范围**： - X86：复杂指令集计算。 - ARM：精简指令集计算。 **默认取值**： 不涉及。

        :param arch_type: The arch_type of this CreatePostPaidInstanceReq.
        :type arch_type: str
        """
        self._arch_type = arch_type

    @property
    def tls_mode(self):
        r"""Gets the tls_mode of this CreatePostPaidInstanceReq.

        **参数解释**： 实例使用的安全协议。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The tls_mode of this CreatePostPaidInstanceReq.
        :rtype: str
        """
        return self._tls_mode

    @tls_mode.setter
    def tls_mode(self, tls_mode):
        r"""Sets the tls_mode of this CreatePostPaidInstanceReq.

        **参数解释**： 实例使用的安全协议。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param tls_mode: The tls_mode of this CreatePostPaidInstanceReq.
        :type tls_mode: str
        """
        self._tls_mode = tls_mode

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
        if not isinstance(other, CreatePostPaidInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
