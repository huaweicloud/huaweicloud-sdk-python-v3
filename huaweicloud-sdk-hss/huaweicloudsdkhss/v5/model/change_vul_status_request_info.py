# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'remark': 'str',
        'select_type': 'str',
        'type': 'str',
        'data_list': 'list[VulOperateInfo]',
        'host_data_list': 'list[HostVulOperateInfo]',
        'backup_info_id': 'str',
        'custom_backup_hosts': 'list[ChangeVulStatusRequestInfoCustomBackupHosts]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'remark': 'remark',
        'select_type': 'select_type',
        'type': 'type',
        'data_list': 'data_list',
        'host_data_list': 'host_data_list',
        'backup_info_id': 'backup_info_id',
        'custom_backup_hosts': 'custom_backup_hosts'
    }

    def __init__(self, operate_type=None, remark=None, select_type=None, type=None, data_list=None, host_data_list=None, backup_info_id=None, custom_backup_hosts=None):
        r"""ChangeVulStatusRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: **参数解释**: 对漏洞进行的处置操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略 - immediate_repair：修复 - manual_repair：人工修复 - verify：验证 - add_to_whitelist：加入白名单  **默认取值**: 不涉及 
        :type operate_type: str
        :param remark: **参数解释**: 本次处置操作的备注信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 
        :type remark: str
        :param select_type: **参数解释**: 处置全部漏洞的类型 **约束限制**: 只有需要对全部漏洞进行处置时需要该参数 **取值范围**: - all_vul：按照指定漏洞类型处置全部漏洞 - all_host：处置全部主机的漏洞  **默认取值**: 不涉及 
        :type select_type: str
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：漏洞类型-linux漏洞 - windows_vul：漏洞类型-windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: linux_vul 
        :type type: str
        :param data_list: **参数解释**: 通过漏洞维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        :param host_data_list: **参数解释**: 通过主机维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        :param backup_info_id: **参数解释**: 本次漏洞处置对应的备份信息id，若不传该参数，则不进行备份 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type backup_info_id: str
        :param custom_backup_hosts: **参数解释**: 自定义备份主机使用的存储库及备份名称列表。不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称 **约束限制**: 只有backup_info_id有值时该参数才会生效 **取值范围**: 最小值1，最大值50 **默认取值**: 不涉及 
        :type custom_backup_hosts: list[:class:`huaweicloudsdkhss.v5.ChangeVulStatusRequestInfoCustomBackupHosts`]
        """
        
        

        self._operate_type = None
        self._remark = None
        self._select_type = None
        self._type = None
        self._data_list = None
        self._host_data_list = None
        self._backup_info_id = None
        self._custom_backup_hosts = None
        self.discriminator = None

        self.operate_type = operate_type
        if remark is not None:
            self.remark = remark
        if select_type is not None:
            self.select_type = select_type
        if type is not None:
            self.type = type
        if data_list is not None:
            self.data_list = data_list
        if host_data_list is not None:
            self.host_data_list = host_data_list
        if backup_info_id is not None:
            self.backup_info_id = backup_info_id
        if custom_backup_hosts is not None:
            self.custom_backup_hosts = custom_backup_hosts

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ChangeVulStatusRequestInfo.

        **参数解释**: 对漏洞进行的处置操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略 - immediate_repair：修复 - manual_repair：人工修复 - verify：验证 - add_to_whitelist：加入白名单  **默认取值**: 不涉及 

        :return: The operate_type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ChangeVulStatusRequestInfo.

        **参数解释**: 对漏洞进行的处置操作类型 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略 - immediate_repair：修复 - manual_repair：人工修复 - verify：验证 - add_to_whitelist：加入白名单  **默认取值**: 不涉及 

        :param operate_type: The operate_type of this ChangeVulStatusRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def remark(self):
        r"""Gets the remark of this ChangeVulStatusRequestInfo.

        **参数解释**: 本次处置操作的备注信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :return: The remark of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ChangeVulStatusRequestInfo.

        **参数解释**: 本次处置操作的备注信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :param remark: The remark of this ChangeVulStatusRequestInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def select_type(self):
        r"""Gets the select_type of this ChangeVulStatusRequestInfo.

        **参数解释**: 处置全部漏洞的类型 **约束限制**: 只有需要对全部漏洞进行处置时需要该参数 **取值范围**: - all_vul：按照指定漏洞类型处置全部漏洞 - all_host：处置全部主机的漏洞  **默认取值**: 不涉及 

        :return: The select_type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        r"""Sets the select_type of this ChangeVulStatusRequestInfo.

        **参数解释**: 处置全部漏洞的类型 **约束限制**: 只有需要对全部漏洞进行处置时需要该参数 **取值范围**: - all_vul：按照指定漏洞类型处置全部漏洞 - all_host：处置全部主机的漏洞  **默认取值**: 不涉及 

        :param select_type: The select_type of this ChangeVulStatusRequestInfo.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def type(self):
        r"""Gets the type of this ChangeVulStatusRequestInfo.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：漏洞类型-linux漏洞 - windows_vul：漏洞类型-windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: linux_vul 

        :return: The type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChangeVulStatusRequestInfo.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：漏洞类型-linux漏洞 - windows_vul：漏洞类型-windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: linux_vul 

        :param type: The type of this ChangeVulStatusRequestInfo.
        :type type: str
        """
        self._type = type

    @property
    def data_list(self):
        r"""Gets the data_list of this ChangeVulStatusRequestInfo.

        **参数解释**: 通过漏洞维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :return: The data_list of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ChangeVulStatusRequestInfo.

        **参数解释**: 通过漏洞维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :param data_list: The data_list of this ChangeVulStatusRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        self._data_list = data_list

    @property
    def host_data_list(self):
        r"""Gets the host_data_list of this ChangeVulStatusRequestInfo.

        **参数解释**: 通过主机维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :return: The host_data_list of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        return self._host_data_list

    @host_data_list.setter
    def host_data_list(self, host_data_list):
        r"""Sets the host_data_list of this ChangeVulStatusRequestInfo.

        **参数解释**: 通过主机维度指定需要处置的漏洞信息 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :param host_data_list: The host_data_list of this ChangeVulStatusRequestInfo.
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        self._host_data_list = host_data_list

    @property
    def backup_info_id(self):
        r"""Gets the backup_info_id of this ChangeVulStatusRequestInfo.

        **参数解释**: 本次漏洞处置对应的备份信息id，若不传该参数，则不进行备份 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The backup_info_id of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._backup_info_id

    @backup_info_id.setter
    def backup_info_id(self, backup_info_id):
        r"""Sets the backup_info_id of this ChangeVulStatusRequestInfo.

        **参数解释**: 本次漏洞处置对应的备份信息id，若不传该参数，则不进行备份 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param backup_info_id: The backup_info_id of this ChangeVulStatusRequestInfo.
        :type backup_info_id: str
        """
        self._backup_info_id = backup_info_id

    @property
    def custom_backup_hosts(self):
        r"""Gets the custom_backup_hosts of this ChangeVulStatusRequestInfo.

        **参数解释**: 自定义备份主机使用的存储库及备份名称列表。不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称 **约束限制**: 只有backup_info_id有值时该参数才会生效 **取值范围**: 最小值1，最大值50 **默认取值**: 不涉及 

        :return: The custom_backup_hosts of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ChangeVulStatusRequestInfoCustomBackupHosts`]
        """
        return self._custom_backup_hosts

    @custom_backup_hosts.setter
    def custom_backup_hosts(self, custom_backup_hosts):
        r"""Sets the custom_backup_hosts of this ChangeVulStatusRequestInfo.

        **参数解释**: 自定义备份主机使用的存储库及备份名称列表。不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称 **约束限制**: 只有backup_info_id有值时该参数才会生效 **取值范围**: 最小值1，最大值50 **默认取值**: 不涉及 

        :param custom_backup_hosts: The custom_backup_hosts of this ChangeVulStatusRequestInfo.
        :type custom_backup_hosts: list[:class:`huaweicloudsdkhss.v5.ChangeVulStatusRequestInfoCustomBackupHosts`]
        """
        self._custom_backup_hosts = custom_backup_hosts

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
        if not isinstance(other, ChangeVulStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
