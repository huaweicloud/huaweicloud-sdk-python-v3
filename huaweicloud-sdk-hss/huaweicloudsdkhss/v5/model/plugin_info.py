# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'installed_attachment_num': 'int',
        'uninstall_attachment_num': 'int',
        'max_cpu_limit': 'int',
        'max_memory_limit': 'int',
        'max_size': 'str',
        'display_mode': 'int'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'installed_attachment_num': 'installed_attachment_num',
        'uninstall_attachment_num': 'uninstall_attachment_num',
        'max_cpu_limit': 'max_cpu_limit',
        'max_memory_limit': 'max_memory_limit',
        'max_size': 'max_size',
        'display_mode': 'display_mode'
    }

    def __init__(self, code=None, name=None, description=None, tags=None, installed_attachment_num=None, uninstall_attachment_num=None, max_cpu_limit=None, max_memory_limit=None, max_size=None, display_mode=None):
        r"""PluginInfo

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 插件编码 **取值范围**: 不涉及 
        :type code: str
        :param name: **参数解释**： 插件名称 **取值范围**: 不涉及 
        :type name: str
        :param description: **参数解释**： 插件的描述信息 **取值范围**: 不涉及 
        :type description: str
        :param tags: **参数解释**： 插件标签信息 **取值范围**: 不涉及 
        :type tags: list[str]
        :param installed_attachment_num: **参数解释**： 已安装插件的主机数量 **取值范围**: 不涉及 
        :type installed_attachment_num: int
        :param uninstall_attachment_num: **参数解释**： 未安装插件的主机数量，包括插件状态为未安装、安装中与安装失败的主机 **取值范围**: 不涉及 
        :type uninstall_attachment_num: int
        :param max_cpu_limit: **参数解释**： 此种类型的插件包中，运行插件所需单核CPU(0-100%)的最大值 **取值范围**: 不涉及 
        :type max_cpu_limit: int
        :param max_memory_limit: **参数解释**： 此种类型的插件包中，运行插件所需内存(MB)的最大值 **取值范围**: 不涉及 
        :type max_memory_limit: int
        :param max_size: **参数解释**： 此种类型的插件包中，插件大小(MB)的最大值 **取值范围**: 不涉及 
        :type max_size: str
        :param display_mode: **参数解释**： 插件展示模式 **取值范围**: - 0：插件所有操作功能均支持 - 1：不支持插件的安装、卸载操作 - 2：插件所有操作功能均不支持 
        :type display_mode: int
        """
        
        

        self._code = None
        self._name = None
        self._description = None
        self._tags = None
        self._installed_attachment_num = None
        self._uninstall_attachment_num = None
        self._max_cpu_limit = None
        self._max_memory_limit = None
        self._max_size = None
        self._display_mode = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if installed_attachment_num is not None:
            self.installed_attachment_num = installed_attachment_num
        if uninstall_attachment_num is not None:
            self.uninstall_attachment_num = uninstall_attachment_num
        if max_cpu_limit is not None:
            self.max_cpu_limit = max_cpu_limit
        if max_memory_limit is not None:
            self.max_memory_limit = max_memory_limit
        if max_size is not None:
            self.max_size = max_size
        if display_mode is not None:
            self.display_mode = display_mode

    @property
    def code(self):
        r"""Gets the code of this PluginInfo.

        **参数解释**： 插件编码 **取值范围**: 不涉及 

        :return: The code of this PluginInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this PluginInfo.

        **参数解释**： 插件编码 **取值范围**: 不涉及 

        :param code: The code of this PluginInfo.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this PluginInfo.

        **参数解释**： 插件名称 **取值范围**: 不涉及 

        :return: The name of this PluginInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PluginInfo.

        **参数解释**： 插件名称 **取值范围**: 不涉及 

        :param name: The name of this PluginInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PluginInfo.

        **参数解释**： 插件的描述信息 **取值范围**: 不涉及 

        :return: The description of this PluginInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PluginInfo.

        **参数解释**： 插件的描述信息 **取值范围**: 不涉及 

        :param description: The description of this PluginInfo.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this PluginInfo.

        **参数解释**： 插件标签信息 **取值范围**: 不涉及 

        :return: The tags of this PluginInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PluginInfo.

        **参数解释**： 插件标签信息 **取值范围**: 不涉及 

        :param tags: The tags of this PluginInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def installed_attachment_num(self):
        r"""Gets the installed_attachment_num of this PluginInfo.

        **参数解释**： 已安装插件的主机数量 **取值范围**: 不涉及 

        :return: The installed_attachment_num of this PluginInfo.
        :rtype: int
        """
        return self._installed_attachment_num

    @installed_attachment_num.setter
    def installed_attachment_num(self, installed_attachment_num):
        r"""Sets the installed_attachment_num of this PluginInfo.

        **参数解释**： 已安装插件的主机数量 **取值范围**: 不涉及 

        :param installed_attachment_num: The installed_attachment_num of this PluginInfo.
        :type installed_attachment_num: int
        """
        self._installed_attachment_num = installed_attachment_num

    @property
    def uninstall_attachment_num(self):
        r"""Gets the uninstall_attachment_num of this PluginInfo.

        **参数解释**： 未安装插件的主机数量，包括插件状态为未安装、安装中与安装失败的主机 **取值范围**: 不涉及 

        :return: The uninstall_attachment_num of this PluginInfo.
        :rtype: int
        """
        return self._uninstall_attachment_num

    @uninstall_attachment_num.setter
    def uninstall_attachment_num(self, uninstall_attachment_num):
        r"""Sets the uninstall_attachment_num of this PluginInfo.

        **参数解释**： 未安装插件的主机数量，包括插件状态为未安装、安装中与安装失败的主机 **取值范围**: 不涉及 

        :param uninstall_attachment_num: The uninstall_attachment_num of this PluginInfo.
        :type uninstall_attachment_num: int
        """
        self._uninstall_attachment_num = uninstall_attachment_num

    @property
    def max_cpu_limit(self):
        r"""Gets the max_cpu_limit of this PluginInfo.

        **参数解释**： 此种类型的插件包中，运行插件所需单核CPU(0-100%)的最大值 **取值范围**: 不涉及 

        :return: The max_cpu_limit of this PluginInfo.
        :rtype: int
        """
        return self._max_cpu_limit

    @max_cpu_limit.setter
    def max_cpu_limit(self, max_cpu_limit):
        r"""Sets the max_cpu_limit of this PluginInfo.

        **参数解释**： 此种类型的插件包中，运行插件所需单核CPU(0-100%)的最大值 **取值范围**: 不涉及 

        :param max_cpu_limit: The max_cpu_limit of this PluginInfo.
        :type max_cpu_limit: int
        """
        self._max_cpu_limit = max_cpu_limit

    @property
    def max_memory_limit(self):
        r"""Gets the max_memory_limit of this PluginInfo.

        **参数解释**： 此种类型的插件包中，运行插件所需内存(MB)的最大值 **取值范围**: 不涉及 

        :return: The max_memory_limit of this PluginInfo.
        :rtype: int
        """
        return self._max_memory_limit

    @max_memory_limit.setter
    def max_memory_limit(self, max_memory_limit):
        r"""Sets the max_memory_limit of this PluginInfo.

        **参数解释**： 此种类型的插件包中，运行插件所需内存(MB)的最大值 **取值范围**: 不涉及 

        :param max_memory_limit: The max_memory_limit of this PluginInfo.
        :type max_memory_limit: int
        """
        self._max_memory_limit = max_memory_limit

    @property
    def max_size(self):
        r"""Gets the max_size of this PluginInfo.

        **参数解释**： 此种类型的插件包中，插件大小(MB)的最大值 **取值范围**: 不涉及 

        :return: The max_size of this PluginInfo.
        :rtype: str
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        r"""Sets the max_size of this PluginInfo.

        **参数解释**： 此种类型的插件包中，插件大小(MB)的最大值 **取值范围**: 不涉及 

        :param max_size: The max_size of this PluginInfo.
        :type max_size: str
        """
        self._max_size = max_size

    @property
    def display_mode(self):
        r"""Gets the display_mode of this PluginInfo.

        **参数解释**： 插件展示模式 **取值范围**: - 0：插件所有操作功能均支持 - 1：不支持插件的安装、卸载操作 - 2：插件所有操作功能均不支持 

        :return: The display_mode of this PluginInfo.
        :rtype: int
        """
        return self._display_mode

    @display_mode.setter
    def display_mode(self, display_mode):
        r"""Sets the display_mode of this PluginInfo.

        **参数解释**： 插件展示模式 **取值范围**: - 0：插件所有操作功能均支持 - 1：不支持插件的安装、卸载操作 - 2：插件所有操作功能均不支持 

        :param display_mode: The display_mode of this PluginInfo.
        :type display_mode: int
        """
        self._display_mode = display_mode

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
        if not isinstance(other, PluginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
