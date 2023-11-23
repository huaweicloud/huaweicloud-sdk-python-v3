# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionConfigRequestBody:

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
        'runtime': 'str',
        'timeout': 'int',
        'handler': 'str',
        'memory_size': 'int',
        'gpu_memory': 'int',
        'user_data': 'str',
        'encrypted_user_data': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'func_vpc': 'FuncVpc',
        'mount_config': 'MountConfig',
        'strategy_config': 'StrategyConfig',
        'custom_image': 'CustomImage',
        'extend_config': 'str',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'pre_stop_handler': 'str',
        'pre_stop_timeout': 'int',
        'ephemeral_storage': 'int',
        'enterprise_project_id': 'str',
        'log_config': 'FuncLogConfig',
        'network_controller': 'NetworkControlConfig',
        'is_stateful_function': 'bool',
        'enable_dynamic_memory': 'bool',
        'enable_auth_in_header': 'bool',
        'domain_names': 'str',
        'restore_hook_handler': 'str',
        'restore_hook_timeout': 'int'
    }

    attribute_map = {
        'func_name': 'func_name',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'handler': 'handler',
        'memory_size': 'memory_size',
        'gpu_memory': 'gpu_memory',
        'user_data': 'user_data',
        'encrypted_user_data': 'encrypted_user_data',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'func_vpc': 'func_vpc',
        'mount_config': 'mount_config',
        'strategy_config': 'strategy_config',
        'custom_image': 'custom_image',
        'extend_config': 'extend_config',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'pre_stop_handler': 'pre_stop_handler',
        'pre_stop_timeout': 'pre_stop_timeout',
        'ephemeral_storage': 'ephemeral_storage',
        'enterprise_project_id': 'enterprise_project_id',
        'log_config': 'log_config',
        'network_controller': 'network_controller',
        'is_stateful_function': 'is_stateful_function',
        'enable_dynamic_memory': 'enable_dynamic_memory',
        'enable_auth_in_header': 'enable_auth_in_header',
        'domain_names': 'domain_names',
        'restore_hook_handler': 'restore_hook_handler',
        'restore_hook_timeout': 'restore_hook_timeout'
    }

    def __init__(self, func_name=None, runtime=None, timeout=None, handler=None, memory_size=None, gpu_memory=None, user_data=None, encrypted_user_data=None, xrole=None, app_xrole=None, description=None, func_vpc=None, mount_config=None, strategy_config=None, custom_image=None, extend_config=None, initializer_handler=None, initializer_timeout=None, pre_stop_handler=None, pre_stop_timeout=None, ephemeral_storage=None, enterprise_project_id=None, log_config=None, network_controller=None, is_stateful_function=None, enable_dynamic_memory=None, enable_auth_in_header=None, domain_names=None, restore_hook_handler=None, restore_hook_timeout=None):
        """UpdateFunctionConfigRequestBody

        The model defined in huaweicloud sdk

        :param func_name: 函数名称。
        :type func_name: str
        :param runtime: FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。
        :type runtime: str
        :param timeout: 函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询客服进行配置
        :type timeout: int
        :param handler: 函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。
        :type handler: str
        :param memory_size: 函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。
        :type memory_size: int
        :param gpu_memory: 函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。
        :type gpu_memory: int
        :param user_data: 用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host&#x3D;{host_ip}，最多定义20个，总长度不超过4KB。
        :type user_data: str
        :param encrypted_user_data: 用户自定义的name/value信息，用于需要加密的配置。
        :type encrypted_user_data: str
        :param xrole: 函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type xrole: str
        :param app_xrole: 函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type app_xrole: str
        :param description: 函数描述。
        :type description: str
        :param func_vpc: 
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        :param mount_config: 
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        :param strategy_config: 
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        :param custom_image: 
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        :param extend_config: 函数扩展配置。
        :type extend_config: str
        :param initializer_handler: 函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。
        :type initializer_handler: str
        :param initializer_timeout: 初始化超时时间，超时函数将被强行停止，范围1～300秒。
        :type initializer_timeout: int
        :param pre_stop_handler: 函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。
        :type pre_stop_handler: str
        :param pre_stop_timeout: 初始化超时时间，超时函数将被强行停止，范围1～90秒。
        :type pre_stop_timeout: int
        :param ephemeral_storage: 临时存储大小, 默认512M, 支持配置10G。
        :type ephemeral_storage: int
        :param enterprise_project_id: 企业项目ID，在企业用户创建函数时必填。
        :type enterprise_project_id: str
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        :param network_controller: 
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        :param is_stateful_function: 是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持
        :type is_stateful_function: bool
        :param enable_dynamic_memory: 是否启动动态内存配置
        :type enable_dynamic_memory: bool
        :param enable_auth_in_header: 是否允许在请求头中添加鉴权信息
        :type enable_auth_in_header: bool
        :param domain_names: 内网域名配置。
        :type domain_names: str
        :param restore_hook_handler: 函数快照式冷启动Restore Hook入口，仅支持Java，规则：xx.xx，必须包含“. ”。如：com.xxx.demo.Test.restoreHook
        :type restore_hook_handler: str
        :param restore_hook_timeout: 快照冷启动Restore Hook的超时时间，超时函数将被强行停止，范围1～300秒。
        :type restore_hook_timeout: int
        """
        
        

        self._func_name = None
        self._runtime = None
        self._timeout = None
        self._handler = None
        self._memory_size = None
        self._gpu_memory = None
        self._user_data = None
        self._encrypted_user_data = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._func_vpc = None
        self._mount_config = None
        self._strategy_config = None
        self._custom_image = None
        self._extend_config = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._pre_stop_handler = None
        self._pre_stop_timeout = None
        self._ephemeral_storage = None
        self._enterprise_project_id = None
        self._log_config = None
        self._network_controller = None
        self._is_stateful_function = None
        self._enable_dynamic_memory = None
        self._enable_auth_in_header = None
        self._domain_names = None
        self._restore_hook_handler = None
        self._restore_hook_timeout = None
        self.discriminator = None

        self.func_name = func_name
        self.runtime = runtime
        self.timeout = timeout
        self.handler = handler
        self.memory_size = memory_size
        if gpu_memory is not None:
            self.gpu_memory = gpu_memory
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
        if func_vpc is not None:
            self.func_vpc = func_vpc
        if mount_config is not None:
            self.mount_config = mount_config
        if strategy_config is not None:
            self.strategy_config = strategy_config
        if custom_image is not None:
            self.custom_image = custom_image
        if extend_config is not None:
            self.extend_config = extend_config
        if initializer_handler is not None:
            self.initializer_handler = initializer_handler
        if initializer_timeout is not None:
            self.initializer_timeout = initializer_timeout
        if pre_stop_handler is not None:
            self.pre_stop_handler = pre_stop_handler
        if pre_stop_timeout is not None:
            self.pre_stop_timeout = pre_stop_timeout
        if ephemeral_storage is not None:
            self.ephemeral_storage = ephemeral_storage
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if log_config is not None:
            self.log_config = log_config
        if network_controller is not None:
            self.network_controller = network_controller
        if is_stateful_function is not None:
            self.is_stateful_function = is_stateful_function
        if enable_dynamic_memory is not None:
            self.enable_dynamic_memory = enable_dynamic_memory
        if enable_auth_in_header is not None:
            self.enable_auth_in_header = enable_auth_in_header
        if domain_names is not None:
            self.domain_names = domain_names
        if restore_hook_handler is not None:
            self.restore_hook_handler = restore_hook_handler
        if restore_hook_timeout is not None:
            self.restore_hook_timeout = restore_hook_timeout

    @property
    def func_name(self):
        """Gets the func_name of this UpdateFunctionConfigRequestBody.

        函数名称。

        :return: The func_name of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this UpdateFunctionConfigRequestBody.

        函数名称。

        :param func_name: The func_name of this UpdateFunctionConfigRequestBody.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def runtime(self):
        """Gets the runtime of this UpdateFunctionConfigRequestBody.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。

        :return: The runtime of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this UpdateFunctionConfigRequestBody.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。

        :param runtime: The runtime of this UpdateFunctionConfigRequestBody.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this UpdateFunctionConfigRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询客服进行配置

        :return: The timeout of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateFunctionConfigRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询客服进行配置

        :param timeout: The timeout of this UpdateFunctionConfigRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        """Gets the handler of this UpdateFunctionConfigRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this UpdateFunctionConfigRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this UpdateFunctionConfigRequestBody.
        :type handler: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        """Gets the memory_size of this UpdateFunctionConfigRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this UpdateFunctionConfigRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this UpdateFunctionConfigRequestBody.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def gpu_memory(self):
        """Gets the gpu_memory of this UpdateFunctionConfigRequestBody.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :return: The gpu_memory of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        """Sets the gpu_memory of this UpdateFunctionConfigRequestBody.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :param gpu_memory: The gpu_memory of this UpdateFunctionConfigRequestBody.
        :type gpu_memory: int
        """
        self._gpu_memory = gpu_memory

    @property
    def user_data(self):
        """Gets the user_data of this UpdateFunctionConfigRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this UpdateFunctionConfigRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this UpdateFunctionConfigRequestBody.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def encrypted_user_data(self):
        """Gets the encrypted_user_data of this UpdateFunctionConfigRequestBody.

        用户自定义的name/value信息，用于需要加密的配置。

        :return: The encrypted_user_data of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._encrypted_user_data

    @encrypted_user_data.setter
    def encrypted_user_data(self, encrypted_user_data):
        """Sets the encrypted_user_data of this UpdateFunctionConfigRequestBody.

        用户自定义的name/value信息，用于需要加密的配置。

        :param encrypted_user_data: The encrypted_user_data of this UpdateFunctionConfigRequestBody.
        :type encrypted_user_data: str
        """
        self._encrypted_user_data = encrypted_user_data

    @property
    def xrole(self):
        """Gets the xrole of this UpdateFunctionConfigRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        """Sets the xrole of this UpdateFunctionConfigRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this UpdateFunctionConfigRequestBody.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        """Gets the app_xrole of this UpdateFunctionConfigRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        """Sets the app_xrole of this UpdateFunctionConfigRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this UpdateFunctionConfigRequestBody.
        :type app_xrole: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        """Gets the description of this UpdateFunctionConfigRequestBody.

        函数描述。

        :return: The description of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFunctionConfigRequestBody.

        函数描述。

        :param description: The description of this UpdateFunctionConfigRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def func_vpc(self):
        """Gets the func_vpc of this UpdateFunctionConfigRequestBody.

        :return: The func_vpc of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        """Sets the func_vpc of this UpdateFunctionConfigRequestBody.

        :param func_vpc: The func_vpc of this UpdateFunctionConfigRequestBody.
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        self._func_vpc = func_vpc

    @property
    def mount_config(self):
        """Gets the mount_config of this UpdateFunctionConfigRequestBody.

        :return: The mount_config of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        return self._mount_config

    @mount_config.setter
    def mount_config(self, mount_config):
        """Sets the mount_config of this UpdateFunctionConfigRequestBody.

        :param mount_config: The mount_config of this UpdateFunctionConfigRequestBody.
        :type mount_config: :class:`huaweicloudsdkfunctiongraph.v2.MountConfig`
        """
        self._mount_config = mount_config

    @property
    def strategy_config(self):
        """Gets the strategy_config of this UpdateFunctionConfigRequestBody.

        :return: The strategy_config of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        """Sets the strategy_config of this UpdateFunctionConfigRequestBody.

        :param strategy_config: The strategy_config of this UpdateFunctionConfigRequestBody.
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        self._strategy_config = strategy_config

    @property
    def custom_image(self):
        """Gets the custom_image of this UpdateFunctionConfigRequestBody.

        :return: The custom_image of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        return self._custom_image

    @custom_image.setter
    def custom_image(self, custom_image):
        """Sets the custom_image of this UpdateFunctionConfigRequestBody.

        :param custom_image: The custom_image of this UpdateFunctionConfigRequestBody.
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        self._custom_image = custom_image

    @property
    def extend_config(self):
        """Gets the extend_config of this UpdateFunctionConfigRequestBody.

        函数扩展配置。

        :return: The extend_config of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._extend_config

    @extend_config.setter
    def extend_config(self, extend_config):
        """Sets the extend_config of this UpdateFunctionConfigRequestBody.

        函数扩展配置。

        :param extend_config: The extend_config of this UpdateFunctionConfigRequestBody.
        :type extend_config: str
        """
        self._extend_config = extend_config

    @property
    def initializer_handler(self):
        """Gets the initializer_handler of this UpdateFunctionConfigRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        """Sets the initializer_handler of this UpdateFunctionConfigRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this UpdateFunctionConfigRequestBody.
        :type initializer_handler: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        """Gets the initializer_timeout of this UpdateFunctionConfigRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :return: The initializer_timeout of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        """Sets the initializer_timeout of this UpdateFunctionConfigRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :param initializer_timeout: The initializer_timeout of this UpdateFunctionConfigRequestBody.
        :type initializer_timeout: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def pre_stop_handler(self):
        """Gets the pre_stop_handler of this UpdateFunctionConfigRequestBody.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :return: The pre_stop_handler of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._pre_stop_handler

    @pre_stop_handler.setter
    def pre_stop_handler(self, pre_stop_handler):
        """Sets the pre_stop_handler of this UpdateFunctionConfigRequestBody.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :param pre_stop_handler: The pre_stop_handler of this UpdateFunctionConfigRequestBody.
        :type pre_stop_handler: str
        """
        self._pre_stop_handler = pre_stop_handler

    @property
    def pre_stop_timeout(self):
        """Gets the pre_stop_timeout of this UpdateFunctionConfigRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :return: The pre_stop_timeout of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._pre_stop_timeout

    @pre_stop_timeout.setter
    def pre_stop_timeout(self, pre_stop_timeout):
        """Sets the pre_stop_timeout of this UpdateFunctionConfigRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :param pre_stop_timeout: The pre_stop_timeout of this UpdateFunctionConfigRequestBody.
        :type pre_stop_timeout: int
        """
        self._pre_stop_timeout = pre_stop_timeout

    @property
    def ephemeral_storage(self):
        """Gets the ephemeral_storage of this UpdateFunctionConfigRequestBody.

        临时存储大小, 默认512M, 支持配置10G。

        :return: The ephemeral_storage of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._ephemeral_storage

    @ephemeral_storage.setter
    def ephemeral_storage(self, ephemeral_storage):
        """Sets the ephemeral_storage of this UpdateFunctionConfigRequestBody.

        临时存储大小, 默认512M, 支持配置10G。

        :param ephemeral_storage: The ephemeral_storage of this UpdateFunctionConfigRequestBody.
        :type ephemeral_storage: int
        """
        self._ephemeral_storage = ephemeral_storage

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateFunctionConfigRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateFunctionConfigRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this UpdateFunctionConfigRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def log_config(self):
        """Gets the log_config of this UpdateFunctionConfigRequestBody.

        :return: The log_config of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        """Sets the log_config of this UpdateFunctionConfigRequestBody.

        :param log_config: The log_config of this UpdateFunctionConfigRequestBody.
        :type log_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncLogConfig`
        """
        self._log_config = log_config

    @property
    def network_controller(self):
        """Gets the network_controller of this UpdateFunctionConfigRequestBody.

        :return: The network_controller of this UpdateFunctionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        return self._network_controller

    @network_controller.setter
    def network_controller(self, network_controller):
        """Sets the network_controller of this UpdateFunctionConfigRequestBody.

        :param network_controller: The network_controller of this UpdateFunctionConfigRequestBody.
        :type network_controller: :class:`huaweicloudsdkfunctiongraph.v2.NetworkControlConfig`
        """
        self._network_controller = network_controller

    @property
    def is_stateful_function(self):
        """Gets the is_stateful_function of this UpdateFunctionConfigRequestBody.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :return: The is_stateful_function of this UpdateFunctionConfigRequestBody.
        :rtype: bool
        """
        return self._is_stateful_function

    @is_stateful_function.setter
    def is_stateful_function(self, is_stateful_function):
        """Sets the is_stateful_function of this UpdateFunctionConfigRequestBody.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :param is_stateful_function: The is_stateful_function of this UpdateFunctionConfigRequestBody.
        :type is_stateful_function: bool
        """
        self._is_stateful_function = is_stateful_function

    @property
    def enable_dynamic_memory(self):
        """Gets the enable_dynamic_memory of this UpdateFunctionConfigRequestBody.

        是否启动动态内存配置

        :return: The enable_dynamic_memory of this UpdateFunctionConfigRequestBody.
        :rtype: bool
        """
        return self._enable_dynamic_memory

    @enable_dynamic_memory.setter
    def enable_dynamic_memory(self, enable_dynamic_memory):
        """Sets the enable_dynamic_memory of this UpdateFunctionConfigRequestBody.

        是否启动动态内存配置

        :param enable_dynamic_memory: The enable_dynamic_memory of this UpdateFunctionConfigRequestBody.
        :type enable_dynamic_memory: bool
        """
        self._enable_dynamic_memory = enable_dynamic_memory

    @property
    def enable_auth_in_header(self):
        """Gets the enable_auth_in_header of this UpdateFunctionConfigRequestBody.

        是否允许在请求头中添加鉴权信息

        :return: The enable_auth_in_header of this UpdateFunctionConfigRequestBody.
        :rtype: bool
        """
        return self._enable_auth_in_header

    @enable_auth_in_header.setter
    def enable_auth_in_header(self, enable_auth_in_header):
        """Sets the enable_auth_in_header of this UpdateFunctionConfigRequestBody.

        是否允许在请求头中添加鉴权信息

        :param enable_auth_in_header: The enable_auth_in_header of this UpdateFunctionConfigRequestBody.
        :type enable_auth_in_header: bool
        """
        self._enable_auth_in_header = enable_auth_in_header

    @property
    def domain_names(self):
        """Gets the domain_names of this UpdateFunctionConfigRequestBody.

        内网域名配置。

        :return: The domain_names of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        """Sets the domain_names of this UpdateFunctionConfigRequestBody.

        内网域名配置。

        :param domain_names: The domain_names of this UpdateFunctionConfigRequestBody.
        :type domain_names: str
        """
        self._domain_names = domain_names

    @property
    def restore_hook_handler(self):
        """Gets the restore_hook_handler of this UpdateFunctionConfigRequestBody.

        函数快照式冷启动Restore Hook入口，仅支持Java，规则：xx.xx，必须包含“. ”。如：com.xxx.demo.Test.restoreHook

        :return: The restore_hook_handler of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._restore_hook_handler

    @restore_hook_handler.setter
    def restore_hook_handler(self, restore_hook_handler):
        """Sets the restore_hook_handler of this UpdateFunctionConfigRequestBody.

        函数快照式冷启动Restore Hook入口，仅支持Java，规则：xx.xx，必须包含“. ”。如：com.xxx.demo.Test.restoreHook

        :param restore_hook_handler: The restore_hook_handler of this UpdateFunctionConfigRequestBody.
        :type restore_hook_handler: str
        """
        self._restore_hook_handler = restore_hook_handler

    @property
    def restore_hook_timeout(self):
        """Gets the restore_hook_timeout of this UpdateFunctionConfigRequestBody.

        快照冷启动Restore Hook的超时时间，超时函数将被强行停止，范围1～300秒。

        :return: The restore_hook_timeout of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._restore_hook_timeout

    @restore_hook_timeout.setter
    def restore_hook_timeout(self, restore_hook_timeout):
        """Sets the restore_hook_timeout of this UpdateFunctionConfigRequestBody.

        快照冷启动Restore Hook的超时时间，超时函数将被强行停止，范围1～300秒。

        :param restore_hook_timeout: The restore_hook_timeout of this UpdateFunctionConfigRequestBody.
        :type restore_hook_timeout: int
        """
        self._restore_hook_timeout = restore_hook_timeout

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
        if not isinstance(other, UpdateFunctionConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
