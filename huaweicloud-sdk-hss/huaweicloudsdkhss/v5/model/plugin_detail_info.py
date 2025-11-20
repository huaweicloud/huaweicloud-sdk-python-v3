# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'version': 'str',
        'agent_version': 'str',
        'arch': 'str',
        'os_type': 'str',
        'version_description': 'str',
        'size': 'str',
        'cpu_limit': 'int',
        'memory_limit': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'version': 'version',
        'agent_version': 'agent_version',
        'arch': 'arch',
        'os_type': 'os_type',
        'version_description': 'version_description',
        'size': 'size',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'update_time': 'update_time'
    }

    def __init__(self, name=None, id=None, version=None, agent_version=None, arch=None, os_type=None, version_description=None, size=None, cpu_limit=None, memory_limit=None, update_time=None):
        r"""PluginDetailInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 插件名称 **取值范围**: 不涉及 
        :type name: str
        :param id: **参数解释**： 插件id **取值范围**: 不涉及 
        :type id: str
        :param version: **参数解释**： 插件版本 **取值范围**: 不涉及 
        :type version: str
        :param agent_version: **参数解释**： 插件支持的最低Agent版本 **取值范围**: 不涉及 
        :type agent_version: str
        :param arch: **参数解释**： 插件架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 
        :type arch: str
        :param os_type: **参数解释**： 插件支持的操作系统类型 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 
        :type os_type: str
        :param version_description: **参数解释**： 插件版本信息描述 **取值范围**: 不涉及 
        :type version_description: str
        :param size: **参数解释**： 插件安装包大小(MB) **取值范围**: 不涉及 
        :type size: str
        :param cpu_limit: **参数解释**： 运行插件所需单核CPU(0-100%) **取值范围**: 不涉及 
        :type cpu_limit: int
        :param memory_limit: **参数解释**： 运行插件所需内存(MB) **取值范围**: 不涉及 
        :type memory_limit: int
        :param update_time: **参数解释**： 插件更新时间 **取值范围**: 不涉及 
        :type update_time: int
        """
        
        

        self._name = None
        self._id = None
        self._version = None
        self._agent_version = None
        self._arch = None
        self._os_type = None
        self._version_description = None
        self._size = None
        self._cpu_limit = None
        self._memory_limit = None
        self._update_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if agent_version is not None:
            self.agent_version = agent_version
        if arch is not None:
            self.arch = arch
        if os_type is not None:
            self.os_type = os_type
        if version_description is not None:
            self.version_description = version_description
        if size is not None:
            self.size = size
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if update_time is not None:
            self.update_time = update_time

    @property
    def name(self):
        r"""Gets the name of this PluginDetailInfo.

        **参数解释**： 插件名称 **取值范围**: 不涉及 

        :return: The name of this PluginDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PluginDetailInfo.

        **参数解释**： 插件名称 **取值范围**: 不涉及 

        :param name: The name of this PluginDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this PluginDetailInfo.

        **参数解释**： 插件id **取值范围**: 不涉及 

        :return: The id of this PluginDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PluginDetailInfo.

        **参数解释**： 插件id **取值范围**: 不涉及 

        :param id: The id of this PluginDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this PluginDetailInfo.

        **参数解释**： 插件版本 **取值范围**: 不涉及 

        :return: The version of this PluginDetailInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginDetailInfo.

        **参数解释**： 插件版本 **取值范围**: 不涉及 

        :param version: The version of this PluginDetailInfo.
        :type version: str
        """
        self._version = version

    @property
    def agent_version(self):
        r"""Gets the agent_version of this PluginDetailInfo.

        **参数解释**： 插件支持的最低Agent版本 **取值范围**: 不涉及 

        :return: The agent_version of this PluginDetailInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this PluginDetailInfo.

        **参数解释**： 插件支持的最低Agent版本 **取值范围**: 不涉及 

        :param agent_version: The agent_version of this PluginDetailInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def arch(self):
        r"""Gets the arch of this PluginDetailInfo.

        **参数解释**： 插件架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 

        :return: The arch of this PluginDetailInfo.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this PluginDetailInfo.

        **参数解释**： 插件架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 

        :param arch: The arch of this PluginDetailInfo.
        :type arch: str
        """
        self._arch = arch

    @property
    def os_type(self):
        r"""Gets the os_type of this PluginDetailInfo.

        **参数解释**： 插件支持的操作系统类型 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 

        :return: The os_type of this PluginDetailInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PluginDetailInfo.

        **参数解释**： 插件支持的操作系统类型 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 

        :param os_type: The os_type of this PluginDetailInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def version_description(self):
        r"""Gets the version_description of this PluginDetailInfo.

        **参数解释**： 插件版本信息描述 **取值范围**: 不涉及 

        :return: The version_description of this PluginDetailInfo.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this PluginDetailInfo.

        **参数解释**： 插件版本信息描述 **取值范围**: 不涉及 

        :param version_description: The version_description of this PluginDetailInfo.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def size(self):
        r"""Gets the size of this PluginDetailInfo.

        **参数解释**： 插件安装包大小(MB) **取值范围**: 不涉及 

        :return: The size of this PluginDetailInfo.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PluginDetailInfo.

        **参数解释**： 插件安装包大小(MB) **取值范围**: 不涉及 

        :param size: The size of this PluginDetailInfo.
        :type size: str
        """
        self._size = size

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this PluginDetailInfo.

        **参数解释**： 运行插件所需单核CPU(0-100%) **取值范围**: 不涉及 

        :return: The cpu_limit of this PluginDetailInfo.
        :rtype: int
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this PluginDetailInfo.

        **参数解释**： 运行插件所需单核CPU(0-100%) **取值范围**: 不涉及 

        :param cpu_limit: The cpu_limit of this PluginDetailInfo.
        :type cpu_limit: int
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this PluginDetailInfo.

        **参数解释**： 运行插件所需内存(MB) **取值范围**: 不涉及 

        :return: The memory_limit of this PluginDetailInfo.
        :rtype: int
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this PluginDetailInfo.

        **参数解释**： 运行插件所需内存(MB) **取值范围**: 不涉及 

        :param memory_limit: The memory_limit of this PluginDetailInfo.
        :type memory_limit: int
        """
        self._memory_limit = memory_limit

    @property
    def update_time(self):
        r"""Gets the update_time of this PluginDetailInfo.

        **参数解释**： 插件更新时间 **取值范围**: 不涉及 

        :return: The update_time of this PluginDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PluginDetailInfo.

        **参数解释**： 插件更新时间 **取值范围**: 不涉及 

        :param update_time: The update_time of this PluginDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
