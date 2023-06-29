# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceBody:

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
        'engine': 'str',
        'engine_version': 'str',
        'capacity': 'float',
        'spec_code': 'str',
        'az_codes': 'list[str]',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'publicip_id': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'description': 'str',
        'enable_ssl': 'bool',
        'private_ip': 'str',
        'instance_num': 'int',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'password': 'str',
        'no_password_access': 'bool',
        'bss_param': 'BssParam',
        'instance_backup_policy': 'BackupPolicy',
        'tags': 'list[ResourceTag]',
        'access_user': 'str',
        'enable_publicip': 'bool',
        'port': 'int',
        'rename_commands': 'object',
        'template_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'capacity': 'capacity',
        'spec_code': 'spec_code',
        'az_codes': 'az_codes',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'publicip_id': 'publicip_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'description': 'description',
        'enable_ssl': 'enable_ssl',
        'private_ip': 'private_ip',
        'instance_num': 'instance_num',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'password': 'password',
        'no_password_access': 'no_password_access',
        'bss_param': 'bss_param',
        'instance_backup_policy': 'instance_backup_policy',
        'tags': 'tags',
        'access_user': 'access_user',
        'enable_publicip': 'enable_publicip',
        'port': 'port',
        'rename_commands': 'rename_commands',
        'template_id': 'template_id'
    }

    def __init__(self, name=None, engine=None, engine_version=None, capacity=None, spec_code=None, az_codes=None, vpc_id=None, subnet_id=None, security_group_id=None, publicip_id=None, enterprise_project_id=None, enterprise_project_name=None, description=None, enable_ssl=None, private_ip=None, instance_num=None, maintain_begin=None, maintain_end=None, password=None, no_password_access=None, bss_param=None, instance_backup_policy=None, tags=None, access_user=None, enable_publicip=None, port=None, rename_commands=None, template_id=None):
        """CreateInstanceBody

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成。  创建单个实例时，名称长度为4到64位的字符串。批量创建实例时，名称长度为4到56位的字符串，且实例名称格式为“自定义名称-n”，其中n从000开始，依次递增。例如，批量创建两个实例，自定义名称为dcs_demo，则两个实例的名称为dcs_demo-000和dcs_demo-001。 
        :type name: str
        :param engine: 缓存引擎：Redis和Memcached。
        :type engine: str
        :param engine_version: 缓存版本。  当缓存引擎为Redis时，取值为3.0、4.0或5.0。  当缓存引擎为Memcached时，该字段为可选，取值为空。 
        :type engine_version: str
        :param capacity: 缓存容量（G Byte） - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 
        :type capacity: float
        :param spec_code: 产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。 
        :type spec_code: str
        :param az_codes: 创建缓存节点到指定且有资源的可用区Code。创建缓存节点到指定且有资源的可用区Code。具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html)，在查询时，请注意查看该可用区是否有资源。  如果是创建主备、Proxy集群、Cluster集群实例，支持跨可用区部署，可以为备节点指定备可用区。在为节点指定可用区时，用逗号分隔开，具体请查看示例。 
        :type az_codes: list[str]
        :param vpc_id: 虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。 
        :type vpc_id: str
        :param subnet_id: 子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。  当engine为Redis且engine_version为3.0时，或engine为Memcached时，该参数为必选。Redis3.0和Memcached实例支持安全组访问控制。  当engine为Redis且engine_version为4.0和5.0时，该参数为可选。Redis4.0和Redis5.0版本实例不支持安全组控制访问，只支持白名单控制。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0002.html)。 
        :type security_group_id: str
        :param publicip_id: Redis缓存实例绑定的弹性IP地址的id。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 
        :type publicip_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。 &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。 
        :type description: str
        :param enable_ssl: Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 
        :type enable_ssl: bool
        :param private_ip: 创建缓存实例手动指定的IP地址,支持Redis和Memcached。
        :type private_ip: str
        :param instance_num: 表示批量创建缓存实例时，购买的实例个数。仅Redis和Memcached实例支持批量创建。  默认值：1  取值范围：1-100 
        :type instance_num: int
        :param maintain_begin: 维护时间窗开始时间，为UTC时间，格式为HH:mm:ss - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 开始时间必须为22:00:00、02:00:00、06:00:00、10:00:00、14:00:00和18:00:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00:00。 
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，为UTC时间，格式为HH:mm:ss。 - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00:00时，结束时间为02:00:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00:00。 
        :type maintain_end: str
        :param password: 缓存实例的认证信息 &gt; 当“no_password_access”配置为“false”或未配置时，请求消息中须包含password参数。 Redis类型的缓存实例密码复杂度要求： - 输入长度为8到32位的字符串。 - 新密码不能与旧密码相同。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$^&amp;*()-_&#x3D;+\\|{}:&#39;\&quot;,&lt;.&gt;/?） 
        :type password: str
        :param no_password_access: 是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 若未配置该参数则默认值为“false”。 
        :type no_password_access: bool
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkdcs.v2.BssParam`
        :param instance_backup_policy: 
        :type instance_backup_policy: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        :param tags: 实例标签键值。
        :type tags: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        :param access_user: 当缓存类型为Redis时，则不需要设置，保持为空即可。  当缓存引擎为Memcached，且“no_password_access”为“false”时才需要设置，表示通过密码认证访问缓存实例的认证用户名。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成，长度为1~64的字符。 &gt;   - 当缓存引擎为Memcached时，该参数为可选项。   - 当缓存引擎为Redis时，该参数不需要设置。 
        :type access_user: str
        :param enable_publicip: Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 
        :type enable_publicip: bool
        :param port: 实例自定义端口。只有创建Redis4.0和Redis5.0实例才支持自定义端口，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示实例使用默认端口6379。如果自定义端口，端口范围为1~65535的任意数字。 
        :type port: int
        :param rename_commands: 支持自定义重命名高危命令。只有创建Redis4.0和Redis5.0实例才支持重命名高危命令，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示没有需要重命名的命令。当前支持重命名的高危命令有command、keys、flushdb、flushall和hgetall，其他命令暂不支持重命名。 
        :type rename_commands: object
        :param template_id: 参数模板ID
        :type template_id: str
        """
        
        

        self._name = None
        self._engine = None
        self._engine_version = None
        self._capacity = None
        self._spec_code = None
        self._az_codes = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._publicip_id = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._description = None
        self._enable_ssl = None
        self._private_ip = None
        self._instance_num = None
        self._maintain_begin = None
        self._maintain_end = None
        self._password = None
        self._no_password_access = None
        self._bss_param = None
        self._instance_backup_policy = None
        self._tags = None
        self._access_user = None
        self._enable_publicip = None
        self._port = None
        self._rename_commands = None
        self._template_id = None
        self.discriminator = None

        self.name = name
        self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        self.capacity = capacity
        self.spec_code = spec_code
        self.az_codes = az_codes
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if description is not None:
            self.description = description
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if private_ip is not None:
            self.private_ip = private_ip
        if instance_num is not None:
            self.instance_num = instance_num
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if password is not None:
            self.password = password
        if no_password_access is not None:
            self.no_password_access = no_password_access
        if bss_param is not None:
            self.bss_param = bss_param
        if instance_backup_policy is not None:
            self.instance_backup_policy = instance_backup_policy
        if tags is not None:
            self.tags = tags
        if access_user is not None:
            self.access_user = access_user
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if port is not None:
            self.port = port
        if rename_commands is not None:
            self.rename_commands = rename_commands
        if template_id is not None:
            self.template_id = template_id

    @property
    def name(self):
        """Gets the name of this CreateInstanceBody.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成。  创建单个实例时，名称长度为4到64位的字符串。批量创建实例时，名称长度为4到56位的字符串，且实例名称格式为“自定义名称-n”，其中n从000开始，依次递增。例如，批量创建两个实例，自定义名称为dcs_demo，则两个实例的名称为dcs_demo-000和dcs_demo-001。 

        :return: The name of this CreateInstanceBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceBody.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成。  创建单个实例时，名称长度为4到64位的字符串。批量创建实例时，名称长度为4到56位的字符串，且实例名称格式为“自定义名称-n”，其中n从000开始，依次递增。例如，批量创建两个实例，自定义名称为dcs_demo，则两个实例的名称为dcs_demo-000和dcs_demo-001。 

        :param name: The name of this CreateInstanceBody.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        """Gets the engine of this CreateInstanceBody.

        缓存引擎：Redis和Memcached。

        :return: The engine of this CreateInstanceBody.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this CreateInstanceBody.

        缓存引擎：Redis和Memcached。

        :param engine: The engine of this CreateInstanceBody.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this CreateInstanceBody.

        缓存版本。  当缓存引擎为Redis时，取值为3.0、4.0或5.0。  当缓存引擎为Memcached时，该字段为可选，取值为空。 

        :return: The engine_version of this CreateInstanceBody.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CreateInstanceBody.

        缓存版本。  当缓存引擎为Redis时，取值为3.0、4.0或5.0。  当缓存引擎为Memcached时，该字段为可选，取值为空。 

        :param engine_version: The engine_version of this CreateInstanceBody.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def capacity(self):
        """Gets the capacity of this CreateInstanceBody.

        缓存容量（G Byte） - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :return: The capacity of this CreateInstanceBody.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this CreateInstanceBody.

        缓存容量（G Byte） - Redis3.0：单机和主备类型实例取值：2、4、8、16、32、64。Proxy集群实例规格支持64、128、256、512和1024。 - Redis4.0和Redis5.0：单机和主备类型实例取值：0.125、0.25、0.5、1、2、4、8、16、32、64。Cluster集群实例规格支持24、32、48、64、96、128、192、256、384、512、768、1024。 - Memcached：单机和主备类型实例取值：2、4、8、16、32、64。 

        :param capacity: The capacity of this CreateInstanceBody.
        :type capacity: float
        """
        self._capacity = capacity

    @property
    def spec_code(self):
        """Gets the spec_code of this CreateInstanceBody.

        产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。 

        :return: The spec_code of this CreateInstanceBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this CreateInstanceBody.

        产品规格编码。具体查询方法如下：  - 方法一：查询产品介绍中的[实例规格](https://support.huaweicloud.com/productdesc-dcs/dcs-pd-0522002.html) - 方法二：登录分布式缓存的控制台界面，点击购买缓存实例，查找对应的实例规格名称 - 方法三：调用[查询产品规格](https://support.huaweicloud.com/api-dcs/ListFlavors.html)接口查询。 

        :param spec_code: The spec_code of this CreateInstanceBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_codes(self):
        """Gets the az_codes of this CreateInstanceBody.

        创建缓存节点到指定且有资源的可用区Code。创建缓存节点到指定且有资源的可用区Code。具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html)，在查询时，请注意查看该可用区是否有资源。  如果是创建主备、Proxy集群、Cluster集群实例，支持跨可用区部署，可以为备节点指定备可用区。在为节点指定可用区时，用逗号分隔开，具体请查看示例。 

        :return: The az_codes of this CreateInstanceBody.
        :rtype: list[str]
        """
        return self._az_codes

    @az_codes.setter
    def az_codes(self, az_codes):
        """Sets the az_codes of this CreateInstanceBody.

        创建缓存节点到指定且有资源的可用区Code。创建缓存节点到指定且有资源的可用区Code。具体查询方法，请参考[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html)，在查询时，请注意查看该可用区是否有资源。  如果是创建主备、Proxy集群、Cluster集群实例，支持跨可用区部署，可以为备节点指定备可用区。在为节点指定可用区时，用逗号分隔开，具体请查看示例。 

        :param az_codes: The az_codes of this CreateInstanceBody.
        :type az_codes: list[str]
        """
        self._az_codes = az_codes

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceBody.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。 

        :return: The vpc_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceBody.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。 

        :param vpc_id: The vpc_id of this CreateInstanceBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceBody.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 

        :return: The subnet_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceBody.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 

        :param subnet_id: The subnet_id of this CreateInstanceBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceBody.

        指定实例所属的安全组。  当engine为Redis且engine_version为3.0时，或engine为Memcached时，该参数为必选。Redis3.0和Memcached实例支持安全组访问控制。  当engine为Redis且engine_version为4.0和5.0时，该参数为可选。Redis4.0和Redis5.0版本实例不支持安全组控制访问，只支持白名单控制。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0002.html)。 

        :return: The security_group_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceBody.

        指定实例所属的安全组。  当engine为Redis且engine_version为3.0时，或engine为Memcached时，该参数为必选。Redis3.0和Memcached实例支持安全组访问控制。  当engine为Redis且engine_version为4.0和5.0时，该参数为可选。Redis4.0和Redis5.0版本实例不支持安全组控制访问，只支持白名单控制。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0002.html)。 

        :param security_group_id: The security_group_id of this CreateInstanceBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def publicip_id(self):
        """Gets the publicip_id of this CreateInstanceBody.

        Redis缓存实例绑定的弹性IP地址的id。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 

        :return: The publicip_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this CreateInstanceBody.

        Redis缓存实例绑定的弹性IP地址的id。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 

        :param publicip_id: The publicip_id of this CreateInstanceBody.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceBody.

        企业项目ID。

        :return: The enterprise_project_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceBody.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this CreateInstanceBody.

        企业项目名称。

        :return: The enterprise_project_name of this CreateInstanceBody.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this CreateInstanceBody.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this CreateInstanceBody.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def description(self):
        """Gets the description of this CreateInstanceBody.

        实例的描述信息。  长度不超过1024的字符串。 > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。 

        :return: The description of this CreateInstanceBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInstanceBody.

        实例的描述信息。  长度不超过1024的字符串。 > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。 

        :param description: The description of this CreateInstanceBody.
        :type description: str
        """
        self._description = description

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this CreateInstanceBody.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :return: The enable_ssl of this CreateInstanceBody.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this CreateInstanceBody.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :param enable_ssl: The enable_ssl of this CreateInstanceBody.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def private_ip(self):
        """Gets the private_ip of this CreateInstanceBody.

        创建缓存实例手动指定的IP地址,支持Redis和Memcached。

        :return: The private_ip of this CreateInstanceBody.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this CreateInstanceBody.

        创建缓存实例手动指定的IP地址,支持Redis和Memcached。

        :param private_ip: The private_ip of this CreateInstanceBody.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def instance_num(self):
        """Gets the instance_num of this CreateInstanceBody.

        表示批量创建缓存实例时，购买的实例个数。仅Redis和Memcached实例支持批量创建。  默认值：1  取值范围：1-100 

        :return: The instance_num of this CreateInstanceBody.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this CreateInstanceBody.

        表示批量创建缓存实例时，购买的实例个数。仅Redis和Memcached实例支持批量创建。  默认值：1  取值范围：1-100 

        :param instance_num: The instance_num of this CreateInstanceBody.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this CreateInstanceBody.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 开始时间必须为22:00:00、02:00:00、06:00:00、10:00:00、14:00:00和18:00:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00:00。 

        :return: The maintain_begin of this CreateInstanceBody.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this CreateInstanceBody.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 开始时间必须为22:00:00、02:00:00、06:00:00、10:00:00、14:00:00和18:00:00。 - 该参数不能单独为空，若该值为空，则结束时间也为空。系统分配一个默认开始时间02:00:00。 

        :param maintain_begin: The maintain_begin of this CreateInstanceBody.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this CreateInstanceBody.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss。 - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00:00时，结束时间为02:00:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00:00。 

        :return: The maintain_end of this CreateInstanceBody.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this CreateInstanceBody.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss。 - 维护时间窗开始和结束时间必须为指定的时间段，可参考[查询维护时间窗时间段](https://support.huaweicloud.com/api-dcs/ListMaintenanceWindows.html)获取。 - 结束时间在开始时间基础上加四个小时，即当开始时间为22:00:00时，结束时间为02:00:00。 - 该参数不能单独为空，若该值为空，则开始时间也为空，系统分配一个默认结束时间06:00:00。 

        :param maintain_end: The maintain_end of this CreateInstanceBody.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def password(self):
        """Gets the password of this CreateInstanceBody.

        缓存实例的认证信息 > 当“no_password_access”配置为“false”或未配置时，请求消息中须包含password参数。 Redis类型的缓存实例密码复杂度要求： - 输入长度为8到32位的字符串。 - 新密码不能与旧密码相同。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$^&*()-_=+\\|{}:'\",<.>/?） 

        :return: The password of this CreateInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateInstanceBody.

        缓存实例的认证信息 > 当“no_password_access”配置为“false”或未配置时，请求消息中须包含password参数。 Redis类型的缓存实例密码复杂度要求： - 输入长度为8到32位的字符串。 - 新密码不能与旧密码相同。 - 必须包含如下四种字符中的三种组合：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$^&*()-_=+\\|{}:'\",<.>/?） 

        :param password: The password of this CreateInstanceBody.
        :type password: str
        """
        self._password = password

    @property
    def no_password_access(self):
        """Gets the no_password_access of this CreateInstanceBody.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 若未配置该参数则默认值为“false”。 

        :return: The no_password_access of this CreateInstanceBody.
        :rtype: bool
        """
        return self._no_password_access

    @no_password_access.setter
    def no_password_access(self, no_password_access):
        """Sets the no_password_access of this CreateInstanceBody.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 若未配置该参数则默认值为“false”。 

        :param no_password_access: The no_password_access of this CreateInstanceBody.
        :type no_password_access: bool
        """
        self._no_password_access = no_password_access

    @property
    def bss_param(self):
        """Gets the bss_param of this CreateInstanceBody.

        :return: The bss_param of this CreateInstanceBody.
        :rtype: :class:`huaweicloudsdkdcs.v2.BssParam`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this CreateInstanceBody.

        :param bss_param: The bss_param of this CreateInstanceBody.
        :type bss_param: :class:`huaweicloudsdkdcs.v2.BssParam`
        """
        self._bss_param = bss_param

    @property
    def instance_backup_policy(self):
        """Gets the instance_backup_policy of this CreateInstanceBody.

        :return: The instance_backup_policy of this CreateInstanceBody.
        :rtype: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        """
        return self._instance_backup_policy

    @instance_backup_policy.setter
    def instance_backup_policy(self, instance_backup_policy):
        """Sets the instance_backup_policy of this CreateInstanceBody.

        :param instance_backup_policy: The instance_backup_policy of this CreateInstanceBody.
        :type instance_backup_policy: :class:`huaweicloudsdkdcs.v2.BackupPolicy`
        """
        self._instance_backup_policy = instance_backup_policy

    @property
    def tags(self):
        """Gets the tags of this CreateInstanceBody.

        实例标签键值。

        :return: The tags of this CreateInstanceBody.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstanceBody.

        实例标签键值。

        :param tags: The tags of this CreateInstanceBody.
        :type tags: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def access_user(self):
        """Gets the access_user of this CreateInstanceBody.

        当缓存类型为Redis时，则不需要设置，保持为空即可。  当缓存引擎为Memcached，且“no_password_access”为“false”时才需要设置，表示通过密码认证访问缓存实例的认证用户名。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成，长度为1~64的字符。 >   - 当缓存引擎为Memcached时，该参数为可选项。   - 当缓存引擎为Redis时，该参数不需要设置。 

        :return: The access_user of this CreateInstanceBody.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this CreateInstanceBody.

        当缓存类型为Redis时，则不需要设置，保持为空即可。  当缓存引擎为Memcached，且“no_password_access”为“false”时才需要设置，表示通过密码认证访问缓存实例的认证用户名。  由英文字符开头，只能由英文字母、数字、中划线和下划线组成，长度为1~64的字符。 >   - 当缓存引擎为Memcached时，该参数为可选项。   - 当缓存引擎为Redis时，该参数不需要设置。 

        :param access_user: The access_user of this CreateInstanceBody.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this CreateInstanceBody.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :return: The enable_publicip of this CreateInstanceBody.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this CreateInstanceBody.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :param enable_publicip: The enable_publicip of this CreateInstanceBody.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def port(self):
        """Gets the port of this CreateInstanceBody.

        实例自定义端口。只有创建Redis4.0和Redis5.0实例才支持自定义端口，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示实例使用默认端口6379。如果自定义端口，端口范围为1~65535的任意数字。 

        :return: The port of this CreateInstanceBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateInstanceBody.

        实例自定义端口。只有创建Redis4.0和Redis5.0实例才支持自定义端口，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示实例使用默认端口6379。如果自定义端口，端口范围为1~65535的任意数字。 

        :param port: The port of this CreateInstanceBody.
        :type port: int
        """
        self._port = port

    @property
    def rename_commands(self):
        """Gets the rename_commands of this CreateInstanceBody.

        支持自定义重命名高危命令。只有创建Redis4.0和Redis5.0实例才支持重命名高危命令，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示没有需要重命名的命令。当前支持重命名的高危命令有command、keys、flushdb、flushall和hgetall，其他命令暂不支持重命名。 

        :return: The rename_commands of this CreateInstanceBody.
        :rtype: object
        """
        return self._rename_commands

    @rename_commands.setter
    def rename_commands(self, rename_commands):
        """Sets the rename_commands of this CreateInstanceBody.

        支持自定义重命名高危命令。只有创建Redis4.0和Redis5.0实例才支持重命名高危命令，Redis3.0和Memcached实例不支持。  创建Redis4.0和Redis5.0实例，如果没发送该参数或该参数为空，表示没有需要重命名的命令。当前支持重命名的高危命令有command、keys、flushdb、flushall和hgetall，其他命令暂不支持重命名。 

        :param rename_commands: The rename_commands of this CreateInstanceBody.
        :type rename_commands: object
        """
        self._rename_commands = rename_commands

    @property
    def template_id(self):
        """Gets the template_id of this CreateInstanceBody.

        参数模板ID

        :return: The template_id of this CreateInstanceBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateInstanceBody.

        参数模板ID

        :param template_id: The template_id of this CreateInstanceBody.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, CreateInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
