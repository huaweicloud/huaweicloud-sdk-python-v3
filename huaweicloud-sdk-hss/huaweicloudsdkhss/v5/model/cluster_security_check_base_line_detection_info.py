# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckBaseLineDetectionInfo:

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
        'check_type_desc': 'str',
        'baseline_item_list': 'list[ClusterSecurityCheckBaselineItemInfo]'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_rule_num': 'check_rule_num',
        'failed_rule_num': 'failed_rule_num',
        'check_type_desc': 'check_type_desc',
        'baseline_item_list': 'baseline_item_list'
    }

    def __init__(self, severity=None, check_name=None, check_type=None, standard=None, check_rule_num=None, failed_rule_num=None, check_type_desc=None, baseline_item_list=None):
        r"""ClusterSecurityCheckBaseLineDetectionInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 基线风险级别 **取值范围**： - High：高危基线 - Medium：中危基线 - Low：低危基线 
        :type severity: str
        :param check_name: **参数解释**： 基线名称 **取值范围**： 不涉及 
        :type check_name: str
        :param check_type: **参数解释**： 基线类型 **取值范围**： 不涉及 
        :type check_type: str
        :param standard: **参数解释**： 标准类型 **取值范围**： - hw_standard：云安全实践 - cn_standard：等保合规 - cis_standard：通用安全标准 
        :type standard: str
        :param check_rule_num: **参数解释**： 检查项数量 **取值范围**： 不涉及 
        :type check_rule_num: int
        :param failed_rule_num: **参数解释**： 风险项数量 **取值范围**： 不涉及 
        :type failed_rule_num: int
        :param check_type_desc: **参数解释**： 基线描述信息 **取值范围**： 不涉及 
        :type check_type_desc: str
        :param baseline_item_list: **参数解释**： 基线检测列表 **取值范围**： 不涉及 
        :type baseline_item_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaselineItemInfo`]
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._check_rule_num = None
        self._failed_rule_num = None
        self._check_type_desc = None
        self._baseline_item_list = None
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
        if baseline_item_list is not None:
            self.baseline_item_list = baseline_item_list

    @property
    def severity(self):
        r"""Gets the severity of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线风险级别 **取值范围**： - High：高危基线 - Medium：中危基线 - Low：低危基线 

        :return: The severity of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线风险级别 **取值范围**： - High：高危基线 - Medium：中危基线 - Low：低危基线 

        :param severity: The severity of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        r"""Gets the check_name of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :return: The check_name of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :param check_name: The check_name of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        r"""Gets the check_type of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线类型 **取值范围**： 不涉及 

        :return: The check_type of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线类型 **取值范围**： 不涉及 

        :param check_type: The check_type of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 标准类型 **取值范围**： - hw_standard：云安全实践 - cn_standard：等保合规 - cis_standard：通用安全标准 

        :return: The standard of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 标准类型 **取值范围**： - hw_standard：云安全实践 - cn_standard：等保合规 - cis_standard：通用安全标准 

        :param standard: The standard of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 检查项数量 **取值范围**： 不涉及 

        :return: The check_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 检查项数量 **取值范围**： 不涉及 

        :param check_rule_num: The check_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def failed_rule_num(self):
        r"""Gets the failed_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 风险项数量 **取值范围**： 不涉及 

        :return: The failed_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: int
        """
        return self._failed_rule_num

    @failed_rule_num.setter
    def failed_rule_num(self, failed_rule_num):
        r"""Sets the failed_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 风险项数量 **取值范围**： 不涉及 

        :param failed_rule_num: The failed_rule_num of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type failed_rule_num: int
        """
        self._failed_rule_num = failed_rule_num

    @property
    def check_type_desc(self):
        r"""Gets the check_type_desc of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线描述信息 **取值范围**： 不涉及 

        :return: The check_type_desc of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        r"""Sets the check_type_desc of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线描述信息 **取值范围**： 不涉及 

        :param check_type_desc: The check_type_desc of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

    @property
    def baseline_item_list(self):
        r"""Gets the baseline_item_list of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线检测列表 **取值范围**： 不涉及 

        :return: The baseline_item_list of this ClusterSecurityCheckBaseLineDetectionInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaselineItemInfo`]
        """
        return self._baseline_item_list

    @baseline_item_list.setter
    def baseline_item_list(self, baseline_item_list):
        r"""Sets the baseline_item_list of this ClusterSecurityCheckBaseLineDetectionInfo.

        **参数解释**： 基线检测列表 **取值范围**： 不涉及 

        :param baseline_item_list: The baseline_item_list of this ClusterSecurityCheckBaseLineDetectionInfo.
        :type baseline_item_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaselineItemInfo`]
        """
        self._baseline_item_list = baseline_item_list

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
        if not isinstance(other, ClusterSecurityCheckBaseLineDetectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
