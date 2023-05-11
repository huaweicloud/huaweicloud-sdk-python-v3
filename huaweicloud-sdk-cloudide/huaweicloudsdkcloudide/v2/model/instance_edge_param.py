# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceEdgeParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'cpu_memory': 'str',
        'description': 'str',
        'instance_name': 'str',
        'instance_user_domain_id': 'str',
        'instance_user_id': 'str',
        'is_temporary': 'bool',
        'plugins': 'list[Plugin]',
        'pvc_quantity': 'str',
        'refresh_time': 'str',
        'stack_id': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'cpu_memory': 'cpu_memory',
        'description': 'description',
        'instance_name': 'instance_name',
        'instance_user_domain_id': 'instance_user_domain_id',
        'instance_user_id': 'instance_user_id',
        'is_temporary': 'is_temporary',
        'plugins': 'plugins',
        'pvc_quantity': 'pvc_quantity',
        'refresh_time': 'refresh_time',
        'stack_id': 'stack_id'
    }

    def __init__(self, arch=None, cpu_memory=None, description=None, instance_name=None, instance_user_domain_id=None, instance_user_id=None, is_temporary=None, plugins=None, pvc_quantity=None, refresh_time=None, stack_id=None):
        """InstanceEdgeParam

        The model defined in huaweicloud sdk

        :param arch: cpu架构 x86|arm
        :type arch: str
        :param cpu_memory: cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G
        :type cpu_memory: str
        :param description: 描述。长度不操过100个字符
        :type description: str
        :param instance_name: 实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间
        :type instance_name: str
        :param instance_user_domain_id: 租户id（对应华为云帐号的domainId）
        :type instance_user_domain_id: str
        :param instance_user_id: 用户id
        :type instance_user_id: str
        :param is_temporary: 是否页面显示（以标签配置为准）
        :type is_temporary: bool
        :param plugins: 插件列表
        :type plugins: list[:class:`huaweicloudsdkcloudide.v2.Plugin`]
        :param pvc_quantity: PVC规格 5GB|10GB|20GB
        :type pvc_quantity: str
        :param refresh_time: 自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。
        :type refresh_time: str
        :param stack_id: 技术栈ID，通过技术栈管理ListStacks接口获取。
        :type stack_id: str
        """
        
        

        self._arch = None
        self._cpu_memory = None
        self._description = None
        self._instance_name = None
        self._instance_user_domain_id = None
        self._instance_user_id = None
        self._is_temporary = None
        self._plugins = None
        self._pvc_quantity = None
        self._refresh_time = None
        self._stack_id = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        self.cpu_memory = cpu_memory
        if description is not None:
            self.description = description
        self.instance_name = instance_name
        if instance_user_domain_id is not None:
            self.instance_user_domain_id = instance_user_domain_id
        if instance_user_id is not None:
            self.instance_user_id = instance_user_id
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if plugins is not None:
            self.plugins = plugins
        self.pvc_quantity = pvc_quantity
        if refresh_time is not None:
            self.refresh_time = refresh_time
        self.stack_id = stack_id

    @property
    def arch(self):
        """Gets the arch of this InstanceEdgeParam.

        cpu架构 x86|arm

        :return: The arch of this InstanceEdgeParam.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this InstanceEdgeParam.

        cpu架构 x86|arm

        :param arch: The arch of this InstanceEdgeParam.
        :type arch: str
        """
        self._arch = arch

    @property
    def cpu_memory(self):
        """Gets the cpu_memory of this InstanceEdgeParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :return: The cpu_memory of this InstanceEdgeParam.
        :rtype: str
        """
        return self._cpu_memory

    @cpu_memory.setter
    def cpu_memory(self, cpu_memory):
        """Sets the cpu_memory of this InstanceEdgeParam.

        cpu规格.arm架构支持4U8G，x86架构支持1U1G,2U4G,2U8G 与技术栈配置的规格对应，可通过技术栈管理ListStacks接口获取。如果标签不为空，以标签配置的技术栈规格为准。 quantum技术栈，x86架构cpu规格为2U8G;其他技术栈，x86架构cpu规格为1U1G,2U4G

        :param cpu_memory: The cpu_memory of this InstanceEdgeParam.
        :type cpu_memory: str
        """
        self._cpu_memory = cpu_memory

    @property
    def description(self):
        """Gets the description of this InstanceEdgeParam.

        描述。长度不操过100个字符

        :return: The description of this InstanceEdgeParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceEdgeParam.

        描述。长度不操过100个字符

        :param description: The description of this InstanceEdgeParam.
        :type description: str
        """
        self._description = description

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceEdgeParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The instance_name of this InstanceEdgeParam.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceEdgeParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param instance_name: The instance_name of this InstanceEdgeParam.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_user_domain_id(self):
        """Gets the instance_user_domain_id of this InstanceEdgeParam.

        租户id（对应华为云帐号的domainId）

        :return: The instance_user_domain_id of this InstanceEdgeParam.
        :rtype: str
        """
        return self._instance_user_domain_id

    @instance_user_domain_id.setter
    def instance_user_domain_id(self, instance_user_domain_id):
        """Sets the instance_user_domain_id of this InstanceEdgeParam.

        租户id（对应华为云帐号的domainId）

        :param instance_user_domain_id: The instance_user_domain_id of this InstanceEdgeParam.
        :type instance_user_domain_id: str
        """
        self._instance_user_domain_id = instance_user_domain_id

    @property
    def instance_user_id(self):
        """Gets the instance_user_id of this InstanceEdgeParam.

        用户id

        :return: The instance_user_id of this InstanceEdgeParam.
        :rtype: str
        """
        return self._instance_user_id

    @instance_user_id.setter
    def instance_user_id(self, instance_user_id):
        """Sets the instance_user_id of this InstanceEdgeParam.

        用户id

        :param instance_user_id: The instance_user_id of this InstanceEdgeParam.
        :type instance_user_id: str
        """
        self._instance_user_id = instance_user_id

    @property
    def is_temporary(self):
        """Gets the is_temporary of this InstanceEdgeParam.

        是否页面显示（以标签配置为准）

        :return: The is_temporary of this InstanceEdgeParam.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this InstanceEdgeParam.

        是否页面显示（以标签配置为准）

        :param is_temporary: The is_temporary of this InstanceEdgeParam.
        :type is_temporary: bool
        """
        self._is_temporary = is_temporary

    @property
    def plugins(self):
        """Gets the plugins of this InstanceEdgeParam.

        插件列表

        :return: The plugins of this InstanceEdgeParam.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.Plugin`]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this InstanceEdgeParam.

        插件列表

        :param plugins: The plugins of this InstanceEdgeParam.
        :type plugins: list[:class:`huaweicloudsdkcloudide.v2.Plugin`]
        """
        self._plugins = plugins

    @property
    def pvc_quantity(self):
        """Gets the pvc_quantity of this InstanceEdgeParam.

        PVC规格 5GB|10GB|20GB

        :return: The pvc_quantity of this InstanceEdgeParam.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        """Sets the pvc_quantity of this InstanceEdgeParam.

        PVC规格 5GB|10GB|20GB

        :param pvc_quantity: The pvc_quantity of this InstanceEdgeParam.
        :type pvc_quantity: str
        """
        self._pvc_quantity = pvc_quantity

    @property
    def refresh_time(self):
        """Gets the refresh_time of this InstanceEdgeParam.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :return: The refresh_time of this InstanceEdgeParam.
        :rtype: str
        """
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, refresh_time):
        """Sets the refresh_time of this InstanceEdgeParam.

        自动休眠时长。 arm架构,自动休眠时长只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例无操作超过自动休眠时长后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :param refresh_time: The refresh_time of this InstanceEdgeParam.
        :type refresh_time: str
        """
        self._refresh_time = refresh_time

    @property
    def stack_id(self):
        """Gets the stack_id of this InstanceEdgeParam.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :return: The stack_id of this InstanceEdgeParam.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this InstanceEdgeParam.

        技术栈ID，通过技术栈管理ListStacks接口获取。

        :param stack_id: The stack_id of this InstanceEdgeParam.
        :type stack_id: str
        """
        self._stack_id = stack_id

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
        if not isinstance(other, InstanceEdgeParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
