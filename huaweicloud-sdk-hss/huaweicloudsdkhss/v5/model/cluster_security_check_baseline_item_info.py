# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckBaselineItemInfo:

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
        'check_item': 'str',
        'check_description': 'str',
        'check_remediation': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_item': 'check_item',
        'check_description': 'check_description',
        'check_remediation': 'check_remediation'
    }

    def __init__(self, severity=None, check_item=None, check_description=None, check_remediation=None):
        r"""ClusterSecurityCheckBaselineItemInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 检查项风险等级 **取值范围**： - High：高危 - Medium：中危 - Low：低危 
        :type severity: str
        :param check_item: **参数解释**： 检查项 **取值范围**： 不涉及 
        :type check_item: str
        :param check_description: **参数解释**： 检查描述 **取值范围**： 不涉及 
        :type check_description: str
        :param check_remediation: **参数解释**： 修复建议 **取值范围**： 不涉及 
        :type check_remediation: str
        """
        
        

        self._severity = None
        self._check_item = None
        self._check_description = None
        self._check_remediation = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_item is not None:
            self.check_item = check_item
        if check_description is not None:
            self.check_description = check_description
        if check_remediation is not None:
            self.check_remediation = check_remediation

    @property
    def severity(self):
        r"""Gets the severity of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查项风险等级 **取值范围**： - High：高危 - Medium：中危 - Low：低危 

        :return: The severity of this ClusterSecurityCheckBaselineItemInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查项风险等级 **取值范围**： - High：高危 - Medium：中危 - Low：低危 

        :param severity: The severity of this ClusterSecurityCheckBaselineItemInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_item(self):
        r"""Gets the check_item of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查项 **取值范围**： 不涉及 

        :return: The check_item of this ClusterSecurityCheckBaselineItemInfo.
        :rtype: str
        """
        return self._check_item

    @check_item.setter
    def check_item(self, check_item):
        r"""Sets the check_item of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查项 **取值范围**： 不涉及 

        :param check_item: The check_item of this ClusterSecurityCheckBaselineItemInfo.
        :type check_item: str
        """
        self._check_item = check_item

    @property
    def check_description(self):
        r"""Gets the check_description of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查描述 **取值范围**： 不涉及 

        :return: The check_description of this ClusterSecurityCheckBaselineItemInfo.
        :rtype: str
        """
        return self._check_description

    @check_description.setter
    def check_description(self, check_description):
        r"""Sets the check_description of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 检查描述 **取值范围**： 不涉及 

        :param check_description: The check_description of this ClusterSecurityCheckBaselineItemInfo.
        :type check_description: str
        """
        self._check_description = check_description

    @property
    def check_remediation(self):
        r"""Gets the check_remediation of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 修复建议 **取值范围**： 不涉及 

        :return: The check_remediation of this ClusterSecurityCheckBaselineItemInfo.
        :rtype: str
        """
        return self._check_remediation

    @check_remediation.setter
    def check_remediation(self, check_remediation):
        r"""Sets the check_remediation of this ClusterSecurityCheckBaselineItemInfo.

        **参数解释**： 修复建议 **取值范围**： 不涉及 

        :param check_remediation: The check_remediation of this ClusterSecurityCheckBaselineItemInfo.
        :type check_remediation: str
        """
        self._check_remediation = check_remediation

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
        if not isinstance(other, ClusterSecurityCheckBaselineItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
