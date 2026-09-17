# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeAddonConfig:

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
        'operation': 'str',
        'version': 'str',
        'values': 'object'
    }

    attribute_map = {
        'addon_template_name': 'addonTemplateName',
        'operation': 'operation',
        'version': 'version',
        'values': 'values'
    }

    def __init__(self, addon_template_name=None, operation=None, version=None, values=None):
        r"""UpgradeAddonConfig

        The model defined in huaweicloud sdk

        :param addon_template_name: **参数解释：** CCE插件名称 **约束限制：** 不涉及 **取值范围：** 集群中已安装的插件名称。[集群中已安装插件详情见[获取AddonInstance列表](https://support.huaweicloud.com/api-cce/cce_02_0326.html)](tag:hws) **默认取值：** 不涉及
        :type addon_template_name: str
        :param operation: **参数解释：** 升级插件的执行动作 **约束限制：** 不涉及 **取值范围：** - patch：表示升级插件版本  **默认取值：** 不涉及
        :type operation: str
        :param version: **参数解释：** 目标插件版本号 **约束限制：** 目标插件版本必须与目标集群版本配套。[集群版本配套关系见[查询AddonTemplates列表](https://support.huaweicloud.com/api-cce/cce_02_0321.html)](tag:hws) **取值范围：** 不涉及 **默认取值：** 不涉及
        :type version: str
        :param values: **参数解释：** 插件参数列表，Key:Value格式。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type values: object
        """
        
        

        self._addon_template_name = None
        self._operation = None
        self._version = None
        self._values = None
        self.discriminator = None

        self.addon_template_name = addon_template_name
        self.operation = operation
        self.version = version
        if values is not None:
            self.values = values

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this UpgradeAddonConfig.

        **参数解释：** CCE插件名称 **约束限制：** 不涉及 **取值范围：** 集群中已安装的插件名称。[集群中已安装插件详情见[获取AddonInstance列表](https://support.huaweicloud.com/api-cce/cce_02_0326.html)](tag:hws) **默认取值：** 不涉及

        :return: The addon_template_name of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this UpgradeAddonConfig.

        **参数解释：** CCE插件名称 **约束限制：** 不涉及 **取值范围：** 集群中已安装的插件名称。[集群中已安装插件详情见[获取AddonInstance列表](https://support.huaweicloud.com/api-cce/cce_02_0326.html)](tag:hws) **默认取值：** 不涉及

        :param addon_template_name: The addon_template_name of this UpgradeAddonConfig.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def operation(self):
        r"""Gets the operation of this UpgradeAddonConfig.

        **参数解释：** 升级插件的执行动作 **约束限制：** 不涉及 **取值范围：** - patch：表示升级插件版本  **默认取值：** 不涉及

        :return: The operation of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this UpgradeAddonConfig.

        **参数解释：** 升级插件的执行动作 **约束限制：** 不涉及 **取值范围：** - patch：表示升级插件版本  **默认取值：** 不涉及

        :param operation: The operation of this UpgradeAddonConfig.
        :type operation: str
        """
        self._operation = operation

    @property
    def version(self):
        r"""Gets the version of this UpgradeAddonConfig.

        **参数解释：** 目标插件版本号 **约束限制：** 目标插件版本必须与目标集群版本配套。[集群版本配套关系见[查询AddonTemplates列表](https://support.huaweicloud.com/api-cce/cce_02_0321.html)](tag:hws) **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The version of this UpgradeAddonConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpgradeAddonConfig.

        **参数解释：** 目标插件版本号 **约束限制：** 目标插件版本必须与目标集群版本配套。[集群版本配套关系见[查询AddonTemplates列表](https://support.huaweicloud.com/api-cce/cce_02_0321.html)](tag:hws) **取值范围：** 不涉及 **默认取值：** 不涉及

        :param version: The version of this UpgradeAddonConfig.
        :type version: str
        """
        self._version = version

    @property
    def values(self):
        r"""Gets the values of this UpgradeAddonConfig.

        **参数解释：** 插件参数列表，Key:Value格式。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The values of this UpgradeAddonConfig.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpgradeAddonConfig.

        **参数解释：** 插件参数列表，Key:Value格式。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param values: The values of this UpgradeAddonConfig.
        :type values: object
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
        if not isinstance(other, UpgradeAddonConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
