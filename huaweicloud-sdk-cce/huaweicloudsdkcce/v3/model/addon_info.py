# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addon_template_name': 'str',
        'addon_instance_id': 'str',
        'target_version': 'str',
        'type': 'str',
        'values': 'dict(str, object)'
    }

    attribute_map = {
        'addon_template_name': 'addonTemplateName',
        'addon_instance_id': 'addonInstanceID',
        'target_version': 'targetVersion',
        'type': 'type',
        'values': 'values'
    }

    def __init__(self, addon_template_name=None, addon_instance_id=None, target_version=None, type=None, values=None):
        r"""AddonInfo

        The model defined in huaweicloud sdk

        :param addon_template_name: **参数解释：** 插件模板名称 **约束限制：** 不涉及 **取值范围：** cce服务支持的插件模板 **默认取值：** 不涉及 
        :type addon_template_name: str
        :param addon_instance_id: **参数解释：** 插件实例ID，可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 此参数必填 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type addon_instance_id: str
        :param target_version: **参数解释：** 插件升级的目标版本 **约束限制：** 插件升级场景下，此参数必填。 **取值范围：** cce服务提供的插件版本，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].spec.versions.version字段获取 **默认取值：** 不涉及 
        :type target_version: str
        :param type: **参数解释：** 插件检查类型 **约束限制：** 此参数必填。 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 
        :type type: str
        :param values: **参数解释：** 插件模板编辑/升级参数（各插件不同），请根据具体插件模板信息填写参数 **约束限制：** 不涉及 
        :type values: dict(str, object)
        """
        
        

        self._addon_template_name = None
        self._addon_instance_id = None
        self._target_version = None
        self._type = None
        self._values = None
        self.discriminator = None

        self.addon_template_name = addon_template_name
        self.addon_instance_id = addon_instance_id
        if target_version is not None:
            self.target_version = target_version
        self.type = type
        if values is not None:
            self.values = values

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this AddonInfo.

        **参数解释：** 插件模板名称 **约束限制：** 不涉及 **取值范围：** cce服务支持的插件模板 **默认取值：** 不涉及 

        :return: The addon_template_name of this AddonInfo.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this AddonInfo.

        **参数解释：** 插件模板名称 **约束限制：** 不涉及 **取值范围：** cce服务支持的插件模板 **默认取值：** 不涉及 

        :param addon_template_name: The addon_template_name of this AddonInfo.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def addon_instance_id(self):
        r"""Gets the addon_instance_id of this AddonInfo.

        **参数解释：** 插件实例ID，可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 此参数必填 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The addon_instance_id of this AddonInfo.
        :rtype: str
        """
        return self._addon_instance_id

    @addon_instance_id.setter
    def addon_instance_id(self, addon_instance_id):
        r"""Sets the addon_instance_id of this AddonInfo.

        **参数解释：** 插件实例ID，可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 此参数必填 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param addon_instance_id: The addon_instance_id of this AddonInfo.
        :type addon_instance_id: str
        """
        self._addon_instance_id = addon_instance_id

    @property
    def target_version(self):
        r"""Gets the target_version of this AddonInfo.

        **参数解释：** 插件升级的目标版本 **约束限制：** 插件升级场景下，此参数必填。 **取值范围：** cce服务提供的插件版本，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].spec.versions.version字段获取 **默认取值：** 不涉及 

        :return: The target_version of this AddonInfo.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this AddonInfo.

        **参数解释：** 插件升级的目标版本 **约束限制：** 插件升级场景下，此参数必填。 **取值范围：** cce服务提供的插件版本，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].spec.versions.version字段获取 **默认取值：** 不涉及 

        :param target_version: The target_version of this AddonInfo.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def type(self):
        r"""Gets the type of this AddonInfo.

        **参数解释：** 插件检查类型 **约束限制：** 此参数必填。 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 

        :return: The type of this AddonInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddonInfo.

        **参数解释：** 插件检查类型 **约束限制：** 此参数必填。 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 

        :param type: The type of this AddonInfo.
        :type type: str
        """
        self._type = type

    @property
    def values(self):
        r"""Gets the values of this AddonInfo.

        **参数解释：** 插件模板编辑/升级参数（各插件不同），请根据具体插件模板信息填写参数 **约束限制：** 不涉及 

        :return: The values of this AddonInfo.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this AddonInfo.

        **参数解释：** 插件模板编辑/升级参数（各插件不同），请根据具体插件模板信息填写参数 **约束限制：** 不涉及 

        :param values: The values of this AddonInfo.
        :type values: dict(str, object)
        """
        self._values = values

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
        if not isinstance(other, AddonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
