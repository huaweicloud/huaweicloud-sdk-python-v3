# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFunctionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_name': 'str',
        'package': 'str',
        'runtime': 'str',
        'timeout': 'int',
        'handler': 'str',
        'depend_version_list': 'list[str]',
        'func_vpc': 'FuncVpc',
        'memory_size': 'int',
        'gpu_memory': 'int',
        'gpu_type': 'str',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'custom_image': 'CustomImage',
        'user_data': 'str',
        'encrypted_user_data': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'func_code': 'FuncCode',
        'mount_config': 'MountConfig',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'pre_stop_handler': 'str',
        'pre_stop_timeout': 'int',
        'enterprise_project_id': 'str',
        'type': 'str',
        'log_config': 'FuncLogConfig',
        'network_controller': 'NetworkControlConfig',
        'is_stateful_function': 'bool',
        'enable_dynamic_memory': 'bool',
        'enable_lts_log': 'bool',
        'lts_custom_tag': 'dict(str, str)',
        'user_data_encrypt_kms_key_id': 'str',
        'code_encrypt_kms_key_id': 'str',
        'domain_names': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'func_name': 'func_name',
        'package': 'package',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'handler': 'handler',
        'depend_version_list': 'depend_version_list',
        'func_vpc': 'func_vpc',
        'memory_size': 'memory_size',
        'gpu_memory': 'gpu_memory',
        'gpu_type': 'gpu_type',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'custom_image': 'custom_image',
        'user_data': 'user_data',
        'encrypted_user_data': 'encrypted_user_data',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'func_code': 'func_code',
        'mount_config': 'mount_config',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'pre_stop_handler': 'pre_stop_handler',
        'pre_stop_timeout': 'pre_stop_timeout',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'log_config': 'log_config',
        'network_controller': 'network_controller',
        'is_stateful_function': 'is_stateful_function',
        'enable_dynamic_memory': 'enable_dynamic_memory',
        'enable_lts_log': 'enable_lts_log',
        'lts_custom_tag': 'lts_custom_tag',
        'user_data_encrypt_kms_key_id': 'user_data_encrypt_kms_key_id',
        'code_encrypt_kms_key_id': 'code_encrypt_kms_key_id',
        'domain_names': 'domain_names',
        'tags': 'tags'
    }

    def __init__(self, func_name=None, package=None, runtime=None, timeout=None, handler=None, depend_version_list=None, func_vpc=None, memory_size=None, gpu_memory=None, gpu_type=None, code_type=None, code_url=None, code_filename=None, custom_image=None, user_data=None, encrypted_user_data=None, xrole=None, app_xrole=None, description=None, func_code=None, mount_config=None, initializer_handler=None, initializer_timeout=None, pre_stop_handler=None, pre_stop_timeout=None, enterprise_project_id=None, type=None, log_config=None, network_controller=None, is_stateful_function=None, enable_dynamic_memory=None, enable_lts_log=None, lts_custom_tag=None, user_data_encrypt_kms_key_id=None, code_encrypt_kms_key_id=None, domain_names=None, tags=None):
        r"""CreateFunctionRequestBody

        The model defined in huaweicloud sdk

        :param func_name: 函数名称。
        :type func_name: str
        :param package: 函数所属的分组Package，用于用户针对函数的自定义分组。
        :type package: str
        :param runtime: FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。
        :type runtime: str
        :param timeout: 函数执行超时时间，超时函数将被强行停止，范围3～259200秒。
        :type timeout: int
        :param handler: 函数执行入口 规则：xx.xx，必须包含“. ”；自定义镜像函数handler为“-” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。
        :type handler: str
        :param depend_version_list: 依赖版本id列表
        :type depend_version_list: list[str]
        :param func_vpc: 
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        :param memory_size: 函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。
        :type memory_size: int
        :param gpu_memory: 函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。
        :type gpu_memory: int
        :param gpu_type: 显卡类型。
        :type gpu_type: str
        :param code_type: 函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。 创建自定义镜像函数此参数非必填，其他类型函数此参数必填。
        :type code_type: str
        :param code_url: 当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。
        :type code_url: str
        :param code_filename: 函数的文件名，当CodeType为jar/zip时必须提供该字段，CodeType为其他值时不需要提供。
        :type code_filename: str
        :param custom_image: 
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        :param user_data: 用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host&#x3D;{host_ip}，最多定义20个，总长度不超过4KB。
        :type user_data: str
        :param encrypted_user_data: 用户自定义的name/value信息，用于需要加密的配置。举例：如配置加密密码，可以设置自定义参数：password&#x3D;{1234}，最多定义20个，总长度不超过4KB。
        :type encrypted_user_data: str
        :param xrole: 函数配置委托。需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。配置后用户可以通过函数执行入口方法中的context参数获取具有委托中权限的token、ak、sk，用于访问其他云服务。如果用户函数不访问任何云服务，则不用提供委托名称。
        :type xrole: str
        :param app_xrole: 函数执行委托。可为函数执行单独配置执行委托，这将减小不必要的性能损耗；不单独配置执行委托时，函数执行和函数配置将使用同一委托。
        :type app_xrole: str
        :param description: 函数描述。
        :type description: str
        :param func_code: 
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        :param mount_config: 
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
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
        :param type: 函数版本；部分局点只支持v1函数，缺省值则为v1
        :type type: str
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        :param network_controller: 
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        :param is_stateful_function: 是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持
        :type is_stateful_function: bool
        :param enable_dynamic_memory: 是否启动动态内存配置
        :type enable_dynamic_memory: bool
        :param enable_lts_log: 是否开启日志，缺省值为false。创建函数时，若此开关为true，且未传入log_config，则由FunctionGraph自动创建日志组日志流。
        :type enable_lts_log: bool
        :param lts_custom_tag: 自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。
        :type lts_custom_tag: dict(str, str)
        :param user_data_encrypt_kms_key_id: 用于环境变量加密的kms主秘钥ID。
        :type user_data_encrypt_kms_key_id: str
        :param code_encrypt_kms_key_id: 用于用户代码加密的kms主秘钥ID。
        :type code_encrypt_kms_key_id: str
        :param domain_names: vpc中配置的内网域名。在函数配置调用DNS服务的接口解析内网域名时，则函数必须具备读取DNS资源权限的委托。
        :type domain_names: str
        :param tags: 函数标签。
        :type tags: str
        """
        
        

        self._func_name = None
        self._package = None
        self._runtime = None
        self._timeout = None
        self._handler = None
        self._depend_version_list = None
        self._func_vpc = None
        self._memory_size = None
        self._gpu_memory = None
        self._gpu_type = None
        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._custom_image = None
        self._user_data = None
        self._encrypted_user_data = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._func_code = None
        self._mount_config = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._pre_stop_handler = None
        self._pre_stop_timeout = None
        self._enterprise_project_id = None
        self._type = None
        self._log_config = None
        self._network_controller = None
        self._is_stateful_function = None
        self._enable_dynamic_memory = None
        self._enable_lts_log = None
        self._lts_custom_tag = None
        self._user_data_encrypt_kms_key_id = None
        self._code_encrypt_kms_key_id = None
        self._domain_names = None
        self._tags = None
        self.discriminator = None

        self.func_name = func_name
        self.package = package
        self.runtime = runtime
        self.timeout = timeout
        self.handler = handler
        if depend_version_list is not None:
            self.depend_version_list = depend_version_list
        if func_vpc is not None:
            self.func_vpc = func_vpc
        self.memory_size = memory_size
        if gpu_memory is not None:
            self.gpu_memory = gpu_memory
        if gpu_type is not None:
            self.gpu_type = gpu_type
        if code_type is not None:
            self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        if custom_image is not None:
            self.custom_image = custom_image
        if user_data is not None:
            self.user_data = user_data
        if encrypted_user_data is not None:
            self.encrypted_user_data = encrypted_user_data
        if xrole is not None:
            self.xrole = xrole
        if app_xrole is not None:
            self.app_xrole = app_xrole
        if description is not None:
            self.description = description
        if func_code is not None:
            self.func_code = func_code
        if mount_config is not None:
            self.mount_config = mount_config
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
        if type is not None:
            self.type = type
        if log_config is not None:
            self.log_config = log_config
        if network_controller is not None:
            self.network_controller = network_controller
        if is_stateful_function is not None:
            self.is_stateful_function = is_stateful_function
        if enable_dynamic_memory is not None:
            self.enable_dynamic_memory = enable_dynamic_memory
        if enable_lts_log is not None:
            self.enable_lts_log = enable_lts_log
        if lts_custom_tag is not None:
            self.lts_custom_tag = lts_custom_tag
        if user_data_encrypt_kms_key_id is not None:
            self.user_data_encrypt_kms_key_id = user_data_encrypt_kms_key_id
        if code_encrypt_kms_key_id is not None:
            self.code_encrypt_kms_key_id = code_encrypt_kms_key_id
        if domain_names is not None:
            self.domain_names = domain_names
        if tags is not None:
            self.tags = tags

    @property
    def func_name(self):
        r"""Gets the func_name of this CreateFunctionRequestBody.

        函数名称。

        :return: The func_name of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this CreateFunctionRequestBody.

        函数名称。

        :param func_name: The func_name of this CreateFunctionRequestBody.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def package(self):
        r"""Gets the package of this CreateFunctionRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this CreateFunctionRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this CreateFunctionRequestBody.
        :type package: str
        """
        self._package = package

    @property
    def runtime(self):
        r"""Gets the runtime of this CreateFunctionRequestBody.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this CreateFunctionRequestBody.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this CreateFunctionRequestBody.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        r"""Gets the timeout of this CreateFunctionRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :return: The timeout of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this CreateFunctionRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :param timeout: The timeout of this CreateFunctionRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        r"""Gets the handler of this CreateFunctionRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ”；自定义镜像函数handler为“-” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this CreateFunctionRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ”；自定义镜像函数handler为“-” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this CreateFunctionRequestBody.
        :type handler: str
        """
        self._handler = handler

    @property
    def depend_version_list(self):
        r"""Gets the depend_version_list of this CreateFunctionRequestBody.

        依赖版本id列表

        :return: The depend_version_list of this CreateFunctionRequestBody.
        :rtype: list[str]
        """
        return self._depend_version_list

    @depend_version_list.setter
    def depend_version_list(self, depend_version_list):
        r"""Sets the depend_version_list of this CreateFunctionRequestBody.

        依赖版本id列表

        :param depend_version_list: The depend_version_list of this CreateFunctionRequestBody.
        :type depend_version_list: list[str]
        """
        self._depend_version_list = depend_version_list

    @property
    def func_vpc(self):
        r"""Gets the func_vpc of this CreateFunctionRequestBody.

        :return: The func_vpc of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        r"""Sets the func_vpc of this CreateFunctionRequestBody.

        :param func_vpc: The func_vpc of this CreateFunctionRequestBody.
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        self._func_vpc = func_vpc

    @property
    def memory_size(self):
        r"""Gets the memory_size of this CreateFunctionRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        r"""Sets the memory_size of this CreateFunctionRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this CreateFunctionRequestBody.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def gpu_memory(self):
        r"""Gets the gpu_memory of this CreateFunctionRequestBody.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :return: The gpu_memory of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        r"""Sets the gpu_memory of this CreateFunctionRequestBody.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :param gpu_memory: The gpu_memory of this CreateFunctionRequestBody.
        :type gpu_memory: int
        """
        self._gpu_memory = gpu_memory

    @property
    def gpu_type(self):
        r"""Gets the gpu_type of this CreateFunctionRequestBody.

        显卡类型。

        :return: The gpu_type of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        r"""Sets the gpu_type of this CreateFunctionRequestBody.

        显卡类型。

        :param gpu_type: The gpu_type of this CreateFunctionRequestBody.
        :type gpu_type: str
        """
        self._gpu_type = gpu_type

    @property
    def code_type(self):
        r"""Gets the code_type of this CreateFunctionRequestBody.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。 创建自定义镜像函数此参数非必填，其他类型函数此参数必填。

        :return: The code_type of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        r"""Sets the code_type of this CreateFunctionRequestBody.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。 创建自定义镜像函数此参数非必填，其他类型函数此参数必填。

        :param code_type: The code_type of this CreateFunctionRequestBody.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        r"""Gets the code_url of this CreateFunctionRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this CreateFunctionRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this CreateFunctionRequestBody.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        r"""Gets the code_filename of this CreateFunctionRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，CodeType为其他值时不需要提供。

        :return: The code_filename of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        r"""Sets the code_filename of this CreateFunctionRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，CodeType为其他值时不需要提供。

        :param code_filename: The code_filename of this CreateFunctionRequestBody.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def custom_image(self):
        r"""Gets the custom_image of this CreateFunctionRequestBody.

        :return: The custom_image of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        return self._custom_image

    @custom_image.setter
    def custom_image(self, custom_image):
        r"""Sets the custom_image of this CreateFunctionRequestBody.

        :param custom_image: The custom_image of this CreateFunctionRequestBody.
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        self._custom_image = custom_image

    @property
    def user_data(self):
        r"""Gets the user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this CreateFunctionRequestBody.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def encrypted_user_data(self):
        r"""Gets the encrypted_user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息，用于需要加密的配置。举例：如配置加密密码，可以设置自定义参数：password={1234}，最多定义20个，总长度不超过4KB。

        :return: The encrypted_user_data of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._encrypted_user_data

    @encrypted_user_data.setter
    def encrypted_user_data(self, encrypted_user_data):
        r"""Sets the encrypted_user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息，用于需要加密的配置。举例：如配置加密密码，可以设置自定义参数：password={1234}，最多定义20个，总长度不超过4KB。

        :param encrypted_user_data: The encrypted_user_data of this CreateFunctionRequestBody.
        :type encrypted_user_data: str
        """
        self._encrypted_user_data = encrypted_user_data

    @property
    def xrole(self):
        r"""Gets the xrole of this CreateFunctionRequestBody.

        函数配置委托。需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。配置后用户可以通过函数执行入口方法中的context参数获取具有委托中权限的token、ak、sk，用于访问其他云服务。如果用户函数不访问任何云服务，则不用提供委托名称。

        :return: The xrole of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        r"""Sets the xrole of this CreateFunctionRequestBody.

        函数配置委托。需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。配置后用户可以通过函数执行入口方法中的context参数获取具有委托中权限的token、ak、sk，用于访问其他云服务。如果用户函数不访问任何云服务，则不用提供委托名称。

        :param xrole: The xrole of this CreateFunctionRequestBody.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        r"""Gets the app_xrole of this CreateFunctionRequestBody.

        函数执行委托。可为函数执行单独配置执行委托，这将减小不必要的性能损耗；不单独配置执行委托时，函数执行和函数配置将使用同一委托。

        :return: The app_xrole of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        r"""Sets the app_xrole of this CreateFunctionRequestBody.

        函数执行委托。可为函数执行单独配置执行委托，这将减小不必要的性能损耗；不单独配置执行委托时，函数执行和函数配置将使用同一委托。

        :param app_xrole: The app_xrole of this CreateFunctionRequestBody.
        :type app_xrole: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        r"""Gets the description of this CreateFunctionRequestBody.

        函数描述。

        :return: The description of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFunctionRequestBody.

        函数描述。

        :param description: The description of this CreateFunctionRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def func_code(self):
        r"""Gets the func_code of this CreateFunctionRequestBody.

        :return: The func_code of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        return self._func_code

    @func_code.setter
    def func_code(self, func_code):
        r"""Sets the func_code of this CreateFunctionRequestBody.

        :param func_code: The func_code of this CreateFunctionRequestBody.
        :type func_code: :class:`huaweicloudsdkfunctiongraph.v2.FuncCode`
        """
        self._func_code = func_code

    @property
    def mount_config(self):
        r"""Gets the mount_config of this CreateFunctionRequestBody.

        :return: The mount_config of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        return self._mount_config

    @mount_config.setter
    def mount_config(self, mount_config):
        r"""Sets the mount_config of this CreateFunctionRequestBody.

        :param mount_config: The mount_config of this CreateFunctionRequestBody.
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        self._mount_config = mount_config

    @property
    def initializer_handler(self):
        r"""Gets the initializer_handler of this CreateFunctionRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        r"""Sets the initializer_handler of this CreateFunctionRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this CreateFunctionRequestBody.
        :type initializer_handler: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        r"""Gets the initializer_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :return: The initializer_timeout of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        r"""Sets the initializer_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :param initializer_timeout: The initializer_timeout of this CreateFunctionRequestBody.
        :type initializer_timeout: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def pre_stop_handler(self):
        r"""Gets the pre_stop_handler of this CreateFunctionRequestBody.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :return: The pre_stop_handler of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._pre_stop_handler

    @pre_stop_handler.setter
    def pre_stop_handler(self, pre_stop_handler):
        r"""Sets the pre_stop_handler of this CreateFunctionRequestBody.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :param pre_stop_handler: The pre_stop_handler of this CreateFunctionRequestBody.
        :type pre_stop_handler: str
        """
        self._pre_stop_handler = pre_stop_handler

    @property
    def pre_stop_timeout(self):
        r"""Gets the pre_stop_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :return: The pre_stop_timeout of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._pre_stop_timeout

    @pre_stop_timeout.setter
    def pre_stop_timeout(self, pre_stop_timeout):
        r"""Sets the pre_stop_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :param pre_stop_timeout: The pre_stop_timeout of this CreateFunctionRequestBody.
        :type pre_stop_timeout: int
        """
        self._pre_stop_timeout = pre_stop_timeout

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateFunctionRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateFunctionRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateFunctionRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this CreateFunctionRequestBody.

        函数版本；部分局点只支持v1函数，缺省值则为v1

        :return: The type of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFunctionRequestBody.

        函数版本；部分局点只支持v1函数，缺省值则为v1

        :param type: The type of this CreateFunctionRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def log_config(self):
        r"""Gets the log_config of this CreateFunctionRequestBody.

        :return: The log_config of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this CreateFunctionRequestBody.

        :param log_config: The log_config of this CreateFunctionRequestBody.
        :type log_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        """
        self._log_config = log_config

    @property
    def network_controller(self):
        r"""Gets the network_controller of this CreateFunctionRequestBody.

        :return: The network_controller of this CreateFunctionRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        return self._network_controller

    @network_controller.setter
    def network_controller(self, network_controller):
        r"""Sets the network_controller of this CreateFunctionRequestBody.

        :param network_controller: The network_controller of this CreateFunctionRequestBody.
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        self._network_controller = network_controller

    @property
    def is_stateful_function(self):
        r"""Gets the is_stateful_function of this CreateFunctionRequestBody.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :return: The is_stateful_function of this CreateFunctionRequestBody.
        :rtype: bool
        """
        return self._is_stateful_function

    @is_stateful_function.setter
    def is_stateful_function(self, is_stateful_function):
        r"""Sets the is_stateful_function of this CreateFunctionRequestBody.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :param is_stateful_function: The is_stateful_function of this CreateFunctionRequestBody.
        :type is_stateful_function: bool
        """
        self._is_stateful_function = is_stateful_function

    @property
    def enable_dynamic_memory(self):
        r"""Gets the enable_dynamic_memory of this CreateFunctionRequestBody.

        是否启动动态内存配置

        :return: The enable_dynamic_memory of this CreateFunctionRequestBody.
        :rtype: bool
        """
        return self._enable_dynamic_memory

    @enable_dynamic_memory.setter
    def enable_dynamic_memory(self, enable_dynamic_memory):
        r"""Sets the enable_dynamic_memory of this CreateFunctionRequestBody.

        是否启动动态内存配置

        :param enable_dynamic_memory: The enable_dynamic_memory of this CreateFunctionRequestBody.
        :type enable_dynamic_memory: bool
        """
        self._enable_dynamic_memory = enable_dynamic_memory

    @property
    def enable_lts_log(self):
        r"""Gets the enable_lts_log of this CreateFunctionRequestBody.

        是否开启日志，缺省值为false。创建函数时，若此开关为true，且未传入log_config，则由FunctionGraph自动创建日志组日志流。

        :return: The enable_lts_log of this CreateFunctionRequestBody.
        :rtype: bool
        """
        return self._enable_lts_log

    @enable_lts_log.setter
    def enable_lts_log(self, enable_lts_log):
        r"""Sets the enable_lts_log of this CreateFunctionRequestBody.

        是否开启日志，缺省值为false。创建函数时，若此开关为true，且未传入log_config，则由FunctionGraph自动创建日志组日志流。

        :param enable_lts_log: The enable_lts_log of this CreateFunctionRequestBody.
        :type enable_lts_log: bool
        """
        self._enable_lts_log = enable_lts_log

    @property
    def lts_custom_tag(self):
        r"""Gets the lts_custom_tag of this CreateFunctionRequestBody.

        自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。

        :return: The lts_custom_tag of this CreateFunctionRequestBody.
        :rtype: dict(str, str)
        """
        return self._lts_custom_tag

    @lts_custom_tag.setter
    def lts_custom_tag(self, lts_custom_tag):
        r"""Sets the lts_custom_tag of this CreateFunctionRequestBody.

        自定义日志标签。函数执行时，可以按照自定义标签配置上报标签到云日志服务(LTS)，用户可以通过标签对日志进行过滤筛选。

        :param lts_custom_tag: The lts_custom_tag of this CreateFunctionRequestBody.
        :type lts_custom_tag: dict(str, str)
        """
        self._lts_custom_tag = lts_custom_tag

    @property
    def user_data_encrypt_kms_key_id(self):
        r"""Gets the user_data_encrypt_kms_key_id of this CreateFunctionRequestBody.

        用于环境变量加密的kms主秘钥ID。

        :return: The user_data_encrypt_kms_key_id of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._user_data_encrypt_kms_key_id

    @user_data_encrypt_kms_key_id.setter
    def user_data_encrypt_kms_key_id(self, user_data_encrypt_kms_key_id):
        r"""Sets the user_data_encrypt_kms_key_id of this CreateFunctionRequestBody.

        用于环境变量加密的kms主秘钥ID。

        :param user_data_encrypt_kms_key_id: The user_data_encrypt_kms_key_id of this CreateFunctionRequestBody.
        :type user_data_encrypt_kms_key_id: str
        """
        self._user_data_encrypt_kms_key_id = user_data_encrypt_kms_key_id

    @property
    def code_encrypt_kms_key_id(self):
        r"""Gets the code_encrypt_kms_key_id of this CreateFunctionRequestBody.

        用于用户代码加密的kms主秘钥ID。

        :return: The code_encrypt_kms_key_id of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_encrypt_kms_key_id

    @code_encrypt_kms_key_id.setter
    def code_encrypt_kms_key_id(self, code_encrypt_kms_key_id):
        r"""Sets the code_encrypt_kms_key_id of this CreateFunctionRequestBody.

        用于用户代码加密的kms主秘钥ID。

        :param code_encrypt_kms_key_id: The code_encrypt_kms_key_id of this CreateFunctionRequestBody.
        :type code_encrypt_kms_key_id: str
        """
        self._code_encrypt_kms_key_id = code_encrypt_kms_key_id

    @property
    def domain_names(self):
        r"""Gets the domain_names of this CreateFunctionRequestBody.

        vpc中配置的内网域名。在函数配置调用DNS服务的接口解析内网域名时，则函数必须具备读取DNS资源权限的委托。

        :return: The domain_names of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        r"""Sets the domain_names of this CreateFunctionRequestBody.

        vpc中配置的内网域名。在函数配置调用DNS服务的接口解析内网域名时，则函数必须具备读取DNS资源权限的委托。

        :param domain_names: The domain_names of this CreateFunctionRequestBody.
        :type domain_names: str
        """
        self._domain_names = domain_names

    @property
    def tags(self):
        r"""Gets the tags of this CreateFunctionRequestBody.

        函数标签。

        :return: The tags of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateFunctionRequestBody.

        函数标签。

        :param tags: The tags of this CreateFunctionRequestBody.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, CreateFunctionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
