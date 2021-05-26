# coding: utf-8

import pprint
import re

import six





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
        'user_data': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'func_vpc': 'FuncVpc',
        'mount_config': 'MountConfig',
        'strategy_config': 'StrategyConfig',
        'extend_config': 'str',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'func_name': 'func_name',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'handler': 'handler',
        'memory_size': 'memory_size',
        'user_data': 'user_data',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'func_vpc': 'func_vpc',
        'mount_config': 'mount_config',
        'strategy_config': 'strategy_config',
        'extend_config': 'extend_config',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, func_name=None, runtime=None, timeout=None, handler=None, memory_size=None, user_data=None, xrole=None, app_xrole=None, description=None, func_vpc=None, mount_config=None, strategy_config=None, extend_config=None, initializer_handler=None, initializer_timeout=None, enterprise_project_id=None):
        """UpdateFunctionConfigRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._func_name = None
        self._runtime = None
        self._timeout = None
        self._handler = None
        self._memory_size = None
        self._user_data = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._func_vpc = None
        self._mount_config = None
        self._strategy_config = None
        self._extend_config = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.func_name = func_name
        self.runtime = runtime
        self.timeout = timeout
        if handler is not None:
            self.handler = handler
        self.memory_size = memory_size
        if user_data is not None:
            self.user_data = user_data
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
        if extend_config is not None:
            self.extend_config = extend_config
        if initializer_handler is not None:
            self.initializer_handler = initializer_handler
        if initializer_timeout is not None:
            self.initializer_timeout = initializer_timeout
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

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
        :type: str
        """
        self._func_name = func_name

    @property
    def runtime(self):
        """Gets the runtime of this UpdateFunctionConfigRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :return: The runtime of this UpdateFunctionConfigRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this UpdateFunctionConfigRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :param runtime: The runtime of this UpdateFunctionConfigRequestBody.
        :type: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this UpdateFunctionConfigRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :return: The timeout of this UpdateFunctionConfigRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateFunctionConfigRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :param timeout: The timeout of this UpdateFunctionConfigRequestBody.
        :type: int
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
        :type: str
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
        :type: int
        """
        self._memory_size = memory_size

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
        :type: str
        """
        self._user_data = user_data

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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._description = description

    @property
    def func_vpc(self):
        """Gets the func_vpc of this UpdateFunctionConfigRequestBody.


        :return: The func_vpc of this UpdateFunctionConfigRequestBody.
        :rtype: FuncVpc
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        """Sets the func_vpc of this UpdateFunctionConfigRequestBody.


        :param func_vpc: The func_vpc of this UpdateFunctionConfigRequestBody.
        :type: FuncVpc
        """
        self._func_vpc = func_vpc

    @property
    def mount_config(self):
        """Gets the mount_config of this UpdateFunctionConfigRequestBody.


        :return: The mount_config of this UpdateFunctionConfigRequestBody.
        :rtype: MountConfig
        """
        return self._mount_config

    @mount_config.setter
    def mount_config(self, mount_config):
        """Sets the mount_config of this UpdateFunctionConfigRequestBody.


        :param mount_config: The mount_config of this UpdateFunctionConfigRequestBody.
        :type: MountConfig
        """
        self._mount_config = mount_config

    @property
    def strategy_config(self):
        """Gets the strategy_config of this UpdateFunctionConfigRequestBody.


        :return: The strategy_config of this UpdateFunctionConfigRequestBody.
        :rtype: StrategyConfig
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        """Sets the strategy_config of this UpdateFunctionConfigRequestBody.


        :param strategy_config: The strategy_config of this UpdateFunctionConfigRequestBody.
        :type: StrategyConfig
        """
        self._strategy_config = strategy_config

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
        :type: str
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
        :type: str
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
        :type: int
        """
        self._initializer_timeout = initializer_timeout

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
        if not isinstance(other, UpdateFunctionConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
