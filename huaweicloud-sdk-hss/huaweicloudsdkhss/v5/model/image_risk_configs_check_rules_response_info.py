# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRiskConfigsCheckRulesResponseInfo:

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
        'check_rule_name': 'str',
        'check_rule_id': 'str',
        'scan_result': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_rule_name': 'check_rule_name',
        'check_rule_id': 'check_rule_id',
        'scan_result': 'scan_result'
    }

    def __init__(self, severity=None, check_name=None, check_type=None, standard=None, check_rule_name=None, check_rule_id=None, scan_result=None):
        r"""ImageRiskConfigsCheckRulesResponseInfo

        The model defined in huaweicloud sdk

        :param severity: 风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param check_name: 基线名称
        :type check_name: str
        :param check_type: 基线类型
        :type check_type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准
        :type standard: str
        :param check_rule_name: 检查项
        :type check_rule_name: str
        :param check_rule_id: 检查项ID
        :type check_rule_id: str
        :param scan_result: 检测结果，包含如下：   - pass：通过   - failed：未通过
        :type scan_result: str
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._check_rule_name = None
        self._check_rule_id = None
        self._scan_result = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_name is not None:
            self.check_name = check_name
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if scan_result is not None:
            self.scan_result = scan_result

    @property
    def severity(self):
        r"""Gets the severity of this ImageRiskConfigsCheckRulesResponseInfo.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ImageRiskConfigsCheckRulesResponseInfo.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this ImageRiskConfigsCheckRulesResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        r"""Gets the check_name of this ImageRiskConfigsCheckRulesResponseInfo.

        基线名称

        :return: The check_name of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ImageRiskConfigsCheckRulesResponseInfo.

        基线名称

        :param check_name: The check_name of this ImageRiskConfigsCheckRulesResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        r"""Gets the check_type of this ImageRiskConfigsCheckRulesResponseInfo.

        基线类型

        :return: The check_type of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ImageRiskConfigsCheckRulesResponseInfo.

        基线类型

        :param check_type: The check_type of this ImageRiskConfigsCheckRulesResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ImageRiskConfigsCheckRulesResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准

        :return: The standard of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ImageRiskConfigsCheckRulesResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准

        :param standard: The standard of this ImageRiskConfigsCheckRulesResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ImageRiskConfigsCheckRulesResponseInfo.

        检查项

        :return: The check_rule_name of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ImageRiskConfigsCheckRulesResponseInfo.

        检查项

        :param check_rule_name: The check_rule_name of this ImageRiskConfigsCheckRulesResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ImageRiskConfigsCheckRulesResponseInfo.

        检查项ID

        :return: The check_rule_id of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ImageRiskConfigsCheckRulesResponseInfo.

        检查项ID

        :param check_rule_id: The check_rule_id of this ImageRiskConfigsCheckRulesResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ImageRiskConfigsCheckRulesResponseInfo.

        检测结果，包含如下：   - pass：通过   - failed：未通过

        :return: The scan_result of this ImageRiskConfigsCheckRulesResponseInfo.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ImageRiskConfigsCheckRulesResponseInfo.

        检测结果，包含如下：   - pass：通过   - failed：未通过

        :param scan_result: The scan_result of this ImageRiskConfigsCheckRulesResponseInfo.
        :type scan_result: str
        """
        self._scan_result = scan_result

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
        if not isinstance(other, ImageRiskConfigsCheckRulesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
