# coding: utf-8

import pprint
import re

import six





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
        'pvc_quantity': 'str',
        'refresh_interval': 'str',
        'repository_id': 'int',
        'stack_id': 'str',
        'task_type': 'str',
        'token': 'str'
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
        'pvc_quantity': 'pvc_quantity',
        'refresh_interval': 'refresh_interval',
        'repository_id': 'repository_id',
        'stack_id': 'stack_id',
        'task_type': 'task_type',
        'token': 'token'
    }

    def __init__(self, agent_id=None, arch=None, cpu_memory=None, description=None, display_name=None, is_temporary=None, label_tag=None, plugin_enable_list=None, plugin_vars=None, pvc_quantity=None, refresh_interval=None, repository_id=None, stack_id=None, task_type=None, token=None):
        """InstanceParam - a model defined in huaweicloud sdk"""
        
        

        self._agent_id = None
        self._arch = None
        self._cpu_memory = None
        self._description = None
        self._display_name = None
        self._is_temporary = None
        self._label_tag = None
        self._plugin_enable_list = None
        self._plugin_vars = None
        self._pvc_quantity = None
        self._refresh_interval = None
        self._repository_id = None
        self._stack_id = None
        self._task_type = None
        self._token = None
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
        self.pvc_quantity = pvc_quantity
        self.refresh_interval = refresh_interval
        if repository_id is not None:
            self.repository_id = repository_id
        self.stack_id = stack_id
        if task_type is not None:
            self.task_type = task_type
        if token is not None:
            self.token = token

    @property
    def agent_id(self):
        """Gets the agent_id of this InstanceParam.

        代理商id，标签为tutorial时使用

        :return: The agent_id of this InstanceParam.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this InstanceParam.

        代理商id，标签为tutorial时使用

        :param agent_id: The agent_id of this InstanceParam.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def arch(self):
        """Gets the arch of this InstanceParam.

        cpu架构 x86|arm

        :return: The arch of this InstanceParam.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this InstanceParam.

        cpu架构 x86|arm

        :param arch: The arch of this InstanceParam.
        :type: str
        """
        self._arch = arch

    @property
    def cpu_memory(self):
        """Gets the cpu_memory of this InstanceParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacksByTag接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :return: The cpu_memory of this InstanceParam.
        :rtype: str
        """
        return self._cpu_memory

    @cpu_memory.setter
    def cpu_memory(self, cpu_memory):
        """Sets the cpu_memory of this InstanceParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacksByTag接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :param cpu_memory: The cpu_memory of this InstanceParam.
        :type: str
        """
        self._cpu_memory = cpu_memory

    @property
    def description(self):
        """Gets the description of this InstanceParam.

        描述

        :return: The description of this InstanceParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceParam.

        描述

        :param description: The description of this InstanceParam.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this InstanceParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The display_name of this InstanceParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InstanceParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param display_name: The display_name of this InstanceParam.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_temporary(self):
        """Gets the is_temporary of this InstanceParam.

        是否临时实例。 false页面会显示

        :return: The is_temporary of this InstanceParam.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this InstanceParam.

        是否临时实例。 false页面会显示

        :param is_temporary: The is_temporary of this InstanceParam.
        :type: bool
        """
        self._is_temporary = is_temporary

    @property
    def label_tag(self):
        """Gets the label_tag of this InstanceParam.

        场景标签

        :return: The label_tag of this InstanceParam.
        :rtype: str
        """
        return self._label_tag

    @label_tag.setter
    def label_tag(self, label_tag):
        """Sets the label_tag of this InstanceParam.

        场景标签

        :param label_tag: The label_tag of this InstanceParam.
        :type: str
        """
        self._label_tag = label_tag

    @property
    def plugin_enable_list(self):
        """Gets the plugin_enable_list of this InstanceParam.

        场景插件列表

        :return: The plugin_enable_list of this InstanceParam.
        :rtype: list[str]
        """
        return self._plugin_enable_list

    @plugin_enable_list.setter
    def plugin_enable_list(self, plugin_enable_list):
        """Sets the plugin_enable_list of this InstanceParam.

        场景插件列表

        :param plugin_enable_list: The plugin_enable_list of this InstanceParam.
        :type: list[str]
        """
        self._plugin_enable_list = plugin_enable_list

    @property
    def plugin_vars(self):
        """Gets the plugin_vars of this InstanceParam.

        场景插件参数

        :return: The plugin_vars of this InstanceParam.
        :rtype: dict(str, str)
        """
        return self._plugin_vars

    @plugin_vars.setter
    def plugin_vars(self, plugin_vars):
        """Sets the plugin_vars of this InstanceParam.

        场景插件参数

        :param plugin_vars: The plugin_vars of this InstanceParam.
        :type: dict(str, str)
        """
        self._plugin_vars = plugin_vars

    @property
    def pvc_quantity(self):
        """Gets the pvc_quantity of this InstanceParam.

        PVC规格 5GB|10GB|20GB

        :return: The pvc_quantity of this InstanceParam.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        """Sets the pvc_quantity of this InstanceParam.

        PVC规格 5GB|10GB|20GB

        :param pvc_quantity: The pvc_quantity of this InstanceParam.
        :type: str
        """
        self._pvc_quantity = pvc_quantity

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this InstanceParam.

        实例的生命周期 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :return: The refresh_interval of this InstanceParam.
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this InstanceParam.

        实例的生命周期 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :param refresh_interval: The refresh_interval of this InstanceParam.
        :type: str
        """
        self._refresh_interval = refresh_interval

    @property
    def repository_id(self):
        """Gets the repository_id of this InstanceParam.

        解放号的仓库id，标签为jfh时使用

        :return: The repository_id of this InstanceParam.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this InstanceParam.

        解放号的仓库id，标签为jfh时使用

        :param repository_id: The repository_id of this InstanceParam.
        :type: int
        """
        self._repository_id = repository_id

    @property
    def stack_id(self):
        """Gets the stack_id of this InstanceParam.

        技术栈ID 目前可取值all，java，go，python，cpp，nodejs，quantum，blockchain，dcn，vue，ruby。

        :return: The stack_id of this InstanceParam.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this InstanceParam.

        技术栈ID 目前可取值all，java，go，python，cpp，nodejs，quantum，blockchain，dcn，vue，ruby。

        :param stack_id: The stack_id of this InstanceParam.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def task_type(self):
        """Gets the task_type of this InstanceParam.

        任务类型，标签为tutorial时使用

        :return: The task_type of this InstanceParam.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this InstanceParam.

        任务类型，标签为tutorial时使用

        :param task_type: The task_type of this InstanceParam.
        :type: str
        """
        self._task_type = task_type

    @property
    def token(self):
        """Gets the token of this InstanceParam.

        解放号的token，标签为jfh时使用

        :return: The token of this InstanceParam.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this InstanceParam.

        解放号的token，标签为jfh时使用

        :param token: The token of this InstanceParam.
        :type: str
        """
        self._token = token

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
        if not isinstance(other, InstanceParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
