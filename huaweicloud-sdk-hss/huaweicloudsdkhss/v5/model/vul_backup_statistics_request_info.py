# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulBackupStatisticsRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'select_type': 'str',
        'type': 'str',
        'data_list': 'list[VulOperateInfo]',
        'host_data_list': 'list[HostVulOperateInfo]'
    }

    attribute_map = {
        'select_type': 'select_type',
        'type': 'type',
        'data_list': 'data_list',
        'host_data_list': 'host_data_list'
    }

    def __init__(self, select_type=None, type=None, data_list=None, host_data_list=None):
        r"""VulBackupStatisticsRequestInfo

        The model defined in huaweicloud sdk

        :param select_type: **参数解释**: 选择全部漏洞类型，该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 
        :type select_type: str
        :param type: **参数解释**: 漏洞类型，当select_type选择all_vul时，需要传递该参数 **约束限制**: 不涉及 **取值范围**: - linux_vul : 漏洞类型-linux漏洞 - windows_vul : 漏洞类型-windows漏洞 - web_cms : Web-CMS漏洞 - app_vul : 应用漏洞 - urgent_vul : 应急漏洞  **默认取值**: linux_vul 
        :type type: str
        :param data_list: **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        :param host_data_list: **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        
        

        self._select_type = None
        self._type = None
        self._data_list = None
        self._host_data_list = None
        self.discriminator = None

        if select_type is not None:
            self.select_type = select_type
        if type is not None:
            self.type = type
        if data_list is not None:
            self.data_list = data_list
        if host_data_list is not None:
            self.host_data_list = host_data_list

    @property
    def select_type(self):
        r"""Gets the select_type of this VulBackupStatisticsRequestInfo.

        **参数解释**: 选择全部漏洞类型，该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 

        :return: The select_type of this VulBackupStatisticsRequestInfo.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        r"""Sets the select_type of this VulBackupStatisticsRequestInfo.

        **参数解释**: 选择全部漏洞类型，该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 

        :param select_type: The select_type of this VulBackupStatisticsRequestInfo.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def type(self):
        r"""Gets the type of this VulBackupStatisticsRequestInfo.

        **参数解释**: 漏洞类型，当select_type选择all_vul时，需要传递该参数 **约束限制**: 不涉及 **取值范围**: - linux_vul : 漏洞类型-linux漏洞 - windows_vul : 漏洞类型-windows漏洞 - web_cms : Web-CMS漏洞 - app_vul : 应用漏洞 - urgent_vul : 应急漏洞  **默认取值**: linux_vul 

        :return: The type of this VulBackupStatisticsRequestInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VulBackupStatisticsRequestInfo.

        **参数解释**: 漏洞类型，当select_type选择all_vul时，需要传递该参数 **约束限制**: 不涉及 **取值范围**: - linux_vul : 漏洞类型-linux漏洞 - windows_vul : 漏洞类型-windows漏洞 - web_cms : Web-CMS漏洞 - app_vul : 应用漏洞 - urgent_vul : 应急漏洞  **默认取值**: linux_vul 

        :param type: The type of this VulBackupStatisticsRequestInfo.
        :type type: str
        """
        self._type = type

    @property
    def data_list(self):
        r"""Gets the data_list of this VulBackupStatisticsRequestInfo.

        **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :return: The data_list of this VulBackupStatisticsRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this VulBackupStatisticsRequestInfo.

        **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :param data_list: The data_list of this VulBackupStatisticsRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        self._data_list = data_list

    @property
    def host_data_list(self):
        r"""Gets the host_data_list of this VulBackupStatisticsRequestInfo.

        **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :return: The host_data_list of this VulBackupStatisticsRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        return self._host_data_list

    @host_data_list.setter
    def host_data_list(self, host_data_list):
        r"""Sets the host_data_list of this VulBackupStatisticsRequestInfo.

        **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :param host_data_list: The host_data_list of this VulBackupStatisticsRequestInfo.
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        self._host_data_list = host_data_list

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
        if not isinstance(other, VulBackupStatisticsRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
