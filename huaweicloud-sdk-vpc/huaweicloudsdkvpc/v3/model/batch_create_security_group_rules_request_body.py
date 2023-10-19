# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSecurityGroupRulesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_rules': 'list[BatchCreateSecurityGroupRulesOption]',
        'ignore_duplicate': 'bool',
        'dry_run': 'bool'
    }

    attribute_map = {
        'security_group_rules': 'security_group_rules',
        'ignore_duplicate': 'ignore_duplicate',
        'dry_run': 'dry_run'
    }

    def __init__(self, security_group_rules=None, ignore_duplicate=None, dry_run=None):
        """BatchCreateSecurityGroupRulesRequestBody

        The model defined in huaweicloud sdk

        :param security_group_rules: 待创建的安全组规则列表
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.BatchCreateSecurityGroupRulesOption`]
        :param ignore_duplicate: 创建时是否忽略重复的安全组规则 默认为false
        :type ignore_duplicate: bool
        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建安全组规则。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建安全组规则。
        :type dry_run: bool
        """
        
        

        self._security_group_rules = None
        self._ignore_duplicate = None
        self._dry_run = None
        self.discriminator = None

        self.security_group_rules = security_group_rules
        if ignore_duplicate is not None:
            self.ignore_duplicate = ignore_duplicate
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this BatchCreateSecurityGroupRulesRequestBody.

        待创建的安全组规则列表

        :return: The security_group_rules of this BatchCreateSecurityGroupRulesRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.BatchCreateSecurityGroupRulesOption`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this BatchCreateSecurityGroupRulesRequestBody.

        待创建的安全组规则列表

        :param security_group_rules: The security_group_rules of this BatchCreateSecurityGroupRulesRequestBody.
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.BatchCreateSecurityGroupRulesOption`]
        """
        self._security_group_rules = security_group_rules

    @property
    def ignore_duplicate(self):
        """Gets the ignore_duplicate of this BatchCreateSecurityGroupRulesRequestBody.

        创建时是否忽略重复的安全组规则 默认为false

        :return: The ignore_duplicate of this BatchCreateSecurityGroupRulesRequestBody.
        :rtype: bool
        """
        return self._ignore_duplicate

    @ignore_duplicate.setter
    def ignore_duplicate(self, ignore_duplicate):
        """Sets the ignore_duplicate of this BatchCreateSecurityGroupRulesRequestBody.

        创建时是否忽略重复的安全组规则 默认为false

        :param ignore_duplicate: The ignore_duplicate of this BatchCreateSecurityGroupRulesRequestBody.
        :type ignore_duplicate: bool
        """
        self._ignore_duplicate = ignore_duplicate

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchCreateSecurityGroupRulesRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建安全组规则。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建安全组规则。

        :return: The dry_run of this BatchCreateSecurityGroupRulesRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchCreateSecurityGroupRulesRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建安全组规则。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建安全组规则。

        :param dry_run: The dry_run of this BatchCreateSecurityGroupRulesRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, BatchCreateSecurityGroupRulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
