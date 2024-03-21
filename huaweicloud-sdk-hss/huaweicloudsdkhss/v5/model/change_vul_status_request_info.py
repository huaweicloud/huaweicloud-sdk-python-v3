# coding: utf-8

import six

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
        """ChangeVulStatusRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: 操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - manual_repair: 人工修复 - verify : 验证 - add_to_whitelist : 加入白名单
        :type operate_type: str
        :param remark: 备注
        :type remark: str
        :param select_type: 选择全部漏洞类型 - all_vul : 选择全部漏洞 - all_host : 选择全部主机漏洞
        :type select_type: str
        :param type: 漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞
        :type type: str
        :param data_list: 漏洞列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        :param host_data_list: 主机维度漏洞列表
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        :param backup_info_id: 本次漏洞处理的备份信息id，若不传该参数，则不进行备份
        :type backup_info_id: str
        :param custom_backup_hosts: 自定义备份主机使用的存储库及备份名称；不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称
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
        """Gets the operate_type of this ChangeVulStatusRequestInfo.

        操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - manual_repair: 人工修复 - verify : 验证 - add_to_whitelist : 加入白名单

        :return: The operate_type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this ChangeVulStatusRequestInfo.

        操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - manual_repair: 人工修复 - verify : 验证 - add_to_whitelist : 加入白名单

        :param operate_type: The operate_type of this ChangeVulStatusRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def remark(self):
        """Gets the remark of this ChangeVulStatusRequestInfo.

        备注

        :return: The remark of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ChangeVulStatusRequestInfo.

        备注

        :param remark: The remark of this ChangeVulStatusRequestInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def select_type(self):
        """Gets the select_type of this ChangeVulStatusRequestInfo.

        选择全部漏洞类型 - all_vul : 选择全部漏洞 - all_host : 选择全部主机漏洞

        :return: The select_type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        """Sets the select_type of this ChangeVulStatusRequestInfo.

        选择全部漏洞类型 - all_vul : 选择全部漏洞 - all_host : 选择全部主机漏洞

        :param select_type: The select_type of this ChangeVulStatusRequestInfo.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def type(self):
        """Gets the type of this ChangeVulStatusRequestInfo.

        漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :return: The type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChangeVulStatusRequestInfo.

        漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :param type: The type of this ChangeVulStatusRequestInfo.
        :type type: str
        """
        self._type = type

    @property
    def data_list(self):
        """Gets the data_list of this ChangeVulStatusRequestInfo.

        漏洞列表

        :return: The data_list of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ChangeVulStatusRequestInfo.

        漏洞列表

        :param data_list: The data_list of this ChangeVulStatusRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        self._data_list = data_list

    @property
    def host_data_list(self):
        """Gets the host_data_list of this ChangeVulStatusRequestInfo.

        主机维度漏洞列表

        :return: The host_data_list of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        return self._host_data_list

    @host_data_list.setter
    def host_data_list(self, host_data_list):
        """Sets the host_data_list of this ChangeVulStatusRequestInfo.

        主机维度漏洞列表

        :param host_data_list: The host_data_list of this ChangeVulStatusRequestInfo.
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        self._host_data_list = host_data_list

    @property
    def backup_info_id(self):
        """Gets the backup_info_id of this ChangeVulStatusRequestInfo.

        本次漏洞处理的备份信息id，若不传该参数，则不进行备份

        :return: The backup_info_id of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._backup_info_id

    @backup_info_id.setter
    def backup_info_id(self, backup_info_id):
        """Sets the backup_info_id of this ChangeVulStatusRequestInfo.

        本次漏洞处理的备份信息id，若不传该参数，则不进行备份

        :param backup_info_id: The backup_info_id of this ChangeVulStatusRequestInfo.
        :type backup_info_id: str
        """
        self._backup_info_id = backup_info_id

    @property
    def custom_backup_hosts(self):
        """Gets the custom_backup_hosts of this ChangeVulStatusRequestInfo.

        自定义备份主机使用的存储库及备份名称；不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称

        :return: The custom_backup_hosts of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ChangeVulStatusRequestInfoCustomBackupHosts`]
        """
        return self._custom_backup_hosts

    @custom_backup_hosts.setter
    def custom_backup_hosts(self, custom_backup_hosts):
        """Sets the custom_backup_hosts of this ChangeVulStatusRequestInfo.

        自定义备份主机使用的存储库及备份名称；不在该列表中的主机备份时系统会自动选取剩余空间最大的存储库，并自动生成备份名称

        :param custom_backup_hosts: The custom_backup_hosts of this ChangeVulStatusRequestInfo.
        :type custom_backup_hosts: list[:class:`huaweicloudsdkhss.v5.ChangeVulStatusRequestInfoCustomBackupHosts`]
        """
        self._custom_backup_hosts = custom_backup_hosts

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
        if not isinstance(other, ChangeVulStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
