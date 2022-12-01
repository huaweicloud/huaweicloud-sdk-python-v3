# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionVersionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
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
        'cpu': 'int',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'code_size': 'int',
        'user_data': 'str',
        'encrypted_user_data': 'str',
        'digest': 'str',
        'version': 'str',
        'image_name': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'last_modified': 'datetime',
        'func_vpc_id': 'str',
        'concurrency': 'int',
        'concurrent_num': 'int',
        'strategy_config': 'StrategyConfig',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'long_time': 'bool',
        'function_async_config': 'FunctionAsyncConfig',
        'type': 'str',
        'enable_cloud_debug': 'str',
        'enable_dynamic_memory': 'bool',
        'enterprise_project_id': 'str',
        'is_stateful_function': 'bool',
        'enable_auth_in_header': 'bool',
        'custom_image': 'CustomImage',
        'reserved_instance_idle_mode': 'bool'
    }

    attribute_map = {
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
        'cpu': 'cpu',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'code_size': 'code_size',
        'user_data': 'user_data',
        'encrypted_user_data': 'encrypted_user_data',
        'digest': 'digest',
        'version': 'version',
        'image_name': 'image_name',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'last_modified': 'last_modified',
        'func_vpc_id': 'func_vpc_id',
        'concurrency': 'concurrency',
        'concurrent_num': 'concurrent_num',
        'strategy_config': 'strategy_config',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'long_time': 'long_time',
        'function_async_config': 'function_async_config',
        'type': 'type',
        'enable_cloud_debug': 'enable_cloud_debug',
        'enable_dynamic_memory': 'enable_dynamic_memory',
        'enterprise_project_id': 'enterprise_project_id',
        'is_stateful_function': 'is_stateful_function',
        'enable_auth_in_header': 'enable_auth_in_header',
        'custom_image': 'custom_image',
        'reserved_instance_idle_mode': 'reserved_instance_idle_mode'
    }

    def __init__(self, func_urn=None, func_name=None, domain_id=None, namespace=None, project_name=None, package=None, runtime=None, timeout=None, handler=None, memory_size=None, cpu=None, code_type=None, code_url=None, code_filename=None, code_size=None, user_data=None, encrypted_user_data=None, digest=None, version=None, image_name=None, xrole=None, app_xrole=None, last_modified=None, func_vpc_id=None, concurrency=None, concurrent_num=None, strategy_config=None, initializer_handler=None, initializer_timeout=None, long_time=None, function_async_config=None, type=None, enable_cloud_debug=None, enable_dynamic_memory=None, enterprise_project_id=None, is_stateful_function=None, enable_auth_in_header=None, custom_image=None, reserved_instance_idle_mode=None):
        """ListFunctionVersionResult

        The model defined in huaweicloud sdk

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
        :param runtime: FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。
        :type runtime: str
        :param timeout: 函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询华为云函数工作流服务进行配置
        :type timeout: int
        :param handler: 函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。
        :type handler: str
        :param memory_size: 函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。
        :type memory_size: int
        :param cpu: 函数占用的cpu资源。 单位为millicore（1 core&#x3D;1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。 函数占用的CPU为基础CPU：200 millicores，再加上内存按比例占用的CPU，计算方法：内存/128 *100 + 200。
        :type cpu: int
        :param code_type: 函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。
        :type code_type: str
        :param code_url: 当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。
        :type code_url: str
        :param code_filename: 函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。
        :type code_filename: str
        :param code_size: 函数大小，单位：字节。
        :type code_size: int
        :param user_data: 用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host&#x3D;{host_ip}，最多定义20个，总长度不超过4KB。
        :type user_data: str
        :param encrypted_user_data: 用户自定义的name/value信息，用于需要加密的配置。
        :type encrypted_user_data: str
        :param digest: 函数代码SHA512 hash值，用于判断函数是否变化。
        :type digest: str
        :param version: 函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。
        :type version: str
        :param image_name: 函数版本的内部标识。
        :type image_name: str
        :param xrole: 函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type xrole: str
        :param app_xrole: 函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。
        :type app_xrole: str
        :param last_modified: 函数最后一次更新时间。
        :type last_modified: datetime
        :param func_vpc_id: 用户的vpcid
        :type func_vpc_id: str
        :param concurrency: 0：函数被禁用;-1：函数被启用。
        :type concurrency: int
        :param concurrent_num: 并发实例数
        :type concurrent_num: int
        :param strategy_config: 
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        :param initializer_handler: 函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。
        :type initializer_handler: str
        :param initializer_timeout: 初始化超时时间，超时函数将被强行停止，范围1～300秒。
        :type initializer_timeout: int
        :param long_time: 是否是支持长时间运行
        :type long_time: bool
        :param function_async_config: 
        :type function_async_config: :class:`huaweicloudsdkfunctiongraph.v2.FunctionAsyncConfig`
        :param type: 函数版本
        :type type: str
        :param enable_cloud_debug: 是否启用cloud debug功能
        :type enable_cloud_debug: str
        :param enable_dynamic_memory: 是否启用动态内存功能
        :type enable_dynamic_memory: bool
        :param enterprise_project_id: 企业项目ID，在企业用户创建函数时必填。
        :type enterprise_project_id: str
        :param is_stateful_function: 是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持
        :type is_stateful_function: bool
        :param enable_auth_in_header: 是否允许在请求头中添加鉴权信息
        :type enable_auth_in_header: bool
        :param custom_image: 
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        :param reserved_instance_idle_mode: 是否开启预留实例闲置模式
        :type reserved_instance_idle_mode: bool
        """
        
        

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
        self._cpu = None
        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._code_size = None
        self._user_data = None
        self._encrypted_user_data = None
        self._digest = None
        self._version = None
        self._image_name = None
        self._xrole = None
        self._app_xrole = None
        self._last_modified = None
        self._func_vpc_id = None
        self._concurrency = None
        self._concurrent_num = None
        self._strategy_config = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._long_time = None
        self._function_async_config = None
        self._type = None
        self._enable_cloud_debug = None
        self._enable_dynamic_memory = None
        self._enterprise_project_id = None
        self._is_stateful_function = None
        self._enable_auth_in_header = None
        self._custom_image = None
        self._reserved_instance_idle_mode = None
        self.discriminator = None

        self.func_urn = func_urn
        self.func_name = func_name
        self.domain_id = domain_id
        self.namespace = namespace
        self.project_name = project_name
        self.package = package
        self.runtime = runtime
        self.timeout = timeout
        self.handler = handler
        self.memory_size = memory_size
        self.cpu = cpu
        self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        self.code_size = code_size
        if user_data is not None:
            self.user_data = user_data
        if encrypted_user_data is not None:
            self.encrypted_user_data = encrypted_user_data
        self.digest = digest
        self.version = version
        self.image_name = image_name
        if xrole is not None:
            self.xrole = xrole
        if app_xrole is not None:
            self.app_xrole = app_xrole
        self.last_modified = last_modified
        if func_vpc_id is not None:
            self.func_vpc_id = func_vpc_id
        if concurrency is not None:
            self.concurrency = concurrency
        if concurrent_num is not None:
            self.concurrent_num = concurrent_num
        if strategy_config is not None:
            self.strategy_config = strategy_config
        if initializer_handler is not None:
            self.initializer_handler = initializer_handler
        if initializer_timeout is not None:
            self.initializer_timeout = initializer_timeout
        if long_time is not None:
            self.long_time = long_time
        if function_async_config is not None:
            self.function_async_config = function_async_config
        if type is not None:
            self.type = type
        if enable_cloud_debug is not None:
            self.enable_cloud_debug = enable_cloud_debug
        if enable_dynamic_memory is not None:
            self.enable_dynamic_memory = enable_dynamic_memory
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_stateful_function is not None:
            self.is_stateful_function = is_stateful_function
        if enable_auth_in_header is not None:
            self.enable_auth_in_header = enable_auth_in_header
        if custom_image is not None:
            self.custom_image = custom_image
        if reserved_instance_idle_mode is not None:
            self.reserved_instance_idle_mode = reserved_instance_idle_mode

    @property
    def func_urn(self):
        """Gets the func_urn of this ListFunctionVersionResult.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this ListFunctionVersionResult.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this ListFunctionVersionResult.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        """Gets the func_name of this ListFunctionVersionResult.

        函数名称。

        :return: The func_name of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this ListFunctionVersionResult.

        函数名称。

        :param func_name: The func_name of this ListFunctionVersionResult.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def domain_id(self):
        """Gets the domain_id of this ListFunctionVersionResult.

        域名id。

        :return: The domain_id of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListFunctionVersionResult.

        域名id。

        :param domain_id: The domain_id of this ListFunctionVersionResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        """Gets the namespace of this ListFunctionVersionResult.

        租户的project id。

        :return: The namespace of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListFunctionVersionResult.

        租户的project id。

        :param namespace: The namespace of this ListFunctionVersionResult.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project_name(self):
        """Gets the project_name of this ListFunctionVersionResult.

        租户的project name。

        :return: The project_name of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListFunctionVersionResult.

        租户的project name。

        :param project_name: The project_name of this ListFunctionVersionResult.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def package(self):
        """Gets the package of this ListFunctionVersionResult.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this ListFunctionVersionResult.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this ListFunctionVersionResult.
        :type package: str
        """
        self._package = package

    @property
    def runtime(self):
        """Gets the runtime of this ListFunctionVersionResult.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。

        :return: The runtime of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ListFunctionVersionResult.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 http: HTTP函数。

        :param runtime: The runtime of this ListFunctionVersionResult.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this ListFunctionVersionResult.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询华为云函数工作流服务进行配置

        :return: The timeout of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ListFunctionVersionResult.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒，可以通过白名单配置延长到12小时，具体可以咨询华为云函数工作流服务进行配置

        :param timeout: The timeout of this ListFunctionVersionResult.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        """Gets the handler of this ListFunctionVersionResult.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this ListFunctionVersionResult.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this ListFunctionVersionResult.
        :type handler: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        """Gets the memory_size of this ListFunctionVersionResult.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this ListFunctionVersionResult.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this ListFunctionVersionResult.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def cpu(self):
        """Gets the cpu of this ListFunctionVersionResult.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。 函数占用的CPU为基础CPU：200 millicores，再加上内存按比例占用的CPU，计算方法：内存/128 *100 + 200。

        :return: The cpu of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ListFunctionVersionResult.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。 函数占用的CPU为基础CPU：200 millicores，再加上内存按比例占用的CPU，计算方法：内存/128 *100 + 200。

        :param cpu: The cpu of this ListFunctionVersionResult.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def code_type(self):
        """Gets the code_type of this ListFunctionVersionResult.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :return: The code_type of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this ListFunctionVersionResult.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :param code_type: The code_type of this ListFunctionVersionResult.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        """Gets the code_url of this ListFunctionVersionResult.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this ListFunctionVersionResult.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this ListFunctionVersionResult.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        """Gets the code_filename of this ListFunctionVersionResult.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        """Sets the code_filename of this ListFunctionVersionResult.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this ListFunctionVersionResult.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def code_size(self):
        """Gets the code_size of this ListFunctionVersionResult.

        函数大小，单位：字节。

        :return: The code_size of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        """Sets the code_size of this ListFunctionVersionResult.

        函数大小，单位：字节。

        :param code_size: The code_size of this ListFunctionVersionResult.
        :type code_size: int
        """
        self._code_size = code_size

    @property
    def user_data(self):
        """Gets the user_data of this ListFunctionVersionResult.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ListFunctionVersionResult.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this ListFunctionVersionResult.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def encrypted_user_data(self):
        """Gets the encrypted_user_data of this ListFunctionVersionResult.

        用户自定义的name/value信息，用于需要加密的配置。

        :return: The encrypted_user_data of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._encrypted_user_data

    @encrypted_user_data.setter
    def encrypted_user_data(self, encrypted_user_data):
        """Sets the encrypted_user_data of this ListFunctionVersionResult.

        用户自定义的name/value信息，用于需要加密的配置。

        :param encrypted_user_data: The encrypted_user_data of this ListFunctionVersionResult.
        :type encrypted_user_data: str
        """
        self._encrypted_user_data = encrypted_user_data

    @property
    def digest(self):
        """Gets the digest of this ListFunctionVersionResult.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :return: The digest of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ListFunctionVersionResult.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :param digest: The digest of this ListFunctionVersionResult.
        :type digest: str
        """
        self._digest = digest

    @property
    def version(self):
        """Gets the version of this ListFunctionVersionResult.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :return: The version of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListFunctionVersionResult.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :param version: The version of this ListFunctionVersionResult.
        :type version: str
        """
        self._version = version

    @property
    def image_name(self):
        """Gets the image_name of this ListFunctionVersionResult.

        函数版本的内部标识。

        :return: The image_name of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListFunctionVersionResult.

        函数版本的内部标识。

        :param image_name: The image_name of this ListFunctionVersionResult.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def xrole(self):
        """Gets the xrole of this ListFunctionVersionResult.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        """Sets the xrole of this ListFunctionVersionResult.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this ListFunctionVersionResult.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        """Gets the app_xrole of this ListFunctionVersionResult.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        """Sets the app_xrole of this ListFunctionVersionResult.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this ListFunctionVersionResult.
        :type app_xrole: str
        """
        self._app_xrole = app_xrole

    @property
    def last_modified(self):
        """Gets the last_modified of this ListFunctionVersionResult.

        函数最后一次更新时间。

        :return: The last_modified of this ListFunctionVersionResult.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ListFunctionVersionResult.

        函数最后一次更新时间。

        :param last_modified: The last_modified of this ListFunctionVersionResult.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def func_vpc_id(self):
        """Gets the func_vpc_id of this ListFunctionVersionResult.

        用户的vpcid

        :return: The func_vpc_id of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._func_vpc_id

    @func_vpc_id.setter
    def func_vpc_id(self, func_vpc_id):
        """Sets the func_vpc_id of this ListFunctionVersionResult.

        用户的vpcid

        :param func_vpc_id: The func_vpc_id of this ListFunctionVersionResult.
        :type func_vpc_id: str
        """
        self._func_vpc_id = func_vpc_id

    @property
    def concurrency(self):
        """Gets the concurrency of this ListFunctionVersionResult.

        0：函数被禁用;-1：函数被启用。

        :return: The concurrency of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this ListFunctionVersionResult.

        0：函数被禁用;-1：函数被启用。

        :param concurrency: The concurrency of this ListFunctionVersionResult.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def concurrent_num(self):
        """Gets the concurrent_num of this ListFunctionVersionResult.

        并发实例数

        :return: The concurrent_num of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._concurrent_num

    @concurrent_num.setter
    def concurrent_num(self, concurrent_num):
        """Sets the concurrent_num of this ListFunctionVersionResult.

        并发实例数

        :param concurrent_num: The concurrent_num of this ListFunctionVersionResult.
        :type concurrent_num: int
        """
        self._concurrent_num = concurrent_num

    @property
    def strategy_config(self):
        """Gets the strategy_config of this ListFunctionVersionResult.

        :return: The strategy_config of this ListFunctionVersionResult.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        """Sets the strategy_config of this ListFunctionVersionResult.

        :param strategy_config: The strategy_config of this ListFunctionVersionResult.
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        self._strategy_config = strategy_config

    @property
    def initializer_handler(self):
        """Gets the initializer_handler of this ListFunctionVersionResult.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        """Sets the initializer_handler of this ListFunctionVersionResult.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this ListFunctionVersionResult.
        :type initializer_handler: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        """Gets the initializer_timeout of this ListFunctionVersionResult.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :return: The initializer_timeout of this ListFunctionVersionResult.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        """Sets the initializer_timeout of this ListFunctionVersionResult.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :param initializer_timeout: The initializer_timeout of this ListFunctionVersionResult.
        :type initializer_timeout: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def long_time(self):
        """Gets the long_time of this ListFunctionVersionResult.

        是否是支持长时间运行

        :return: The long_time of this ListFunctionVersionResult.
        :rtype: bool
        """
        return self._long_time

    @long_time.setter
    def long_time(self, long_time):
        """Sets the long_time of this ListFunctionVersionResult.

        是否是支持长时间运行

        :param long_time: The long_time of this ListFunctionVersionResult.
        :type long_time: bool
        """
        self._long_time = long_time

    @property
    def function_async_config(self):
        """Gets the function_async_config of this ListFunctionVersionResult.

        :return: The function_async_config of this ListFunctionVersionResult.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FunctionAsyncConfig`
        """
        return self._function_async_config

    @function_async_config.setter
    def function_async_config(self, function_async_config):
        """Sets the function_async_config of this ListFunctionVersionResult.

        :param function_async_config: The function_async_config of this ListFunctionVersionResult.
        :type function_async_config: :class:`huaweicloudsdkfunctiongraph.v2.FunctionAsyncConfig`
        """
        self._function_async_config = function_async_config

    @property
    def type(self):
        """Gets the type of this ListFunctionVersionResult.

        函数版本

        :return: The type of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListFunctionVersionResult.

        函数版本

        :param type: The type of this ListFunctionVersionResult.
        :type type: str
        """
        self._type = type

    @property
    def enable_cloud_debug(self):
        """Gets the enable_cloud_debug of this ListFunctionVersionResult.

        是否启用cloud debug功能

        :return: The enable_cloud_debug of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._enable_cloud_debug

    @enable_cloud_debug.setter
    def enable_cloud_debug(self, enable_cloud_debug):
        """Sets the enable_cloud_debug of this ListFunctionVersionResult.

        是否启用cloud debug功能

        :param enable_cloud_debug: The enable_cloud_debug of this ListFunctionVersionResult.
        :type enable_cloud_debug: str
        """
        self._enable_cloud_debug = enable_cloud_debug

    @property
    def enable_dynamic_memory(self):
        """Gets the enable_dynamic_memory of this ListFunctionVersionResult.

        是否启用动态内存功能

        :return: The enable_dynamic_memory of this ListFunctionVersionResult.
        :rtype: bool
        """
        return self._enable_dynamic_memory

    @enable_dynamic_memory.setter
    def enable_dynamic_memory(self, enable_dynamic_memory):
        """Sets the enable_dynamic_memory of this ListFunctionVersionResult.

        是否启用动态内存功能

        :param enable_dynamic_memory: The enable_dynamic_memory of this ListFunctionVersionResult.
        :type enable_dynamic_memory: bool
        """
        self._enable_dynamic_memory = enable_dynamic_memory

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListFunctionVersionResult.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this ListFunctionVersionResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListFunctionVersionResult.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this ListFunctionVersionResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_stateful_function(self):
        """Gets the is_stateful_function of this ListFunctionVersionResult.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :return: The is_stateful_function of this ListFunctionVersionResult.
        :rtype: bool
        """
        return self._is_stateful_function

    @is_stateful_function.setter
    def is_stateful_function(self, is_stateful_function):
        """Sets the is_stateful_function of this ListFunctionVersionResult.

        是否支持有状态，如果需要支持，需要固定传参为true，v2版本支持

        :param is_stateful_function: The is_stateful_function of this ListFunctionVersionResult.
        :type is_stateful_function: bool
        """
        self._is_stateful_function = is_stateful_function

    @property
    def enable_auth_in_header(self):
        """Gets the enable_auth_in_header of this ListFunctionVersionResult.

        是否允许在请求头中添加鉴权信息

        :return: The enable_auth_in_header of this ListFunctionVersionResult.
        :rtype: bool
        """
        return self._enable_auth_in_header

    @enable_auth_in_header.setter
    def enable_auth_in_header(self, enable_auth_in_header):
        """Sets the enable_auth_in_header of this ListFunctionVersionResult.

        是否允许在请求头中添加鉴权信息

        :param enable_auth_in_header: The enable_auth_in_header of this ListFunctionVersionResult.
        :type enable_auth_in_header: bool
        """
        self._enable_auth_in_header = enable_auth_in_header

    @property
    def custom_image(self):
        """Gets the custom_image of this ListFunctionVersionResult.

        :return: The custom_image of this ListFunctionVersionResult.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        return self._custom_image

    @custom_image.setter
    def custom_image(self, custom_image):
        """Sets the custom_image of this ListFunctionVersionResult.

        :param custom_image: The custom_image of this ListFunctionVersionResult.
        :type custom_image: :class:`huaweicloudsdkfunctiongraph.v2.CustomImage`
        """
        self._custom_image = custom_image

    @property
    def reserved_instance_idle_mode(self):
        """Gets the reserved_instance_idle_mode of this ListFunctionVersionResult.

        是否开启预留实例闲置模式

        :return: The reserved_instance_idle_mode of this ListFunctionVersionResult.
        :rtype: bool
        """
        return self._reserved_instance_idle_mode

    @reserved_instance_idle_mode.setter
    def reserved_instance_idle_mode(self, reserved_instance_idle_mode):
        """Sets the reserved_instance_idle_mode of this ListFunctionVersionResult.

        是否开启预留实例闲置模式

        :param reserved_instance_idle_mode: The reserved_instance_idle_mode of this ListFunctionVersionResult.
        :type reserved_instance_idle_mode: bool
        """
        self._reserved_instance_idle_mode = reserved_instance_idle_mode

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
        if not isinstance(other, ListFunctionVersionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
