# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRiskConfigsInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'check_name': 'str',
        'check_type': 'str',
        'standard': 'str',
        'check_rule_num': 'int',
        'failed_rule_num': 'int',
        'check_type_desc': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_rule_num': 'check_rule_num',
        'failed_rule_num': 'failed_rule_num',
        'check_type_desc': 'check_type_desc'
    }

    def __init__(self, severity=None, check_name=None, check_type=None, standard=None, check_rule_num=None, failed_rule_num=None, check_type_desc=None):
        r"""ImageRiskConfigsInfoResponseInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 
        :type severity: str
        :param check_name: **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如&#39;CentOS 7&#39;、&#39;EulerOS&#39;等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 
        :type check_name: str
        :param check_type: **参数解释** 用于区分基线的类型 **取值范围** 字符长度0-256位 
        :type check_type: str
        :param standard: **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 
        :type standard: str
        :param check_rule_num: **参数解释** 该基线对应的安全配置检测总检查项数量 **取值范围** 取值0-2097152 
        :type check_rule_num: int
        :param failed_rule_num: **参数解释** 该基线检测中未通过（存在安全风险）的检查项数量 **取值范围** 取值0-2097152 
        :type failed_rule_num: int
        :param check_type_desc: **参数解释** 该基线的详细描述，说明基线的检测目的、适用场景等信息 **取值范围** 字符长度0-65534位，支持中文、英文、数字、常用标点符号及空格 
        :type check_type_desc: str
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._check_rule_num = None
        self._failed_rule_num = None
        self._check_type_desc = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_name is not None:
            self.check_name = check_name
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if failed_rule_num is not None:
            self.failed_rule_num = failed_rule_num
        if check_type_desc is not None:
            self.check_type_desc = check_type_desc

    @property
    def severity(self):
        r"""Gets the severity of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 

        :return: The severity of this ImageRiskConfigsInfoResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 镜像安全配置检测结果的风险等级，用于筛选指定风险等级的检测记录 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 **默认取值** 无 

        :param severity: The severity of this ImageRiskConfigsInfoResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        r"""Gets the check_name of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如'CentOS 7'、'EulerOS'等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 

        :return: The check_name of this ImageRiskConfigsInfoResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 安全配置检测的基线名称，用于筛选指定基线的检测结果（如'CentOS 7'、'EulerOS'等） **约束限制** 仅支持功能介绍中列出的系统基线（CentOS 7、Debian 10、EulerOS、Ubuntu16） **取值范围** 支持的基线名称列表详见功能介绍 **默认取值** 无 

        :param check_name: The check_name of this ImageRiskConfigsInfoResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        r"""Gets the check_type of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 用于区分基线的类型 **取值范围** 字符长度0-256位 

        :return: The check_type of this ImageRiskConfigsInfoResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 用于区分基线的类型 **取值范围** 字符长度0-256位 

        :param check_type: The check_type of this ImageRiskConfigsInfoResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 

        :return: The standard of this ImageRiskConfigsInfoResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 安全配置检测遵循的标准，用于筛选符合指定标准的检测结果 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值** 无 

        :param standard: The standard of this ImageRiskConfigsInfoResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线对应的安全配置检测总检查项数量 **取值范围** 取值0-2097152 

        :return: The check_rule_num of this ImageRiskConfigsInfoResponseInfo.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线对应的安全配置检测总检查项数量 **取值范围** 取值0-2097152 

        :param check_rule_num: The check_rule_num of this ImageRiskConfigsInfoResponseInfo.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def failed_rule_num(self):
        r"""Gets the failed_rule_num of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线检测中未通过（存在安全风险）的检查项数量 **取值范围** 取值0-2097152 

        :return: The failed_rule_num of this ImageRiskConfigsInfoResponseInfo.
        :rtype: int
        """
        return self._failed_rule_num

    @failed_rule_num.setter
    def failed_rule_num(self, failed_rule_num):
        r"""Sets the failed_rule_num of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线检测中未通过（存在安全风险）的检查项数量 **取值范围** 取值0-2097152 

        :param failed_rule_num: The failed_rule_num of this ImageRiskConfigsInfoResponseInfo.
        :type failed_rule_num: int
        """
        self._failed_rule_num = failed_rule_num

    @property
    def check_type_desc(self):
        r"""Gets the check_type_desc of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线的详细描述，说明基线的检测目的、适用场景等信息 **取值范围** 字符长度0-65534位，支持中文、英文、数字、常用标点符号及空格 

        :return: The check_type_desc of this ImageRiskConfigsInfoResponseInfo.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        r"""Sets the check_type_desc of this ImageRiskConfigsInfoResponseInfo.

        **参数解释** 该基线的详细描述，说明基线的检测目的、适用场景等信息 **取值范围** 字符长度0-65534位，支持中文、英文、数字、常用标点符号及空格 

        :param check_type_desc: The check_type_desc of this ImageRiskConfigsInfoResponseInfo.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

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
        if not isinstance(other, ImageRiskConfigsInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
