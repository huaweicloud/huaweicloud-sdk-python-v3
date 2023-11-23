# coding: utf-8

import six

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

    def __init__(self, name=None, description=None, engine=None, engine_version=None, storage_space=None, access_user=None, password=None, vpc_id=None, security_group_id=None, subnet_id=None, available_zones=None, product_id=None, broker_num=None, maintain_begin=None, maintain_end=None, enable_publicip=None, publicip_id=None, ssl_enable=None, storage_spec_code=None, enterprise_project_id=None, tags=None, bss_param=None):
        """CreateInstanceReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。
        :type name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。  &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。
        :type description: str
        :param engine: 消息引擎：rabbitmq。
        :type engine: str
        :param engine_version: 消息引擎的版本。   - RabbitMQ版本有：3.8.35[和3.7.17](tag:g42,hk_g42,tm,hk_tm)。 
        :type engine_version: str
        :param storage_space: 消息存储空间，单位GB。   - 单机RabbitMQ实例的存储空间的取值范围100GB~90000GB。   - 集群RabbitMQ实例的存储空间的取值范围为100GB*节点数~90000GB、200GB*节点数~90000GB、300GB*节点数~90000GB。 
        :type storage_space: int
        :param access_user: 认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。
        :type access_user: str
        :param password: 实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|[{}]:&#39;\&quot;,&lt;.&gt;/?）
        :type password: str
        :param vpc_id: 租户VPC ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。
        :type vpc_id: str
        :param security_group_id: 租户安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。
        :type security_group_id: str
        :param subnet_id: 子网ID。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。
        :type subnet_id: str
        :param available_zones: 创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。
        :type available_zones: list[str]
        :param product_id: 产品标识。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。  如果产品ID为集群类型（即对应的type为cluster），broker_num字段为必选。
        :type product_id: str
        :param broker_num: 代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7
        :type broker_num: int
        :param maintain_begin: 维护时间窗开始时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 开始时间必须为22:00、02:00、06:00、10:00、14:00和18:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00时，结束时间为02:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00。
        :type maintain_end: str
        :param enable_publicip: RabbitMQ实例是否开启公网访问功能。 - true：开启 - false：不开启
        :type enable_publicip: bool
        :param publicip_id: RabbitMQ实例绑定的弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。
        :type publicip_id: str
        :param ssl_enable: 是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。
        :type ssl_enable: bool
        :param storage_spec_code: 存储IO规格。  取值范围：   - dms.physical.storage.high.v2   - dms.physical.storage.ultra.v2   - dms.physical.storage.high.dss.v2(专属云)   - dms.physical.storage.ultra.dss.v2(专属云)
        :type storage_spec_code: str
        :param enterprise_project_id: 企业项目ID。若为企业项目账号，该参数必填。
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
        """
        
        

        self._name = None
        self._description = None
        self._engine = None
        self._engine_version = None
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
        self.storage_space = storage_space
        self.access_user = access_user
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
        """Gets the name of this CreateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :return: The name of this CreateInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :param name: The name of this CreateInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :return: The description of this CreateInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :param description: The description of this CreateInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        """Gets the engine of this CreateInstanceReq.

        消息引擎：rabbitmq。

        :return: The engine of this CreateInstanceReq.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this CreateInstanceReq.

        消息引擎：rabbitmq。

        :param engine: The engine of this CreateInstanceReq.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this CreateInstanceReq.

        消息引擎的版本。   - RabbitMQ版本有：3.8.35[和3.7.17](tag:g42,hk_g42,tm,hk_tm)。 

        :return: The engine_version of this CreateInstanceReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CreateInstanceReq.

        消息引擎的版本。   - RabbitMQ版本有：3.8.35[和3.7.17](tag:g42,hk_g42,tm,hk_tm)。 

        :param engine_version: The engine_version of this CreateInstanceReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def storage_space(self):
        """Gets the storage_space of this CreateInstanceReq.

        消息存储空间，单位GB。   - 单机RabbitMQ实例的存储空间的取值范围100GB~90000GB。   - 集群RabbitMQ实例的存储空间的取值范围为100GB*节点数~90000GB、200GB*节点数~90000GB、300GB*节点数~90000GB。 

        :return: The storage_space of this CreateInstanceReq.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this CreateInstanceReq.

        消息存储空间，单位GB。   - 单机RabbitMQ实例的存储空间的取值范围100GB~90000GB。   - 集群RabbitMQ实例的存储空间的取值范围为100GB*节点数~90000GB、200GB*节点数~90000GB、300GB*节点数~90000GB。 

        :param storage_space: The storage_space of this CreateInstanceReq.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def access_user(self):
        """Gets the access_user of this CreateInstanceReq.

        认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :return: The access_user of this CreateInstanceReq.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this CreateInstanceReq.

        认证用户名，只能由英文字母开头且由英文字母、数字、中划线、下划线组成，长度为4~64的字符。

        :param access_user: The access_user of this CreateInstanceReq.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def password(self):
        """Gets the password of this CreateInstanceReq.

        实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :return: The password of this CreateInstanceReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateInstanceReq.

        实例的认证密码。  复杂度要求： - 输入长度为8到32位的字符串。 - 必须包含如下四种字符中的两种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|[{}]:'\",<.>/?）

        :param password: The password of this CreateInstanceReq.
        :type password: str
        """
        self._password = password

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceReq.

        租户VPC ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :return: The vpc_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceReq.

        租户VPC ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。

        :param vpc_id: The vpc_id of this CreateInstanceReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceReq.

        租户安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :return: The security_group_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceReq.

        租户安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :param security_group_id: The security_group_id of this CreateInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceReq.

        子网ID。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :return: The subnet_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceReq.

        子网ID。  获取方法如下：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。

        :param subnet_id: The subnet_id of this CreateInstanceReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def available_zones(self):
        """Gets the available_zones of this CreateInstanceReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。

        :return: The available_zones of this CreateInstanceReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this CreateInstanceReq.

        创建节点到指定且有资源的可用区ID。请参考[查询可用区信息](ListAvailableZones.xml)获取可用区ID。  该参数不能为空数组或者数组的值为空。

        :param available_zones: The available_zones of this CreateInstanceReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def product_id(self):
        """Gets the product_id of this CreateInstanceReq.

        产品标识。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。  如果产品ID为集群类型（即对应的type为cluster），broker_num字段为必选。

        :return: The product_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateInstanceReq.

        产品标识。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。  如果产品ID为集群类型（即对应的type为cluster），broker_num字段为必选。

        :param product_id: The product_id of this CreateInstanceReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def broker_num(self):
        """Gets the broker_num of this CreateInstanceReq.

        代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7

        :return: The broker_num of this CreateInstanceReq.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this CreateInstanceReq.

        代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7

        :param broker_num: The broker_num of this CreateInstanceReq.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this CreateInstanceReq.

        维护时间窗开始时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 开始时间必须为22:00、02:00、06:00、10:00、14:00和18:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00。

        :return: The maintain_begin of this CreateInstanceReq.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this CreateInstanceReq.

        维护时间窗开始时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 开始时间必须为22:00、02:00、06:00、10:00、14:00和18:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00。

        :param maintain_begin: The maintain_begin of this CreateInstanceReq.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this CreateInstanceReq.

        维护时间窗结束时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00时，结束时间为02:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00。

        :return: The maintain_end of this CreateInstanceReq.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this CreateInstanceReq.

        维护时间窗结束时间，格式为HH:mm。 - 维护时间窗开始和结束时间必须为指定的时间段。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00时，结束时间为02:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00。

        :param maintain_end: The maintain_end of this CreateInstanceReq.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this CreateInstanceReq.

        RabbitMQ实例是否开启公网访问功能。 - true：开启 - false：不开启

        :return: The enable_publicip of this CreateInstanceReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this CreateInstanceReq.

        RabbitMQ实例是否开启公网访问功能。 - true：开启 - false：不开启

        :param enable_publicip: The enable_publicip of this CreateInstanceReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        """Gets the publicip_id of this CreateInstanceReq.

        RabbitMQ实例绑定的弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :return: The publicip_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this CreateInstanceReq.

        RabbitMQ实例绑定的弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :param publicip_id: The publicip_id of this CreateInstanceReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this CreateInstanceReq.

        是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。

        :return: The ssl_enable of this CreateInstanceReq.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this CreateInstanceReq.

        是否打开SSL加密访问。 - true：打开SSL加密访问。 - false：不打开SSL加密访问。

        :param ssl_enable: The ssl_enable of this CreateInstanceReq.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def storage_spec_code(self):
        """Gets the storage_spec_code of this CreateInstanceReq.

        存储IO规格。  取值范围：   - dms.physical.storage.high.v2   - dms.physical.storage.ultra.v2   - dms.physical.storage.high.dss.v2(专属云)   - dms.physical.storage.ultra.dss.v2(专属云)

        :return: The storage_spec_code of this CreateInstanceReq.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        """Sets the storage_spec_code of this CreateInstanceReq.

        存储IO规格。  取值范围：   - dms.physical.storage.high.v2   - dms.physical.storage.ultra.v2   - dms.physical.storage.high.dss.v2(专属云)   - dms.physical.storage.ultra.dss.v2(专属云)

        :param storage_spec_code: The storage_spec_code of this CreateInstanceReq.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceReq.

        企业项目ID。若为企业项目账号，该参数必填。

        :return: The enterprise_project_id of this CreateInstanceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceReq.

        企业项目ID。若为企业项目账号，该参数必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateInstanceReq.

        标签列表。

        :return: The tags of this CreateInstanceReq.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstanceReq.

        标签列表。

        :param tags: The tags of this CreateInstanceReq.
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def bss_param(self):
        """Gets the bss_param of this CreateInstanceReq.

        :return: The bss_param of this CreateInstanceReq.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this CreateInstanceReq.

        :param bss_param: The bss_param of this CreateInstanceReq.
        :type bss_param: :class:`huaweicloudsdkrabbitmq.v2.BssParam`
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
        if not isinstance(other, CreateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
