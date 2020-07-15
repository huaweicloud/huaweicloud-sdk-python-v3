# coding: utf-8

import pprint
import re

import six





class UpdateFunctionCodeRequestBody:


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
        'digest': 'str',
        'version': 'str',
        'image_name': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'version_description': 'str',
        'last_modified': 'datetime',
        'last_modified_utc': 'int',
        'func_code': 'FuncCode',
        'func_vpc': 'FuncVpc',
        'mount_config': 'MountConfig',
        'concurrency': 'int',
        'depend_list': 'list[str]',
        'strategy_config': 'StrategyConfig',
        'extend_config': 'str',
        'dependencies': 'list[Dependency]',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
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
        'last_modified_utc': 'last_modified_utc',
        'func_code': 'func_code',
        'func_vpc': 'func_vpc',
        'mount_config': 'mount_config',
        'concurrency': 'concurrency',
        'depend_list': 'depend_list',
        'strategy_config': 'strategy_config',
        'extend_config': 'extend_config',
        'dependencies': 'dependencies',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, func_urn=None, func_name=None, domain_id=None, namespace=None, project_name=None, package=None, runtime=None, timeout=None, handler=None, memory_size=None, cpu=None, code_type=None, code_url=None, code_filename=None, code_size=None, user_data=None, digest=None, version=None, image_name=None, xrole=None, app_xrole=None, description=None, version_description=None, last_modified=None, last_modified_utc=None, func_code=None, func_vpc=None, mount_config=None, concurrency=None, depend_list=None, strategy_config=None, extend_config=None, dependencies=None, initializer_handler=None, initializer_timeout=None, enterprise_project_id=None):
        """UpdateFunctionCodeRequestBody - a model defined in huaweicloud sdk"""
        
        

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
        self._digest = None
        self._version = None
        self._image_name = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._version_description = None
        self._last_modified = None
        self._last_modified_utc = None
        self._func_code = None
        self._func_vpc = None
        self._mount_config = None
        self._concurrency = None
        self._depend_list = None
        self._strategy_config = None
        self._extend_config = None
        self._dependencies = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._enterprise_project_id = None
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
        self.digest = digest
        self.version = version
        self.image_name = image_name
        if xrole is not None:
            self.xrole = xrole
        if app_xrole is not None:
            self.app_xrole = app_xrole
        if description is not None:
            self.description = description
        if version_description is not None:
            self.version_description = version_description
        self.last_modified = last_modified
        if last_modified_utc is not None:
            self.last_modified_utc = last_modified_utc
        if func_code is not None:
            self.func_code = func_code
        if func_vpc is not None:
            self.func_vpc = func_vpc
        if mount_config is not None:
            self.mount_config = mount_config
        if concurrency is not None:
            self.concurrency = concurrency
        if depend_list is not None:
            self.depend_list = depend_list
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def func_urn(self):
        """Gets the func_urn of this UpdateFunctionCodeRequestBody.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this UpdateFunctionCodeRequestBody.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        """Gets the func_name of this UpdateFunctionCodeRequestBody.

        函数名称。

        :return: The func_name of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this UpdateFunctionCodeRequestBody.

        函数名称。

        :param func_name: The func_name of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._func_name = func_name

    @property
    def domain_id(self):
        """Gets the domain_id of this UpdateFunctionCodeRequestBody.

        域名id。

        :return: The domain_id of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UpdateFunctionCodeRequestBody.

        域名id。

        :param domain_id: The domain_id of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        """Gets the namespace of this UpdateFunctionCodeRequestBody.

        租户的project id。

        :return: The namespace of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdateFunctionCodeRequestBody.

        租户的project id。

        :param namespace: The namespace of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._namespace = namespace

    @property
    def project_name(self):
        """Gets the project_name of this UpdateFunctionCodeRequestBody.

        租户的project name。

        :return: The project_name of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateFunctionCodeRequestBody.

        租户的project name。

        :param project_name: The project_name of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._project_name = project_name

    @property
    def package(self):
        """Gets the package of this UpdateFunctionCodeRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this UpdateFunctionCodeRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._package = package

    @property
    def runtime(self):
        """Gets the runtime of this UpdateFunctionCodeRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :return: The runtime of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this UpdateFunctionCodeRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :param runtime: The runtime of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this UpdateFunctionCodeRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :return: The timeout of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateFunctionCodeRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :param timeout: The timeout of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        """Gets the handler of this UpdateFunctionCodeRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this UpdateFunctionCodeRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        """Gets the memory_size of this UpdateFunctionCodeRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this UpdateFunctionCodeRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._memory_size = memory_size

    @property
    def cpu(self):
        """Gets the cpu of this UpdateFunctionCodeRequestBody.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。 函数占用的CPU为基础CPU：200 millicores，再加上内存按比例占用的CPU，计算方法：内存/128 *100 + 200。

        :return: The cpu of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this UpdateFunctionCodeRequestBody.

        函数占用的cpu资源。 单位为millicore（1 core=1000 millicores）。 取值与MemorySize成比例，默认是128M内存占0.1个核（100 millicores）。 函数占用的CPU为基础CPU：200 millicores，再加上内存按比例占用的CPU，计算方法：内存/128 *100 + 200。

        :param cpu: The cpu of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._cpu = cpu

    @property
    def code_type(self):
        """Gets the code_type of this UpdateFunctionCodeRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :return: The code_type of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this UpdateFunctionCodeRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :param code_type: The code_type of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        """Gets the code_url of this UpdateFunctionCodeRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this UpdateFunctionCodeRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        """Gets the code_filename of this UpdateFunctionCodeRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        """Sets the code_filename of this UpdateFunctionCodeRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._code_filename = code_filename

    @property
    def code_size(self):
        """Gets the code_size of this UpdateFunctionCodeRequestBody.

        函数大小，单位：字节。

        :return: The code_size of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        """Sets the code_size of this UpdateFunctionCodeRequestBody.

        函数大小，单位：字节。

        :param code_size: The code_size of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._code_size = code_size

    @property
    def user_data(self):
        """Gets the user_data of this UpdateFunctionCodeRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this UpdateFunctionCodeRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._user_data = user_data

    @property
    def digest(self):
        """Gets the digest of this UpdateFunctionCodeRequestBody.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :return: The digest of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this UpdateFunctionCodeRequestBody.

        函数代码SHA512 hash值，用于判断函数是否变化。

        :param digest: The digest of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._digest = digest

    @property
    def version(self):
        """Gets the version of this UpdateFunctionCodeRequestBody.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :return: The version of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateFunctionCodeRequestBody.

        函数版本号，由系统自动生成，规则：vYYYYMMDD-HHMMSS（v+年月日-时分秒）。

        :param version: The version of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._version = version

    @property
    def image_name(self):
        """Gets the image_name of this UpdateFunctionCodeRequestBody.

        函数版本的内部标识。

        :return: The image_name of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this UpdateFunctionCodeRequestBody.

        函数版本的内部标识。

        :param image_name: The image_name of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._image_name = image_name

    @property
    def xrole(self):
        """Gets the xrole of this UpdateFunctionCodeRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        """Sets the xrole of this UpdateFunctionCodeRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        """Gets the app_xrole of this UpdateFunctionCodeRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        """Sets the app_xrole of this UpdateFunctionCodeRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        """Gets the description of this UpdateFunctionCodeRequestBody.

        函数描述。

        :return: The description of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFunctionCodeRequestBody.

        函数描述。

        :param description: The description of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._description = description

    @property
    def version_description(self):
        """Gets the version_description of this UpdateFunctionCodeRequestBody.

        函数版本描述。

        :return: The version_description of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """Sets the version_description of this UpdateFunctionCodeRequestBody.

        函数版本描述。

        :param version_description: The version_description of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._version_description = version_description

    @property
    def last_modified(self):
        """Gets the last_modified of this UpdateFunctionCodeRequestBody.

        函数最后一次更新时间。

        :return: The last_modified of this UpdateFunctionCodeRequestBody.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UpdateFunctionCodeRequestBody.

        函数最后一次更新时间。

        :param last_modified: The last_modified of this UpdateFunctionCodeRequestBody.
        :type: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_utc(self):
        """Gets the last_modified_utc of this UpdateFunctionCodeRequestBody.

        函数最后一次更新utc时间。

        :return: The last_modified_utc of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._last_modified_utc

    @last_modified_utc.setter
    def last_modified_utc(self, last_modified_utc):
        """Sets the last_modified_utc of this UpdateFunctionCodeRequestBody.

        函数最后一次更新utc时间。

        :param last_modified_utc: The last_modified_utc of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._last_modified_utc = last_modified_utc

    @property
    def func_code(self):
        """Gets the func_code of this UpdateFunctionCodeRequestBody.


        :return: The func_code of this UpdateFunctionCodeRequestBody.
        :rtype: FuncCode
        """
        return self._func_code

    @func_code.setter
    def func_code(self, func_code):
        """Sets the func_code of this UpdateFunctionCodeRequestBody.


        :param func_code: The func_code of this UpdateFunctionCodeRequestBody.
        :type: FuncCode
        """
        self._func_code = func_code

    @property
    def func_vpc(self):
        """Gets the func_vpc of this UpdateFunctionCodeRequestBody.


        :return: The func_vpc of this UpdateFunctionCodeRequestBody.
        :rtype: FuncVpc
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        """Sets the func_vpc of this UpdateFunctionCodeRequestBody.


        :param func_vpc: The func_vpc of this UpdateFunctionCodeRequestBody.
        :type: FuncVpc
        """
        self._func_vpc = func_vpc

    @property
    def mount_config(self):
        """Gets the mount_config of this UpdateFunctionCodeRequestBody.


        :return: The mount_config of this UpdateFunctionCodeRequestBody.
        :rtype: MountConfig
        """
        return self._mount_config

    @mount_config.setter
    def mount_config(self, mount_config):
        """Sets the mount_config of this UpdateFunctionCodeRequestBody.


        :param mount_config: The mount_config of this UpdateFunctionCodeRequestBody.
        :type: MountConfig
        """
        self._mount_config = mount_config

    @property
    def concurrency(self):
        """Gets the concurrency of this UpdateFunctionCodeRequestBody.


        :return: The concurrency of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this UpdateFunctionCodeRequestBody.


        :param concurrency: The concurrency of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._concurrency = concurrency

    @property
    def depend_list(self):
        """Gets the depend_list of this UpdateFunctionCodeRequestBody.

        依赖id列表

        :return: The depend_list of this UpdateFunctionCodeRequestBody.
        :rtype: list[str]
        """
        return self._depend_list

    @depend_list.setter
    def depend_list(self, depend_list):
        """Sets the depend_list of this UpdateFunctionCodeRequestBody.

        依赖id列表

        :param depend_list: The depend_list of this UpdateFunctionCodeRequestBody.
        :type: list[str]
        """
        self._depend_list = depend_list

    @property
    def strategy_config(self):
        """Gets the strategy_config of this UpdateFunctionCodeRequestBody.


        :return: The strategy_config of this UpdateFunctionCodeRequestBody.
        :rtype: StrategyConfig
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        """Sets the strategy_config of this UpdateFunctionCodeRequestBody.


        :param strategy_config: The strategy_config of this UpdateFunctionCodeRequestBody.
        :type: StrategyConfig
        """
        self._strategy_config = strategy_config

    @property
    def extend_config(self):
        """Gets the extend_config of this UpdateFunctionCodeRequestBody.

        函数扩展配置。

        :return: The extend_config of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._extend_config

    @extend_config.setter
    def extend_config(self, extend_config):
        """Sets the extend_config of this UpdateFunctionCodeRequestBody.

        函数扩展配置。

        :param extend_config: The extend_config of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._extend_config = extend_config

    @property
    def dependencies(self):
        """Gets the dependencies of this UpdateFunctionCodeRequestBody.

        函数依赖代码包列表。

        :return: The dependencies of this UpdateFunctionCodeRequestBody.
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this UpdateFunctionCodeRequestBody.

        函数依赖代码包列表。

        :param dependencies: The dependencies of this UpdateFunctionCodeRequestBody.
        :type: list[Dependency]
        """
        self._dependencies = dependencies

    @property
    def initializer_handler(self):
        """Gets the initializer_handler of this UpdateFunctionCodeRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        """Sets the initializer_handler of this UpdateFunctionCodeRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this UpdateFunctionCodeRequestBody.
        :type: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        """Gets the initializer_timeout of this UpdateFunctionCodeRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :return: The initializer_timeout of this UpdateFunctionCodeRequestBody.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        """Sets the initializer_timeout of this UpdateFunctionCodeRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :param initializer_timeout: The initializer_timeout of this UpdateFunctionCodeRequestBody.
        :type: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateFunctionCodeRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this UpdateFunctionCodeRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateFunctionCodeRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this UpdateFunctionCodeRequestBody.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateFunctionCodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
