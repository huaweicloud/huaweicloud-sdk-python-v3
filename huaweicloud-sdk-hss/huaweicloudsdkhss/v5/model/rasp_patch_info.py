# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RaspPatchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chk_feature_id': 'int',
        'patch_name': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'cve_list': 'list[RaspCveInfo]',
        'artifact': 'str',
        'vuln_version': 'str',
        'plugin_version': 'str',
        'description': 'str',
        'optional_protective_action': 'int',
        'protective_action': 'int'
    }

    attribute_map = {
        'chk_feature_id': 'chk_feature_id',
        'patch_name': 'patch_name',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'cve_list': 'cve_list',
        'artifact': 'artifact',
        'vuln_version': 'vuln_version',
        'plugin_version': 'plugin_version',
        'description': 'description',
        'optional_protective_action': 'optional_protective_action',
        'protective_action': 'protective_action'
    }

    def __init__(self, chk_feature_id=None, patch_name=None, vul_id=None, vul_name=None, cve_list=None, artifact=None, vuln_version=None, plugin_version=None, description=None, optional_protective_action=None, protective_action=None):
        r"""RaspPatchInfo

        The model defined in huaweicloud sdk

        :param chk_feature_id: **参数解释**: 特征检查项ID **取值范围**: 最小值0，最大值2097152 
        :type chk_feature_id: int
        :param patch_name: **参数解释**: 补丁名称 **取值范围**: 字符长度0-128位 
        :type patch_name: str
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512位 
        :type vul_name: str
        :param cve_list: **参数解释**: CVE列表 **取值范围**: 0-128个RaspCveInfo对象 
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.RaspCveInfo`]
        :param artifact: **参数解释**: 目标组件 **取值范围**: 字符长度0-128位 
        :type artifact: str
        :param vuln_version: **参数解释**: 影响版本 **取值范围**: 字符长度0-128位 
        :type vuln_version: str
        :param plugin_version: **参数解释**: 补丁版本 **取值范围**: 字符长度0-64位 
        :type plugin_version: str
        :param description: **参数解释**: 漏洞说明 **取值范围**: 字符长度0-512位 
        :type description: str
        :param optional_protective_action: **参数解释**: 可选防护动作 **取值范围**: 最小值1，最大值3 
        :type optional_protective_action: int
        :param protective_action: **参数解释**: 防护动作 **取值范围**: 最小值1，最大值2 
        :type protective_action: int
        """
        
        

        self._chk_feature_id = None
        self._patch_name = None
        self._vul_id = None
        self._vul_name = None
        self._cve_list = None
        self._artifact = None
        self._vuln_version = None
        self._plugin_version = None
        self._description = None
        self._optional_protective_action = None
        self._protective_action = None
        self.discriminator = None

        if chk_feature_id is not None:
            self.chk_feature_id = chk_feature_id
        if patch_name is not None:
            self.patch_name = patch_name
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if cve_list is not None:
            self.cve_list = cve_list
        if artifact is not None:
            self.artifact = artifact
        if vuln_version is not None:
            self.vuln_version = vuln_version
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if description is not None:
            self.description = description
        if optional_protective_action is not None:
            self.optional_protective_action = optional_protective_action
        if protective_action is not None:
            self.protective_action = protective_action

    @property
    def chk_feature_id(self):
        r"""Gets the chk_feature_id of this RaspPatchInfo.

        **参数解释**: 特征检查项ID **取值范围**: 最小值0，最大值2097152 

        :return: The chk_feature_id of this RaspPatchInfo.
        :rtype: int
        """
        return self._chk_feature_id

    @chk_feature_id.setter
    def chk_feature_id(self, chk_feature_id):
        r"""Sets the chk_feature_id of this RaspPatchInfo.

        **参数解释**: 特征检查项ID **取值范围**: 最小值0，最大值2097152 

        :param chk_feature_id: The chk_feature_id of this RaspPatchInfo.
        :type chk_feature_id: int
        """
        self._chk_feature_id = chk_feature_id

    @property
    def patch_name(self):
        r"""Gets the patch_name of this RaspPatchInfo.

        **参数解释**: 补丁名称 **取值范围**: 字符长度0-128位 

        :return: The patch_name of this RaspPatchInfo.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        r"""Sets the patch_name of this RaspPatchInfo.

        **参数解释**: 补丁名称 **取值范围**: 字符长度0-128位 

        :param patch_name: The patch_name of this RaspPatchInfo.
        :type patch_name: str
        """
        self._patch_name = patch_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this RaspPatchInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :return: The vul_id of this RaspPatchInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this RaspPatchInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :param vul_id: The vul_id of this RaspPatchInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this RaspPatchInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512位 

        :return: The vul_name of this RaspPatchInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this RaspPatchInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512位 

        :param vul_name: The vul_name of this RaspPatchInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def cve_list(self):
        r"""Gets the cve_list of this RaspPatchInfo.

        **参数解释**: CVE列表 **取值范围**: 0-128个RaspCveInfo对象 

        :return: The cve_list of this RaspPatchInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RaspCveInfo`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this RaspPatchInfo.

        **参数解释**: CVE列表 **取值范围**: 0-128个RaspCveInfo对象 

        :param cve_list: The cve_list of this RaspPatchInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.RaspCveInfo`]
        """
        self._cve_list = cve_list

    @property
    def artifact(self):
        r"""Gets the artifact of this RaspPatchInfo.

        **参数解释**: 目标组件 **取值范围**: 字符长度0-128位 

        :return: The artifact of this RaspPatchInfo.
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        r"""Sets the artifact of this RaspPatchInfo.

        **参数解释**: 目标组件 **取值范围**: 字符长度0-128位 

        :param artifact: The artifact of this RaspPatchInfo.
        :type artifact: str
        """
        self._artifact = artifact

    @property
    def vuln_version(self):
        r"""Gets the vuln_version of this RaspPatchInfo.

        **参数解释**: 影响版本 **取值范围**: 字符长度0-128位 

        :return: The vuln_version of this RaspPatchInfo.
        :rtype: str
        """
        return self._vuln_version

    @vuln_version.setter
    def vuln_version(self, vuln_version):
        r"""Sets the vuln_version of this RaspPatchInfo.

        **参数解释**: 影响版本 **取值范围**: 字符长度0-128位 

        :param vuln_version: The vuln_version of this RaspPatchInfo.
        :type vuln_version: str
        """
        self._vuln_version = vuln_version

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this RaspPatchInfo.

        **参数解释**: 补丁版本 **取值范围**: 字符长度0-64位 

        :return: The plugin_version of this RaspPatchInfo.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this RaspPatchInfo.

        **参数解释**: 补丁版本 **取值范围**: 字符长度0-64位 

        :param plugin_version: The plugin_version of this RaspPatchInfo.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def description(self):
        r"""Gets the description of this RaspPatchInfo.

        **参数解释**: 漏洞说明 **取值范围**: 字符长度0-512位 

        :return: The description of this RaspPatchInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RaspPatchInfo.

        **参数解释**: 漏洞说明 **取值范围**: 字符长度0-512位 

        :param description: The description of this RaspPatchInfo.
        :type description: str
        """
        self._description = description

    @property
    def optional_protective_action(self):
        r"""Gets the optional_protective_action of this RaspPatchInfo.

        **参数解释**: 可选防护动作 **取值范围**: 最小值1，最大值3 

        :return: The optional_protective_action of this RaspPatchInfo.
        :rtype: int
        """
        return self._optional_protective_action

    @optional_protective_action.setter
    def optional_protective_action(self, optional_protective_action):
        r"""Sets the optional_protective_action of this RaspPatchInfo.

        **参数解释**: 可选防护动作 **取值范围**: 最小值1，最大值3 

        :param optional_protective_action: The optional_protective_action of this RaspPatchInfo.
        :type optional_protective_action: int
        """
        self._optional_protective_action = optional_protective_action

    @property
    def protective_action(self):
        r"""Gets the protective_action of this RaspPatchInfo.

        **参数解释**: 防护动作 **取值范围**: 最小值1，最大值2 

        :return: The protective_action of this RaspPatchInfo.
        :rtype: int
        """
        return self._protective_action

    @protective_action.setter
    def protective_action(self, protective_action):
        r"""Sets the protective_action of this RaspPatchInfo.

        **参数解释**: 防护动作 **取值范围**: 最小值1，最大值2 

        :param protective_action: The protective_action of this RaspPatchInfo.
        :type protective_action: int
        """
        self._protective_action = protective_action

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
        if not isinstance(other, RaspPatchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
