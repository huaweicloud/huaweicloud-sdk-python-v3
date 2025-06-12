# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceByEngineReq:

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
        'broker_num': 'int',
        'storage_space': 'int',
        'access_user': 'str',
        'password': 'str',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'available_zones': 'list[str]',
        'product_id': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'enable_publicip': 'bool',
        'tenant_ips': 'list[str]',
        'publicip_id': 'str',
        'ssl_enable': 'bool',
        'kafka_security_protocol': 'str',
        'sasl_enabled_mechanisms': 'list[str]',
        'port_protocol': 'PortProtocol',
        'retention_policy': 'str',
        'ipv6_enable': 'bool',
        'disk_encrypted_enable': 'bool',
        'disk_encrypted_key': 'str',
        'connector_enable': 'bool',
        'enable_auto_topic': 'bool',
        'storage_spec_code': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[TagEntity]',
        'arch_type': 'str',
        'vpc_client_plain': 'bool',
        'bss_param': 'BssParam'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'broker_num': 'broker_num',
        'storage_space': 'storage_space',
        'access_user': 'access_user',
        'password': 'password',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'available_zones': 'available_zones',
        'product_id': 'product_id',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'enable_publicip': 'enable_publicip',
        'tenant_ips': 'tenant_ips',
        'publicip_id': 'publicip_id',
        'ssl_enable': 'ssl_enable',
        'kafka_security_protocol': 'kafka_security_protocol',
        'sasl_enabled_mechanisms': 'sasl_enabled_mechanisms',
        'port_protocol': 'port_protocol',
        'retention_policy': 'retention_policy',
        'ipv6_enable': 'ipv6_enable',
        'disk_encrypted_enable': 'disk_encrypted_enable',
        'disk_encrypted_key': 'disk_encrypted_key',
        'connector_enable': 'connector_enable',
        'enable_auto_topic': 'enable_auto_topic',
        'storage_spec_code': 'storage_spec_code',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'arch_type': 'arch_type',
        'vpc_client_plain': 'vpc_client_plain',
        'bss_param': 'bss_param'
    }

    def __init__(self, name=None, description=None, engine=None, engine_version=None, broker_num=None, storage_space=None, access_user=None, password=None, vpc_id=None, security_group_id=None, subnet_id=None, available_zones=None, product_id=None, maintain_begin=None, maintain_end=None, enable_publicip=None, tenant_ips=None, publicip_id=None, ssl_enable=None, kafka_security_protocol=None, sasl_enabled_mechanisms=None, port_protocol=None, retention_policy=None, ipv6_enable=None, disk_encrypted_enable=None, disk_encrypted_key=None, connector_enable=None, enable_auto_topic=None, storage_spec_code=None, enterprise_project_id=None, tags=None, arch_type=None, vpc_client_plain=None, bss_param=None):
        r"""CreateInstanceByEngineReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。
        :type name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\&quot;&gt;\&quot;与\&quot;&lt;\&quot;，字符串首字符不能为\&quot;&#x3D;\&quot;,\&quot;+\&quot;,\&quot;-\&quot;,\&quot;@\&quot;的全角和半角字符。](tag:hcs,fcs)  &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。
        :type description: str
        :param engine: 消息引擎。取值填写为：kafka。
        :type engine: str
        :param engine_version: 消息引擎的版本。取值填写为：   [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc)   [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc)   - 2.7   [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu)
        :type engine_version: str
        :param broker_num: 代理个数。
        :type broker_num: int
        :param storage_space: 消息存储空间，单位GB。   [- Kafka实例规格为c6.2u4g.cluster时，存储空间取值范围300GB ~ 300000GB。   - Kafka实例规格为c6.4u8g.cluster时，存储空间取值范围300GB ~ 600000GB。   - Kafka实例规格为c6.8u16g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.12u24g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.16u32g.cluster时，存储空间取值范围300GB ~ 1500000GB。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)      [- Kafka实例规格为kafka.2u8g.cluster时，存储空间取值范围300GB~300000GB。](tag:fcs)   [- Kafka实例规格为kafka.4u16g.cluster时，存储空间取值范围300GB~600000GB。   - Kafka实例规格为kafka.8u32g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.16u64g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.32u128g.cluster时，存储空间取值范围300GB~1500000GB。](tag:hcs,fcs)
        :type storage_space: int
        :param access_user: 当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。
        :type access_user: str
        :param password: 当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|[{}]:&#39;\&quot;,&lt;.&gt;/?）和空格，并且不能以-开头
        :type password: str
        :param vpc_id: 虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。
        :type vpc_id: str
        :param security_group_id: 指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。
        :type security_group_id: str
        :param subnet_id: 子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。
        :type subnet_id: str
        :param available_zones: 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。  创建Kafka实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。
        :type available_zones: list[str]
        :param product_id: 产品ID。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。
        :type product_id: str
        :param maintain_begin: 维护时间窗开始时间，格式为HH:mm。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，格式为HH:mm。
        :type maintain_end: str
        :param enable_publicip: 是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启
        :type enable_publicip: bool
        :param tenant_ips: 创建实例时可以手动指定实例节点的内网IP地址，仅支持指定IPv4地址。  指定内网IP地址数量必须小于等于创建的节点数量。  如果指定的内网IP地址数量小于创建的节点数量时，系统会自动为剩余的节点随机分配内网IP地址。
        :type tenant_ips: list[str]
        :param publicip_id: 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。
        :type publicip_id: str
        :param ssl_enable: 是否开启SASL加密访问。  [实例创建后将不支持动态开启和关闭。](tag:ocb,hws_ocb,hcs)  - true：开启SASL加密访问。 - false：关闭SASL加密访问。
        :type ssl_enable: bool
        :param kafka_security_protocol: 开启SASL后使用的安全协议。 - SASL_SSL: 使用SSL证书加密传输，支持账号密码认证，安全性更高。 - SASL_PLAINTEXT: 通过明文传输，支持账号密码认证，性能更好。  若该字段值为空，默认开启SASL_SSL认证机制。实例创建后，此参数不支持动态修改。 若创建实例时，使用了port_protocol参数，则Kafka的内网访问安全协议以及公网访问安全协议会使用port_protocol中的值，则此参数无效。
        :type kafka_security_protocol: str
        :param sasl_enabled_mechanisms: 开启SASL后使用的认证机制，如果开启了SASL认证功能（即ssl_enable&#x3D;true），该字段为必选。  若该字段值为空，默认开启PLAIN认证机制。  选择其一进行SASL认证即可，支持同时开启两种认证机制。 取值如下： - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。
        :type sasl_enabled_mechanisms: list[str]
        :param port_protocol: 
        :type port_protocol: :class:`huaweicloudsdkkafka.v2.PortProtocol`
        :param retention_policy: 磁盘的容量到达容量阈值后，对于消息的处理策略。  取值如下： - produce_reject：表示拒绝消息写入。 - time_base：表示自动删除最老消息。
        :type retention_policy: str
        :param ipv6_enable: 是否开启ipv6。仅在虚拟私有云支持ipv6时生效。
        :type ipv6_enable: bool
        :param disk_encrypted_enable: 是否开启磁盘加密。
        :type disk_encrypted_enable: bool
        :param disk_encrypted_key: 磁盘加密key，未开启磁盘加密时为空
        :type disk_encrypted_key: str
        :param connector_enable: 是否开启消息转储功能。  默认不开启消息转储。
        :type connector_enable: bool
        :param enable_auto_topic: 是否打开kafka自动创建Topic功能。 - true：开启 - false：关闭  当您选择开启，表示生产或消费一个未创建的Topic时，会自动创建一个包含3个分区和3个副本的Topic。  默认是false关闭。
        :type enable_auto_topic: bool
        :param storage_spec_code: 存储IO规格。  取值范围：   - dms.physical.storage.high.v2：使用高IO的磁盘类型。   - dms.physical.storage.ultra.v2：使用超高IO的磁盘类型。  [如何选择磁盘类型请参考《云硬盘 [产品介绍](tag:hws,hws_hk,hws_eu,cmcc)[用户指南](tag:dt,g42,hk_g42,ctc,tm,hk_tm,sbc,ocb,hws_ocb)》的“磁盘类型及性能介绍”。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)
        :type storage_spec_code: str
        :param enterprise_project_id: 企业项目ID。若为企业项目账号，该参数必填。
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        :param arch_type: CPU架构。当前只支持X86架构[以及arm架构](tag:hcs,fcs,ctc)。  取值范围：   - X86   [- arm](tag:hcs,fcs,ctc)
        :type arch_type: str
        :param vpc_client_plain: VPC内网明文访问。
        :type vpc_client_plain: bool
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkkafka.v2.BssParam`
        """
        
        

        self._name = None
        self._description = None
        self._engine = None
        self._engine_version = None
        self._broker_num = None
        self._storage_space = None
        self._access_user = None
        self._password = None
        self._vpc_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._available_zones = None
        self._product_id = None
        self._maintain_begin = None
        self._maintain_end = None
        self._enable_publicip = None
        self._tenant_ips = None
        self._publicip_id = None
        self._ssl_enable = None
        self._kafka_security_protocol = None
        self._sasl_enabled_mechanisms = None
        self._port_protocol = None
        self._retention_policy = None
        self._ipv6_enable = None
        self._disk_encrypted_enable = None
        self._disk_encrypted_key = None
        self._connector_enable = None
        self._enable_auto_topic = None
        self._storage_spec_code = None
        self._enterprise_project_id = None
        self._tags = None
        self._arch_type = None
        self._vpc_client_plain = None
        self._bss_param = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.engine = engine
        self.engine_version = engine_version
        self.broker_num = broker_num
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
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if tenant_ips is not None:
            self.tenant_ips = tenant_ips
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if kafka_security_protocol is not None:
            self.kafka_security_protocol = kafka_security_protocol
        if sasl_enabled_mechanisms is not None:
            self.sasl_enabled_mechanisms = sasl_enabled_mechanisms
        if port_protocol is not None:
            self.port_protocol = port_protocol
        if retention_policy is not None:
            self.retention_policy = retention_policy
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if disk_encrypted_enable is not None:
            self.disk_encrypted_enable = disk_encrypted_enable
        if disk_encrypted_key is not None:
            self.disk_encrypted_key = disk_encrypted_key
        if connector_enable is not None:
            self.connector_enable = connector_enable
        if enable_auto_topic is not None:
            self.enable_auto_topic = enable_auto_topic
        self.storage_spec_code = storage_spec_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if arch_type is not None:
            self.arch_type = arch_type
        if vpc_client_plain is not None:
            self.vpc_client_plain = vpc_client_plain
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceByEngineReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :return: The name of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceByEngineReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :param name: The name of this CreateInstanceByEngineReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateInstanceByEngineReq.

        实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs,fcs)  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :return: The description of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstanceByEngineReq.

        实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs,fcs)  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :param description: The description of this CreateInstanceByEngineReq.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        r"""Gets the engine of this CreateInstanceByEngineReq.

        消息引擎。取值填写为：kafka。

        :return: The engine of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateInstanceByEngineReq.

        消息引擎。取值填写为：kafka。

        :param engine: The engine of this CreateInstanceByEngineReq.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CreateInstanceByEngineReq.

        消息引擎的版本。取值填写为：   [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc)   [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc)   - 2.7   [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu)

        :return: The engine_version of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CreateInstanceByEngineReq.

        消息引擎的版本。取值填写为：   [- 1.1.0](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt,sbc,cmcc)   [- 2.3.0](tag:g42,tm,hk_g42,ctc,hk_tm,dt,sbc,cmcc)   - 2.7   [- 3.x](tag:hws,hws_hk,dt,sbc,hcs,fcs,ctc,tm,hk_tm,hws_eu)

        :param engine_version: The engine_version of this CreateInstanceByEngineReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def broker_num(self):
        r"""Gets the broker_num of this CreateInstanceByEngineReq.

        代理个数。

        :return: The broker_num of this CreateInstanceByEngineReq.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this CreateInstanceByEngineReq.

        代理个数。

        :param broker_num: The broker_num of this CreateInstanceByEngineReq.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def storage_space(self):
        r"""Gets the storage_space of this CreateInstanceByEngineReq.

        消息存储空间，单位GB。   [- Kafka实例规格为c6.2u4g.cluster时，存储空间取值范围300GB ~ 300000GB。   - Kafka实例规格为c6.4u8g.cluster时，存储空间取值范围300GB ~ 600000GB。   - Kafka实例规格为c6.8u16g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.12u24g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.16u32g.cluster时，存储空间取值范围300GB ~ 1500000GB。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)      [- Kafka实例规格为kafka.2u8g.cluster时，存储空间取值范围300GB~300000GB。](tag:fcs)   [- Kafka实例规格为kafka.4u16g.cluster时，存储空间取值范围300GB~600000GB。   - Kafka实例规格为kafka.8u32g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.16u64g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.32u128g.cluster时，存储空间取值范围300GB~1500000GB。](tag:hcs,fcs)

        :return: The storage_space of this CreateInstanceByEngineReq.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        r"""Sets the storage_space of this CreateInstanceByEngineReq.

        消息存储空间，单位GB。   [- Kafka实例规格为c6.2u4g.cluster时，存储空间取值范围300GB ~ 300000GB。   - Kafka实例规格为c6.4u8g.cluster时，存储空间取值范围300GB ~ 600000GB。   - Kafka实例规格为c6.8u16g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.12u24g.cluster时，存储空间取值范围300GB ~ 1500000GB。   - Kafka实例规格为c6.16u32g.cluster时，存储空间取值范围300GB ~ 1500000GB。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)      [- Kafka实例规格为kafka.2u8g.cluster时，存储空间取值范围300GB~300000GB。](tag:fcs)   [- Kafka实例规格为kafka.4u16g.cluster时，存储空间取值范围300GB~600000GB。   - Kafka实例规格为kafka.8u32g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.16u64g.cluster时，存储空间取值范围300GB~1500000GB。   - Kafka实例规格为kafka.32u128g.cluster时，存储空间取值范围300GB~1500000GB。](tag:hcs,fcs)

        :param storage_space: The storage_space of this CreateInstanceByEngineReq.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def access_user(self):
        r"""Gets the access_user of this CreateInstanceByEngineReq.

        当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :return: The access_user of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        r"""Sets the access_user of this CreateInstanceByEngineReq.

        当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :param access_user: The access_user of this CreateInstanceByEngineReq.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def password(self):
        r"""Gets the password of this CreateInstanceByEngineReq.

        当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）和空格，并且不能以-开头

        :return: The password of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateInstanceByEngineReq.

        当ssl_enable为true时，该参数必选，ssl_enable为false时，该参数无效。  实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）和空格，并且不能以-开头

        :param password: The password of this CreateInstanceByEngineReq.
        :type password: str
        """
        self._password = password

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceByEngineReq.

        虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :return: The vpc_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceByEngineReq.

        虚拟私有云ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :param vpc_id: The vpc_id of this CreateInstanceByEngineReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateInstanceByEngineReq.

        指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :return: The security_group_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateInstanceByEngineReq.

        指定实例所属的安全组。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :param security_group_id: The security_group_id of this CreateInstanceByEngineReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceByEngineReq.

        子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :return: The subnet_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceByEngineReq.

        子网信息。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :param subnet_id: The subnet_id of this CreateInstanceByEngineReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def available_zones(self):
        r"""Gets the available_zones of this CreateInstanceByEngineReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。  创建Kafka实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。

        :return: The available_zones of this CreateInstanceByEngineReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this CreateInstanceByEngineReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。  创建Kafka实例，支持节点部署在1个或3个及3个以上的可用区。在为节点指定可用区时，用逗号分隔开。

        :param available_zones: The available_zones of this CreateInstanceByEngineReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateInstanceByEngineReq.

        产品ID。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。

        :return: The product_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateInstanceByEngineReq.

        产品ID。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。

        :param product_id: The product_id of this CreateInstanceByEngineReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def maintain_begin(self):
        r"""Gets the maintain_begin of this CreateInstanceByEngineReq.

        维护时间窗开始时间，格式为HH:mm。

        :return: The maintain_begin of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        r"""Sets the maintain_begin of this CreateInstanceByEngineReq.

        维护时间窗开始时间，格式为HH:mm。

        :param maintain_begin: The maintain_begin of this CreateInstanceByEngineReq.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        r"""Gets the maintain_end of this CreateInstanceByEngineReq.

        维护时间窗结束时间，格式为HH:mm。

        :return: The maintain_end of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        r"""Sets the maintain_end of this CreateInstanceByEngineReq.

        维护时间窗结束时间，格式为HH:mm。

        :param maintain_end: The maintain_end of this CreateInstanceByEngineReq.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this CreateInstanceByEngineReq.

        是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启

        :return: The enable_publicip of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this CreateInstanceByEngineReq.

        是否开启公网访问功能。默认不开启公网。 - true：开启 - false：不开启

        :param enable_publicip: The enable_publicip of this CreateInstanceByEngineReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def tenant_ips(self):
        r"""Gets the tenant_ips of this CreateInstanceByEngineReq.

        创建实例时可以手动指定实例节点的内网IP地址，仅支持指定IPv4地址。  指定内网IP地址数量必须小于等于创建的节点数量。  如果指定的内网IP地址数量小于创建的节点数量时，系统会自动为剩余的节点随机分配内网IP地址。

        :return: The tenant_ips of this CreateInstanceByEngineReq.
        :rtype: list[str]
        """
        return self._tenant_ips

    @tenant_ips.setter
    def tenant_ips(self, tenant_ips):
        r"""Sets the tenant_ips of this CreateInstanceByEngineReq.

        创建实例时可以手动指定实例节点的内网IP地址，仅支持指定IPv4地址。  指定内网IP地址数量必须小于等于创建的节点数量。  如果指定的内网IP地址数量小于创建的节点数量时，系统会自动为剩余的节点随机分配内网IP地址。

        :param tenant_ips: The tenant_ips of this CreateInstanceByEngineReq.
        :type tenant_ips: list[str]
        """
        self._tenant_ips = tenant_ips

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this CreateInstanceByEngineReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :return: The publicip_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this CreateInstanceByEngineReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :param publicip_id: The publicip_id of this CreateInstanceByEngineReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this CreateInstanceByEngineReq.

        是否开启SASL加密访问。  [实例创建后将不支持动态开启和关闭。](tag:ocb,hws_ocb,hcs)  - true：开启SASL加密访问。 - false：关闭SASL加密访问。

        :return: The ssl_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this CreateInstanceByEngineReq.

        是否开启SASL加密访问。  [实例创建后将不支持动态开启和关闭。](tag:ocb,hws_ocb,hcs)  - true：开启SASL加密访问。 - false：关闭SASL加密访问。

        :param ssl_enable: The ssl_enable of this CreateInstanceByEngineReq.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def kafka_security_protocol(self):
        r"""Gets the kafka_security_protocol of this CreateInstanceByEngineReq.

        开启SASL后使用的安全协议。 - SASL_SSL: 使用SSL证书加密传输，支持账号密码认证，安全性更高。 - SASL_PLAINTEXT: 通过明文传输，支持账号密码认证，性能更好。  若该字段值为空，默认开启SASL_SSL认证机制。实例创建后，此参数不支持动态修改。 若创建实例时，使用了port_protocol参数，则Kafka的内网访问安全协议以及公网访问安全协议会使用port_protocol中的值，则此参数无效。

        :return: The kafka_security_protocol of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._kafka_security_protocol

    @kafka_security_protocol.setter
    def kafka_security_protocol(self, kafka_security_protocol):
        r"""Sets the kafka_security_protocol of this CreateInstanceByEngineReq.

        开启SASL后使用的安全协议。 - SASL_SSL: 使用SSL证书加密传输，支持账号密码认证，安全性更高。 - SASL_PLAINTEXT: 通过明文传输，支持账号密码认证，性能更好。  若该字段值为空，默认开启SASL_SSL认证机制。实例创建后，此参数不支持动态修改。 若创建实例时，使用了port_protocol参数，则Kafka的内网访问安全协议以及公网访问安全协议会使用port_protocol中的值，则此参数无效。

        :param kafka_security_protocol: The kafka_security_protocol of this CreateInstanceByEngineReq.
        :type kafka_security_protocol: str
        """
        self._kafka_security_protocol = kafka_security_protocol

    @property
    def sasl_enabled_mechanisms(self):
        r"""Gets the sasl_enabled_mechanisms of this CreateInstanceByEngineReq.

        开启SASL后使用的认证机制，如果开启了SASL认证功能（即ssl_enable=true），该字段为必选。  若该字段值为空，默认开启PLAIN认证机制。  选择其一进行SASL认证即可，支持同时开启两种认证机制。 取值如下： - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。

        :return: The sasl_enabled_mechanisms of this CreateInstanceByEngineReq.
        :rtype: list[str]
        """
        return self._sasl_enabled_mechanisms

    @sasl_enabled_mechanisms.setter
    def sasl_enabled_mechanisms(self, sasl_enabled_mechanisms):
        r"""Sets the sasl_enabled_mechanisms of this CreateInstanceByEngineReq.

        开启SASL后使用的认证机制，如果开启了SASL认证功能（即ssl_enable=true），该字段为必选。  若该字段值为空，默认开启PLAIN认证机制。  选择其一进行SASL认证即可，支持同时开启两种认证机制。 取值如下： - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。

        :param sasl_enabled_mechanisms: The sasl_enabled_mechanisms of this CreateInstanceByEngineReq.
        :type sasl_enabled_mechanisms: list[str]
        """
        self._sasl_enabled_mechanisms = sasl_enabled_mechanisms

    @property
    def port_protocol(self):
        r"""Gets the port_protocol of this CreateInstanceByEngineReq.

        :return: The port_protocol of this CreateInstanceByEngineReq.
        :rtype: :class:`huaweicloudsdkkafka.v2.PortProtocol`
        """
        return self._port_protocol

    @port_protocol.setter
    def port_protocol(self, port_protocol):
        r"""Sets the port_protocol of this CreateInstanceByEngineReq.

        :param port_protocol: The port_protocol of this CreateInstanceByEngineReq.
        :type port_protocol: :class:`huaweicloudsdkkafka.v2.PortProtocol`
        """
        self._port_protocol = port_protocol

    @property
    def retention_policy(self):
        r"""Gets the retention_policy of this CreateInstanceByEngineReq.

        磁盘的容量到达容量阈值后，对于消息的处理策略。  取值如下： - produce_reject：表示拒绝消息写入。 - time_base：表示自动删除最老消息。

        :return: The retention_policy of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        r"""Sets the retention_policy of this CreateInstanceByEngineReq.

        磁盘的容量到达容量阈值后，对于消息的处理策略。  取值如下： - produce_reject：表示拒绝消息写入。 - time_base：表示自动删除最老消息。

        :param retention_policy: The retention_policy of this CreateInstanceByEngineReq.
        :type retention_policy: str
        """
        self._retention_policy = retention_policy

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this CreateInstanceByEngineReq.

        是否开启ipv6。仅在虚拟私有云支持ipv6时生效。

        :return: The ipv6_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this CreateInstanceByEngineReq.

        是否开启ipv6。仅在虚拟私有云支持ipv6时生效。

        :param ipv6_enable: The ipv6_enable of this CreateInstanceByEngineReq.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def disk_encrypted_enable(self):
        r"""Gets the disk_encrypted_enable of this CreateInstanceByEngineReq.

        是否开启磁盘加密。

        :return: The disk_encrypted_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._disk_encrypted_enable

    @disk_encrypted_enable.setter
    def disk_encrypted_enable(self, disk_encrypted_enable):
        r"""Sets the disk_encrypted_enable of this CreateInstanceByEngineReq.

        是否开启磁盘加密。

        :param disk_encrypted_enable: The disk_encrypted_enable of this CreateInstanceByEngineReq.
        :type disk_encrypted_enable: bool
        """
        self._disk_encrypted_enable = disk_encrypted_enable

    @property
    def disk_encrypted_key(self):
        r"""Gets the disk_encrypted_key of this CreateInstanceByEngineReq.

        磁盘加密key，未开启磁盘加密时为空

        :return: The disk_encrypted_key of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._disk_encrypted_key

    @disk_encrypted_key.setter
    def disk_encrypted_key(self, disk_encrypted_key):
        r"""Sets the disk_encrypted_key of this CreateInstanceByEngineReq.

        磁盘加密key，未开启磁盘加密时为空

        :param disk_encrypted_key: The disk_encrypted_key of this CreateInstanceByEngineReq.
        :type disk_encrypted_key: str
        """
        self._disk_encrypted_key = disk_encrypted_key

    @property
    def connector_enable(self):
        r"""Gets the connector_enable of this CreateInstanceByEngineReq.

        是否开启消息转储功能。  默认不开启消息转储。

        :return: The connector_enable of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._connector_enable

    @connector_enable.setter
    def connector_enable(self, connector_enable):
        r"""Sets the connector_enable of this CreateInstanceByEngineReq.

        是否开启消息转储功能。  默认不开启消息转储。

        :param connector_enable: The connector_enable of this CreateInstanceByEngineReq.
        :type connector_enable: bool
        """
        self._connector_enable = connector_enable

    @property
    def enable_auto_topic(self):
        r"""Gets the enable_auto_topic of this CreateInstanceByEngineReq.

        是否打开kafka自动创建Topic功能。 - true：开启 - false：关闭  当您选择开启，表示生产或消费一个未创建的Topic时，会自动创建一个包含3个分区和3个副本的Topic。  默认是false关闭。

        :return: The enable_auto_topic of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._enable_auto_topic

    @enable_auto_topic.setter
    def enable_auto_topic(self, enable_auto_topic):
        r"""Sets the enable_auto_topic of this CreateInstanceByEngineReq.

        是否打开kafka自动创建Topic功能。 - true：开启 - false：关闭  当您选择开启，表示生产或消费一个未创建的Topic时，会自动创建一个包含3个分区和3个副本的Topic。  默认是false关闭。

        :param enable_auto_topic: The enable_auto_topic of this CreateInstanceByEngineReq.
        :type enable_auto_topic: bool
        """
        self._enable_auto_topic = enable_auto_topic

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this CreateInstanceByEngineReq.

        存储IO规格。  取值范围：   - dms.physical.storage.high.v2：使用高IO的磁盘类型。   - dms.physical.storage.ultra.v2：使用超高IO的磁盘类型。  [如何选择磁盘类型请参考《云硬盘 [产品介绍](tag:hws,hws_hk,hws_eu,cmcc)[用户指南](tag:dt,g42,hk_g42,ctc,tm,hk_tm,sbc,ocb,hws_ocb)》的“磁盘类型及性能介绍”。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)

        :return: The storage_spec_code of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this CreateInstanceByEngineReq.

        存储IO规格。  取值范围：   - dms.physical.storage.high.v2：使用高IO的磁盘类型。   - dms.physical.storage.ultra.v2：使用超高IO的磁盘类型。  [如何选择磁盘类型请参考《云硬盘 [产品介绍](tag:hws,hws_hk,hws_eu,cmcc)[用户指南](tag:dt,g42,hk_g42,ctc,tm,hk_tm,sbc,ocb,hws_ocb)》的“磁盘类型及性能介绍”。](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,dt)

        :param storage_spec_code: The storage_spec_code of this CreateInstanceByEngineReq.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceByEngineReq.

        企业项目ID。若为企业项目账号，该参数必填。

        :return: The enterprise_project_id of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceByEngineReq.

        企业项目ID。若为企业项目账号，该参数必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceByEngineReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateInstanceByEngineReq.

        标签列表。

        :return: The tags of this CreateInstanceByEngineReq.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateInstanceByEngineReq.

        标签列表。

        :param tags: The tags of this CreateInstanceByEngineReq.
        :type tags: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def arch_type(self):
        r"""Gets the arch_type of this CreateInstanceByEngineReq.

        CPU架构。当前只支持X86架构[以及arm架构](tag:hcs,fcs,ctc)。  取值范围：   - X86   [- arm](tag:hcs,fcs,ctc)

        :return: The arch_type of this CreateInstanceByEngineReq.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this CreateInstanceByEngineReq.

        CPU架构。当前只支持X86架构[以及arm架构](tag:hcs,fcs,ctc)。  取值范围：   - X86   [- arm](tag:hcs,fcs,ctc)

        :param arch_type: The arch_type of this CreateInstanceByEngineReq.
        :type arch_type: str
        """
        self._arch_type = arch_type

    @property
    def vpc_client_plain(self):
        r"""Gets the vpc_client_plain of this CreateInstanceByEngineReq.

        VPC内网明文访问。

        :return: The vpc_client_plain of this CreateInstanceByEngineReq.
        :rtype: bool
        """
        return self._vpc_client_plain

    @vpc_client_plain.setter
    def vpc_client_plain(self, vpc_client_plain):
        r"""Sets the vpc_client_plain of this CreateInstanceByEngineReq.

        VPC内网明文访问。

        :param vpc_client_plain: The vpc_client_plain of this CreateInstanceByEngineReq.
        :type vpc_client_plain: bool
        """
        self._vpc_client_plain = vpc_client_plain

    @property
    def bss_param(self):
        r"""Gets the bss_param of this CreateInstanceByEngineReq.

        :return: The bss_param of this CreateInstanceByEngineReq.
        :rtype: :class:`huaweicloudsdkkafka.v2.BssParam`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        r"""Sets the bss_param of this CreateInstanceByEngineReq.

        :param bss_param: The bss_param of this CreateInstanceByEngineReq.
        :type bss_param: :class:`huaweicloudsdkkafka.v2.BssParam`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, CreateInstanceByEngineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
