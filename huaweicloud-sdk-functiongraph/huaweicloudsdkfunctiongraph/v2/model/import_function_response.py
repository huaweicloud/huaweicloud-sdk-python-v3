# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFunctionResponse(SdkResponse):

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
        'gpu_memory': 'int',
        'cpu': 'int',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'code_size': 'int',
        'user_data': 'str',
        'digest': 'str',
        'version': 'str',
        'image_name': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'version_description': 'str',
        'last_modified': 'datetime',
        'func_vpc': 'FuncVpc',
        'depend_list': 'list[str]',
        'depend_version_list': 'list[str]',
        'strategy_config': 'StrategyConfig',
        'extend_config': 'str',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'pre_stop_handler': 'str',
        'pre_stop_timeout': 'int',
        'enterprise_project_id': 'str'
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
        'gpu_memory': 'gpu_memory',
        'cpu': 'cpu',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'code_size': 'code_size',
        'user_data': 'user_data',
        'digest': 'digest',
        'version': 'version',
        'image_name': 'image_name',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'version_description': 'version_description',
        'last_modified': 'last_modified',
        'func_vpc': 'func_vpc',
        'depend_list': 'depend_list',
        'depend_version_list': 'depend_version_list',
        'strategy_config': 'strategy_config',
        'extend_config': 'extend_config',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'pre_stop_handler': 'pre_stop_handler',
        'pre_stop_timeout': 'pre_stop_timeout',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, func_urn=None, func_name=None, domain_id=None, namespace=None, project_name=None, package=None, runtime=None, timeout=None, handler=None, memory_size=None, gpu_memory=None, cpu=None, code_type=None, code_url=None, code_filename=None, code_size=None, user_data=None, digest=None, version=None, image_name=None, xrole=None, app_xrole=None, description=None, version_description=None, last_modified=None, func_vpc=None, depend_list=None, depend_version_list=None, strategy_config=None, extend_config=None, initializer_handler=None, initializer_timeout=None, pre_stop_handler=None, pre_stop_timeout=None, enterprise_project_id=None):
        r"""ImportFunctionResponse

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
        :param user_data: 用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host&#x3D;{host_ip}，最多定义20个，总长度不超过4KB。
        :type user_data: str
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
        :param description: 函数描述。
        :type description: str
        :param version_description: 函数版本描述。
        :type version_description: str
        :param last_modified: 函数最后一次更新时间。
        :type last_modified: datetime
        :param func_vpc: 
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        :param depend_list: 依赖id列表
        :type depend_list: list[str]
        :param depend_version_list: 依赖版本id列表
        :type depend_version_list: list[str]
        :param strategy_config: 
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        :param extend_config: 函数扩展配置。
        :type extend_config: str
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
        """
        
        super(ImportFunctionResponse, self).__init__()

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
        self._user_data = None
        self._digest = None
        self._version = None
        self._image_name = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._version_description = None
        self._last_modified = None
        self._func_vpc = None
        self._depend_list = None
        self._depend_version_list = None
        self._strategy_config = None
        self._extend_config = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._pre_stop_handler = None
        self._pre_stop_timeout = None
        self._enterprise_project_id = None
        self.discriminator = None

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
        if user_data is not None:
            self.user_data = user_data
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
        if version_description is not None:
            self.version_description = version_description
        if last_modified is not None:
            self.last_modified = last_modified
        if func_vpc is not None:
            self.func_vpc = func_vpc
        if depend_list is not None:
            self.depend_list = depend_list
        if depend_version_list is not None:
            self.depend_version_list = depend_version_list
        if strategy_config is not None:
            self.strategy_config = strategy_config
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def func_urn(self):
        r"""Gets the func_urn of this ImportFunctionResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this ImportFunctionResponse.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this ImportFunctionResponse.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this ImportFunctionResponse.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        r"""Gets the func_name of this ImportFunctionResponse.

        函数名称。

        :return: The func_name of this ImportFunctionResponse.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        r"""Sets the func_name of this ImportFunctionResponse.

        函数名称。

        :param func_name: The func_name of this ImportFunctionResponse.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ImportFunctionResponse.

        域名id。

        :return: The domain_id of this ImportFunctionResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ImportFunctionResponse.

        域名id。

        :param domain_id: The domain_id of this ImportFunctionResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ImportFunctionResponse.

        租户的project id。

        :return: The namespace of this ImportFunctionResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImportFunctionResponse.

        租户的project id。

        :param namespace: The namespace of this ImportFunctionResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project_name(self):
        r"""Gets the project_name of this ImportFunctionResponse.

        租户的project name。

        :return: The project_name of this ImportFunctionResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ImportFunctionResponse.

        租户的project name。

        :param project_name: The project_name of this ImportFunctionResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def package(self):
        r"""Gets the package of this ImportFunctionResponse.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this ImportFunctionResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this ImportFunctionResponse.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this ImportFunctionResponse.
        :type package: str
        """
        self._package = package

    @property
    def runtime(self):
        r"""Gets the runtime of this ImportFunctionResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this ImportFunctionResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ImportFunctionResponse.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this ImportFunctionResponse.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        r"""Gets the timeout of this ImportFunctionResponse.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :return: The timeout of this ImportFunctionResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ImportFunctionResponse.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :param timeout: The timeout of this ImportFunctionResponse.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        r"""Gets the handler of this ImportFunctionResponse.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this ImportFunctionResponse.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this ImportFunctionResponse.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this ImportFunctionResponse.
        :type handler: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        r"""Gets the memory_size of this ImportFunctionResponse.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this ImportFunctionResponse.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        r"""Sets the memory_size of this ImportFunctionResponse.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this ImportFunctionResponse.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def gpu_memory(self):
        r"""Gets the gpu_memory of this ImportFunctionResponse.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :return: The gpu_memory of this ImportFunctionResponse.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        r"""Sets the gpu_memory of this ImportFunctionResponse.

        函数消耗的显存，只支持自定义运行时与自定义镜像函数配置GPU。 单位MB。 取值范围为：1024、2048、3072、4096、5120、6144、7168、8192、9216、10240、11264、12288、13312、14336、15360、16384。 最小值为1024，最大值为16384。

        :param gpu_memory: The gpu_memory of this ImportFunctionResponse.
        :type gpu_memory: int
        """
        self._gpu_memory = gpu_memory

    @property
    def cpu(self):
        r"""Gets the cpu of this ImportFunctionResponse.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。

        :return: The cpu of this ImportFunctionResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ImportFunctionResponse.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。

        :param cpu: The cpu of this ImportFunctionResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def code_type(self):
        r"""Gets the code_type of this ImportFunctionResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :return: The code_type of this ImportFunctionResponse.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        r"""Sets the code_type of this ImportFunctionResponse.

        函数代码类型，取值有5种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。 Custom-Image-Swr: 函数代码来源与SWR自定义镜像。

        :param code_type: The code_type of this ImportFunctionResponse.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        r"""Gets the code_url of this ImportFunctionResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this ImportFunctionResponse.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this ImportFunctionResponse.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this ImportFunctionResponse.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        r"""Gets the code_filename of this ImportFunctionResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this ImportFunctionResponse.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        r"""Sets the code_filename of this ImportFunctionResponse.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this ImportFunctionResponse.
        :type code_filename: str
        """
        self._code_filename = code_filename

    @property
    def code_size(self):
        r"""Gets the code_size of this ImportFunctionResponse.

        函数大小，单位：字节。

        :return: The code_size of this ImportFunctionResponse.
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        r"""Sets the code_size of this ImportFunctionResponse.

        函数大小，单位：字节。

        :param code_size: The code_size of this ImportFunctionResponse.
        :type code_size: int
        """
        self._code_size = code_size

    @property
    def user_data(self):
        r"""Gets the user_data of this ImportFunctionResponse.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this ImportFunctionResponse.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this ImportFunctionResponse.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this ImportFunctionResponse.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def digest(self):
        r"""Gets the digest of this ImportFunctionResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :return: The digest of this ImportFunctionResponse.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this ImportFunctionResponse.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :param digest: The digest of this ImportFunctionResponse.
        :type digest: str
        """
        self._digest = digest

    @property
    def version(self):
        r"""Gets the version of this ImportFunctionResponse.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :return: The version of this ImportFunctionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ImportFunctionResponse.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :param version: The version of this ImportFunctionResponse.
        :type version: str
        """
        self._version = version

    @property
    def image_name(self):
        r"""Gets the image_name of this ImportFunctionResponse.

        函数版本的内部标识。

        :return: The image_name of this ImportFunctionResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImportFunctionResponse.

        函数版本的内部标识。

        :param image_name: The image_name of this ImportFunctionResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def xrole(self):
        r"""Gets the xrole of this ImportFunctionResponse.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this ImportFunctionResponse.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        r"""Sets the xrole of this ImportFunctionResponse.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this ImportFunctionResponse.
        :type xrole: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        r"""Gets the app_xrole of this ImportFunctionResponse.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this ImportFunctionResponse.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        r"""Sets the app_xrole of this ImportFunctionResponse.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this ImportFunctionResponse.
        :type app_xrole: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        r"""Gets the description of this ImportFunctionResponse.

        函数描述。

        :return: The description of this ImportFunctionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImportFunctionResponse.

        函数描述。

        :param description: The description of this ImportFunctionResponse.
        :type description: str
        """
        self._description = description

    @property
    def version_description(self):
        r"""Gets the version_description of this ImportFunctionResponse.

        函数版本描述。

        :return: The version_description of this ImportFunctionResponse.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ImportFunctionResponse.

        函数版本描述。

        :param version_description: The version_description of this ImportFunctionResponse.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def last_modified(self):
        r"""Gets the last_modified of this ImportFunctionResponse.

        函数最后一次更新时间。

        :return: The last_modified of this ImportFunctionResponse.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this ImportFunctionResponse.

        函数最后一次更新时间。

        :param last_modified: The last_modified of this ImportFunctionResponse.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def func_vpc(self):
        r"""Gets the func_vpc of this ImportFunctionResponse.

        :return: The func_vpc of this ImportFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        r"""Sets the func_vpc of this ImportFunctionResponse.

        :param func_vpc: The func_vpc of this ImportFunctionResponse.
        :type func_vpc: :class:`huaweicloudsdkfunctiongraph.v2.FuncVpc`
        """
        self._func_vpc = func_vpc

    @property
    def depend_list(self):
        r"""Gets the depend_list of this ImportFunctionResponse.

        依赖id列表

        :return: The depend_list of this ImportFunctionResponse.
        :rtype: list[str]
        """
        return self._depend_list

    @depend_list.setter
    def depend_list(self, depend_list):
        r"""Sets the depend_list of this ImportFunctionResponse.

        依赖id列表

        :param depend_list: The depend_list of this ImportFunctionResponse.
        :type depend_list: list[str]
        """
        self._depend_list = depend_list

    @property
    def depend_version_list(self):
        r"""Gets the depend_version_list of this ImportFunctionResponse.

        依赖版本id列表

        :return: The depend_version_list of this ImportFunctionResponse.
        :rtype: list[str]
        """
        return self._depend_version_list

    @depend_version_list.setter
    def depend_version_list(self, depend_version_list):
        r"""Sets the depend_version_list of this ImportFunctionResponse.

        依赖版本id列表

        :param depend_version_list: The depend_version_list of this ImportFunctionResponse.
        :type depend_version_list: list[str]
        """
        self._depend_version_list = depend_version_list

    @property
    def strategy_config(self):
        r"""Gets the strategy_config of this ImportFunctionResponse.

        :return: The strategy_config of this ImportFunctionResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        r"""Sets the strategy_config of this ImportFunctionResponse.

        :param strategy_config: The strategy_config of this ImportFunctionResponse.
        :type strategy_config: :class:`huaweicloudsdkfunctiongraph.v2.StrategyConfig`
        """
        self._strategy_config = strategy_config

    @property
    def extend_config(self):
        r"""Gets the extend_config of this ImportFunctionResponse.

        函数扩展配置。

        :return: The extend_config of this ImportFunctionResponse.
        :rtype: str
        """
        return self._extend_config

    @extend_config.setter
    def extend_config(self, extend_config):
        r"""Sets the extend_config of this ImportFunctionResponse.

        函数扩展配置。

        :param extend_config: The extend_config of this ImportFunctionResponse.
        :type extend_config: str
        """
        self._extend_config = extend_config

    @property
    def initializer_handler(self):
        r"""Gets the initializer_handler of this ImportFunctionResponse.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this ImportFunctionResponse.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        r"""Sets the initializer_handler of this ImportFunctionResponse.

        函数初始化入口，规则：xx.xx，必须包含“. ”。当配置初始化函数时，此参数必填。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this ImportFunctionResponse.
        :type initializer_handler: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        r"""Gets the initializer_timeout of this ImportFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :return: The initializer_timeout of this ImportFunctionResponse.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        r"""Sets the initializer_timeout of this ImportFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。当配置初始化函数时，此参数必填。

        :param initializer_timeout: The initializer_timeout of this ImportFunctionResponse.
        :type initializer_timeout: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def pre_stop_handler(self):
        r"""Gets the pre_stop_handler of this ImportFunctionResponse.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :return: The pre_stop_handler of this ImportFunctionResponse.
        :rtype: str
        """
        return self._pre_stop_handler

    @pre_stop_handler.setter
    def pre_stop_handler(self, pre_stop_handler):
        r"""Sets the pre_stop_handler of this ImportFunctionResponse.

        函数预停止函数的入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.pre_stop_handler，则表示函数的文件名为myfunction.js，初始化的入口函数名为pre_stop_handler。

        :param pre_stop_handler: The pre_stop_handler of this ImportFunctionResponse.
        :type pre_stop_handler: str
        """
        self._pre_stop_handler = pre_stop_handler

    @property
    def pre_stop_timeout(self):
        r"""Gets the pre_stop_timeout of this ImportFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :return: The pre_stop_timeout of this ImportFunctionResponse.
        :rtype: int
        """
        return self._pre_stop_timeout

    @pre_stop_timeout.setter
    def pre_stop_timeout(self, pre_stop_timeout):
        r"""Sets the pre_stop_timeout of this ImportFunctionResponse.

        初始化超时时间，超时函数将被强行停止，范围1～90秒。

        :param pre_stop_timeout: The pre_stop_timeout of this ImportFunctionResponse.
        :type pre_stop_timeout: int
        """
        self._pre_stop_timeout = pre_stop_timeout

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ImportFunctionResponse.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this ImportFunctionResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ImportFunctionResponse.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this ImportFunctionResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ImportFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
