# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleKeyInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_name': 'str',
        'check_rule_id': 'str',
        'standard': 'str',
        'fix_values': 'list[CheckRuleFixValuesInfo]'
    }

    attribute_map = {
        'check_name': 'check_name',
        'check_rule_id': 'check_rule_id',
        'standard': 'standard',
        'fix_values': 'fix_values'
    }

    def __init__(self, check_name=None, check_rule_id=None, standard=None, fix_values=None):
        r"""CheckRuleKeyInfoRequestInfo

        The model defined in huaweicloud sdk

        :param check_name: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows
        :type check_name: str
        :param check_rule_id: 检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules
        :type check_rule_id: str
        :param standard: 基线标准, 类别包含如下：   - cn_standard#等保合规标准   - hw_standard#云安全实践标准
        :type standard: str
        :param fix_values: 用户键入的检查项修复参数数组
        :type fix_values: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixValuesInfo`]
        """
        
        

        self._check_name = None
        self._check_rule_id = None
        self._standard = None
        self._fix_values = None
        self.discriminator = None

        if check_name is not None:
            self.check_name = check_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if standard is not None:
            self.standard = standard
        if fix_values is not None:
            self.fix_values = fix_values

    @property
    def check_name(self):
        r"""Gets the check_name of this CheckRuleKeyInfoRequestInfo.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :return: The check_name of this CheckRuleKeyInfoRequestInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this CheckRuleKeyInfoRequestInfo.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :param check_name: The check_name of this CheckRuleKeyInfoRequestInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this CheckRuleKeyInfoRequestInfo.

        检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules

        :return: The check_rule_id of this CheckRuleKeyInfoRequestInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this CheckRuleKeyInfoRequestInfo.

        检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules

        :param check_rule_id: The check_rule_id of this CheckRuleKeyInfoRequestInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def standard(self):
        r"""Gets the standard of this CheckRuleKeyInfoRequestInfo.

        基线标准, 类别包含如下：   - cn_standard#等保合规标准   - hw_standard#云安全实践标准

        :return: The standard of this CheckRuleKeyInfoRequestInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this CheckRuleKeyInfoRequestInfo.

        基线标准, 类别包含如下：   - cn_standard#等保合规标准   - hw_standard#云安全实践标准

        :param standard: The standard of this CheckRuleKeyInfoRequestInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def fix_values(self):
        r"""Gets the fix_values of this CheckRuleKeyInfoRequestInfo.

        用户键入的检查项修复参数数组

        :return: The fix_values of this CheckRuleKeyInfoRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixValuesInfo`]
        """
        return self._fix_values

    @fix_values.setter
    def fix_values(self, fix_values):
        r"""Sets the fix_values of this CheckRuleKeyInfoRequestInfo.

        用户键入的检查项修复参数数组

        :param fix_values: The fix_values of this CheckRuleKeyInfoRequestInfo.
        :type fix_values: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixValuesInfo`]
        """
        self._fix_values = fix_values

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
        if not isinstance(other, CheckRuleKeyInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
