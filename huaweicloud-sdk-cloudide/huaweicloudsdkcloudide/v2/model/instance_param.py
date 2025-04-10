# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'arch': 'str',
        'cpu_memory': 'str',
        'description': 'str',
        'display_name': 'str',
        'is_temporary': 'bool',
        'label_tag': 'str',
        'plugin_enable_list': 'list[str]',
        'plugin_vars': 'dict(str, str)',
        'port_id': 'str',
        'private_ip': 'str',
        'pvc_quantity': 'str',
        'refresh_interval': 'str',
        'repository_id': 'int',
        'stack_id': 'str',
        'task_type': 'str',
        'token': 'str',
        'vpc_id': 'str',
        'instance_domain_id': 'str',
        'instance_user_id': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'arch': 'arch',
        'cpu_memory': 'cpu_memory',
        'description': 'description',
        'display_name': 'display_name',
        'is_temporary': 'is_temporary',
        'label_tag': 'label_tag',
        'plugin_enable_list': 'plugin_enable_list',
        'plugin_vars': 'plugin_vars',
        'port_id': 'port_id',
        'private_ip': 'private_ip',
        'pvc_quantity': 'pvc_quantity',
        'refresh_interval': 'refresh_interval',
        'repository_id': 'repository_id',
        'stack_id': 'stack_id',
        'task_type': 'task_type',
        'token': 'token',
        'vpc_id': 'vpc_id',
        'instance_domain_id': 'instance_domain_id',
        'instance_user_id': 'instance_user_id'
    }

    def __init__(self, agent_id=None, arch=None, cpu_memory=None, description=None, display_name=None, is_temporary=None, label_tag=None, plugin_enable_list=None, plugin_vars=None, port_id=None, private_ip=None, pvc_quantity=None, refresh_interval=None, repository_id=None, stack_id=None, task_type=None, token=None, vpc_id=None, instance_domain_id=None, instance_user_id=None):
        r"""InstanceParam

        The model defined in huaweicloud sdk

        :param agent_id: 代理商id，教程活动场景下使用
        :type agent_id: str
        :param arch: cpu架构 x86|arm
        :type arch: str
        :param cpu_memory: cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G
        :type cpu_memory: str
        :param description: 描述
        :type description: str
        :param display_name: 实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间
        :type display_name: str
        :param is_temporary: 是否页面显示（以标签配置为准）
        :type is_temporary: bool
        :param label_tag: 实例标签（不同的第三方需要和CodeArtsIDEOnline服务共同设定标签），不传默认为default
        :type label_tag: str
        :param plugin_enable_list: 预装插件列表
        :type plugin_enable_list: list[str]
        :param plugin_vars: 预装插件参数，请注意敏感信息保护，若涉及敏感信息，请自行加密
        :type plugin_vars: dict(str, str)
        :param port_id: 云服务器对应的portId，小网连接ecs的场景下使用
        :type port_id: str
        :param private_ip: 云服务器ip，小网连接ecs的场景下使用
        :type private_ip: str
        :param pvc_quantity: PVC规格 5GB|10GB|20GB
        :type pvc_quantity: str
        :param refresh_interval: 自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止
        :type refresh_interval: str
        :param repository_id: 解放号的仓库id，解放号场景下使用
        :type repository_id: int
        :param stack_id: 技术栈ID，通过技术栈管理ListStacks接口获取。
        :type stack_id: str
        :param task_type: 任务类型，教程活动场景下使用
        :type task_type: str
        :param token: 解放号的token，解放号场景下使用
        :type token: str
        :param vpc_id: 云服务器对应的vpcId，小网连接ecs的场景下使用
        :type vpc_id: str
        :param instance_domain_id: 实例授权用户租户ID
        :type instance_domain_id: str
        :param instance_user_id: 实例授权用户ID
        :type instance_user_id: str
        """
        
        

        self._agent_id = None
        self._arch = None
        self._cpu_memory = None
        self._description = None
        self._display_name = None
        self._is_temporary = None
        self._label_tag = None
        self._plugin_enable_list = None
        self._plugin_vars = None
        self._port_id = None
        self._private_ip = None
        self._pvc_quantity = None
        self._refresh_interval = None
        self._repository_id = None
        self._stack_id = None
        self._task_type = None
        self._token = None
        self._vpc_id = None
        self._instance_domain_id = None
        self._instance_user_id = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if arch is not None:
            self.arch = arch
        self.cpu_memory = cpu_memory
        if description is not None:
            self.description = description
        self.display_name = display_name
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if label_tag is not None:
            self.label_tag = label_tag
        if plugin_enable_list is not None:
            self.plugin_enable_list = plugin_enable_list
        if plugin_vars is not None:
            self.plugin_vars = plugin_vars
        if port_id is not None:
            self.port_id = port_id
        if private_ip is not None:
            self.private_ip = private_ip
        self.pvc_quantity = pvc_quantity
        self.refresh_interval = refresh_interval
        if repository_id is not None:
            self.repository_id = repository_id
        self.stack_id = stack_id
        if task_type is not None:
            self.task_type = task_type
        if token is not None:
            self.token = token
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if instance_domain_id is not None:
            self.instance_domain_id = instance_domain_id
        if instance_user_id is not None:
            self.instance_user_id = instance_user_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this InstanceParam.

        代理商id，教程活动场景下使用

        :return: The agent_id of this InstanceParam.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this InstanceParam.

        代理商id，教程活动场景下使用

        :param agent_id: The agent_id of this InstanceParam.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def arch(self):
        r"""Gets the arch of this InstanceParam.

        cpu架构 x86|arm

        :return: The arch of this InstanceParam.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this InstanceParam.

        cpu架构 x86|arm

        :param arch: The arch of this InstanceParam.
        :type arch: str
        """
        self._arch = arch

    @property
    def cpu_memory(self):
        r"""Gets the cpu_memory of this InstanceParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :return: The cpu_memory of this InstanceParam.
        :rtype: str
        """
        return self._cpu_memory

    @cpu_memory.setter
    def cpu_memory(self, cpu_memory):
        r"""Sets the cpu_memory of this InstanceParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :param cpu_memory: The cpu_memory of this InstanceParam.
        :type cpu_memory: str
        """
        self._cpu_memory = cpu_memory

    @property
    def description(self):
        r"""Gets the description of this InstanceParam.

        描述

        :return: The description of this InstanceParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstanceParam.

        描述

        :param description: The description of this InstanceParam.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this InstanceParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The display_name of this InstanceParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this InstanceParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param display_name: The display_name of this InstanceParam.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def is_temporary(self):
        r"""Gets the is_temporary of this InstanceParam.

        是否页面显示（以标签配置为准）

        :return: The is_temporary of this InstanceParam.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        r"""Sets the is_temporary of this InstanceParam.

        是否页面显示（以标签配置为准）

        :param is_temporary: The is_temporary of this InstanceParam.
        :type is_temporary: bool
        """
        self._is_temporary = is_temporary

    @property
    def label_tag(self):
        r"""Gets the label_tag of this InstanceParam.

        实例标签（不同的第三方需要和CodeArtsIDEOnline服务共同设定标签），不传默认为default

        :return: The label_tag of this InstanceParam.
        :rtype: str
        """
        return self._label_tag

    @label_tag.setter
    def label_tag(self, label_tag):
        r"""Sets the label_tag of this InstanceParam.

        实例标签（不同的第三方需要和CodeArtsIDEOnline服务共同设定标签），不传默认为default

        :param label_tag: The label_tag of this InstanceParam.
        :type label_tag: str
        """
        self._label_tag = label_tag

    @property
    def plugin_enable_list(self):
        r"""Gets the plugin_enable_list of this InstanceParam.

        预装插件列表

        :return: The plugin_enable_list of this InstanceParam.
        :rtype: list[str]
        """
        return self._plugin_enable_list

    @plugin_enable_list.setter
    def plugin_enable_list(self, plugin_enable_list):
        r"""Sets the plugin_enable_list of this InstanceParam.

        预装插件列表

        :param plugin_enable_list: The plugin_enable_list of this InstanceParam.
        :type plugin_enable_list: list[str]
        """
        self._plugin_enable_list = plugin_enable_list

    @property
    def plugin_vars(self):
        r"""Gets the plugin_vars of this InstanceParam.

        预装插件参数，请注意敏感信息保护，若涉及敏感信息，请自行加密

        :return: The plugin_vars of this InstanceParam.
        :rtype: dict(str, str)
        """
        return self._plugin_vars

    @plugin_vars.setter
    def plugin_vars(self, plugin_vars):
        r"""Sets the plugin_vars of this InstanceParam.

        预装插件参数，请注意敏感信息保护，若涉及敏感信息，请自行加密

        :param plugin_vars: The plugin_vars of this InstanceParam.
        :type plugin_vars: dict(str, str)
        """
        self._plugin_vars = plugin_vars

    @property
    def port_id(self):
        r"""Gets the port_id of this InstanceParam.

        云服务器对应的portId，小网连接ecs的场景下使用

        :return: The port_id of this InstanceParam.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this InstanceParam.

        云服务器对应的portId，小网连接ecs的场景下使用

        :param port_id: The port_id of this InstanceParam.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this InstanceParam.

        云服务器ip，小网连接ecs的场景下使用

        :return: The private_ip of this InstanceParam.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this InstanceParam.

        云服务器ip，小网连接ecs的场景下使用

        :param private_ip: The private_ip of this InstanceParam.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def pvc_quantity(self):
        r"""Gets the pvc_quantity of this InstanceParam.

        PVC规格 5GB|10GB|20GB

        :return: The pvc_quantity of this InstanceParam.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        r"""Sets the pvc_quantity of this InstanceParam.

        PVC规格 5GB|10GB|20GB

        :param pvc_quantity: The pvc_quantity of this InstanceParam.
        :type pvc_quantity: str
        """
        self._pvc_quantity = pvc_quantity

    @property
    def refresh_interval(self):
        r"""Gets the refresh_interval of this InstanceParam.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止

        :return: The refresh_interval of this InstanceParam.
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        r"""Sets the refresh_interval of this InstanceParam.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止

        :param refresh_interval: The refresh_interval of this InstanceParam.
        :type refresh_interval: str
        """
        self._refresh_interval = refresh_interval

    @property
    def repository_id(self):
        r"""Gets the repository_id of this InstanceParam.

        解放号的仓库id，解放号场景下使用

        :return: The repository_id of this InstanceParam.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this InstanceParam.

        解放号的仓库id，解放号场景下使用

        :param repository_id: The repository_id of this InstanceParam.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def stack_id(self):
        r"""Gets the stack_id of this InstanceParam.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :return: The stack_id of this InstanceParam.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this InstanceParam.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :param stack_id: The stack_id of this InstanceParam.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def task_type(self):
        r"""Gets the task_type of this InstanceParam.

        任务类型，教程活动场景下使用

        :return: The task_type of this InstanceParam.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this InstanceParam.

        任务类型，教程活动场景下使用

        :param task_type: The task_type of this InstanceParam.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def token(self):
        r"""Gets the token of this InstanceParam.

        解放号的token，解放号场景下使用

        :return: The token of this InstanceParam.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this InstanceParam.

        解放号的token，解放号场景下使用

        :param token: The token of this InstanceParam.
        :type token: str
        """
        self._token = token

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this InstanceParam.

        云服务器对应的vpcId，小网连接ecs的场景下使用

        :return: The vpc_id of this InstanceParam.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this InstanceParam.

        云服务器对应的vpcId，小网连接ecs的场景下使用

        :param vpc_id: The vpc_id of this InstanceParam.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def instance_domain_id(self):
        r"""Gets the instance_domain_id of this InstanceParam.

        实例授权用户租户ID

        :return: The instance_domain_id of this InstanceParam.
        :rtype: str
        """
        return self._instance_domain_id

    @instance_domain_id.setter
    def instance_domain_id(self, instance_domain_id):
        r"""Sets the instance_domain_id of this InstanceParam.

        实例授权用户租户ID

        :param instance_domain_id: The instance_domain_id of this InstanceParam.
        :type instance_domain_id: str
        """
        self._instance_domain_id = instance_domain_id

    @property
    def instance_user_id(self):
        r"""Gets the instance_user_id of this InstanceParam.

        实例授权用户ID

        :return: The instance_user_id of this InstanceParam.
        :rtype: str
        """
        return self._instance_user_id

    @instance_user_id.setter
    def instance_user_id(self, instance_user_id):
        r"""Sets the instance_user_id of this InstanceParam.

        实例授权用户ID

        :param instance_user_id: The instance_user_id of this InstanceParam.
        :type instance_user_id: str
        """
        self._instance_user_id = instance_user_id

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
        if not isinstance(other, InstanceParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
