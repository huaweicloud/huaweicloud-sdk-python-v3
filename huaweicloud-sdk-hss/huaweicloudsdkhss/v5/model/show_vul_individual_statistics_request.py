# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulIndividualStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'statistics_types': 'list[str]'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'statistics_types': 'statistics_types'
    }

    def __init__(self, enterprise_project_id=None, statistics_types=None):
        r"""ShowVulIndividualStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param statistics_types: **参数解释**: 需要查询的漏洞统计数据类型列表，多个类型以逗号分隔。 **约束限制**: 必填 **取值范围**: - need_urgent_repair_num：需要紧急修复的漏洞数量 - unhandled_num：未完成修复的漏洞数量 - existed_vul_host_num：存在漏洞的服务器数量 - today_handled_num：今日处理的漏洞数量 - all_handled_num：累计处理的漏洞数量 - vul_library_info：漏洞库统计数据 - linux_vul_unhandled_num：未处置的Linux漏洞数量 - windows_vul_unhandled_num：未处置的Windows漏洞数量 - web_cms_vul_unhandled_num：未处置的Web CMS漏洞数量 - app_vul_unhandled_num：未处置的应用漏洞数量 - urgent_vul_unhandled_num：未处置的应急漏洞数量 - max_vul_handle_num：单次最大可处置的漏洞数量  **默认取值**: 不涉及 
        :type statistics_types: list[str]
        """
        
        

        self._enterprise_project_id = None
        self._statistics_types = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.statistics_types = statistics_types

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowVulIndividualStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowVulIndividualStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowVulIndividualStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowVulIndividualStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def statistics_types(self):
        r"""Gets the statistics_types of this ShowVulIndividualStatisticsRequest.

        **参数解释**: 需要查询的漏洞统计数据类型列表，多个类型以逗号分隔。 **约束限制**: 必填 **取值范围**: - need_urgent_repair_num：需要紧急修复的漏洞数量 - unhandled_num：未完成修复的漏洞数量 - existed_vul_host_num：存在漏洞的服务器数量 - today_handled_num：今日处理的漏洞数量 - all_handled_num：累计处理的漏洞数量 - vul_library_info：漏洞库统计数据 - linux_vul_unhandled_num：未处置的Linux漏洞数量 - windows_vul_unhandled_num：未处置的Windows漏洞数量 - web_cms_vul_unhandled_num：未处置的Web CMS漏洞数量 - app_vul_unhandled_num：未处置的应用漏洞数量 - urgent_vul_unhandled_num：未处置的应急漏洞数量 - max_vul_handle_num：单次最大可处置的漏洞数量  **默认取值**: 不涉及 

        :return: The statistics_types of this ShowVulIndividualStatisticsRequest.
        :rtype: list[str]
        """
        return self._statistics_types

    @statistics_types.setter
    def statistics_types(self, statistics_types):
        r"""Sets the statistics_types of this ShowVulIndividualStatisticsRequest.

        **参数解释**: 需要查询的漏洞统计数据类型列表，多个类型以逗号分隔。 **约束限制**: 必填 **取值范围**: - need_urgent_repair_num：需要紧急修复的漏洞数量 - unhandled_num：未完成修复的漏洞数量 - existed_vul_host_num：存在漏洞的服务器数量 - today_handled_num：今日处理的漏洞数量 - all_handled_num：累计处理的漏洞数量 - vul_library_info：漏洞库统计数据 - linux_vul_unhandled_num：未处置的Linux漏洞数量 - windows_vul_unhandled_num：未处置的Windows漏洞数量 - web_cms_vul_unhandled_num：未处置的Web CMS漏洞数量 - app_vul_unhandled_num：未处置的应用漏洞数量 - urgent_vul_unhandled_num：未处置的应急漏洞数量 - max_vul_handle_num：单次最大可处置的漏洞数量  **默认取值**: 不涉及 

        :param statistics_types: The statistics_types of this ShowVulIndividualStatisticsRequest.
        :type statistics_types: list[str]
        """
        self._statistics_types = statistics_types

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
        if not isinstance(other, ShowVulIndividualStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
