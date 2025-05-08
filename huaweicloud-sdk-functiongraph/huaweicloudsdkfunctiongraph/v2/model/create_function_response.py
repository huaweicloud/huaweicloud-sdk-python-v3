# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFunctionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_id': 'str',
        'func_urn': 'str',
        'func_name': 'str',
        'domain_id': 'str',
        'namespace': 'str',
        'project_name': 'str',
        'package': 'str',
        'runtime': 'str',
        'timeout': 'int',
        'handler': 'str',
        'memory_size': 'int',
        'gpu_memory': 'int',
        'cpu': 'int',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'code_size': 'int',
        'domain_names': 'str',
        'user_data': 'str',
        'encrypted_user_data': 'str',
        'digest': 'str',
        'version': 'str',
        'image_name': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'last_modified': 'datetime',
        'func_vpc': 'FuncVpc',
        'mount_config': 'MountConfig',
        'reserved_instance_count': 'int',
        'depend_list': 'list[str]',
        'depend_version_list': 'list[str]',
        'strategy_config': 'StrategyConfig',
        'extend_config': 'str',
        'dependencies': 'list[Dependency]',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'pre_stop_handler': 'str',
        'pre_stop_timeout': 'int',
        'enterprise_project_id': 'str',
        'long_time': 'bool',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'type': 'str',
        'enable_cloud_debug': 'str',
        'enable_dynamic_memory': 'bool',
        'is_stateful_function': 'bool',
        'custom_image': 'CustomImage',
        'is_bridge_function': 'bool',
        'apig_route_enable': 'bool',
        'heartbeat_handler': 'str',
        'enable_class_isolation': 'bool',
        'gpu_type': 'str',
        'allow_ephemeral_storage': 'bool',
        'ephemeral_storage': 'int',
        'network_controller': 'NetworkControlConfig',
        'resource_id': 'str',
        'is_return_stream': 'bool',
        'enable_auth_in_header': 'bool',
        'enable_lts_log': 'bool',
        'lts_custom_tag': 'dict(str, str)',
        'user_data_encrypt_kms_key_id': 'str',
        'code_encrypt_kms_key_id': 'str'
    }

    attribute_map = {
        'func_id': 'func_id',
        'func_urn': 'func_urn',
        'func_name': 'func_name',
        'domain_id': 'domain_id',
        'namespace': 'namespace',
        'project_name': 'project_name',
        'package': 'package',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'handler': 'handler',
        'memory_size': 'memory_size',
        'gpu_memory': 'gpu_memory',
        'cpu': 'cpu',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'code_size': 'code_size',
        'domain_names': 'domain_names',
        'user_data': 'user_data',
        'encrypted_user_data': 'encrypted_user_data',
        'digest': 'digest',
        'version': 'version',
        'image_name': 'image_name',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'last_modified': 'last_modified',
        'func_vpc': 'func_vpc',
        'mount_config': 'mount_config',
        'reserved_instance_count': 'reserved_instance_count',
        'depend_list': 'depend_list',
        'depend_version_list': 'depend_version_list',
        'strategy_config': 'strategy_config',
        'extend_config': 'extend_config',
        'dependencies': 'dependencies',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'pre_stop_handler': 'pre_stop_handler',
        'pre_stop_timeout': 'pre_stop_timeout',
        'enterprise_project_id': 'enterprise_project_id',
        'long_time': 'long_time',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'type': 'type',
        'enable_cloud_debug': 'enable_cloud_debug',
        'enable_dynamic_memory': 'enable_dynamic_memory',
        'is_stateful_function': 'is_stateful_function',
        'custom_image': 'custom_image',
        'is_bridge_function': 'is_bridge_function',
        'apig_route_enable': 'apig_route_enable',
        'heartbeat_handler': 'heartbeat_handler',
        'enable_class_isolation': 'enable_class_isolation',
        'gpu_type': 'gpu_type',
        'allow_ephemeral_storage': 'allow_ephemeral_storage',
        'ephemeral_storage': 'ephemeral_storage',
        'network_controller': 'network_controller',
        'resource_id': 'resource_id',
        'is_return_stream': 'is_return_stream',
        'enable_auth_in_header': 'enable_auth_in_header',
        'enable_lts_log': 'enable_lts_log',
        'lts_custom_tag': 'lts_custom_tag',
        'user_data_encrypt_kms_key_id': 'user_data_encrypt_kms_key_id',
        'code_encrypt_kms_key_id': 'code_encrypt_kms_key_id'
    }

    def __init__(self, func_id=None, func_urn=None, func_name=None, domain_id=None, namespace=None, project_name=None, package=None, runtime=None, timeout=None, handler=None, memory_size=None, gpu_memory=None, cpu=None, code_type=None, code_url=None, code_filename=None, code_size=None, domain_names=None, user_data=None, encrypted_user_data=None, digest=None, version=None, image_name=None, xrole=None, app_xrole=None, description=None, last_modified=None, func_vpc=None, mount_config=None, reserved_instance_count=None, depend_list=None, depend_version_list=None, strategy_config=None, extend_config=None, dependencies=None, initializer_handler=None, initializer_timeout=None, pre_stop_handler=None, pre_stop_timeout=None, enterprise_project_id=None, long_time=None, log_group_id=None, log_stream_id=None, type=None, enable_cloud_debug=None, enable_dynamic_memory=None, is_stateful_function=None, custom_image=None, is_bridge_function=None, apig_route_enable=None, heartbeat_handler=None, enable_class_isolation=None, gpu_type=None, allow_ephemeral_storage=None, ephemeral_storage=None, network_controller=None, resource_id=None, is_return_stream=None, enable_auth_in_header=None, enable_lts_log=None, lts_custom_tag=None, user_data_encrypt_kms_key_id=None, code_encrypt_kms_key_id=None):
        r"""CreateFunctionResponse

        The model defined in huaweicloud sdk

        :param func_id: 函数id，唯一标识函数。
        :type func_id: str
        :param func_urn: 函数的URN（Uniform Resource Name），唯一标识函数。
        :type func_urn: str
        :param func_name: 函数名称。
        :type func_name: str
        :param domain_id: 域名id。
        :type domain_id: str
        :param namespace: 租户的project id。
        :type namespace: str
        :param project_name: 租户的project name。
        :type project_name: str
        :param package: 函数所属的分组Package，用于用户针对函数的自定义分组。
        :type package: str
        :param runtime: FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。
        :type runtime: str
        :param timeout: 函数执行超时时间，超时函数将被强行停止，范围3～259200秒。
        :type timeout: int
        :param handler: 函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。
        :type handler: str
        :param memory_size: 函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。
        :type memory_size: int
        :param gpu_memory: 函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。
        :type gpu_memory: int
        :param cpu: 函数占用的cpu资源。 单位为millicore（1 core&#x3D;1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。
        :type cpu: int
        :param code_type: 函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。
        :type code_type: str
        :param code_url: 当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。
        :type code_url: str
        :param code_filename: 函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。
        :type code_filename: str
        :param code_size: 函数大小，单位：字节。
        :type code_size: int
        :param domain_names: 函数配置的需要支持域名解析的内网域名。
        :type domain_names: str
        :param user_data: 用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host&#x3D;{host_ip}，最多定义20个，总长度不超过4KB。
        :type user_data: str
        :param encrypted_user_data: 用户自定义的name/value信息，用于需要加密的配置。
        :type encrypted_user_data: str
        :param digest: 函数代码SHA512 hash值，用于判断函数是否变化。
        :type digest: str
        :param version: 函数版本号。
        :type version: str
        :param image_name: 函数版本的内部标识。
        :type image_name: str
        :param xrole: 函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type xrole: str
        :param app_xrole: 函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type app_xrole: str
        :param description: 函数描述。
        :type description: str
        :param last_modified: 函数最后一次更新时间。
        :type last_modified: datetime
        :param func_vpc: 
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        :param mount_config: 
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        :param reserved_instance_count: 函数预留实例数量。
        :type reserved_instance_count: int
        :param depend_list: 依赖id列表
        :type depend_list: list[str]
        :param depend_version_list: 依赖版本id列表
        :type depend_version_list: list[str]
        :param strategy_config: 
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        :param extend_config: 函数扩展配置。
        :type extend_config: str
        :param dependencies: 函数依赖代码包列表。
        :type dependencies: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        :param initializer_handler: 函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。
        :type initializer_handler: str
        :param initializer_timeout: 初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。
        :type initializer_timeout: int
        :param pre_stop_handler: 函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。
        :type pre_stop_handler: str
        :param pre_stop_timeout: 初始化超时时间，超时函数将被强行停止，范围1～90秒。
        :type pre_stop_timeout: int
        :param enterprise_project_id: 企业项目ID，在企业用户创建函数时必填。
        :type enterprise_project_id: str
        :param long_time: 是否允许进行长时间超时设置。
        :type long_time: bool
        :param log_group_id: 自定义日志查询组id
        :type log_group_id: str
        :param log_stream_id: 自定义日志查询流id
        :type log_stream_id: str
        :param type: v2表示为正式版本,v1为废弃版本。
        :type type: str
        :param enable_cloud_debug: 适配CloudDebug场景，是否开启云调试（已废弃）
        :type enable_cloud_debug: str
        :param enable_dynamic_memory: 是否启动动态内存配置
        :type enable_dynamic_memory: bool
        :param is_stateful_function: 是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持
        :type is_stateful_function: bool
        :param custom_image: 
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        :param is_bridge_function: 是否为bridge函数
        :type is_bridge_function: bool
        :param apig_route_enable: 是否配置下沉apig路由规则。
        :type apig_route_enable: bool
        :param heartbeat_handler: 心跳函数函数的入口，规则：xx.xx，必须包含“. ”，只支持JAVA运行时配置。 心跳函数入口需要与函数执行入口在同一文件下。在开启心跳函数配置时，此参数必填。
        :type heartbeat_handler: str
        :param enable_class_isolation: 类隔离开关，只支持JAVA运行时配置。开启类隔离后可以支持Kafka转储并提升类加载效率，但也可能会导致某些兼容性问题，请谨慎开启。
        :type enable_class_isolation: bool
        :param gpu_type: 显卡类型。
        :type gpu_type: str
        :param allow_ephemeral_storage: 是否支持配置临时存储。
        :type allow_ephemeral_storage: bool
        :param ephemeral_storage: 临时存储大小。默认情况下会为函数的/tmp目录分配512MB的空间。您可以通过临时存储设置将函数的/tmp目录大小调整为10G。
        :type ephemeral_storage: int
        :param network_controller: 
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        :param resource_id: 资源id。
        :type resource_id: str
        :param is_return_stream: 是否返回流式数据（已废弃）
        :type is_return_stream: bool
        :param enable_auth_in_header: 是否允许在请求头中添加鉴权信息，只支持自定义镜像函数（创建函数时不支持修改）
        :type enable_auth_in_header: bool
        :param enable_lts_log: 是否开启日志。
        :type enable_lts_log: bool
        :param lts_custom_tag: 自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。
        :type lts_custom_tag: dict(str, str)
        :param user_data_encrypt_kms_key_id: 用于环境变量加密的kms主秘钥ID。
        :type user_data_encrypt_kms_key_id: str
        :param code_encrypt_kms_key_id: 用于用户代码加密的kms主秘钥ID。
        :type code_encrypt_kms_key_id: str
        """
        
        super(CreateFunctionResponse, self).__init__()

        self._func_id = None
        self._func_urn = None
        self._func_name = None
        self._domain_id = None
        self._namespace = None
        self._project_name = None
        self._package = None
        self._runtime = None
        self._timeout = None
        self._handler = None
        self._memory_size = None
        self._gpu_memory = None
        self._cpu = None
        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._code_size = None
        self._domain_names = None
        self._user_data = None
        self._encrypted_user_data = None
        self._digest = None
        self._version = None
        self._image_name = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._last_modified = None
        self._func_vpc = None
        self._mount_config = None
        self._reserved_instance_count = None
        self._depend_list = None
        self._depend_version_list = None
        self._strategy_config = None
        self._extend_config = None
        self._dependencies = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._pre_stop_handler = None
        self._pre_stop_timeout = None
        self._enterprise_project_id = None
        self._long_time = None
        self._log_group_id = None
        self._log_stream_id = None
        self._type = None
        self._enable_cloud_debug = None
        self._enable_dynamic_memory = None
        self._is_stateful_function = None
        self._custom_image = None
        self._is_bridge_function = None
        self._apig_route_enable = None
        self._heartbeat_handler = None
        self._enable_class_isolation = None
        self._gpu_type = None
        self._allow_ephemeral_storage = None
        self._ephemeral_storage = None
        self._network_controller = None
        self._resource_id = None
        self._is_return_stream = None
        self._enable_auth_in_header = None
        self._enable_lts_log = None
        self._lts_custom_tag = None
        self._user_data_encrypt_kms_key_id = None
        self._code_encrypt_kms_key_id = None
        self.discriminator = None

        if func_id is not None:
            self.func_id = func_id
        if func_urn is not None:
            self.func_urn = func_urn
        if func_name is not None:
            self.func_name = func_name
        if domain_id is not None:
            self.domain_id = domain_id
        if namespace is not None:
            self.namespace = namespace
        if project_name is not None:
            self.project_name = project_name
        if package is not None:
            self.package = package
        if runtime is not None:
            self.runtime = runtime
        if timeout is not None:
            self.timeout = timeout
        if handler is not None:
            self.handler = handler
        if memory_size is not None:
            self.memory_size = memory_size
        if gpu_memory is not None:
            self.gpu_memory = gpu_memory
        if cpu is not None:
            self.cpu = cpu
        if code_type is not None:
            self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        if code_size is not None:
            self.code_size = code_size
        if domain_names is not None:
            self.domain_names = domain_names
        if user_data is not None:
            self.user_data = user_data
        if encrypted_user_data is not None:
            self.encrypted_user_data = encrypted_user_data
        if digest is not None:
            self.digest = digest
        if version is not None:
            self.version = version
        if image_name is not None:
            self.image_name = image_name
        if xrole is not None:
            self.xrole = xrole
        if app_xrole is not None:
            self.app_xrole = app_xrole
        if description is not None:
            self.description = description
        if last_modified is not None:
            self.last_modified = last_modified
        if func_vpc is not None:
            self.func_vpc = func_vpc
        if mount_config is not None:
            self.mount_config = mount_config
        if reserved_instance_count is not None:
            self.reserved_instance_count = reserved_instance_count
        if depend_list is not None:
            self.depend_list = depend_list
        if depend_version_list is not None:
            self.depend_version_list = depend_version_list
        if strategy_config is not None:
            self.strategy_config = strategy_config
        if extend_config is not None:
            self.extend_config = extend_config
        if dependencies is not None:
            self.dependencies = dependencies
        if initializer_handler is not None:
            self.initializer_handler = initializer_handler
        if initializer_timeout is not None:
            self.initializer_timeout = initializer_timeout
        if pre_stop_handler is not None:
            self.pre_stop_handler = pre_stop_handler
        if pre_stop_timeout is not None:
            self.pre_stop_timeout = pre_stop_timeout
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if long_time is not None:
            self.long_time = long_time
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if type is not None:
            self.type = type
        if enable_cloud_debug is not None:
            self.enable_cloud_debug = enable_cloud_debug
        if enable_dynamic_memory is not None:
            self.enable_dynamic_memory = enable_dynamic_memory
        if is_stateful_function is not None:
            self.is_stateful_function = is_stateful_function
        if custom_image is not None:
            self.custom_image = custom_image
        if is_bridge_function is not None:
            self.is_bridge_function = is_bridge_function
        if apig_route_enable is not None:
            self.apig_route_enable = apig_route_enable
        if heartbeat_handler is not None:
            self.heartbeat_handler = heartbeat_handler
        if enable_class_isolation is not None:
            self.enable_class_isolation = enable_class_isolation
        if gpu_type is not None:
            self.gpu_type = gpu_type
        if allow_ephemeral_storage is not None:
            self.allow_ephemeral_storage = allow_ephemeral_storage
        if ephemeral_storage is not None:
            self.ephemeral_storage = ephemeral_storage
        if network_controller is not None:
            self.network_controller = network_controller
        if resource_id is not None:
            self.resource_id = resource_id
        if is_return_stream is not None:
            self.is_return_stream = is_return_stream
        if enable_auth_in_header is not None:
            self.enable_auth_in_header = enable_auth_in_header
        if enable_lts_log is not None:
            self.enable_lts_log = enable_lts_log
        if lts_custom_tag is not None:
            self.lts_custom_tag = lts_custom_tag
        if user_data_encrypt_kms_key_id is not None:
            self.user_data_encrypt_kms_key_id = user_data_encrypt_kms_key_id
        if code_encrypt_kms_key_id is not None:
            self.code_encrypt_kms_key_id = code_encrypt_kms_key_id

    @property
    def func_id(self):
        r"""Gets the func_id of this CreateFunctionResponse.

        函数id，唯一标识函数。

        :return: The func_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._func_id

    @func_id.setter
    def func_id(self, func_id):
        r"""Sets the func_id of this CreateFunctionResponse.

        函数id，唯一标识函数。

        :param func_id: The func_id of this CreateFunctionResponse.
        :type func_id: str
        """
        self._func_id = func_id

    @property
    def func_urn(self):
        r"""Gets the func_urn of this CreateFunctionResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this CreateFunctionResponse.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this CreateFunctionResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this CreateFunctionResponse.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        r"""Gets the func_name of this CreateFunctionResponse.

        函数名称。

        :return: The func_name of this CreateFunctionResponse.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this CreateFunctionResponse.

        函数名称。

        :param func_name: The func_name of this CreateFunctionResponse.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateFunctionResponse.

        域名id。

        :return: The domain_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateFunctionResponse.

        域名id。

        :param domain_id: The domain_id of this CreateFunctionResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateFunctionResponse.

        租户的project id。

        :return: The namespace of this CreateFunctionResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateFunctionResponse.

        租户的project id。

        :param namespace: The namespace of this CreateFunctionResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project_name(self):
        r"""Gets the project_name of this CreateFunctionResponse.

        租户的project name。

        :return: The project_name of this CreateFunctionResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this CreateFunctionResponse.

        租户的project name。

        :param project_name: The project_name of this CreateFunctionResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def package(self):
        r"""Gets the package of this CreateFunctionResponse.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this CreateFunctionResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this CreateFunctionResponse.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this CreateFunctionResponse.
        :type package: str
        """
        self._package = package

    @property
    def runtime(self):
        r"""Gets the runtime of this CreateFunctionResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this CreateFunctionResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this CreateFunctionResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this CreateFunctionResponse.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        r"""Gets the timeout of this CreateFunctionResponse.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :return: The timeout of this CreateFunctionResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this CreateFunctionResponse.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :param timeout: The timeout of this CreateFunctionResponse.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        r"""Gets the handler of this CreateFunctionResponse.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this CreateFunctionResponse.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this CreateFunctionResponse.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this CreateFunctionResponse.
        :type handler: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        r"""Gets the memory_size of this CreateFunctionResponse.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this CreateFunctionResponse.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        r"""Sets the memory_size of this CreateFunctionResponse.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this CreateFunctionResponse.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def gpu_memory(self):
        r"""Gets the gpu_memory of this CreateFunctionResponse.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :return: The gpu_memory of this CreateFunctionResponse.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        r"""Sets the gpu_memory of this CreateFunctionResponse.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :param gpu_memory: The gpu_memory of this CreateFunctionResponse.
        :type gpu_memory: int
        """
        self._gpu_memory = gpu_memory

    @property
    def cpu(self):
        r"""Gets the cpu of this CreateFunctionResponse.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。

        :return: The cpu of this CreateFunctionResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CreateFunctionResponse.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。

        :param cpu: The cpu of this CreateFunctionResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def code_type(self):
        r"""Gets the code_type of this CreateFunctionResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :return: The code_type of this CreateFunctionResponse.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        r"""Sets the code_type of this CreateFunctionResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :param code_type: The code_type of this CreateFunctionResponse.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        r"""Gets the code_url of this CreateFunctionResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this CreateFunctionResponse.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this CreateFunctionResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this CreateFunctionResponse.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        r"""Gets the code_filename of this CreateFunctionResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this CreateFunctionResponse.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        r"""Sets the code_filename of this CreateFunctionResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this CreateFunctionResponse.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def code_size(self):
        r"""Gets the code_size of this CreateFunctionResponse.

        函数大小，单位：字节。

        :return: The code_size of this CreateFunctionResponse.
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        r"""Sets the code_size of this CreateFunctionResponse.

        函数大小，单位：字节。

        :param code_size: The code_size of this CreateFunctionResponse.
        :type code_size: int
        """
        self._code_size = code_size

    @property
    def domain_names(self):
        r"""Gets the domain_names of this CreateFunctionResponse.

        函数配置的需要支持域名解析的内网域名。

        :return: The domain_names of this CreateFunctionResponse.
        :rtype: str
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        r"""Sets the domain_names of this CreateFunctionResponse.

        函数配置的需要支持域名解析的内网域名。

        :param domain_names: The domain_names of this CreateFunctionResponse.
        :type domain_names: str
        """
        self._domain_names = domain_names

    @property
    def user_data(self):
        r"""Gets the user_data of this CreateFunctionResponse.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this CreateFunctionResponse.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this CreateFunctionResponse.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this CreateFunctionResponse.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def encrypted_user_data(self):
        r"""Gets the encrypted_user_data of this CreateFunctionResponse.

        用户自定义的name/value信息，用于需要加密的配置。

        :return: The encrypted_user_data of this CreateFunctionResponse.
        :rtype: str
        """
        return self._encrypted_user_data

    @encrypted_user_data.setter
    def encrypted_user_data(self, encrypted_user_data):
        r"""Sets the encrypted_user_data of this CreateFunctionResponse.

        用户自定义的name/value信息，用于需要加密的配置。

        :param encrypted_user_data: The encrypted_user_data of this CreateFunctionResponse.
        :type encrypted_user_data: str
        """
        self._encrypted_user_data = encrypted_user_data

    @property
    def digest(self):
        r"""Gets the digest of this CreateFunctionResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :return: The digest of this CreateFunctionResponse.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this CreateFunctionResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :param digest: The digest of this CreateFunctionResponse.
        :type digest: str
        """
        self._digest = digest

    @property
    def version(self):
        r"""Gets the version of this CreateFunctionResponse.

        函数版本号。

        :return: The version of this CreateFunctionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateFunctionResponse.

        函数版本号。

        :param version: The version of this CreateFunctionResponse.
        :type version: str
        """
        self._version = version

    @property
    def image_name(self):
        r"""Gets the image_name of this CreateFunctionResponse.

        函数版本的内部标识。

        :return: The image_name of this CreateFunctionResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CreateFunctionResponse.

        函数版本的内部标识。

        :param image_name: The image_name of this CreateFunctionResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def xrole(self):
        r"""Gets the xrole of this CreateFunctionResponse.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this CreateFunctionResponse.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        r"""Sets the xrole of this CreateFunctionResponse.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this CreateFunctionResponse.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        r"""Gets the app_xrole of this CreateFunctionResponse.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this CreateFunctionResponse.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        r"""Sets the app_xrole of this CreateFunctionResponse.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this CreateFunctionResponse.
        :type app_xrole: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        r"""Gets the description of this CreateFunctionResponse.

        函数描述。

        :return: The description of this CreateFunctionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFunctionResponse.

        函数描述。

        :param description: The description of this CreateFunctionResponse.
        :type description: str
        """
        self._description = description

    @property
    def last_modified(self):
        r"""Gets the last_modified of this CreateFunctionResponse.

        函数最后一次更新时间。

        :return: The last_modified of this CreateFunctionResponse.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this CreateFunctionResponse.

        函数最后一次更新时间。

        :param last_modified: The last_modified of this CreateFunctionResponse.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def func_vpc(self):
        r"""Gets the func_vpc of this CreateFunctionResponse.

        :return: The func_vpc of this CreateFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        r"""Sets the func_vpc of this CreateFunctionResponse.

        :param func_vpc: The func_vpc of this CreateFunctionResponse.
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        self._func_vpc = func_vpc

    @property
    def mount_config(self):
        r"""Gets the mount_config of this CreateFunctionResponse.

        :return: The mount_config of this CreateFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        return self._mount_config

    @mount_config.setter
    def mount_config(self, mount_config):
        r"""Sets the mount_config of this CreateFunctionResponse.

        :param mount_config: The mount_config of this CreateFunctionResponse.
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        self._mount_config = mount_config

    @property
    def reserved_instance_count(self):
        r"""Gets the reserved_instance_count of this CreateFunctionResponse.

        函数预留实例数量。

        :return: The reserved_instance_count of this CreateFunctionResponse.
        :rtype: int
        """
        return self._reserved_instance_count

    @reserved_instance_count.setter
    def reserved_instance_count(self, reserved_instance_count):
        r"""Sets the reserved_instance_count of this CreateFunctionResponse.

        函数预留实例数量。

        :param reserved_instance_count: The reserved_instance_count of this CreateFunctionResponse.
        :type reserved_instance_count: int
        """
        self._reserved_instance_count = reserved_instance_count

    @property
    def depend_list(self):
        r"""Gets the depend_list of this CreateFunctionResponse.

        依赖id列表

        :return: The depend_list of this CreateFunctionResponse.
        :rtype: list[str]
        """
        return self._depend_list

    @depend_list.setter
    def depend_list(self, depend_list):
        r"""Sets the depend_list of this CreateFunctionResponse.

        依赖id列表

        :param depend_list: The depend_list of this CreateFunctionResponse.
        :type depend_list: list[str]
        """
        self._depend_list = depend_list

    @property
    def depend_version_list(self):
        r"""Gets the depend_version_list of this CreateFunctionResponse.

        依赖版本id列表

        :return: The depend_version_list of this CreateFunctionResponse.
        :rtype: list[str]
        """
        return self._depend_version_list

    @depend_version_list.setter
    def depend_version_list(self, depend_version_list):
        r"""Sets the depend_version_list of this CreateFunctionResponse.

        依赖版本id列表

        :param depend_version_list: The depend_version_list of this CreateFunctionResponse.
        :type depend_version_list: list[str]
        """
        self._depend_version_list = depend_version_list

    @property
    def strategy_config(self):
        r"""Gets the strategy_config of this CreateFunctionResponse.

        :return: The strategy_config of this CreateFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        r"""Sets the strategy_config of this CreateFunctionResponse.

        :param strategy_config: The strategy_config of this CreateFunctionResponse.
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        self._strategy_config = strategy_config

    @property
    def extend_config(self):
        r"""Gets the extend_config of this CreateFunctionResponse.

        函数扩展配置。

        :return: The extend_config of this CreateFunctionResponse.
        :rtype: str
        """
        return self._extend_config

    @extend_config.setter
    def extend_config(self, extend_config):
        r"""Sets the extend_config of this CreateFunctionResponse.

        函数扩展配置。

        :param extend_config: The extend_config of this CreateFunctionResponse.
        :type extend_config: str
        """
        self._extend_config = extend_config

    @property
    def dependencies(self):
        r"""Gets the dependencies of this CreateFunctionResponse.

        函数依赖代码包列表。

        :return: The dependencies of this CreateFunctionResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        r"""Sets the dependencies of this CreateFunctionResponse.

        函数依赖代码包列表。

        :param dependencies: The dependencies of this CreateFunctionResponse.
        :type dependencies: list[:class:`huaweicloudsdkfunctiongraph.v2.Dependency`]
        """
        self._dependencies = dependencies

    @property
    def initializer_handler(self):
        r"""Gets the initializer_handler of this CreateFunctionResponse.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this CreateFunctionResponse.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        r"""Sets the initializer_handler of this CreateFunctionResponse.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this CreateFunctionResponse.
        :type initializer_handler: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        r"""Gets the initializer_timeout of this CreateFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :return: The initializer_timeout of this CreateFunctionResponse.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        r"""Sets the initializer_timeout of this CreateFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :param initializer_timeout: The initializer_timeout of this CreateFunctionResponse.
        :type initializer_timeout: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def pre_stop_handler(self):
        r"""Gets the pre_stop_handler of this CreateFunctionResponse.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :return: The pre_stop_handler of this CreateFunctionResponse.
        :rtype: str
        """
        return self._pre_stop_handler

    @pre_stop_handler.setter
    def pre_stop_handler(self, pre_stop_handler):
        r"""Sets the pre_stop_handler of this CreateFunctionResponse.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :param pre_stop_handler: The pre_stop_handler of this CreateFunctionResponse.
        :type pre_stop_handler: str
        """
        self._pre_stop_handler = pre_stop_handler

    @property
    def pre_stop_timeout(self):
        r"""Gets the pre_stop_timeout of this CreateFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :return: The pre_stop_timeout of this CreateFunctionResponse.
        :rtype: int
        """
        return self._pre_stop_timeout

    @pre_stop_timeout.setter
    def pre_stop_timeout(self, pre_stop_timeout):
        r"""Sets the pre_stop_timeout of this CreateFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :param pre_stop_timeout: The pre_stop_timeout of this CreateFunctionResponse.
        :type pre_stop_timeout: int
        """
        self._pre_stop_timeout = pre_stop_timeout

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateFunctionResponse.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateFunctionResponse.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateFunctionResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def long_time(self):
        r"""Gets the long_time of this CreateFunctionResponse.

        是否允许进行长时间超时设置。

        :return: The long_time of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._long_time

    @long_time.setter
    def long_time(self, long_time):
        r"""Sets the long_time of this CreateFunctionResponse.

        是否允许进行长时间超时设置。

        :param long_time: The long_time of this CreateFunctionResponse.
        :type long_time: bool
        """
        self._long_time = long_time

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this CreateFunctionResponse.

        自定义日志查询组id

        :return: The log_group_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this CreateFunctionResponse.

        自定义日志查询组id

        :param log_group_id: The log_group_id of this CreateFunctionResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this CreateFunctionResponse.

        自定义日志查询流id

        :return: The log_stream_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this CreateFunctionResponse.

        自定义日志查询流id

        :param log_stream_id: The log_stream_id of this CreateFunctionResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def type(self):
        r"""Gets the type of this CreateFunctionResponse.

        v2表示为正式版本,v1为废弃版本。

        :return: The type of this CreateFunctionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFunctionResponse.

        v2表示为正式版本,v1为废弃版本。

        :param type: The type of this CreateFunctionResponse.
        :type type: str
        """
        self._type = type

    @property
    def enable_cloud_debug(self):
        r"""Gets the enable_cloud_debug of this CreateFunctionResponse.

        适配CloudDebug场景，是否开启云调试（已废弃）

        :return: The enable_cloud_debug of this CreateFunctionResponse.
        :rtype: str
        """
        return self._enable_cloud_debug

    @enable_cloud_debug.setter
    def enable_cloud_debug(self, enable_cloud_debug):
        r"""Sets the enable_cloud_debug of this CreateFunctionResponse.

        适配CloudDebug场景，是否开启云调试（已废弃）

        :param enable_cloud_debug: The enable_cloud_debug of this CreateFunctionResponse.
        :type enable_cloud_debug: str
        """
        self._enable_cloud_debug = enable_cloud_debug

    @property
    def enable_dynamic_memory(self):
        r"""Gets the enable_dynamic_memory of this CreateFunctionResponse.

        是否启动动态内存配置

        :return: The enable_dynamic_memory of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._enable_dynamic_memory

    @enable_dynamic_memory.setter
    def enable_dynamic_memory(self, enable_dynamic_memory):
        r"""Sets the enable_dynamic_memory of this CreateFunctionResponse.

        是否启动动态内存配置

        :param enable_dynamic_memory: The enable_dynamic_memory of this CreateFunctionResponse.
        :type enable_dynamic_memory: bool
        """
        self._enable_dynamic_memory = enable_dynamic_memory

    @property
    def is_stateful_function(self):
        r"""Gets the is_stateful_function of this CreateFunctionResponse.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :return: The is_stateful_function of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._is_stateful_function

    @is_stateful_function.setter
    def is_stateful_function(self, is_stateful_function):
        r"""Sets the is_stateful_function of this CreateFunctionResponse.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :param is_stateful_function: The is_stateful_function of this CreateFunctionResponse.
        :type is_stateful_function: bool
        """
        self._is_stateful_function = is_stateful_function

    @property
    def custom_image(self):
        r"""Gets the custom_image of this CreateFunctionResponse.

        :return: The custom_image of this CreateFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        return self._custom_image

    @custom_image.setter
    def custom_image(self, custom_image):
        r"""Sets the custom_image of this CreateFunctionResponse.

        :param custom_image: The custom_image of this CreateFunctionResponse.
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        self._custom_image = custom_image

    @property
    def is_bridge_function(self):
        r"""Gets the is_bridge_function of this CreateFunctionResponse.

        是否为bridge函数

        :return: The is_bridge_function of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._is_bridge_function

    @is_bridge_function.setter
    def is_bridge_function(self, is_bridge_function):
        r"""Sets the is_bridge_function of this CreateFunctionResponse.

        是否为bridge函数

        :param is_bridge_function: The is_bridge_function of this CreateFunctionResponse.
        :type is_bridge_function: bool
        """
        self._is_bridge_function = is_bridge_function

    @property
    def apig_route_enable(self):
        r"""Gets the apig_route_enable of this CreateFunctionResponse.

        是否配置下沉apig路由规则。

        :return: The apig_route_enable of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._apig_route_enable

    @apig_route_enable.setter
    def apig_route_enable(self, apig_route_enable):
        r"""Sets the apig_route_enable of this CreateFunctionResponse.

        是否配置下沉apig路由规则。

        :param apig_route_enable: The apig_route_enable of this CreateFunctionResponse.
        :type apig_route_enable: bool
        """
        self._apig_route_enable = apig_route_enable

    @property
    def heartbeat_handler(self):
        r"""Gets the heartbeat_handler of this CreateFunctionResponse.

        心跳函数函数的入口，规则：xx.xx，必须包含“. ”，只支持JAVA运行时配置。 心跳函数入口需要与函数执行入口在同一文件下。在开启心跳函数配置时，此参数必填。

        :return: The heartbeat_handler of this CreateFunctionResponse.
        :rtype: str
        """
        return self._heartbeat_handler

    @heartbeat_handler.setter
    def heartbeat_handler(self, heartbeat_handler):
        r"""Sets the heartbeat_handler of this CreateFunctionResponse.

        心跳函数函数的入口，规则：xx.xx，必须包含“. ”，只支持JAVA运行时配置。 心跳函数入口需要与函数执行入口在同一文件下。在开启心跳函数配置时，此参数必填。

        :param heartbeat_handler: The heartbeat_handler of this CreateFunctionResponse.
        :type heartbeat_handler: str
        """
        self._heartbeat_handler = heartbeat_handler

    @property
    def enable_class_isolation(self):
        r"""Gets the enable_class_isolation of this CreateFunctionResponse.

        类隔离开关，只支持JAVA运行时配置。开启类隔离后可以支持Kafka转储并提升类加载效率，但也可能会导致某些兼容性问题，请谨慎开启。

        :return: The enable_class_isolation of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._enable_class_isolation

    @enable_class_isolation.setter
    def enable_class_isolation(self, enable_class_isolation):
        r"""Sets the enable_class_isolation of this CreateFunctionResponse.

        类隔离开关，只支持JAVA运行时配置。开启类隔离后可以支持Kafka转储并提升类加载效率，但也可能会导致某些兼容性问题，请谨慎开启。

        :param enable_class_isolation: The enable_class_isolation of this CreateFunctionResponse.
        :type enable_class_isolation: bool
        """
        self._enable_class_isolation = enable_class_isolation

    @property
    def gpu_type(self):
        r"""Gets the gpu_type of this CreateFunctionResponse.

        显卡类型。

        :return: The gpu_type of this CreateFunctionResponse.
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        r"""Sets the gpu_type of this CreateFunctionResponse.

        显卡类型。

        :param gpu_type: The gpu_type of this CreateFunctionResponse.
        :type gpu_type: str
        """
        self._gpu_type = gpu_type

    @property
    def allow_ephemeral_storage(self):
        r"""Gets the allow_ephemeral_storage of this CreateFunctionResponse.

        是否支持配置临时存储。

        :return: The allow_ephemeral_storage of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._allow_ephemeral_storage

    @allow_ephemeral_storage.setter
    def allow_ephemeral_storage(self, allow_ephemeral_storage):
        r"""Sets the allow_ephemeral_storage of this CreateFunctionResponse.

        是否支持配置临时存储。

        :param allow_ephemeral_storage: The allow_ephemeral_storage of this CreateFunctionResponse.
        :type allow_ephemeral_storage: bool
        """
        self._allow_ephemeral_storage = allow_ephemeral_storage

    @property
    def ephemeral_storage(self):
        r"""Gets the ephemeral_storage of this CreateFunctionResponse.

        临时存储大小。默认情况下会为函数的/tmp目录分配512MB的空间。您可以通过临时存储设置将函数的/tmp目录大小调整为10G。

        :return: The ephemeral_storage of this CreateFunctionResponse.
        :rtype: int
        """
        return self._ephemeral_storage

    @ephemeral_storage.setter
    def ephemeral_storage(self, ephemeral_storage):
        r"""Sets the ephemeral_storage of this CreateFunctionResponse.

        临时存储大小。默认情况下会为函数的/tmp目录分配512MB的空间。您可以通过临时存储设置将函数的/tmp目录大小调整为10G。

        :param ephemeral_storage: The ephemeral_storage of this CreateFunctionResponse.
        :type ephemeral_storage: int
        """
        self._ephemeral_storage = ephemeral_storage

    @property
    def network_controller(self):
        r"""Gets the network_controller of this CreateFunctionResponse.

        :return: The network_controller of this CreateFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        return self._network_controller

    @network_controller.setter
    def network_controller(self, network_controller):
        r"""Sets the network_controller of this CreateFunctionResponse.

        :param network_controller: The network_controller of this CreateFunctionResponse.
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        self._network_controller = network_controller

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateFunctionResponse.

        资源id。

        :return: The resource_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateFunctionResponse.

        资源id。

        :param resource_id: The resource_id of this CreateFunctionResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def is_return_stream(self):
        r"""Gets the is_return_stream of this CreateFunctionResponse.

        是否返回流式数据（已废弃）

        :return: The is_return_stream of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._is_return_stream

    @is_return_stream.setter
    def is_return_stream(self, is_return_stream):
        r"""Sets the is_return_stream of this CreateFunctionResponse.

        是否返回流式数据（已废弃）

        :param is_return_stream: The is_return_stream of this CreateFunctionResponse.
        :type is_return_stream: bool
        """
        self._is_return_stream = is_return_stream

    @property
    def enable_auth_in_header(self):
        r"""Gets the enable_auth_in_header of this CreateFunctionResponse.

        是否允许在请求头中添加鉴权信息，只支持自定义镜像函数（创建函数时不支持修改）

        :return: The enable_auth_in_header of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._enable_auth_in_header

    @enable_auth_in_header.setter
    def enable_auth_in_header(self, enable_auth_in_header):
        r"""Sets the enable_auth_in_header of this CreateFunctionResponse.

        是否允许在请求头中添加鉴权信息，只支持自定义镜像函数（创建函数时不支持修改）

        :param enable_auth_in_header: The enable_auth_in_header of this CreateFunctionResponse.
        :type enable_auth_in_header: bool
        """
        self._enable_auth_in_header = enable_auth_in_header

    @property
    def enable_lts_log(self):
        r"""Gets the enable_lts_log of this CreateFunctionResponse.

        是否开启日志。

        :return: The enable_lts_log of this CreateFunctionResponse.
        :rtype: bool
        """
        return self._enable_lts_log

    @enable_lts_log.setter
    def enable_lts_log(self, enable_lts_log):
        r"""Sets the enable_lts_log of this CreateFunctionResponse.

        是否开启日志。

        :param enable_lts_log: The enable_lts_log of this CreateFunctionResponse.
        :type enable_lts_log: bool
        """
        self._enable_lts_log = enable_lts_log

    @property
    def lts_custom_tag(self):
        r"""Gets the lts_custom_tag of this CreateFunctionResponse.

        自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。

        :return: The lts_custom_tag of this CreateFunctionResponse.
        :rtype: dict(str, str)
        """
        return self._lts_custom_tag

    @lts_custom_tag.setter
    def lts_custom_tag(self, lts_custom_tag):
        r"""Sets the lts_custom_tag of this CreateFunctionResponse.

        自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。

        :param lts_custom_tag: The lts_custom_tag of this CreateFunctionResponse.
        :type lts_custom_tag: dict(str, str)
        """
        self._lts_custom_tag = lts_custom_tag

    @property
    def user_data_encrypt_kms_key_id(self):
        r"""Gets the user_data_encrypt_kms_key_id of this CreateFunctionResponse.

        用于环境变量加密的kms主秘钥ID。

        :return: The user_data_encrypt_kms_key_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._user_data_encrypt_kms_key_id

    @user_data_encrypt_kms_key_id.setter
    def user_data_encrypt_kms_key_id(self, user_data_encrypt_kms_key_id):
        r"""Sets the user_data_encrypt_kms_key_id of this CreateFunctionResponse.

        用于环境变量加密的kms主秘钥ID。

        :param user_data_encrypt_kms_key_id: The user_data_encrypt_kms_key_id of this CreateFunctionResponse.
        :type user_data_encrypt_kms_key_id: str
        """
        self._user_data_encrypt_kms_key_id = user_data_encrypt_kms_key_id

    @property
    def code_encrypt_kms_key_id(self):
        r"""Gets the code_encrypt_kms_key_id of this CreateFunctionResponse.

        用于用户代码加密的kms主秘钥ID。

        :return: The code_encrypt_kms_key_id of this CreateFunctionResponse.
        :rtype: str
        """
        return self._code_encrypt_kms_key_id

    @code_encrypt_kms_key_id.setter
    def code_encrypt_kms_key_id(self, code_encrypt_kms_key_id):
        r"""Sets the code_encrypt_kms_key_id of this CreateFunctionResponse.

        用于用户代码加密的kms主秘钥ID。

        :param code_encrypt_kms_key_id: The code_encrypt_kms_key_id of this CreateFunctionResponse.
        :type code_encrypt_kms_key_id: str
        """
        self._code_encrypt_kms_key_id = code_encrypt_kms_key_id

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
        if not isinstance(other, CreateFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
