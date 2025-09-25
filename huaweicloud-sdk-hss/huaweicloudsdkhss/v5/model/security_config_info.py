# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigInfo:

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
        'check_rule_num': 'int',
        'failed_rule_num': 'int',
        'scan_time': 'int',
        'check_type_desc': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_rule_num': 'check_rule_num',
        'failed_rule_num': 'failed_rule_num',
        'scan_time': 'scan_time',
        'check_type_desc': 'check_type_desc'
    }

    def __init__(self, severity=None, check_name=None, check_rule_num=None, failed_rule_num=None, scan_time=None, check_type_desc=None):
        r"""SecurityConfigInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 
        :type severity: str
        :param check_name: **参数解释**： 基线名称 **取值范围**： 不涉及 
        :type check_name: str
        :param check_rule_num: **参数解释**： 检查项数量 **取值范围**： 不涉及 
        :type check_rule_num: int
        :param failed_rule_num: **参数解释**： 风险项数量 **取值范围**： 不涉及 
        :type failed_rule_num: int
        :param scan_time: **参数解释**： 最新检测时间 **取值范围**： 不涉及 
        :type scan_time: int
        :param check_type_desc: **参数解释**： 基线描述信息 **取值范围**： 不涉及 
        :type check_type_desc: str
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_rule_num = None
        self._failed_rule_num = None
        self._scan_time = None
        self._check_type_desc = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_name is not None:
            self.check_name = check_name
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if failed_rule_num is not None:
            self.failed_rule_num = failed_rule_num
        if scan_time is not None:
            self.scan_time = scan_time
        if check_type_desc is not None:
            self.check_type_desc = check_type_desc

    @property
    def severity(self):
        r"""Gets the severity of this SecurityConfigInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :return: The severity of this SecurityConfigInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityConfigInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :param severity: The severity of this SecurityConfigInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        r"""Gets the check_name of this SecurityConfigInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :return: The check_name of this SecurityConfigInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this SecurityConfigInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :param check_name: The check_name of this SecurityConfigInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this SecurityConfigInfo.

        **参数解释**： 检查项数量 **取值范围**： 不涉及 

        :return: The check_rule_num of this SecurityConfigInfo.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this SecurityConfigInfo.

        **参数解释**： 检查项数量 **取值范围**： 不涉及 

        :param check_rule_num: The check_rule_num of this SecurityConfigInfo.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def failed_rule_num(self):
        r"""Gets the failed_rule_num of this SecurityConfigInfo.

        **参数解释**： 风险项数量 **取值范围**： 不涉及 

        :return: The failed_rule_num of this SecurityConfigInfo.
        :rtype: int
        """
        return self._failed_rule_num

    @failed_rule_num.setter
    def failed_rule_num(self, failed_rule_num):
        r"""Sets the failed_rule_num of this SecurityConfigInfo.

        **参数解释**： 风险项数量 **取值范围**： 不涉及 

        :param failed_rule_num: The failed_rule_num of this SecurityConfigInfo.
        :type failed_rule_num: int
        """
        self._failed_rule_num = failed_rule_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityConfigInfo.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :return: The scan_time of this SecurityConfigInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityConfigInfo.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this SecurityConfigInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def check_type_desc(self):
        r"""Gets the check_type_desc of this SecurityConfigInfo.

        **参数解释**： 基线描述信息 **取值范围**： 不涉及 

        :return: The check_type_desc of this SecurityConfigInfo.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        r"""Sets the check_type_desc of this SecurityConfigInfo.

        **参数解释**： 基线描述信息 **取值范围**： 不涉及 

        :param check_type_desc: The check_type_desc of this SecurityConfigInfo.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

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
        if not isinstance(other, SecurityConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
